lst=[2,14,5,26,14,14,7,6,14,5,]
# fnum=0
# for rnum in lst:
#    count= lst.count(rnum)
#    if count>fnum:
#        fnum=rnum
# print(rnum)

dup_lst=[]
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] == lst[j]:
            dup_lst.append(lst[i])

print(dup_lst)
