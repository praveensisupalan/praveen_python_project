mobiles=open("mobiles.txt")
all_mobiles=[ ]
for lines in mobiles:
    mobile=lines.rstrip("\n").split(",")
    all_mobiles.append(mobile)

print(all_mobiles)

costly_mobiles=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mobiles)

fivegMob=[mob for mob in all_mobiles if mob[3]=="5g"]
print(fivegMob)