
def dic_swap(lst): # function for swaping if incorrect order
    i=0
    n=len(lst)
    while i<n:
        if type(lst[i][0])==int:
            lst[i]=lst[i][::-1]
        i+=1

def Ck_Same(dic,s): # check if any duplicate age or name are there
    for i in dic[s].items():
        if i[1]>1:
            break
    else:
        return False
    return True

def MergeAge(d): # merging age for same name
    global form
    lst=list(form)
    l=[]
    for i in d["name"].items():
        if i[1]>1:
            l.append(i[0])
    i=0
    n=len(l)
    while i < n :
        m=len(form)-1
        age=[]
        idx=-1
        while m >=0:
            if form[m][0]==l[i]:
                age.append(str(form[m][1]))
                idx=m
                lst.pop(m)
            m-=1
        lst.insert(idx,[form[idx][0],int("".join(age[::-1]))])
        i+=1
    form=lst

def MergeName(d): # cube rooted age and merged name for same age
    global form
    lst=list(form)
    l=[]
    for i in d["age"].items():
        if i[1]>1:
            l.append(i[0])
    i=0
    n=len(l)
    while i < n :
        m=len(form)-1
        name=[]
        idx=-1
        while m >=0:
            if form[m][1]==l[i]:
                name.append(str(form[m][0]))
                idx=m
                lst.pop(m)
            m-=1
        lst.insert(idx,["".join(name[::-1]),int((form[idx][1])**(1/3))])
        i+=1
    form=lst

def disp(l): # displaying output in desired format
    print(list(map(lambda x:dict((x,)),l)))


# taking input and converting it to nested list
form = list(map((lambda x : list(next(iter(x.items())))),eval(input())))

dic_swap(form) # swapping incorrect order element

# creating record of repitition of both names and age
data = {"name":{x[0]:0 for x in form},"age":{x[1]:0 for x in form}}
for i in form:
    data["name"][i[0]]+=1
    data["age"][i[1]]+=1


# statements according to the problem
if Ck_Same(data,"age"):
    MergeName(data)
    disp(form)
elif Ck_Same(data,"name"):
    MergeAge(data)
    disp(form)
else:
    disp(form)
