#regular expression(regex)
'''a='codegnan is in vja'
print(a)

b='codegnan\nis\tin\nvja'
print(b)

#rstring
a=r'codegnan\nis\tin\nvja'
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents whitespaces
\S->it represents non-whitespaces'''

#compile()
'''import re
a='cap cash map money mother max demo doctor dog cup'
b=re.compile(r'm\w\w\w')
print(b)

#search
c=b.search(a)
print(c)

b=re.search(r'm\w+',a)
print(b)'''

#findall
'''c=re.findall(r'm\w+',a)
print(c)
print(*c)

b=re.search(r'map',a)
print(b)'''

'''c=re.findall(r'c\w+',a)
print(*c)


c=re.findall(r'd\w+',a)
print(*c)'''

#split()
'''d=re.split(r'm',a)
print(d)

d=re.split(r'\s',a)
print(d)

#sub()
e=re.sub(r'm','a',a)
print(e)


e=re.sub(r'mother','father',a)
print(e)'''


'''d='12 36 95 87 45 63 21 54 987'
e=re.search(r'9\d+',d)
print(e)
print('-----------')
c=re.findall(r'2\d',d)
print(*c)
print('-----------')
a=re.split(r'6\d',d)
print(a)
print('-----------')
g=re.split(r'\D',d)
print(g)
print('-----------')
b=re.sub(r'2','7',d)
print(b)
print('-----------')'''



#error handling
#syntax error
'''for i in range(10):
print(i)'''

#run_time error
'''a=int(input('a value'))
b=int(input('b value'))
print(a//b)'''


#logical error

'''a=10
b=20
print(a-b)'''

'''a=3
b=7
if a>b:
    print('less')'''


#exception handling
'''while True:
    a=int(input('a value'))
    b=int(input('b value'))
    try :
        c=a//b
        print(c)
    except:
        print('exception is raised')
    else:
        print('no exceptions')
    finally:
        print('the program ends here...............')'''
