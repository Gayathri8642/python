Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[9,9.0,'xyz',3+1j,True]
print(a)
[9, 9.0, 'xyz', (3+1j), True]
type(a)
<class 'list'>
a.append("ok")
print(a)
[9, 9.0, 'xyz', (3+1j), True, 'ok']
a.append('kijigh','sdhuhu')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.append('kijigh','sdhuhu')
TypeError: list.append() takes exactly one argument (2 given)
a.append['kijigh','sdhuhu']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.append['kijigh','sdhuhu']
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append(['kijigh','sdhuhu'])
print(a)
[9, 9.0, 'xyz', (3+1j), True, 'ok', ['kijigh', 'sdhuhu']]
a.extend(['html','css'])
print(a)
[9, 9.0, 'xyz', (3+1j), True, 'ok', ['kijigh', 'sdhuhu'], 'html', 'css']
a.insert(1,89)
print(a)
[9, 89, 9.0, 'xyz', (3+1j), True, 'ok', ['kijigh', 'sdhuhu'], 'html', 'css']
print(a[1:4])
[89, 9.0, 'xyz']
a=['python','java','c']
a.index('java')
1
a.copy()
['python', 'java', 'c']
a.clear()
a
[]
a.append('hii')
a
['hii']
a=['banana','apple','grapes','custard apple','dragon']
a.sort()
a
['apple', 'banana', 'custard apple', 'dragon', 'grapes']
b=[9,6,7,5,8,6,4]
b.sort()
b
[4, 5, 6, 6, 7, 8, 9]
a.reverse()
>>> a
['grapes', 'dragon', 'custard apple', 'banana', 'apple']
>>> b.reverse()
>>> b
[9, 8, 7, 6, 6, 5, 4]
>>> c=['red','black','white']
>>> c.pop()
'white'
>>> c
['red', 'black']
>>> c.pop("red")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c.pop("red")
TypeError: 'str' object cannot be interpreted as an integer
>>> c.pop(0)
'red'
>>> c
['black']
>>> g=['ghee','butter','milk']
>>> g.remove()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    g.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> g.remove("milk")
>>> g
['ghee', 'butter']
>>> g.count('e')
0
>>> g.count('ghee')
1
>>> len(g)
2
>>> #tuple
>>> a=(3,4.5,'python',3+4j,True)
>>> print(a)
(3, 4.5, 'python', (3+4j), True)
>>> type(a)
<class 'tuple'>
>>> a.count('3')
0
>>> a.count(3)
1
>>> a.index(4.5)
1
