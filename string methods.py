Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=' '
len()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
len(d)
1
#count()
g="twinkle twinkle little star"
a.count("twinkle")
0
g.count("twinkle")
2
g.count('a')
1
#find a string
a="gayathri"
a.find("a")
1
a.find("g")
0
a.find("w")
-1
#escape sequences
#\n->new line
#\t-> tab spaces (4-8)
a="name\nmobile no\tmailid\naddress"
\
print(a)
name
mobile no	mailid
address
a="name\nmobile no\tmailid\naddress"
print(a)
name
mobile no	mailid
address
b="name:Gayathri\nmobile no:2598746315\tmailid:gahyfg@gmail.com\naddress:vjrg"
print(b)
name:Gayathri
mobile no:2598746315	mailid:gahyfg@gmail.com
address:vjrg
















#replace
a="work until you succeed"
a.replace("work","wait")
'wait until you succeed'
a.replace("a","i")
'work until you succeed'
a.replace("o","a")
'wark until yau succeed'
#upper

#upper
a="python"
a="python"
a.upper()
'PYTHON'
b="GAYATHRI"
b.lower()
'gayathri'
a.capitalize()
'Python'
c="gayathri twisha"
c.title()
'Gayathri Twisha'
a.isupper()
False
a.islower()
True
a.startswith("p")
True
a.endswith("g")
False
a.isalpha()
True
b="alkaline basic"
b.isalpha()
False
c="alkalinebasic"
b.isalpha()
False
c.isalpha()
True
d=12345
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="12345"
d.isdigit()
True
\
e="alkaline12"
e.isalnum()
True
f="alkaline 12"
f.isalnum()
False
#split
a='python java c c++'
a.split()
['python', 'java', 'c', 'c++']
b='123456 45689'
b.split()
['123456', '45689']
#join
z="gay","ath","ri"
"".join(z)
'gayathri'
" ".join(z)
'gay ath ri'
#srip
#lsrip(),rstrip()
a='            gayathri         '
a.strip()
'gayathri'
a.lstrip()
'gayathri         '
a.rstrip()
'            gayathri'
#concatenation
a='python'
b='course'
print(a+b)
pythoncourse
print(a+""+b)
pythoncourse
print(a+" "+b)
python course
fname="gayathri"
sname="twisha"
print(fname+" "+sname)
gayathri twisha
print((fname+" "+sname).title())
Gayathri Twisha
print((fname.title()+" "+sname.title())

print(fname.title()+" "+sname.title())
      
SyntaxError: '(' was never closed
print(fname.title()+" "+sname.title())
...       
Gayathri Twisha
>>> #formatting
...       
>>> a=8
...       
>>> b=9
...       
>>> print(a+b)
...       
17
>>> print("the sum is ",a+b)
...       
the sum is  17
>>> a="taduvai"
...       
>>> print("my native is ",a)
...       
my native is  taduvai
>>> #format method
...       
>>> a='motu'
...       
>>> b='patlu'
...       
>>> print("hello {} {}".format(a,b))
...       
hello motu patlu
>>> print("hello {} hello{}".format(a,b))
...       
hello motu hellopatlu
>>> print("hello {} hello{}".format(a,b))
...       
hello motu hellopatlu
>>> #fstring
...       
>>> a="chota"
...       
>>> b="bheem"
...       
>>> print(f"hello {a}{b}")
...       
hello chotabheem
>>> print(f"hello {a} {b}")
...       
hello chota bheem
