from bow import BagOfWords
from bow import WordFilters

class fetureExpress(object):

    def __init__(self,training_file,test_file):
        self.train_file = training_file
        self.text_file = test_file

    def _form_lib(self,train_file):
        total_word = []  # to store the word that appeared in the file in list
        label,sentence_total = self._handle_file(train_file)
        for value in sentence_total:
            word = value.split()
            word.remove(word[0])
            total_word += word
        word_fit = WordFilters.stopwords("en", total_word)

        self.word_lib = BagOfWords(word_fit)
        self.word_lib = dict(self.word_lib)
        for key in self.word_lib:
            self.word_lib[key] = 0
        return self.word_lib

    def _handle_file(self,file):
        file = open(file, 'r')
        label = []  # label for every sentence
        sentence_total = []  # to store every sentence in file in list

        for line in file:
            # erase illegal word
            line1 = line.rstrip('\n')
            line1 = line1.replace('?', '')
            line1 = line1.replace(',', '')
            line1 = line1.replace("''", '')
            line1 = line1.replace("``", '')
            line_list = line1.split(":")

            label.append(line_list[0])
            sentence_total.append(line_list[1])

        file.close()

        return [label,sentence_total]

    def _extract_feature(self,sentencetotal,word_lib):
        temp = []
        for sentence in sentencetotal:
            word = sentence.split()
            word.remove(word[0])
            word_fit = WordFilters.stopwords("en",word)
            feature = BagOfWords(word_fit)
            feature = dict(feature)
            temp.append(feature)

        sample_list = []
        for sentence in sentencetotal:
            temp = self.word_lib.copy()
            for temp_key in temp:
                for sentence_key in sentence:
                    if sentence_key == temp_key:
                        temp[temp_key] = sentence[sentence_key]
            sample_list.append(temp)

        return sample_list

    def _train_feature(self):
        train_label,sentencetotal = self._handle_file(self.train_file)
        self._form_lib(self.train_file)
        sample_list = self._extract_feature(sentencetotal,self.word_lib)
        return train_label,sample_list
    
    def _test_feature(self):
        test_label,sentencetotal = self._handle_file(self.test_file)
        sample_list = self._extract_feature(sentencetotal,self.word_lib)
        return test_label,sample_list

    def getfeature(self):
        train_label, train_samle = self._train_feature()
        test_label, test_sample = self._test_feature()
        return [train_label,train_samle,test_label,test_sample]

    def test(self,file):
        label,sentence_total = self._handle_file(file)
        return [label, sentence_total]

        
    

        





