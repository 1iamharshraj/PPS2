from re import match
from datetime import date as dtob, timedelta


def Check_Cred(User, Pass):  # code for checking username and password
    Cred = [User, Pass]
    fob = open("Credentials.txt", "r")
    for i in fob.readlines():
        if Cred == i.strip().split("~"):
            return True
    else:
        return False


def Get_Amount(Des, Ages, type="A"):  # function for getting total amount of a reservation
    global places
    fare = places[Des] if type == "A" else (places[Des] + 100)
    n = len(Ages) - 1
    Amount = 0
    while n >= 0:
        if Ages[n] < 60:
            Amount += fare
        else:
            Amount += fare * 0.9
        n -= 1
    return int(Amount)


def Reserve(NP, BM):  # function for writing reservation in file
    global seat
    Name = []
    Age = []
    for x in range(NP):
        Name.append(input("Name :"))
        age = int(input("age :"))
        Age.append(age)
    place = input("Destination :")
    Date = input("Date of Journey :")
    for x in places:
        if x == place:
            Amount = Get_Amount(place, Age, BM)
    f = open("result.txt", "a+")
    f.write("Remaining Seats :" + "\n")
    f.write("Regular =" + str(A) + "\n")
    f.write("Tatkal =" + str(B) + "\n")
    n = len(Name)
    i = 0
    while i < n:
        f.write(Name[i] + "-" + str(Age[i]) + "-" + "Bengaluru " + "-" + place + "-" + str(seat) + "\n")
        seat -= 1
        i += 1
    f.write("Date of Journey: " + Date + "\n")
    f.write("total fare = Rs. " + str(Amount) + "\n\n")
    f.close()


def FindType(lst):  # function for getting type of reservation
    global places
    Age = list(map(lambda x: int(x.split("-")[1]), lst[3:-2]))
    cost = int(lst[-1][17:])
    des = (lst[3].split("-"))[-2]
    c = Get_Amount(des, Age)
    if c == cost:
        return "A"
    else:
        return "B"


def Lines(fob):  # function for reading file and getting structured data
    l = []
    line = True
    l1 = []
    while line:
        line = fob.readline()
        if not line.strip():
            l.append(l1)
            l1 = []
        else:
            l1.append(line.strip())
    return l


def AddLines(line):  # function for writing structured data to file
    Str = ""
    for i in line:
        Str += "\n".join(i) + "\n\n"
    return Str


def FindTypeDes(lst):  # function for getting type and destination
    global places
    Age = list(map(lambda x: int(x.split("-")[1]), lst[3:-2]))
    cost = int(lst[-1][17:])
    des = (lst[3].split("-"))[-2]
    c = Get_Amount(des, Age)
    if c == cost:
        t = "A"
    else:
        t = "B"
    return t, des


def Refund(Rdate, Cdate, cost):  # function for getting refund amount
    print(Rdate)
    day, month, year = tuple(map(int, Rdate.split("-")))
    Rdate = dtob(day=day, month=month, year=year)
    if Rdate - timedelta(days=20) > Cdate:
        return int(cost)
    elif Rdate - timedelta(weeks=2) > Cdate:
        return int(cost * 0.90)
    elif Rdate - timedelta(weeks=1) > Cdate:
        return int(cost * 0.80)
    elif Rdate - timedelta(days=4) > Cdate:
        return int(cost * 0.50)
    else:
        return 0


def Seat():  # Function for updating seat number
    global A, B, seat
    seat = A + B


A = 12
B = 3
seat = A + B

if Check_Cred(input("Username : "), input("Password : ")):  # Checking Username and pass
    while True:
        s = \
            '''\t\tMain Menu
            ------------
            1. Booking
            2. Cancellation
            3. Exit'''
        print(s)
        cho = input()
        if cho == "1":
            M = \
                '''\t\tBooking Menu
               ------------
              A. Regular ({A} seats)
              B. Tatkal ({B} seats)
            '''.format(A=A, B=B)
            print(M)
            BM = input()
            places = {"Hosur": 75, "Vaniyambadi": 250, "Vellore": 500, "Walaja": 600, "Chennai": 750}
            NP = int(input("Number of Passengers :"))

            if BM == "A":
                if A >= NP:
                    A -= NP
                    Reserve(NP, BM)
                    Seat()
                else:
                    f1 = open("result.txt", "a")
                    print("insufficient seats!!! Try for Other Dates")
                    f1.write("insufficient seats!!! Try for Other Dates\n\n")
                    f1.close()
            else:
                if B >= NP:
                    B -= NP
                    Reserve(NP, BM)
                    Seat()
                else:
                    f1 = open("result.txt", "a")
                    print("insufficient seats!!! Try for Other Dates")
                    f1.write("insufficient seats!!! Try for Other Dates\n\n")
                    f1.close()
        elif cho == "2":
            dic = {"name": [], "age": []}
            while True:
                name = input()
                if match(r"[0-9]*-[0-9]*-[0-9]*", name):
                    date = name
                    break
                age = input()
                dic["name"].append(name)
                dic["age"].append(age)
            f = open("result.txt", "r+")
            lines = Lines(f)
            f.close()
            for rec in lines:
                for data in rec[3:-2]:
                    d = data.split("-")
                    if (d[0], d[1]) in zip(dic["name"], dic["age"]):
                        if date == rec[-2][-10:]:
                            i = lines.index(rec)
                            break
            try:
                l = lines[i]
                f = open("result.txt", "w")
                f.write(AddLines(lines))
                tpe, des = FindTypeDes(l)
                if tpe == "A":
                    A += len(dic["age"])
                    Seat()
                else:
                    B += len(dic["age"])
                    Seat()
                f.write(
                    "Remaining seates :\nRegular = {A}\nTatkal = {B}\nNo. of Passengers to cancel = {no}\n".format(A=A,
                                                                                                                   B=B,
                                                                                                                   no=len(
                                                                                                                       dic[
                                                                                                                           "age"])))
                i = 0
                n = len(dic) - 1
                while i < n:
                    f.write("Cancelled Passenger Name= {name}\nCancelled Passenger Age = {age}\n".format(
                        name=dic["name"][i], age=dic["age"][i])
                    )
                    i += 1
                amount = Get_Amount(des, list(map(int, (dic["age"]))), tpe)
                ref = Refund(date, dtob(day=15, month=11, year=2022), amount)
                f.write("Refund Amount = Rs. {ref}\n".format(ref=ref))
                f.write("Cancellation Charge = Rs. {can}\n\n".format(can=amount - ref))
                f.close()

            except NameError:
                print("No match")
        elif cho == "3":
            break
else:
    print("Invalid")
