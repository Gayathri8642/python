Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int
int(8)
8
int(8.5)
8
int("python")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(8+8j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(8+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
>>> float(5)
5.0
>>> float(5.6)
5.6
>>> float("python")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
>>> float(5+5j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(5+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> str(5)
'5'
>>> str(5.6)
'5.6'
>>> str("python")
'python'
>>> str(5+10j)
'(5+10j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> complex(9)
(9+0j)
>>> complex(9.6)
(9.6+0j)
>>> complex("python")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
bool(5)
True
bool(9.5)
True
bool("python")
True
bool(True)
True
bool(False)
False
