from itertools import combinations, combinations_with_replacement


def IsRamanujanNum(N):
    rang = list(range(1, N)) * 2
    com = combinations(rang, 2)
    for i1, i2 in com:
        S = i1 ** 3 + i2 ** 3
        if S == N:
            return True
    else:
        return False


'''
for i in range(637 + 60, 1000):
    if IsRamanujanNum(i):
        print(i)
        break
'''


def RamNum(x):
    for N in range(637 + x, 1000):
        rang = range(1, round(N ** (1 / 3)) + 1)
        com = combinations_with_replacement(rang, 2)
        for i1, i2 in com:
            S = i1 ** 3 + i2 ** 3
            if S == N:
                return N
    else:
        return None


# print(RamNum(60))


'''
s = [2, 9, 16, 25, 36, 55, 65, 72, 91, 126, 128, 133, 152, 189, 217, 224, 243, 250, 280, 341, 344, 351, 370, 407, 432,
     468, 513, 520, 539, 559, 576, 637, 686, 728, 730, 737]
for i in s:
    print(IsRamanujanNum(i))
'''

input()
arr1 = set(input().split())
input()
arr2 = set(input().split())

for i in arr1.symmetric_difference(arr2):
    print(i)
n, m = list(map(int, input().split()))
