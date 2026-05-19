import pandas as p
class CBMS:
    data = {'name':[], 'mobile':[], 'mail_id':[]}
    def add_contact(self):
        self.name=input('enter name').capitalize()
        CBMS.data['name'].append(self.name)
        self.mobile=int(input('enter mobile number'))
        CBMS.data['mobile'].append(self.mobile)
        self.mail_id=input('enter mail id')
        CBMS.data['mail_id'].append(self.mail_id)
    def update_contact(self):
        self.old_number=int(input('enter old mobile number'))            
        self.new_number=int(input('enter new mobile number'))
        if self.old_number in CBMS.data['mobile']:
            i= CBMS.data['mobile'].index(self.old_number)
            CBMS.data['mobile'][i] = self.new_number
        else:
            print('invalid mobile number')
    def list_of_contacts(self):
        print(p.DataFrame(CBMS.data))        
    def delete_contact(self):
        self.delete=input('enter name').capitalize()
        if self.delete in CBMS.data['name']:
            s=CBMS.data['name'].index(self.delete)
            CBMS.data['name'].remove(self.delete)
            del CBMS.data['mobile'][s]
            del CBMS.data['mail_id'][s]

a=CBMS()
while True:
    o=int(input("""Enter the choice:
                1.add contact
                2.update contact
                3.list of contacts
                4.delete contact
                5.exit"""))
    if o==1:
        a.add_contact()
    elif o==2:
        a.update_contact()
    elif o==3:
        a.list_of_contacts()
    elif o==4:
        a.delete_contact()
    elif o==5:
        break
    else:
        print('invalid option')



#Contact Base Management System

'''contacts = []

while True:
    print("Contact Base Management System".upper())
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: ") )

    if choice == 1:
        n = int(input("How many contacts do you want to add? "))

        for i in range(n):
            print(f"\nEnter Details for Contact {i+1}")

            name = input("Enter Name: ")
            mobile = input("Enter Mobile Number: ")
            email = input("Enter Mail ID: ")

            contact = {
                "Name": name,
                "Mobile": mobile,
                "Email": email
            }

            contacts.append(contact)

        print("\nContacts Added Successfully!")

    
    elif choice == 2:
        old_mobile = input("Enter Old Mobile Number: ")
        found = False

        for contact in contacts:
            if contact["Mobile"] == old_mobile:
                new_mobile = input("Enter New Mobile Number: ")
                contact["Mobile"] = new_mobile

                print("\nContact Updated Successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found!")

    
    elif choice == 3:

        if len(contacts) == 0:
            print("\nNo Contacts Available.")

        else:
            print("\n================ CONTACT LIST ================\n")

            print("{:<5} {:<20} {:<15} {:<30}".format(
                "S.No", "Name", "Mobile", "Email"))

            print("-" * 75)

            for i, contact in enumerate(contacts, start=1):
                print("{:<5} {:<20} {:<15} {:<30}".format(
                    i,
                    contact["Name"],
                    contact["Mobile"],
                    contact["Email"]
                ))

    
    elif choice == 4:
        mobile = input("Enter Mobile Number to Delete: ")
        found = False

        for contact in contacts:
            if contact["Mobile"] == mobile:
                contacts.remove(contact)
                found = True
                print("Contact Deleted Successfully!")
                break

        if not found:
            print("Contact Not Found!")

    
    elif choice == 5:
        print("Bye Bye!!!")
        break

    else:
        print("Invalid Choice! Please Try Again.")'''

'''class Contact:
    def __init__(self):
        self.contacts = {}

    def addcontact(self):
        name = input("Enter name: ")
        mobile = input("Enter mobile no: ")
        mailid = input("Enter mailid: ")

        self.contacts[name] = {
            "mobile": mobile,
            "mailid": mailid
        }

        print("Contact Added Successfully")

    def update(self):
        name = input("Enter contact name to update: ")

        if name in self.contacts:

            field = input("What do you want to update? mobile/mailid: ").lower()

            new_value = input(f"Enter new {field}: ")

            self.contacts[name][field] = new_value

            print("Updated Successfully")

        else:
            print("Contact not found")

    def listcontact(self):

        if len(self.contacts) == 0:
            print("No contacts available")

        else:
            print("\n{:<15} {:<15} {:<25}".format("NAME", "MOBILE", "MAIL ID"))
            print("-" * 55)

            for name, details in self.contacts.items():

                mobile = details.get("mobile", "Not Available")
                mailid = details.get("mailid", "Not Available")

                print("{:<15} {:<15} {:<25}".format(name, mobile, mailid))

    def remove(self):

        name = input("Enter contact name: ")

        if name in self.contacts:

            field = input("What do you want to delete? mobile/mailid: ").lower()

            if field in self.contacts[name]:

                del self.contacts[name][field]

                print("Deleted Successfully")

                print(self.contacts)

            else:
                print("Field not found")

        else:
            print("Contact not found")


obj = Contact()

print("WELCOME TO CONTACT MANAGEMENT SYSTEM")

while True:

    x = int(input("""
1) Add Contact
2) Update Contact
3) List Contact
4) Remove Contact
5) Exit

Enter choice: """))

    if x == 1:
        obj.addcontact()

    elif x == 2:
        obj.update()

    elif x == 3:
        obj.listcontact()

    elif x == 4:
        obj.remove()

    elif x == 5:
        print("Bye Bye...")
        break

    else:
        print("Invalid Choice")'''
        
