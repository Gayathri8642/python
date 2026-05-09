#file handling
#write()
'''a=open('pyth.txt','w')
a.write('codegnan')
a.close()'''


'''a=open('pyth.txt','w')
a.write('python')
a.close()'''

#append()
'''a=open('pyth.txt','a')
a.write('\thello')
a.close()'''


'''a=open('pyth.txt','a')
a.write(input())
a.close()'''
'''a=open('pyth.txt','a')
n=input()
a.write(n)
a.close()'''

#read()
'''a=open('pyth.txt')
print(a.read())#it will display entire data
print(a.readline())#it will display first line
print(a.readlines())#it will display with \n
print(a.read(6))'''

#writelines()->it makes every object side by side
'''a=['Gayathri','twisha','sai','leela','veera']
b=open('om.txt','w')
b.writelines(a)
b.close()'''


'''a=['Gayathri','twisha','sai','leela','veera']
b=open('om.txt','w')
b.writelines('\n'.join(a))
b.close()'''

'''a=open('modules.py')
print(a.read())

a=open('C:\\Users\\Gayathri\\Downloads\\python\\conditions and loops based problems.py')
print(a.read())'''
