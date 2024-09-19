# class foo():
#     def __init__(self,x=10):
#         self.x=x
#
#     def bar(self,y=20):
#         return self.x*y


#this is where we are doing inheritance
# class Goo(foo):
#
#     def bar(self,y=20):
#         return self.x*y*1000



#
# f=foo()
# g=Goo()
# print(f.bar())
# print(g.bar())


#example code from the book

#__repr__ return string of a object

# class MyList(list):
#     def __repr__(self):
#         list_string=list.__repr__(self)
#         return list_string.replace(' ','')
#
# my_list=MyList([1,3])
# print(my_list)
# with_space=list([1,3])
# print(with_space)

#one More example

class foo:
    def __init__(self, size=10):
        self.size = size

    def __iter__(self):
        self.counter=list(range(self.size))
        return self

    def __next__(self):
        if self.counter:
            return self.counter.pop()
        else:
            raise StopIteration

f=foo()
list(f)
for i in foo(3):
    print(i)