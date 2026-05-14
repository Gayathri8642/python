#object instantiation
'''class Details:
    def Data(se,n,a,p):
        se.n=n
        se.a=a
        se.p=p
    def display(se):
        print(se.n,se.a,se.p)
x=Details()
print(dir(x))
x.Data('om',24,'vja')
x.display()
y=Details()
y.Data('sri',24,'vja')
y.display()
z=Details()
z.Data('gayathri',22,'vja')
z.display()'''

#object intialization
'''class Details:
    #creating a constructor
    def __init__(se,n,a,p):
        se.n=n
        se.a=a
        se.p=p
    def display(se):
        print(se.n,se.a,se.p)
x=Details('om',24,'vja')
print(dir(x))
x.display()'''


'''class Details:
    
    def __init__(se,n,a,p):
        se.n=n
        se.a=a
        se.p=p
    def display(se):
        print(se.n,se.a,se.p)
n=input()
a=int(input())
p=input()
x=Details(n,a,p)
print(dir(x))
x.display()'''


'''class Details:
    
    def __init__(se):
        se.n=input()
        se.a=int(input())
        se.p=input()
    def display(se):
        print(se.n,se.a,se.p)
x=Details()
print(dir(x))
x.display()'''

'''class Details:
    
    def __init__(se,n,a,p):
        se.n=n
        se.a=a
        se.p=p
    def display(se):
        print(se.n,se.a,se.p)
x=Details(input(),int(input()),input())
print(dir(x))
x.display()'''


#difference between _ and __
'''class employee():
    def __init__(se):
        se.n='gayathri'
        se._mail='gayathri@codegnan.com' #here _ doesnot raise any error even if we call
        #it directly and doesnot treated as sny special char
        se.__sal=10000 #here __ raises any error even if we call it directly and doesnot treated as sny special char to
        overcome that we use _class name__variable
x=employee()
print(dir(x))
print(x.n)
print(x._mail)
print(x._employee__sal)'''


class employee():
    def __init__(se):
        se.n='gayathri'
        se._mail='gayathri@codegnan.com'
        se.__sal=70000
class employee1():
    def __init__(se):
        se.n='kusuma'
        se._mail='kusuma@codegnan.com'
        se.__sal=60000
class employee2():
    def __init__(se):
        se.n='dathri'
        se._mail='dathri@codegnan.com'
        se.__sal=50000
x=employee()
print(dir(x))
print(x.n)
print(x._mail)
print(x._employee__sal)
y=employee1()
print(y.n)
print(y._mail)
print(y._employee1__sal)
y=employee2()
print(y.n)
print(y._mail)
print(y._employee2__sal)

