#**kwargs
'''def c(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
c()
a={"idnos":[10,20,30],
         "names":["satyanarayana","kalyani","kusuma"],
         "places":["vgm","taduvai","tir"]}
c(**a)'''


'''def sk(*b,**a):
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    d=7
    for i in b:
        d=d+i
        print(d)
    for i,k in a.items():
        print("key is",i)
        print("value is",k)    
sk()
b=(2,3,4,5,6,7,8,9)
a={"no":[1,2,3],"names":["gayathri","dhatri","twisha"]}
sk(*b,**a)'''

#global and local variables
#1st case of global variable

'''a=5
def c():
    print("inside value",a)
c()
print("outside value",a)'''


#2nd case of global variables

'''a=5
def c():
    a=9
    a=a**2
    print("inside value",a)
c()
print("outside value",a)'''


#3rd case of global variable

'''a=5
def c():
    a=7
    print("inside value",a)
    a=10
    print("updated value",a+5)
    b=12#local variable
    b=b+a
    print("b value",b)
c()
print("a value",a)
print("b value",b)#it rises error becoz it is a local variable'''

#usage of global keyword
'''a=5
def g():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=15
    b=b+a
    print("value of b is",b)
g()
print("value of a is",a)
print("value of b is",b)'''

#generators

'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(21))
print(a)
print(*a)
print(type(a))'''

'''a=(i for i in range(21))
print(a)
print(list(a))
print(type(a))'''


'''a=(i for i in range(21))
print(a)
print(tuple(a))
print(type(a))'''

'''a=(i for i in range(21))
print(a)
print(set(a))
print(type(a))'''



'''a,b=[int(x) for x in input("enter thr values").split(",")]
def c(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*c(a,b))'''


'''a,b=[int(x) for x in input("enter thr values").split(",")]
def c(a,b):
    while a<b:
        a+=1
        return a
print(c(a,b))'''


#yield v/s return

'''def my():
    return "python"
    return "java"
    return "ds"
print(my())'''

'''def my():
    return "python","java","ds"
print(*my())'''


def my():
    yield "apple"
    yield "mango"
    yield "grapes"
print(*my())

#next()

d=my()
print(next(d))
print(next(d))
print(next(d))

