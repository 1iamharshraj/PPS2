from re import findall

seq = "AGCT"
P1, P2 = input(), input()
# print("MATCH" if len(findall(seq,input()))==len(findall(seq,input())) else "MISMATCH")

if len(findall(seq, P1)) == len(findall(seq, P2)):
    print("MATCH")
else:
    print("MISMATCH")
