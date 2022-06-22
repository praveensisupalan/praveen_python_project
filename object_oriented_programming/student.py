class student:
    name:str
    std:int
    roll_no:int
    gender:str
    def __init__(self,**kwargs):
        self.name=kwargs.
        self.std=std
        self.roll_no=roll_no
        self.gender=gender
    def pri_student(self):
        print(self.name,self.std,self.roll_no,self.gender)
std1=student("praveen",10,21,"male")

std1.pri_student()