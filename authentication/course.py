class Course:
    course:str
    status:bool

    def post(self,**kwargs):
        self.course=kwargs.get("course")
        self.status=kwargs.get("status")

    def __str__(self):
        return self.course
class Batch:
    course:Course
    batch_code:str
    start_date:str

    def post(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code
class Student:
    stud_name:str
    gender:str
    roll_no:int
    batch:Batch

    def post(self,**kwargs):
        self.stud_name=kwargs.get("stud_name")
        self.gender = kwargs.get("gender")
        self.roll_no = kwargs.get("roll_no")
        self.batch = kwargs.get("batch")

    def __str__(self):
        return self.stud_name




django=Course()
django.post(course="django",status=True)

Bigdata=Course()
Bigdata.post(course="Bigdata",status=True)

dj_batch1=Batch()
dj_batch1.post(course=django,batch_code="may22",start_date="may 1")

BD_batch1=Batch()
BD_batch1.post(course=Bigdata,batch_code="jun22",start_date="june 15")

Praveen=Student()
Praveen.post(stud_name="praveen",gender="male",roll_no=21,batch=dj_batch1)

farook=Student()
farook.post(stud_name="farook",gender="male",roll_no=11,batch=BD_batch1)

ram=Student()
ram.post(stud_name="ram",gender="male",roll_no=25,batch=dj_batch1)

print(Praveen,Praveen.batch.course.course)