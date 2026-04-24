'''a=input("enter string")
if a[0:3]==a[-3:]:
    print("match ends")
else:
    print("not matched")'''

'''a=input("enter the string")
b=len(a)
N=b//2
if a[0:N]==a[-1:-(N+1):-1]:
    print("mirrored pattern")
else:
    print("not mirrored pattern")'''

#to exchange 1st and last two values  
'''a=input()
b=a.split()
c=len(b)
for i in range(c,0,-1):
    if i==c//2:
        pass
    print(b[i-1],end=" ")'''

'''inp = input().split()
a,b=inp[0],inp[1]
inp[0],inp[1] = inp[-1],inp[-2]
inp[-1],inp[-2]=a,b
print(inp)'''

#not to repeat the values without using sets
'''a=input().split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)'''

#write a program to find 1st non repeating character
'''a=input()
for i in a:
    if a.count(i)==1:
        print(i)
        break'''


#patterns
'''n=int(input())
for i in range(0,n):
    print('*'*n)'''
    
'''n = int(input())  
for i in range(1, n + 1):
    print(" "*(n-i)+'* '*i)'''
   
    
'''n=int(input())
for i in range(1,n+1):
    print(((10**i)//9)*i)'''

'''n=int(input())
for i in range(n,0,-1):
    print(' '*(n-i)+'* '*i)'''

#sum of first n natural numbers
'''n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''

#factorial of a number
'''n=int(input())
f=1
for i in range(1,n+1):
    f*=i
print(f)'''


# multiplication table
'''n=int(input())
for i in range(1,11):
    print(n,'*',i,'=',n*i)'''

#Reverse a number
'''n=int(input())
a=0
while n>0:
    d=n%10
    a=(a*10)+d
    n//=10
print(a)'''


#palindrome number
'''n=int(input())
m=n
a=0
while n>0:
    d=n%10
    a=(a*10)+d
    n//=10
if m==a:
    print("s")'''


#Count digits in a number
"""n=int(input())
count=0
a=0
while n>0:
    n//=10
    count+=1
print(count)"""


#Sum of digits
'''n=int(input())
a=0
while n>0:
    a+=n%10
    n//=10
print(a)'''


#Fibonacci series
'''a=0
b=1
n=int(input())
print(a,b,end=' ')
for i in range(0,n):
    c=a+b
    a,b=b,c
    print(c,end=' ')
print(c)'''

#Right-Angled Triangle
'''n=int(input())
for i in range(n+1):
    print('*'*i)'''
    
    
# Inverted Right Triangle

'''n=int(input())
for i in range(n,0,-1):
    print('*'*i)'''

#Pyramid Pattern
"""n=int(input())
for i in range(n+1):
    print(" "*(n-i),'* '*i)"""


#Number Triangle
'''n=int(input())
for i in range(n+1):
    for k in range(1,i+1):
        print(k,end=' ')
    print()'''


#Floyd’s Triangle
'''n=int(input())
num=1
for i in range(1,n+1):
    for k in range(i):
        print(num,end='')
        num+=1
    print()'''



#Diamond Pattern
'''n=int(input())
for i in range(n+1):
    print(' '*(n-i),'* '*i)

for i in range(n-1,0,-1):
    print(' '*(n-i),'* '*i)'''



#Hollow Square

'''n=int(input())
for i in range(n):
    if i==0 or i==(n-1):
        print('* '*n)
    else:
        print('*',' '*(n+1),'*')'''

#right triangle
'''n=int(input())
for i in range(n,0,-1):
    print(' '*(n-i),'*'*i)'''


#square
"""n=int(input())
for i in range(n):
    print("*"*n)"""


























