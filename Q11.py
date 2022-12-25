def IsPerfectNum(n):
    Sum = 1
    f = 2
    while f ** 2 < n:
        if n % f == 0:
            Sum += f + n // f
        f += 1
    if Sum == n and Sum != 1:
        return True
    else:
        return False


def IsPerfectSq(n):
    if n ** (1 / 2) == int(n ** (1 / 2)):
        return True
    else:
        return False


def IsRamanujanNum1(N):
    lst = list(range(1, round(N ** (1 / 3)) + 1)) * 2

    def cube(cu):

        s = 0
        for i in cu:
            s += i ** 3
        return s

    def CuCk(l, n, N, o=2):
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
                if len(com) == o and cube(com) == N:
                    raise ArithmeticError
        return flst

    try:
        CuCk(lst, 2, N)
        return False
    except ArithmeticError:
        return True


def SpecNumInRange(func, start, stop, rev=False):
    for i in range(start, stop, 1 * (-1 if rev else 1)):
        if func(i):
            return i
    return False


mark = int(input())

if mark < 50:
    room = SpecNumInRange(IsPerfectNum, 500 + mark, 1, rev=True)
    if room:
        print(room)
else:
    room = SpecNumInRange(IsRamanujanNum1, 637 + mark, 1000)
    if room:
        print(room)
    else:
        print(SpecNumInRange(IsPerfectSq, 637 + mark, 1000))

