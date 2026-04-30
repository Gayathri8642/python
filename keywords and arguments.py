#keyword and positional arguments
'''def details(id,name,mailid):
    id=10
    name='gayathri'
    mailid='g@gmail.com'
    print(id,name,mailid)
details(id="id",name='name',mailid='mailid')'''


'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name='name',mailid='mailid')
details(id=20,name='twisha',mailid='t@gmail.com')
details(30,'leela','l@gmail.com')
details('veera','v@gmail.com',40)
details(name='satyanarayana',mailid='s@gmail.com',id=50)'''

#default arguments
'''def grocery(item,price):
    print("item is %s"%item)
    print('price is %f'%price)
grocery('sugar',100)'''

'''def grocery(item='rice',price=2000):
    print("item is %s"%item)
    print('price is %f'%price)
grocery()'''

'''def grocery(item,price=500):
    print("item is %s"%item)
    print('price is %f'%price)
grocery("ghee")'''


#non default follows default argument(gives error)
'''def grocery(item='dal',price):
    print("item is %s"%item)
    print('price is %f'%price)
grocery(300)'''


'''def grocery(cake,price,qty):
    print("cake is %s"%cake)
    print('price is %f'%price)
    print('qty is %i'%qty)

grocery('brownie',1000,2)  


def grocery(cake='strawberry',price=700,qty=3):
    print("cake is %s"%cake)
    print('price is %.2f'%price)
    print('qty is %i'%qty)

grocery() 


def grocery(cake,price=700,qty=3):
    print("cake is %s"%cake)
    print('price is %.2f'%price)
    print('qty is %i'%qty)

grocery("chocolate")'''

'''def grocery(cake="blackforest",price,qty):
    print("cake is %s"%cake)
    print('price is %.2f'%price)
    print('qty is %i'%qty)

grocery(700,6)'''


# *arguments
'''a=[2,3,4,5,6,7,8,9]
print(a)
print(*a)'''

'''b=(1,2,3,4)
print(b)
print(*b)'''

'''c={6,8,7,9,10}
print(c)
print(*c)'''

'''d={'c':'tup','b':'set'}
print(d)
print(*d)'''

'''a='codegnan'
print(a)
print(*a)'''

'''a,b,c=1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)'''#raises a value error


'''*a,b,c=1,2,3,4,5,6,7,8,9
print(*a)
print(b)
print(c)'''


'''a,*b,c=1,2,3,4,5,6,7,8,9
print(a)
print(*b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#raises a value error


'''a,b,c="cod"
print(a)
print(b)
print(c)'''


'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''



#task

#body mass index
while True:
    w=float(input("enter weight"))
    h=float(input("enter height"))
    b=w/(h*h)
    if b<18.5:
        print("Under weight")
    elif b>=18.5 and b<=24.50:
        print("Healthy weight")
    elif b>24.5 and b<=29.50:
        print("Over weight")
    elif b>30:
        print("Obesity")
    else :
        print("no comments")

















































    
