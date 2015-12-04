from math import *
from transform import Transform


class TF_IDF(Transform):

    def __init__(self, mat):
        Transform.__init__(self, mat)
        self.total_doc = len(self.mat)

    def transform(self):
        r, c = self.mat.shape
        trans_med_mat = self.mat.copy()

        for row in xrange(0, r):
            total_word = reduce(lambda x, y: x+y, self.mat[row])
            total_word = float(total_word)

            for col in xrange(0, c):
                trans_med_mat[row, col] = float(trans_med_mat[row, col])

                if trans_med_mat[row][col] != 0:
                    trans_med_mat[row, col] = self.tfidf(
                        row, col, total_word)

        return trans_med_mat

    def tfidf(self, row, col, total_word):
        term_freq = self.mat[row][col] / float(total_word)
        inverse_doc_freq = log(abs(self.total_doc / float(
            self.get_term_doc_occurences(col))))
        return term_freq * inverse_doc_freq

    def get_term_doc_occurences(self, col):

        term_doc_occurrences = 0

        r, c = self.mat.shape

        for n in xrange(0, r):
            if self.mat[n][col] > 0:
                term_doc_occurrences += 1
        return term_doc_occurrences
