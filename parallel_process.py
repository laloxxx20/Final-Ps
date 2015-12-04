# import time
from mpi4py import MPI
from vector_space import VectorSpace


def NOT(a):
    return 1-a


def XNOR(a, b):
    return NOT(a ^ b)


def get_requests(filename):
    txt = open(filename)

    list_request = []
    request = ''

    line = txt.readline()
    while line:
        if line.find('GET http') >= 0 or line.find('POST http') >= 0:
            request = request + line
            line = txt.readline()
        else:
            while XNOR(
                        (line.find('GET http') == -1),
                        (line.find('POST') == -1)):
                request = request + line
                line = txt.readline()
                if line == '':
                    break
            list_request.append(request)
            request = ''
    print len(list_request)
    return list_request


# vector_space = VectorSpace(get_requests('testing_attacks.txt'))
# print "list: ", vector_space.search(["select * from where drop table"])


list_request = get_requests('testing_attacks.txt')
vector_space = VectorSpace(list_request)

attacks = [
    ("sql", "select * from where drop table statement odbc union"),
    ("lce", "dir c /winnt/system32/cmd.exe"),
    ("pt", "virtual include file"),
    ("SSIA", "virtual include statement odbc progra"),
    ("XI", "path count child text position comment"),
    ("CS", "document.cookie alert javascript document.location.replace url http"),
    ("LI", "had* objectclass *o  brien* netscaperoot"),
]

print "attacks[0][0]: ", attacks[0][0]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

i = 0
while i<7:
    if rank == i:
        print attacks[i][0] + ": " 
        print vector_space.search(attacks[i][1])
    i = i + 1
