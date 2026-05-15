#polymorphism
#operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(6))
#print(a.__div__(b))-> this division operator is not there in this so it will raise error
print(a.__pow__(b))
print(a.__le__(b))#le->less than or equal to
print(a.__ge__(b))#ge->greater than or equal to
a='code';b='gnan'
print(a.__add__(b))
a='python';b='course'
print(a.__add__(b))
print(a.__add__(" "+b).title())
print("gayathri".__add__(" "+"twisha").title())
a=[1,2,3,4,5,6];b=[7,8,9,10,11,12]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))'''


#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,v):
        return self.a*v.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(9)
#x=5
#y=5
print(x+y)#here we have to give same operator we used above or else it will raise an error

#method overloading

class new():
    def s(se,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('the sum is',a+b+c)
        elif a!=None and b!=None:
            print('the product is',a*b)
        else:
            print('program ends')
x=new()
x.s()
x.s(2,4,5)
x.s(5,4)'''

#method overriding
'''class a():
    def spe(se):
        print('animal can make sounds')
class d():
    def spe(se):
        print('dog barks')
x=a()
y=d()
x.spe()
y.spe()'''


class vehicles:
    def speed(se):
        print('you should maintain speed while driving not to go fast')

class bike:
    def speed(se):
        print('you should wear a helmet not to drive rashly')








        
a=vehicles()
b=bike()
a.speed()
b.speed()

