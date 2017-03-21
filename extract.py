from bow import BagOfWords
from bow import WordFilters
from sklearn.ensemble import RandomForestClassifier


file = open('test.label','r')
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

data = []
data_sentence = []
# convert dict value into list
for i in sample_list:
    data_sentence = list(i.values())
    data.append(data_sentence)

rf = RandomForestClassifier()
rf.fit(data,label)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)
test_sample = []
test_sample.append(data[4])
print rf.predict_proba(test_sample)
# DESC ENTY HUM LOC
s = set(label)
l = list(s)
l.sort()
print l
