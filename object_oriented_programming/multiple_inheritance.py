class p1:
    def m1(self):
        print("m1")


class p2:
    def m2(self):
        print("m2")


class p3(p2,p1):
    def m3(self):
        print("m3")

p3=p3()

p3.m3()
p3.m2()
p3.m1()

