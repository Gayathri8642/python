#Inheritance
#single inheritance
'''class RBI():
    cash=100000
    def available_cash(cls):
        print('available cash is',cls.cash)
        print('available cash is',RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print('new cash is',cls.cash+cls.cash)
        print('new cash is',cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#multiple inheritance
'''class Father():
    def inh(genes):
        print('Height of Father is 6 inches')
class Mother():
    def inhm(genes):
        print('Weight of Mother is 60kgs')
class kid(Father,Mother):
    dob='08062004'
    def inhk(genes):
        print('Date of birth of kid is',genes.dob)
a=kid()
a.inhk()
a.inhm()
a.inh()'''
    
'''class Father():
    def inh(genes,h):
        print('Height of Father is',h)
class Mother():
    def inhm(genes,w):
        print('Weight of Mother is',w)
class kid(Father,Mother):
    def inhk(genes,d):
        print('Date of birth of kid is',d)
h=int(input('height'))
w=int(input('weight'))
d=eval(input('dob'))
a=kid()
a.inhk(d)
a.inhm(w)
a.inh(h)'''

#multi level inheritance
'''class gp():
    def inh(se):
        print('They gives 300acres of land')
class p(gp):
    def inhp(se):
        print('They gave a pucca house')
class c(p):
    def inhc(se):
        print('we gave a car')
a=c()
a.inh()
a.inhp()
a.inhc()'''


'''class gp():
    def inh(se,l):
        print(f'They gives {l}acres of land')
class p(gp):
    def inhp(se,h):
        print(f'They gave a {h} houses')
class c(p):
    def inhc(se,ca):
        print(f'we gave {ca} cars')
l=int(input())
h=int(input())
ca=int(input())
a=c()
a.inh(l)
a.inhp(h)
a.inhc(ca)'''



