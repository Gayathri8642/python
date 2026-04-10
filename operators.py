Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithematic operators
a=2
b=8
print(a+b)
10
print(a-b)
-6
print(a*b)
16
print(a//b)
0
print(a/b)
0.25
print(a**b)
256
print(a%b)
2
#assignment operators
a=8
b=9
print(a+=b)
SyntaxError: invalid syntax
b+=a
b
17
print(b)
17
a
8
b-=7
b
10
b*=5
b
50
b//=10
b
5
b/=6
b
0.8333333333333334
b%=2
b
0.8333333333333334
b**=2
b
0.6944444444444445
a+-=7
SyntaxError: invalid syntax
a+=7
a
15
a-=9
a
6
a*=9
a
54
a//=4
a
13
a/=4
a
3.25
a%=4
a
3.25
a**=2
a
10.5625
#comparision operators
a=9
b=9
c=12
a<c
True
c>a
True
c<=a
False
c>=a
True
a<=c
True
a>=c
False
a>c
False
c<a
False
c!=a
True
b!=a
False
c==a
False
a==b
True
a==c
False
#logical operators
a=9
b=11
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b<=a
True
a!=b or a==b
True
not True
False
not False
True
#identify operators
a=6
if type(a) is int:
    print("it is int")

    
it is int
b=6.5
if type(b) is int :
    print("true")

    
if type(b) is not int :
    print("true")

    
true
#membership operators
a=2,8,3,4,5,6,7,9
if 5 in a:
    print(5)

    
5
if  in a:
    print(5)
    
SyntaxError: invalid syntax
if  10 in a:
    print(10)

...     
>>> if 10 not in a:
...     print (10)
... 
...     
10
>>> #bitwise operators
>>> a=9
>>> b=78
>>> a&b
8
>>> a=6
>>> b=8
>>> bin(a)
'0b110'
>>> bin(b)
'0b1000'
>>> a&b
0
>>> a|b
14
>>> a^b
14
>>> a=4
>>> b=8
>>> bin(4)
'0b100'
>>> bin(b)
'0b1000'
>>> a^b
12
>>> a~b
SyntaxError: invalid syntax
>>> ~a
-5
>>> a<<2
16
>>> a>>6
0
