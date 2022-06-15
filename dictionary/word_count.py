txt="hai hai hello hello hai hello"

words= txt.split(" ")

wc={}
for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1

print(wc)
