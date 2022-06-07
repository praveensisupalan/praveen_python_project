lst1 = [10, 11, 12, 13, 14]

lst2 = [11, 14, 15, 16, 10]

commlst = []

for num in lst1:
    if num in lst2:
        commlst.append(num)

print(commlst)


# most frequent numbers
#
# firsr recursuve num