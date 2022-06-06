arr=[1,2,3,13,14,15,16,65,78,89]

element=140
flag=0
for num in arr:
    if num==element:
        flag=1
        break
if flag==1:
    print(True)
else:
    print(False)