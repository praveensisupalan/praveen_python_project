lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]

# for sub_lst in lst:
#     for num in sub_lst:
#         if num >=16:
#             print(num)
# print(max(lst))
flat_lst=[]
for sub_lst in lst:
    for num in sub_lst:
        flat_lst.append(num)
print(flat_lst)
print(max(flat_lst))

