stus = open("students.txt")
astu = [stu.rstrip("\n") for stu in stus]

fail = open("failed.txt")
fstu = [fstu.rstrip("\n") for fstu in fail]

passed = open("passed.txt", "w")

pstus = set(astu) - set(fstu)
print(pstus)
for pstu in pstus:
    passed.write(pstu)
