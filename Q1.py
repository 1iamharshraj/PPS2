lst = eval(input())
n = len(lst)-1
c=False
while n >= 0 :
    if type(lst[n]) == list:
        lst[n:n+1] = lst[n]
        c=True
    n-=1
if c:
    print(len(lst))
else:
    print("cannot unpack")
