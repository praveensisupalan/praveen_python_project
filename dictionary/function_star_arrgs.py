# def add(*num):
#     return sum(num)
#
# print(add(100,1,3,))
#
# def max_of(*NUM):
#     return max(NUM)
# print(max_of(1000,2000,500))


        #**kwargs

def add_num(**kwargs):
    print(kwargs)
    print(sum([value for key,value in kwargs.items()]))
                #OR
    # print(sum([value for value in kwargs.values()]))

add_num(num1=27,num2=33,num3=30)