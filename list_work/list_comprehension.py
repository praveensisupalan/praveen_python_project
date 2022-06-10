lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]

flat_lst=[num for sub_lst in lst for num in sub_lst]

print(flat_lst)
#
# numgt_sixteen=[num for num in flat_lst if num>16]
# print(numgt_sixteen)
#
# odd_num=[num for num in flat_lst if num%2 !=0]
# print(odd_num)
#
# even=[num for num in flat_lst if num%2==0]
# print(sum(even))

mapped_lst=[num+1 if num>25 else num-1 for num in flat_lst]
print(mapped_lst)


