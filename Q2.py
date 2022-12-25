import re
chrs = tuple(input().split(","))
c=0
for ch in chrs:
    a=False
    A=False
    num=False
    Ch=False
    if len(ch) in range(6,13):
        for i in ch:
            if re.match("[a-z]",i):
                a = True
            elif re.match("[A-Z]",i):
                A = True
            elif re.match("[0-9]",i) :
                num = True
            elif i in ["$","@","#"] :
                Ch =True
            else:
                break
        else:
            if a and A and num and Ch:
                print(ch)
                c+=1
if not c:
    print("Invalid")