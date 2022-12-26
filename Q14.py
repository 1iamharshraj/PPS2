def F1(Id): # function for total amount of entered customerID
    rowss = Rows()
    c = 0
    for row in rowss:
        if Id == row[0]:
            c += float(row[4].strip())
    return c


def F2(): # function for maximum and minimum rate product
    rowss = Rows()
    l = []
    for x in rowss:
        l.append([float(x[-1].strip()), x[1]])
    l.sort()
    return l[0], l[-1]


def F3(): # function for getting max total amount and id
    rowss = Rows()
    data = {x[0]: 0 for x in rowss}
    for x in rowss:
        data[x[0]] += float(x[-1].strip())
    tup = list(data.items())
    tup.sort(key=lambda x: x[1])
    return tup[-1]


def Rows():
    fob1 = open("bill.txt", "r")
    lines = fob1.readlines()
    fob1.close()
    return list(map(lambda x: x.split(","), lines[1:-2]))


def totalamount(rowss):
    c1 = 0
    for row in rowss:
        c1 += float(row[4])
    return c1


first_row = ['customerId', 'Product', 'Quantity', 'rate', 'TotalPrice']
rows = []
for _ in range(int(input(" No. of customers : "))):
    Id = input("Customer ID : ")
    for i in range(int(input("No. of Products : "))):
        prdt = input("Product : ")
        qt = int(input("Quantity : "))
        rate = float(input("Rate : "))
        rows.append([Id, prdt, str(qt), "%.2f" % rate, "%.2f" % (qt * rate)])

with open('bill.txt', 'w+') as fob:
    fob.write(",".join(first_row) + "\n")
    for r in rows:
        fob.write(",".join(r) + "\n")
    fob.write("\nTotal Amount: Rs:{T}".format(T=totalamount(rows)))

print("\nFUNCTION OUTPUTS")
# using F1
print("\n",F1("111"), "\n")  # giving Id 111

# using F2
print("min : ", F2()[0], "max : ", F2()[1], "\n")

# using F3
print(F3())
