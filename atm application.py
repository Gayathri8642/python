#ATM Application
while True:
    a=input("insert card")
    if a=="c":
        print("welcome Gayathri")
        pwd=input("Enter the password:")
        if pwd=="1234":
            op=int(input("1.balance check 2.withdraw"))
            if op==1:
                   print("Your balance is 100000")
            elif op==2:
                g=int(input("Enter the amount:"))
                rem=100000-g
                print("remaining balance is ",rem)
        else:
            print("incorrrect password")
    else:
        print("invalid card")
