def Valuate(lst, key):
    s = 0
    for i in range(len(lst)):
        if key[i + 1] == lst[i]:
            s += 2
        elif lst[i] == "X":
            s += 0
        else:
            s += -0.25
    return s


def RemRep(lst):
    n = len(lst) - 1
    while n > 0:
        if lst[n][0] == lst[n - 1][0]:
            lst[n - 1:n + 1] = [[lst[n][0], lst[n][1] + "," + lst[n - 1][1]]]
        n -= 1


key = {1: "A", 2: "B", 3: "B", 4: "A", 5: "A"}
Scores = []

for i in range(int(input())):
    C = Valuate(input().split(), key)
    Scores.append([C, "C" + str(i + 1)])
Scores.sort(reverse=True)

RemRep(Scores)

print("Rank Candidates Total")
Rank = 1
for i in Scores:
    print(Rank, i[1], "{sc:.2f}".format(sc=i[0]))
    Rank += 1

