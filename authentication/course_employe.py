class EMP:
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.role


class Department:
    def __init__(self,**kwargs):
        employ_role=kwargs.get("employ_role")
        if emp.role=="hr":
            self.dep_name=kwargs.get("dep_name")
            self.employ_role=kwargs.get("employ_role")
        else:
            print("no access")
    def __str__(self):
        return self.dep_name

emp=EMP(name="rahul",role="hr")

dep=Department(dep_name="cs",employ_role=emp)

print(dep,dep.employ_role)
