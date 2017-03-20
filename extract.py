from bow import BagOfWords
from bow import WordFilters

file = open('train_1000.label','r')
label = [] # label for every sentence
total_word = []  # to store the word that appeared in the file in list
sentence_total = [] # to store every sentence in file in list

for line in file:
    # erase illegal word
    line1 = line.rstrip('\n')
    line1 = line1.replace('?', '')
    line1 = line1.replace(',', '')
    line1 = line1.replace("''",'')
    line1 = line1.replace("``",'')

    line_list = line1.split(":")

    label.append(line_list[0])
    word =line_list[1].split()
    word.remove(word[0])
    sentence_total.append(word)
    total_word += word

file.close()

word_fit = WordFilters.stopwords("en", total_word)

word_lib = BagOfWords(word_fit)
word_lib = dict(word_lib)
for key in word_lib:
    word_lib[key] = 0
sample_list = []

temp = []
for sentence in sentence_total:
    word_fit = WordFilters.stopwords("en",sentence)
    feature =  BagOfWords(word_fit)
    feature = dict(feature)
    temp.append(feature)
sentence_total = temp

for sentence in sentence_total:
    temp = word_lib.copy()
    for temp_key in temp:
        for sentence_key in sentence:
            if sentence_key == temp_key:
                temp[temp_key] = sentence[sentence_key]
    sample_list.append(temp)

for key in sample_list[0]:
    if sample_list[0][key] == 1:
        print key








