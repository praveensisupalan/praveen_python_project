arr=[1,2,3,13,14,15,16,65,78,89]

element=13
flag=0
for num in arr:
    if num==element:
        flag=1
        break
print ("element found" if flag==1 else "element not found" )