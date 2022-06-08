lst = [1,2, 3, 4, 6]

ele = 7

# for i in range(0, len(lst)):
#     for j in range((i + 1), len(lst)):
#         curr_sum = lst[i] + lst[j]
#         if curr_sum == sum:
#             print(f"pairs are {lst[i]}, {lst[j]}")
#             break

lst.sort()

low =0
upp=len(lst)-1

while(low<upp):
    crr_sum = lst[low] + lst[upp]
    if ele==crr_sum:
        print(f"pairs {lst[low]},{lst[upp]}")
        low+=1
        # break
    elif ele>crr_sum:
        low+=1
    elif ele<crr_sum:
        upp-=1