# Write an XLS file with a single worksheet, containing
# a heading row and some rows of data.

import xlwt
import datetime
ezxf = xlwt.easyxf

def write_xls(file_name, sheet_name, headings, data, heading_xf, data_xfs):
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheet_name)
    rowx = 0
    for colx, value in enumerate(headings):
        sheet.write(rowx, colx, value, heading_xf)
    sheet.set_panes_frozen(True) # frozen headings instead of split panes
    sheet.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
    sheet.set_remove_splits(True) # if user does unfreeze, don't leave a split there
    for row in data:
        rowx += 1
        for colx, value in enumerate(row):
            sheet.write(rowx, colx, value, data_xfs[colx])
    book.save(file_name)

def result_excel(file_name,predict):
    data = []
    file = open(file_name, 'r')
    i = 0
    total = 0
    correct = 0
    for line in file:
        row = []
        # erase illegal word
        line1 = line.rstrip('\n')
        line1 = line1.replace('?', '')
        line1 = line1.replace(',', '')
        line1 = line1.replace("''", '')
        line1 = line1.replace("``", '')
        line_list = line1.split(":")
        coarse = line_list[0]
        word = line_list[1].split()
        fine = word[0]
        sentence = line_list[1].replace(fine, ' ')
        row.append(coarse)
        row.append(fine)
        row.append(sentence)
        row.append(predict[i])
        if(predict[i] == coarse):
            judge = 'T'
            correct += 1
        else:
            judge = 'F'
        i += 1
        row.append(judge)
        data.append(row)
        total += 1
    file.close()
    hdngs = ['Coarse', 'Fine', 'Sentence', 'Predect', 'Judge']
    kinds = 'text    text          text        text        text'.split()

    heading_xf = ezxf('font: bold on; align: wrap on, vert centre, horiz center')
    kind_to_xf_map = {
        'text': ezxf(),
    }
    data_xfs = [kind_to_xf_map[k] for k in kinds]
    write_xls('result.xls', 'result', hdngs, data, heading_xf, data_xfs)

    correct = float(correct)
    total = float(total)
    correct_rate = correct/total
    return correct_rate
