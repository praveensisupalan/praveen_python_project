lst = [2,  5, 26, 14, 5, 5, 14, 7, 6, 14, 5, 5]

for num in lst:
    count = lst.count(num)

    if (count >= 2):
        print(num)
        break
