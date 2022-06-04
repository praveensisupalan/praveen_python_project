num=3
# update=num
# res=num
# i=1
# print(num,"*",end="")
# while(i<num):
#     res+=(update*10)+num
#     update=(update*10)+num
#     print(update,"*",end="")
#
#
#     i=i+1
# print("=",res)

# or
i=1
pattern=""
sum=0
while(i<=num):
    pattern=pattern+str(num)
    sum=sum+int(pattern)
    i=i+1
print(sum)