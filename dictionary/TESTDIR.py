smart_tv={"name":"MItv","brand":"redmi","color":"black","price":10000,"size":22}
# print(smart_tv)
#
# smart_tv["processer"]="snapdragon"
# print("processer" in smart_tv)
#
# print(smart_tv)
#
# smart_tv["color"]="blue"
# print(smart_tv)
#
# print(smart_tv.get("name"))
# print(smart_tv.get("brand"))

# if "size" in smart_tv:
#     smart_tv["size"]=72
# else:
#     smart_tv["size"]=32
         #or
# smart_tv["size"]=72 if "size" in smart_tv else 32
# print(smart_tv)

# if price is <10000 updATE to -1000 else

if smart_tv["price"]>10000:
    smart_tv["price"]-=500
else:
    smart_tv["price"]-=1000
print(smart_tv)
