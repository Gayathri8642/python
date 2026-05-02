#built in functions

'''print("Hello World")


a=[23,65,98,45,92]
print(max(a))
a=[64,89,12,35,45,99]
print(min(a))
a=(56,95,78,32,61,54)
print(sum(a))
a=[64,89,12,35,45,99]
print(sorted(a))

a=list(map(int,input("enter values").split()))
print(len(a))
a=int(input())
b=int(input())
print(pow(a,b))
print(type(a))
a=20
for i in range(a):
    print(i)'''



'''print(dir())
print(dir(__builtins__))'''

#fromkeys
'''a="codegnan"
print(a)
print(type(a))
print(list(a))
print(tuple(a))
print(set(a))
#we cannot convert directly into dictionery so we use fromkeys
b=dict.fromkeys(a)
print(b)
b=dict.fromkeys(a,"gayathri")
print(b)
b[a]="twisha"
print(b)
b["a"]="twisha"
print(b)'''


#eval()-->it accepts any type data but we have to give string value in quotes
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''


#zip()-->we can combine multiple collections into one collection and for built in function we should definitely use datatype

'''a=[10,20,30,40,50]
b=["gayathri","twisha","sai","leela","veera"]

print(a+b)

c=list(zip(a,b))
print(c)

c=tuple(zip(a,b))
print(c)

c=set(zip(a,b))
print(c)

c=dict(zip(a,b))
print(c)'''



#enumerate()-->we can give counter to the collection and we can also give values
'''a=["satyanarayana","kalyani","haranatha","pravaksha"]
for i in range(len(a)):
    print(i,a[i])'''

'''a=["satyanarayana","kalyani","haranatha","pravaksha"]
b=dict(enumerate(a))
print(b)

b=dict(enumerate(a,101))
print(b)'''


'''for i in range(ord('a'),ord('z')+1):
    print(chr(i),end="")

for i in range(ord('A'),ord('Z')+1):
    print(chr(i),end="")'''


'''for i in range(97,123):
    print(chr(i),end=" ")

for i in range(65,91):
    print(chr(i),end=" ")'''


'''n=input()
for i in range(len(n)):
    print(n[i],ord(n[i]))'''

n=input()
for i in n:
    print(i,ord(i))
    


