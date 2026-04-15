Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={3,5.6,'king',True}
print(a)
{'king', True, 3, 5.6}
type(a)
<class 'set'>
b={7,8,9,10,11,16}
type(b)
<class 'set'>
b
{16, 7, 8, 9, 10, 11}
b.add(59)
b
{16, 7, 8, 9, 10, 11, 59}
b={7,8,9,7,8,8,9,10}
b
{8, 9, 10, 7}
c={'h',6,55,2.9}
d={6,55}
b.issubset(a)
False
d.issubset(c)
True
c.issuperset(d)
True
d.issuperset(c)
False
d.difference(c)
set()
d
{6, 55}
a={95,'oki','mnop',156}
c.difference(d)
{'h', 2.9}
c
{'h', 2.9, 6, 55}
a={95,'oki','mnop',156}
b={99,58,'oki',516}
a.union(b)
{99, 516, 'mnop', 'oki', 58, 156, 95}
a.intersection(b)
{'oki'}
b.difference(a)
{58, 99, 516}
a.difference(b)
{'mnop', 156, 95}
a={1,2,3,4,5,6,7}
b={'mine',84,64,7,8,9,6,5,4}
a.update(b)
a
{64, 1, 2, 3, 4, 5, 6, 7, 'mine', 8, 9, 84}
a.isdisjoint()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.isdisjoint()
TypeError: set.isdisjoint() takes exactly one argument (0 given)
a.isdisjoint(b)
False
b.isdisjoint(a)
False
c=
SyntaxError: invalid syntax
c={'c','cde',96,36,1.5}
d={'c','cde',956,369,458,6.5}
c.symmetric_difference(d)
{1.5, 6.5, 458, 96, 36, 369, 956}
a={1,2,3,4,5,6,7}
b={84,64,7,8,9,6,5,4}
a.difference_update(b)
a
{1, 2, 3}
>>> b.difference_update(a)
>>> b
{64, 4, 5, 6, 7, 8, 9, 84}
>>> a={1,2,3,4,5,6,7}
>>> b={84,64,7,8,9,6,5,4}
>>> a.intersection_update(b)
>>> a
{4, 5, 6, 7}
>>> b.intersection_update(a)
>>> b
{4, 5, 6, 7}
>>> a={1,2,3,4,5,6,7}
>>> b={84,64,7,8,9,6,5,4}
>>> a.symmetric_difference_update(b)
>>> a
{64, 1, 2, 3, 8, 9, 84}
>>> b.symmetric_difference_update(a)
>>> b
{1, 2, 3, 4, 5, 6, 7}
>>> b={84,64,7,8,9,6,5,4}
>>> b.pop()
64
>>> b.pop(6)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b.pop(6)
TypeError: set.pop() takes no arguments (1 given)
>>> KeyboardInterrupt
>>> b.remove(6)
>>> b
{4, 5, 7, 8, 9, 84}
>>> c={'h',6,55,2.9}
>>> c.discard(6)
>>> c
{'h', 2.9, 55}
>>> d=c.copy()
>>> d
{'h', 2.9, 55}
>>> d.clear()
>>> d
set()
>>> b=set()
>>> b.add(98989)
>>> b
{98989}
