class MatFormatter:

    def __init__(self, mat):
        self.mat = mat

    def good_print(self):
        out = ""

        r, c = self.mat.shape

        for row in xrange(0, r):
            out += "["

            for col in xrange(0, c):
                out += "%+0.2f " % self.mat[row][col]
            out += "]\n"

        return out
