master_word="macdedbhgg"
chk_word="egg"
count=0

for j in chk_word:
    print(j)
    for i in master_word:

        if i==j:
            count+=1

if count==4:
    print(True)
else:
    print(False)

