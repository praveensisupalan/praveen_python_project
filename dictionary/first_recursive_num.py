alph="CAABDD"

# let_count={}#c:1
# for let in alph:
#     if let in let_count:
#         print("first recursive let", let)
#         break
#     else:
#         let_count[let]=1


# second recursive num
lett_count={}
recursive_lett=[]
for lett in alph:
    if lett in lett_count:
        recursive_lett.append(lett)
    else:
        lett_count[lett]=1
print("second recursive =",recursive_lett[1])


#wordcount
#first recursive char
#second     "        "
#most recursive char
