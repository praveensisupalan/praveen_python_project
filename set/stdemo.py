# st1={1,2,3,4,5}
# st2={10,11,12,2,3}
#
# union_st=st1.union(st2)
# print(union_st)
#
# intersecrion_st=st1.intersection(st2)
# print(intersecrion_st)
#
# difference_st=st1.difference(st2)
# print(difference_st)
#


students=["hari","ram","farook","ramu","bilal"]
passed_stu=["hari","ram","bilal"]
stu=set(students)
passedstu=set(passed_stu)
failed_stu=stu - (passedstu)
print(failed_stu)