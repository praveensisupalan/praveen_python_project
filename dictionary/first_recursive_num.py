#first recursive char

# alph="CCAABDD"

# letter_count={}
# for letter in alph:
#     if letter in letter_count:
#         print("first recursive letter =",letter)
#     else:
#         letter_count[letter]=1



# second recursive letter
# alph="CCAABDD"
#
# letter_count={}
#
# rep_letter=[]
# for letter in alph:
#     if letter in letter_count:
#         rep_letter.append(letter)
#     else:
#         letter_count[letter]=1
# print("second recusive letter =",rep_letter[1])
# print(letter_count)
#


#most recursive char
alph="CCAAAABB"
letter_count={}
for letter in alph:
    if letter in letter_count:
        letter_count[letter]+=1
    else:
        letter_count[letter]=1
print(max(letter_count.items(),key=lambda iteam:iteam[1]))

# letter_count={'C': 2, 'A': 4, 'B': 4}
#
# print("maximum",max(letter_count.items(),key=lambda iteam:iteam[1]))
# print("minimum",min(letter_count.items(),key=lambda iteam:iteam[1]))