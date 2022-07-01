file=open("abc.txt")
list=[line.rstrip("\n") for line in file]
print(list)