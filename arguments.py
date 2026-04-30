#variable length arguments
'''def c(*a):
    print(a)
    print(type(a))
c()
c(2,3,4,5,6)
b=[5,6,7,8,9]
c(*b)
d={3,4,5,6,7}
c(*d)
e={"name":"kalyani","n":"kusuma"}
c(*e)'''


'''def c1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)        
c1()
c1(2,3,4,5,6,7)
c1(2,3.4,4,6.2,5,3)
c1(1,2,3,4,5.3,6.2,"dhatri")'''
#we get error where we string until then the numbers will be added so we need to write condition by usind typecasting

'''def c1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
c1(1,2,3,4,5.3,6.2,"dhatri")'''
