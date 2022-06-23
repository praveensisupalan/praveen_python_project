class editor:
    def functionality(self):
        self.funct=["createnewfile","execute","save"]
        return self.funct

class py_charm(editor):
    def functionality(self):
        funct=super().functionality()
        funct.append(["debug","versioncontrol"])
        return funct
py=py_charm()

print(py.functionality())