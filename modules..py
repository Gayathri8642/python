#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.log(10))
print(math.sin(30))
print(math.cos(60))
print(math.pow(2,3))
print(math.asin(-1))
print(math.acos(-1))
print(math.tan(1))#here it doesnot give exact values as in trignometry but gives decimal values
print(math.ceil(5.8))#it round of to next highest value
print(math.floor(5.8))#it gives by removing decimal

#here we use from so we dont need to import always
from math import pi,log,sqrt
print(pi)
print(sqrt(7))
print(log(10))'''


#sys module
'''import sys
print(sys.path)
for i in sys.path:
    print(i)
print(sys.version)'''

#os module
'''import os
print(os.path)
print(os.getcwd())#cwd -> current working directory
print(os.listdir())
os.mkdir('om')#makes new directory
print(os.listdir())'''


#random module
'''import random
a=random.sample(range(10,30),5)#it prints required number of numbers randomly suppose here 5
print(a)

#randint()
import random
a=random.randint(20,30)
print(a)#randint prints only 1 number

#choice()
import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)#here it picks value from given'''


#task ->dice code
'''import random
while True:
    a=int(input("print the roll of dice"))
    b=random.randint(1,6)
    print(b)
    o=int(input("1.yes    2.no"))
    if o==1:
        continue
    else:
        break'''

