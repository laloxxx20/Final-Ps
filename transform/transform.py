from mat_formatter import MatFormatter
from scipy import array


class Transform:
    def __init__(self, mat):
        self.mat = array(mat, dtype=float)

    def __repr__(self):
        MatFormatter(self.mat).good_print
