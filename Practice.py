class Foo:
    def __init__(self,x):
        self.x=x
    # def fullname(self,surname='vyas'):
    #     return self.name+" "+surname

    def __add__(self,y):
        return self.x + y.x

a = Foo(5)
b=Foo(6)
print(a+b)

# print(f.fullname())
