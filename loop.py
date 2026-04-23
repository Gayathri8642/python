
#loops
#for,while,range,break,continue,pass

#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=(5,6,7,8,9,10)
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a={3,5,4,9,8,7,12}
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a={"name":"gayathri","year":2026,"month":"april"}
for i in a:
    print(i)
print(type(a))
print(type(i))
for i in a.keys():
    print(i)
print(type(a))
print(type(i))
for i in a.values():
    print(i)
print(type(a))
print(type(i))
for i in a.items():
    print(i)
print(type(a))
print(type(i))'''

'''a="codegnan"
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a=[1.2,3.6,6.3,4.6,64.99]
for i in a:
    print(i)
print(type(a))'''

'''a=['a','b','c','d','e']
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(True,False)
for i in a:
    print(i)
print(type(a))'''

'''a=[3+6j,9+8j]
for i in a:
    print(i)
print(type(a))
print(type(i))'''


#task 
'''a=["codegnan","python","course"]
for i in a:
    print(i.upper(),end="")'''
    
'''a=["codegnan","python","course"]
b=str(a)
c=b.upper()
print(c)'''


'''#student
a=int(input())
if a>=91 and a<=100:
    print(" grade A")
elif a>=81 and a<=90:
    print(" grade B")
elif a>=71 and a<=80:
    print(" grade C")
elif a>=51 and a<=70:
    print(" grade D")
elif a<=50:
    print("FAIL")'''



#while loop
'''a=10
while a<1:
    print("true")'''

'''a=10
while a>1:
    print("true")'''

'''a=10
while a<1:
    print("a")'''

'''a=10
while a>=1:
    print("true")'''

'''a=60
while a<30:
    a=a-1
    print("a")'''

'''a=60
while a<30:
    print("a")
    a=a-1'''


'''a=10
while a>30:
    print("a")
    a=a+1'''

'''a=10
while a>30:
    a=a+1
    print("a")'''

'''a=10
while a>30:
    a+=1
    print("a")'''

'''a=10
while a>30:
    print("a")
    a+=1'''

'''while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible for vote")
    else :
        print("not eligible for vote")'''
    



'''while True:
    num=int(input("enter the number"))
    if num%2==0:
        print("even")
    else :
        print("odd")'''

#range
#start-stop-step

'''for i in range(5):
    print(i)'''
    

'''for i in range(5,15):
    print(i)'''


'''for i in range(2,20,2):
    print(i,end=",")'''


'''for i in range(5,50,5):
    print(i,end=",")'''

'''for i in range(0,30,3):
    print(i,end=",")'''

'''while True:
    a=int(input('enter marks'))
    if a in range(91,101):
        print("A")
    elif a in range(81,91):
        print("B")
    elif a in range(71,81):
        print("C")
    elif a in range(51,71):
        print("D")
    else:
        print("Fail")'''


#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''
        
'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''

'''for i in range(20):
    if i==12:
        break
    print(i)'''
          

#continue
'''a=20
while a>5:
    print(a)
    a=a-1
    if a==20:
        continue'''


'''a=20
while a>5:
    a=a-1
    if a==20:
        continue
    print(a)'''


'''for i in range(20):
    if i==12:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=='t':
        break
    print(i)'''


'''a="python"
for i in a:
    if i=='t':
        continue
    print(i)'''


#pass
'''a=40
while a>10:
    print(a)
    a=a-1
    if a==15:
        pass'''


for i in range(40):
    if i==20:
        pass
    print(i)
    
    









    
