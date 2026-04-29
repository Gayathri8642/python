#function
'''a=20
b=10
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is ",a*b)
a=200
b=100
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is ",a*b)
a=2000
b=1000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is ",a*b)'''


'''def cal(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is ",a*b)
cal(10,20)
cal(100,200)
cal(1000,2000)'''

'''def cal(a,b):
    print("the int div is",a//b)
    print("the power is",a**b)
    print("the remainder is ",a%b)
cal(20,10)
cal(200,2)
cal(20,10)'''

'''def add(a,b):
    print("the sum is",a+b)
add(4,5)'''


'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def full():
    fnam=input("1st name")
    lnam=input("2nd name")
    print((fnam+" "+lnam).title())
full()'''

#print v/s return
'''def sub(a,b):
    print(a-b)
sub(3,8)

def sub(a,b):
    return(a-b)
print(sub(3,8))'''

'''def call(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
call(6,8)'''
#here return only gives value of 1st one because after that the function is called off
'''def call(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(call(6,8))'''


'''def call(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(call(6,8))'''



#task
#split bill
'''while True:
    def div():
        b=int(input('how much bill'))
        p=int(input('how many persons'))
        return b/p
    print(div())'''



'''while True:
    def div():
        b=int(input('how much bill'))
        p=int(input('how many persons'))
        c=b/p
        print(f'{c}')
    div()'''


'''while True:
    def div():
        b=int(input('how much bill'))
        p=int(input('how many persons'))
        c=b/p
        print('{}'.format(c))
    div()'''



'''while True:
    def div():
        b=int(input('how much bill'))
        p=int(input('how many persons'))
        print(f'{b/p}')
    div()'''


'''while True:
    def div():
        b=int(input('how much bill'))
        p=int(input('how many persons'))
        print('{}'.format(b/p))
    div()'''

#task
'''def sk():
    a=int(input('a value'))
    b=int(input('b value'))
    o=int(input('what do you want to do  1.add2.sub 3.mul'))
    if o==1: 
        print('sum is',a+b)
    elif o==2:
        print('diff is',a-b)
    elif o==3:
        print('sum is',a*b)
sk()'''
        
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input('a value'))
    b=int(input('b value'))
    o=int(input('what do you want to do  1.add2.sub 3.mul'))
    if o==1: 
        add()
    elif o==2:
        sub()
    elif o==3:
        mul()'''



#application


def ticketprice():
    g=input('enter your gender male or female :')
    a=int(input('enter your age'))
    if g=="male" and a>=60:
        p=1000*(30/100)
        p=1000-p
        print(p)
    elif g=="male" and a<60:
        print(1000)
    elif g=='female' and a>=60:
        p=1000*(50/100)
        p=1000-p
        print(p)
    elif g=='female' and a<60:
        p=1000*(30/100)
        p=1000-p
        print(p)
ticketprice()











