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
