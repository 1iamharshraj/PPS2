# Function to create combinations
# without itertools
def n_length_combo(lst, n):
    print(" lst: ", lst, " n: ", n)
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]
        print(" i: ", i, " m: ", m, " remlst: ", remLst)
        remainlst_combo = n_length_combo(remLst, n - 1)
        for p in remainlst_combo:
            l.append([m, *p])
            print("remainlst_combo: ", remainlst_combo, " [m, *p]:", [m, *p], " l: ", l)

    return l


'''

from re import findall

seq = "AGCT"
P1, P2 = input(), input()
# print("MATCH" if len(findall(seq,input()))==len(findall(seq,input())) else "MISMATCH")

if len(findall(seq, P1)) == len(findall(seq, P2)):
    print(len(findall(seq, P1)))
    print(len(findall(seq, P2)))
    print("MATCH")
else:
    print(len(findall(seq, P1)))
    print(len(findall(seq, P2)))
    print("MISMATCH")
'''


def IsRamanujanNum(N):
    lst = list(range(1, round(N ** (1 / 3)) + 1)) * 2
    print(lst)

    def cube(cu):
        s = 0
        for i in cu:
            s += i ** 3
        return s

    def CuCk(l, n, N):
        if n == 0:
            return [[]]
        flst = []
        for i in range(len(l)):
            f = l[i]
            remf = l[i + 1:]
            remcomb = CuCk(remf, n - 1, N)
            for j in remcomb:
                com = [f, *j]
                flst.append(com)
                if len(com) == n and cube(com) == N:
                    print(com)
                    raise ArithmeticError

        return flst

    try:
        CuCk(lst, 2, N)
        return False
    except ArithmeticError:
        return True


# Python3 program to print all combination
# of size r in an array of size n

''' arr[] ---> Input Array
	chosen[] ---> Temporary array to store
			current combination
	start & end ---> Starting and Ending indexes in arr[]
	r---> Size of a combination to be printed

	'''


def CombinationRepetitionUtil(chosen, arr, index,
                              r, start, end):
    # Current combination is ready,
    # print it
    if index == r:
        for j in range(r):
            print(chosen[j], end=" ")

        print()
        return

    # When no more elements are
    # there to put in chosen[]
    if start > n:
        return

    # Current is included, put
    # next at next location
    chosen[index] = arr[start]

    # Current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    CombinationRepetitionUtil(chosen, arr, index + 1,
                              r, start, end)
    CombinationRepetitionUtil(chosen, arr, index,
                              r, start + 1, end)


# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# CombinationRepetitionUtil()
def CombinationRepetition(arr, n, r):
    # A temporary array to store
    # all combination one by one
    chosen = [0] * r

    # Print all combination using
    # temporary array 'chosen[]'
    CombinationRepetitionUtil(chosen, arr, 0, r, 0, n)


'''
# Driver code
arr = [1, 2, 3, 4]
r = 2
n = len(arr) - 1

CombinationRepetition(arr, n, r)
'''


def IsRamanujanNum2(N: int) -> bool:
    global r
    r = 0
    lst = range(N)

    def cube(cu):
        s = 0
        for i in cu:
            s += i ** 3
        return s

    def CuCk(l, n, N):
        global r
        if n == 0:
            return [[]]
        flst = []
        for i in range(len(l)):
            f = l[i]
            remf = l[i + 1:]
            remcomb = CuCk(remf, n - 1, N)
            for j in remcomb:
                com = [f, *j]
                flst.append(com)
                if len(com) == n and cube(com) == N:
                    print(com)
                    raise ArithmeticError

        return flst

    try:
        CuCk(lst, 2, N)
        return False
    except ArithmeticError:
        return True


s = [2, 9, 16, 25, 36, 55, 65, 72, 91, 126, 128, 133, 152, 189, 217, 224, 243, 250, 280, 341, 344, 351, 370, 407, 432,
     468, 513, 520, 539, 559, 576, 637, 686, 728, 730, 737]


def IsPerfectNum(n):
    Sum = 1
    f = 2
    while f ** 2 < n:
        if n % f == 0:
            Sum += f + n // f
        f += 1
    if Sum == n:
        return True
    else:
        return False


print(IsPerfectNum(496))
