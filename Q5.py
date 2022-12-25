import re, string


def SingleD(n):
    while n > 9:
        l = n
        s = 0
        while l:
            s += l % 10
            l //= 10
        n = s

    return n


def num(ch):
    ch = ch.upper()
    if ch in {'A', 'J', 'S'}:
        return 1
    elif ch in {'B', 'K', 'T'}:
        return 2
    elif ch in {'C', 'L', 'U'}:
        return 3
    elif ch in {'D', 'M', 'V'}:
        return 4
    elif ch in {'E', 'N', 'W'}:
        return 5
    elif ch in {'F', 'O', 'X'}:
        return 6
    elif ch in {'G', 'P', 'Y'}:
        return 7
    elif ch in {'H', 'Q', 'Z'}:
        return 8
    elif ch in {'I', 'R'}:
        return 9
    else:
        return 0


def Destiny(s):
    Sum = 0
    for x in s:
        Sum += num(x) * data[x]

    return SingleD(Sum)


def SoulUrge(s):
    global v
    return Destiny(s.intersection(v))


def Dream(s):
    global c
    return Destiny(s.intersection(c))


v = {'A', 'E', 'I', 'O', 'U'}
c = set(string.ascii_uppercase).difference(v)

st = "".join(input().upper().split())

data = {x: 0 for x in st}
for x in st:
    data[x] += 1

Set = set(st)

if re.match("^[A-Za-z ]+$", st):
    print(Destiny(Set))
    print(SoulUrge(Set))
    print(Dream(Set))
else:
    print("Wrong input")