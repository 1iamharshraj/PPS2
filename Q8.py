from re import findall

seq = "AGCT"
P1, P2 = input().strip(), input().strip()
if P1 == "":
    P1 = "CCCAGCTAGCTAGCTAGCTAGCTAGCTAGCTTTTGGGAGCTAGCTAGCTGAA"

if len(findall(seq, P1)) == len(findall(seq, P2)):
    print("MATCH")
else:
    print("MISMATCH")
