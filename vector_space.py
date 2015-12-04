from parser import Parser
from transform.tfidf import TF_IDF

import sys


try:
    from numpy import dot
    from numpy.linalg import norm
except:
    print "Error: Requires numpy, Have you installed scipy?"
    sys.exit()


class VectorSpace:
    collec_doc_term_vecs = []
    vec_index_keyword_map = []

    parser = None

    def __init__(self, docs=[], transforms=[TF_IDF]):
        self.collec_doc_term_vecs = []
        self.parser = Parser()
        if len(docs) > 0:
            self.building(docs, transforms)

    def _search(self, searchList):
        query_vector = self.building_query_vector(searchList)

        rate = [self.cos(query_vector, doc_vector) for doc_vector in self.collec_doc_term_vecs]
        # ratings.sort(reverse=True)
        return rate

    def building(self, docs, transforms):
        self.vec_index_keyword_map = self.get_vec_keyword(
            docs)

        mat = [self.make_vec(document) for document in docs]
        mat = reduce(
            lambda mat, transform: transform(
                mat).transform(), transforms, mat)
        self.collec_doc_term_vecs = mat

    def get_vec_keyword(self, document_list):
        vocabulary_list = self.parser.tokenise_delete_stop_words(
            document_list)
        unique_vocabulary_list = self.delete_duplicates(vocabulary_list)

        vector_index = {}
        offset = 0

        for word in unique_vocabulary_list:
            vector_index[word] = offset
            offset += 1
        return vector_index

    def make_vec(self, word_string):
        vector = [0] * len(self.vec_index_keyword_map)

        word_list = self.parser.tokenise_delete_stop_words(
            word_string.split(" "))

        for word in word_list:
            try:
                vector[self.vec_index_keyword_map[word]] += 1
            except:
                pass
        return vector

    def building_query_vector(self, term_list):
        query = self.make_vec(" ".join(term_list))
        return query

    def delete_duplicates(self, list):
        return set((item for item in list))

    def cos(self, vector1, vector2):
        """ cos = ( V1 * V2 ) / ||V1|| x ||V2|| """
        return float(dot(vector1, vector2) / (norm(vector1) * norm(vector2)))
