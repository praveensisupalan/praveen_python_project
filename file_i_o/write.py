f=open("test.txt","w")

lst=["hai","hello","django"]

for line in lst:
    line+="\n"
    f.write(line)

