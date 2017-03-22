from bow import BagOfWords
from bow import WordFilters
from sklearn.ensemble import RandomForestClassifier
import xlwt
from get_result_file import result_excel

file = open('train_2000.label','r')
label = [] # label for every sentence
total_word = []  # to store the word that appeared in the file in list
sentence_total = [] # to store every sentence in file in list

for line in file:
    # erase illegal word
    line1 = line.rstrip('\n')
    line1 = line1.replace('?', '')
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

temp = []
for sentence in sentence_total:
    word_fit = WordFilters.stopwords("en",sentence)
    feature =  BagOfWords(word_fit)
    feature = dict(feature)
    temp.append(feature)
sentence_total = temp

sample_list = []
for sentence in sentence_total:
    temp = word_lib.copy()
    for temp_key in temp:
        for sentence_key in sentence:
            if sentence_key == temp_key:
                temp[temp_key] = sentence[sentence_key]
    sample_list.append(temp)

data = []
data_sentence = []
# convert dict value into list
for i in sample_list:
    data_sentence = list(i.values())
    data.append(data_sentence)
#test
sentence_total1 = [] # to store every sentence in file in list

file1 = open('TREC_10.label','r')
label1 = [] # label for every sentence
for line in file1:
    # erase illegal word
    line1 = line.rstrip('\n')
    line1 = line1.replace('?', '')
    line1 = line1.replace(',', '')
    line1 = line1.replace("''",'')
    line1 = line1.replace("``",'')
    line_list = line1.split(":")

    label1.append(line_list[0])
    word =line_list[1].split()
    word.remove(word[0])
    sentence_total1.append(word)

file1.close()
temp = []
for sentence in sentence_total1:
    word_fit = WordFilters.stopwords("en",sentence)
    feature =  BagOfWords(word_fit)
    feature = dict(feature)
    temp.append(feature)
sentence_total1 = temp

sample_list = []
for sentence in sentence_total1:
    temp = word_lib.copy()
    for temp_key in temp:
        for sentence_key in sentence:
            if sentence_key == temp_key:
                temp[temp_key] = sentence[sentence_key]
    sample_list.append(temp)

test = []
test_sentence = []
# convert dict value into list
for i in sample_list:
    test_sentence = list(i.values())
    test.append(test_sentence)
#test

# random forest model
rf = RandomForestClassifier()
rf.fit(data,label)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)

# store the result in excel file
result = []
result = rf.predict(test)

result_excel('TREC_10.label',result)

