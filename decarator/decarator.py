def dec(fun):
    def inner_fun(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return inner_fun



@dec
def sub(n1,n2):
    return n1-n2
@dec
def div(n1,n2):
    return n1/n2

print(sub(5,10))
print(div(5,10))