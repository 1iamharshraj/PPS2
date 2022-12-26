def is_1prime(dic):  # function for checking prime number
    for i in ele["int"]:
        if i < 2:
            continue
        n = 2
        while n <= i ** (1 / 2):
            if i % n == 0:
                break
            n += 1
        else:
            return True
    return False

 
def is_1palindrome(dic):  # function for checking palindrome
    for i in ele["str"]:
        if i.casefold() == i.casefold()[::-1]:
            break
    else:
        return False
    return True


def interchange(l):  # function for reversing str and complex number
    n = len(l)
    i = 0
    while i < n:
        if type(l[i]) == str:
            l[i] = l[i][::-1]
        elif type(l[i]) == complex:
            l[i] = complex(l[i].imag, l[i].real)
        i += 1


def negate(l):  # function for negating and conjugating
    n = len(l)
    i = 0
    while i < n:
        if type(l[i]) == int:
            l[i] = -l[i]
        elif type(l[i]) == complex:
            l[i] = complex(l[i].real, -l[i].imag)
        i += 1


def unpack(l):  # function for unpacking
    i = 0
    n = len(l)
    L = list(l)
    while i < n:
        if type(L[i]) == str:
            l[l.index(L[i]):l.index(L[i]) + 1] = list(L[i])
        i += 1


lst = eval(input())

ele = {"str": [], "int": [], "complex": []}

for i in lst:  # updating elements in dictionary:ele
    if type(i) == int:
        ele["int"].append(i)
    elif type(i) == str:
        ele["str"].append(i)
    elif type(i) == complex:
        ele["complex"].append(i)

# statements for transforming the list
if is_1palindrome(ele):
    negate(lst)
elif is_1prime(ele):
    interchange(lst)

if is_1prime(ele) and is_1palindrome(ele):
    print(lst[len(lst) // 2])
elif len(lst) == 1:
    print("Invalid Data")
elif not (is_1prime(ele) or is_1palindrome(ele)):
    unpack(lst)
    print(lst)
else:
    print(lst) 