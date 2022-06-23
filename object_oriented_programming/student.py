class student:
    name:str
    std:int
    roll_no:int
    gender:str
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.std=kwargs.get("std")
        self.roll_no=kwargs.get("roll_no")
        self.gender=kwargs.get("gender")
    def pri_student(self):
        print(self.name,self.std,self.roll_no,self.gender)
std1=student(name="praveen",std=10,roll_no=21,gender="male")
std1.pri_student()