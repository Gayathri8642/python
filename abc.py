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
n=5
for i in range(0,n+1):
    print(' '*(n-i)+'*'*i+' '*(n-i))
    
   
    
    










































