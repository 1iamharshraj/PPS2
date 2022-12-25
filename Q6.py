
Pan = input()
mid=len(Pan)//2

if (Pan[:mid].isupper() and Pan[-1].isupper())and Pan[mid:-1].isdigit()and(len(Pan)>=10):
    print("Valid")
else:
    print("Invalid")