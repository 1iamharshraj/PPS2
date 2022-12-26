c=0
for line in open('diabetes.csv'):
    if " " in line:
        c+=1
print(len([line for line in open('diabetes.csv')]))
print(c)