mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
# #q1 total number of out_of_stock mobiles
#
# outmob=[mob for mob in mobiles if mob[-1]==0]
# print("num of out of stock phones=",len(outmob))
#
# #q2 total stock
#
# total_stock= [stock[-1] for stock in mobiles]
# print("total stock=",sum(total_stock))
#
# # q3 pritn mobiles available in range 20k to 30k
#
# in_range=[ mob for mob in mobiles  if  mob[4]in range(20000,30000) ]
#
# print(in_range )


# # q4 print all 5g phone
#
# phone_5g=[mob for mob in mobiles if mob[2]=="5g"]
# print(phone_5g)

# # q5 print samsung mobiles
# samsung_mob=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(samsung_mob)

# # q6 print costly mobile
# max_prices=max([mob[4] for mob in mobiles])
# costly_mob=[mob for mob in mobiles if mob[4]==max_prices]
# print(costly_mob)

# # q7 prin low cost mobiles
#
# min_price=min(mob[4] for mob in mobiles)
# lowcost_mob=[mob for mob in mobiles if mob[4]==min_price]
# print(lowcost_mob)]

#q8 print all mobiles having stock >10
stock_less10=[mob for mob in mobiles if mob[-1]>10]
print(stock_less10)=