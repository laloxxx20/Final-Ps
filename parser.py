# import os
from porter_STEMMER import PorterSTEMMER
# from nltk.stem.snowball import SnowballSTEMMER
# import nltk


class Parser:
    STOP_WORDS_FILE = 'tokens_request.txt'

    STEMMER = None
    stopwords = []

    def __init__(self, stopwords_io_stream=None):
        # self.STEMMER = SnowballSTEMMER("english", ignore_stopwords=True)
        self.STEMMER = PorterSTEMMER()

        if(not stopwords_io_stream):
            stopwords_io_stream = open(Parser.STOP_WORDS_FILE, 'r')

        self.stopwords = stopwords_io_stream.read().split()
        # print "self.stopwords: ", self.stopwords

    def tokenise_delete_stop_words(self, document_list):
        if not document_list:
            return []

        voca_str = " ".join(document_list)

        tokenised_vocabulary_list = self.tokenise(voca_str)
        clean_word_list = self.del_stop_words(tokenised_vocabulary_list)
        # print "clean_list: ", clean_word_list
        return clean_word_list

    def del_stop_words(self, list):
        return [word for word in list if word not in self.stopwords]

    def tokenise(self, string):
        string = self.cln(string)
        words = string.split(" ")

        return [self.STEMMER.stem(w, 0, len(w)-1) for w in words]

    def cln(self, string):
        # string = string.replace(".", "")
        # string = string.replace("\s+", " ")
        txt = open('tokens_request.txt')
        for line in txt:
            line = line.replace('\n', "")
            # print "line: [" + line + "]"
            string = string.replace(line, " ")

        string = string.lower()
        return string
