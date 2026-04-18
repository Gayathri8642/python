#Conditions
#if, else, elif
#if, if-elif, if-else, if-elif-else, nested-if, multiple-if, multiple-elif
#identity, logical, comparison, and membership operators are used for conditions

#if condition by using comparison operators <,>,<=,>=,!=,==

'''a=2
b=4
if a<b:
    print("true")'''

'''a=2
b=5
if a>b:
    print("true")'''

'''a=5
b=10
if a<=b:
    print("a<b")'''

'''a=7
b=11
if b>=a:
    print('True')'''

'''a=2
b=4
if a!=b:
    print("Not equal")'''

'''a=10
b=10
if a==b:
    print("Equal")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a<b:
    print("a<b")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a>b:
    print("a>b")'''

'''a=int(input("a value:"))
if a>=23:
    print("True")'''

'''a="python"
if a=="java":
    print("True")'''

'''a="python"
if a=="python":
    print("True")'''

'''a=input("name:")
if a=="bhanu":
    print("True")'''

#if condition by using logical operators and, or, not

'''a=9
b=12
if a<b and b>a:
    print("True")'''

'''a=9
b=12
if a<=b and b>=a:
    print("True")'''

'''a=20
b=30
if a!=b and b==a:
    print("True")'''

'''a=9
b=12
if a<b or b>a:
    print("True")'''

'''a=9
b=12
if a<=b or b>=a:
    print("True")'''

'''a=9
b=12
if a!=b or b==a:
    print("True")'''

'''a=9
b=12
if not a<b:
    print("true")'''

'''a=9
b=12
if not a>b:
    print("True")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a<b and b>a:
    print("True")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a!=b or b>=a:
    print("True")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if not b>a:
    print("True")'''

#if condition by using identity operators   is, is not

'''a=9
if type(a) is int:
    print("it is integer")'''

'''a=9
if type(a) is not int:
    print("it is int")'''

'''a=float(input("value:"))
if type(a) is float:
    print("it is float")'''

'''a=float(input("value:"))
if type(a) is not float:
    print("it is float")'''

'''a=str(input("value:"))
if type(a) is str:
    print("it is string")'''

'''a=complex(input("value:"))
if type(a) is complex:
    print("It is complex")'''

#if condition by using membership operators  in, not in

'''a=[3,4,5,6,7,8,9]
if 7 in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9]
if 7 not in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9]
if 10 not in a:
    print("true")'''

'''a=list(map(int,input("Enter list elements:").split(',')))
b=int(input())
if b in a:
    print("True")'''
    
'''a=list(map(int,input("Enter list elements:").split(',')))
b=int(input())
if b not in a:
    print("True")'''

'''a=set(map(int,input("Enter values:").split()))
b=set(map(int,input("Enter values:").split()))
z=a.union(b)
print(z)'''
