Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
a={'name':'gayathri','year':2025,'month':12}
a
{'name': 'gayathri', 'year': 2025, 'month': 12}
print(a)
{'name': 'gayathri', 'year': 2025, 'month': 12}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['gayathri', 2025, 12])
a.items()
dict_items([('name', 'gayathri'), ('year', 2025), ('month', 12)])
a={'y':2026,'m':4,'d':16}
a['y']
2026
a[2026]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a[2026]
KeyError: 2026
a.update({'t':6})
a
{'y': 2026, 'm': 4, 'd': 16, 't': 6}
a.update({'h':7,'mi':35})
a
{'y': 2026, 'm': 4, 'd': 16, 't': 6, 'h': 7, 'mi': 35}
a={'name':'gayathri','mail':'ggtslv@gmail.com'}
a.setdefault("city","vja")
'vja'
a
{'name': 'gayathri', 'mail': 'ggtslv@gmail.com', 'city': 'vja'}
a.pop('name')
'gayathri'
a
{'mail': 'ggtslv@gmail.com', 'city': 'vja'}
b={'y': 2026, 'm': 4, 'd': 16, 't': 6}
b.popitem()
('t', 6)
b.popitem(16)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.popitem(16)
TypeError: dict.popitem() takes no arguments (1 given)
>>> a.copy()
{'mail': 'ggtslv@gmail.com', 'city': 'vja'}
>>> a
{'mail': 'ggtslv@gmail.com', 'city': 'vja'}
>>> a.get('city')
'vja'
>>> a
{'mail': 'ggtslv@gmail.com', 'city': 'vja'}
>>> a.clear()
>>> a
{}
>>> a.update({'n':'gayathri'})
>>> a
{'n': 'gayathri'}
>>> a.copy(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.copy(c)
NameError: name 'c' is not defined
>>> c={'y': 2026, 'm': 4, 'd': 16}
>>> c={'y': 2026, 'm': 4, 'd': 16,'d':16}
>>> c
{'y': 2026, 'm': 4, 'd': 16}
>>> KeyboardInterrupt
>>> c={'y': 2026, 'm': 4, 'd': 16,'d':15}
>>> c
{'y': 2026, 'm': 4, 'd': 15}
>>> c={'y': 2026, 'm': 4, 'd': 16,'d1':16}
>>> c
{'y': 2026, 'm': 4, 'd': 16, 'd1': 16}
>>> a={'i':[1,2,3,4],'n':['gayathri','kusuma','dhatri']}
>>> print(a)
{'i': [1, 2, 3, 4], 'n': ['gayathri', 'kusuma', 'dhatri']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['i', 'n'])
>>> a.values()
dict_values([[1, 2, 3, 4], ['gayathri', 'kusuma', 'dhatri']])
a
>>> .items()
SyntaxError: invalid syntax
>>> a.items()
dict_items([('i', [1, 2, 3, 4]), ('n', ['gayathri', 'kusuma', 'dhatri'])])
