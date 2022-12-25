def Combinations(lst, n):
    if n == 0:
        return [[]]
    l1 = []
    for i in range(len(lst)):
        x = lst[i]
        Rem_lst = lst[i + 1:]
        Rem_Combo = Combinations(Rem_lst, n - 1)
        for j in Rem_Combo:
            l1.append([x, *j])
    return l1


def AddL(lst):
    global data
    s = 0
    for i in lst:
        s += data[i]
    return s


Str = input()
LuckyNumber = int(input())
group = int(input())

data = {Str[x]: x + 1 for x in range(len(Str))}
combo = Combinations(list(Str), group)

for i in combo:
    if AddL(i) == LuckyNumber:
        print("".join(i))