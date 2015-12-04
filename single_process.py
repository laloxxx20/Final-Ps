# import time
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
    # print len(list_request)
    return list_request


# list_request = get_requests('anomalousTrafficTest.txt')
list_request = get_requests('testing_attacks.txt')

vector_space = VectorSpace(list_request)
print "list sql: ", vector_space.search(
    ["select * from where drop table statement odbc union"])
print "list command execution: ", vector_space.search(
    ["dir c /winnt/system32/cmd.exe"])
print "list path traversal: ", vector_space.search(
    ["virtual include file"])
print "list SSI Atack: ", vector_space.search(
    ["virtual include statement odbc progra"])
print "list XPATH injection: ", vector_space.search(
    ["path count child text position comment"])
print "list Cross Site Scripting: ", vector_space.search(
    ["document.cookie alert javascript document.location.replace url http "])
print "list LDAP Injection: ", vector_space.search([
    "had* objectclass *o  brien* netscaperoot"])
