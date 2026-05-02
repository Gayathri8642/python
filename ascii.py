Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #ASCII-->american standard code information interchange
... #chr(),ord()
>>> chr(30)
'\x1e'
>>> chr(90)
'Z'
>>> 
>>> chr(65)
'A'
>>> chr(91)
'['
>>> ord('a')
97
>>> ord('z')
122
>>> ord(350)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ord(350)
TypeError: ord() expected string of length 1, but int found
