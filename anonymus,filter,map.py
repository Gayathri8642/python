#anonymus functions(nameless function)

'''def mul(x):
    print((2*x)+5)
mul(5)'''


'''def mul(x):
    print((2*x)+5)
x=int(input())
mul(x)'''

#syntax
#a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))


b=int(input())
a=lambda x:2*x+5
print(a(b))'''

'''a=lambda b,c:b-c
print(a(5,4))


b=int(input())
c=int(input())
a=lambda b,c:b-c
print(a(b,c))'''


'''a="codegnan"
c=lambda a:a.upper()
print(c(a))

a=input()
c=lambda a:a.upper()
print(c(a))

b="python course"
c=lambda b:b.title()
print(c(b))

b=input()
c=lambda b:b.title()
print(c(b))'''


'''f=input("first name")
l=input("last name")
fn=lambda f,l:(f+" "+l).title()
print(fn(f,l))'''

'''f,l=[x for x in input("enter the names").split(",")]
fn=lambda f,l:(f+" "+l).title()
print(fn(f,l))'''

#filter()
'''a=[2,5,7,9,10,12,16,18,20]
b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),{},set()
'''c=[[],(),set(),{},"",None,1,"a",2.6,3+4j,True,False]#it remooves empty datatypes 
b=list(filter(None,c))
print(b)'''

#map()

'''a=[2,3,6,4,8,9,10,15,69]
b=[1,4,5,8,9,8,62,45,68,95]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''

'''a=input()
b=input()
print(a+b)'''

'''a,b=input().split()
print(a+b)'''

'''a,b=[x for x in input().split(",")]
print(a+b)'''

'''a=int(input())
b=int(input())
print(a+b)'''

'''a,b=[int(x) for x in input().split()]
print(a+b)'''

'''a,b=int(input().split())
print(a+b)#it gives error'''

'''a,b=map(int,input().split())
print(a+b)'''


'''a,b=map(str,input().split())
print(a+b)'''

'''a=list(map(int,input().split()))
print(a)
print(type(a))'''

'''a=tuple(map(int,input().split()))
print(a)
print(type(a))'''

'''a=set(map(int,input().split()))
print(a)
print(type(a))'''

'''a=list(map(eval,input().split()))
print(a)
print(type(a))'''

'''n=int(input())
u = {input("Keys:"):input("Values:") for _ in range(n)}
print(u)'''

a=input('enter the key and value pairs')
b=dict(i.split(':') for i in a.split(" "))
print(b)





