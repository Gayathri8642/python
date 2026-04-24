#multiple if conditionds using comparision
'''a=9
b=8
if a<b:
    print("greater")
if b<a:
    print('less')
if a==b:
    print("equal")'''


'''a=9
b=8
if a>b:
    print("greater")
if b<a:
    print('less')
if a==b:
    print("equal")'''


#multiple if conditionds using logical

'''a=91
b=23
if a<b and b>a:
    print('a is lesser')
if a>b or b<a:
    print('b is lesser')
if not a<b and b<a:
    print('b is only lesser')'''

'''a=91
b=23
if a>b or b>a:
    print('a is lesser')
if a>b or b<a:
    print('b is lesser')
if not a<b and b<a:
    print('b is only lesser')'''


#multiple if conditionds using identiy
'''a=94
b=95.6
if type(a)is int and type(b)is int:
    print('true both int')
if type(a)is int and type(b)is float:
    print('true')
if type(a)is not float or type(b)is not int:
    print('true for both')'''

'''a='no'
b='yes'
if type(a)is int and type(b)is int:
    print('true both int')
if type(a)is str and type(b)is str:
    print('true')
if type(a)is not float or type(b)is not int:
    print('true for both')'''

#multiple if conditionds using membership

'''a=[91,65,48,69,78]
if 26 in a:
    print('yes is there')
if 26 not in a:
    print('not there')
if 26 not in a and 48 in a:
    print('true')'''

'''a=['a','b','c','g','h']
if 'g' in a:
    print('yes is there')
if 'g' not in a or 'a' in a:
    print('not there')
if 'g' not in a and 'h' in a:
    print('true')'''


#nested if conditions usind comparision
'''a=5
b=10
if a<b:
    print('less')
    if b>a:
        print('greater')'''

'''a=10
b=26
if a>b:
    print("less")
    if b>a:
        print('greater')'''

'''a=10
b=2
if a>b:
    print("less")
    if b>a:
        print('greater')
    else :
        print("true")'''

'''a=10
b=26
if a>b:
    print("less")
    if b==a:
        print('greater')'''

'''a=10
b=26
if a>b:
    print("less")
    if b>a:
        print('greater')
else :
    print("true")'''

'''a=10
b=26
if a>b:
    print("less")
    if b>a:
        print('greater')
    else :
        print("yes")
else :
        print("true")'''
    
'''a=10
b=26
if a<b:
    print("less")
    if b>a:
        print('greater')
    elif b<a:
        print("lesser")
    else :
        print("yes")
else :
        print("true")'''


#social media login
'''user_name=input("enter username")
if user_name=='Gayathri':
    password=input("enter password")
    if password=='8642':
        print("login successful")
    else:
        print('wrong password')
else:
    print("invalid login credentials")'''


'''user_name=input("enter username")
password=input("enter password")
if user_name=='Gayathri' and password=='8642':
    print("login successful")
  
else:
    print("invalid login credentials")'''


#bakery different types of cakes
'''price=int(input("enter cost"))
if price==1200:
    print('redvalvet cake')
elif price==1000:
    print('choco almond')
elif price==800:
    print('chocolate cake')
elif price==600:
    print('butterscotch cake')
else:
    print('sorry,cake not available')'''
#pizza
'''name=input("enter order").lower()
if name=='bbq pizza':
    print(1000)
elif name=='crispy chicken pizza':
    print(800)
elif name=='paneer pizza':
    print(600)
elif name=='corn pizza':
    print(400)
elif name=='french fries coke':
    print(200)
else:
    print('sorry not available')'''














