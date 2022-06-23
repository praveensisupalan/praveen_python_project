class parent:
    def properties(self):
        self.props={"mobile":"iphone","bike":"pashion pro"}
        return self.props
class child(parent):
    def properties(self):
        props= super().properties()
        props["car"]="swift"
        return props
ch=child()

print(ch.properties())


