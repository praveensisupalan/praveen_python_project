num=123
res=0
while(num !=0):
    LastDigit=num%10
    # res=(res*10)+
    res=res+str( LastDigit)
    num = num//10
print(res)