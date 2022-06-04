#greatest  common divicer


num1=33
num2=35
gcd=1
limit=num1 if num1<num2 else num2
for i in range(2,(limit+1)):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)