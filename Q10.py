def Combination(lst, n):
    if n == 0:
        return [[]]
    l1 = []
    for i in range(0, len(lst)):
        x = lst[i]
        Rem_lst = lst[i + 1:]
        Rem_combo = Combination(Rem_lst, n - 1)
        for j in Rem_combo:
            l1.append([x, *j])
    return l1


Str = input()
if Str.isalpha():
    combos = [combo for combo in
              (combinations for combinations in (Combination(list(Str), i) for i in range(1, len(Str) + 1)))]

    length = len(combos) - 1

    while length >= 0:
        flag = False
        n = 0
        l = len(combos[length])
        while n < l:
            if combos[length][n] == combos[length][n][::-1]:
                print(len(combos[length][n]))
                break
            n += 1
        if flag:
            break
        length -= 1
    else:
        print(0)
else:
    print("Invaid Input")