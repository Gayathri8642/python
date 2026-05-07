#calendar module
'''import calendar
a=2026
m=6
print(calendar.month(a,m))

import calendar
a=2026
print(calendar.calendar(a))'''

'''import calendar
m=int(input('enter month'))
y=int(input('enter year'))
print(calendar.month(y,m))'''

#date and time
'''from datetime import date
a=date.today()
print(a)'''


'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import datetime
a=datetime.date.today().isocalendar()[1]
print(a)
import datetime
a=datetime.date.today().isoweekday()
print(a)'''

#unix time to human readable time
'''import time
a=time.time()#unix or epoch time
print(a)
b=time.localtime(a)
print(b)
print(f'today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}')
print(time.ctime())#this gives current time like (Thu May  7 16:24:49 2026)
print(time.asctime())
print(f'today date is {b.tm_hour}-{b.tm_min}-{b.tm_sec}')
print(f'today date is {b.tm_mday}-{b.tm_yday}-{b.tm_isdst}')'''


#task
'''import random
import time
a=random.sample(range(10),10)
for _ in a :
    print(_)
    time.sleep(2)

import random
import time
a=random.randint(1000,9999)
for _ in range(10):
    print(_)
    time.sleep(2)'''

#task
'''while True:
    n=int(input('Number of students'))
    p=0
    m=0
    for _ in range(n):
        a=input(f'student{_+1}:').lower()
        if a=='p':
            p+=1
        elif a=='a':
            m+=1
        else:
            pass
    print(f'Total students {n}')
    print(f'Presentees {p}')
    print(f'absentees {m}')
    o=int(input("do you want to continue 1.Continue 2.No"))
    if o==1:
          continue
    else:
        break'''


