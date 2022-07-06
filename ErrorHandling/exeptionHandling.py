
num1=int(input("enter num1= "))
num2=int(input("enter num2= "))
try:
    res=num1/num2
    print(f"result= {res}")

except Exception as e:
    num2 = int(input("enter a none zero num2= "))
    res=num1/num2
    print(f"result= {res}")

finally:
    print("db transaction")
    print("file operation")