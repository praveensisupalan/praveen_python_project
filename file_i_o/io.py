file=open("abc.txt")
list=[line.strip("\n") for line in file]
print(list)