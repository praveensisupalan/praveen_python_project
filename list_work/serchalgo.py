lst=[2,14,5,26,7,6]
ele=2
lst.sort()
flag=0

low=0
upp=len(lst)-1
while(low<=upp):
    mid=(low+upp)//2
    if lst[mid]==ele:
        flag=1
        break
    elif ele >lst[mid]:
        low= mid+1
    elif ele<lst[mid]:
        upp= mid-1
print("found" if flag>0 else "not found")



