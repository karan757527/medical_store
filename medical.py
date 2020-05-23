# moules i need
import os
import pickle
from getpass import getpass

# database functions
def load_db(filename):
    with open(filename, 'rb') as file:
        db = pickle.load(file)
        file.close()
    return db

def update_db(filename,obj):
    with open(filename, 'wb') as fp:
        pickle.dump(obj, fp)
        fp.close()
    return True

#title
def title():
    print("-"*80)
    print("Agrawal Pharmacy , Jaipur".center(80))
    print("-"*80)

# admin functions
def add_employee():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    e_db=load_db("employee.pkl")
    print("Add Employee".center(80))
    print("-"*80)
    name=input("Enter Employee name: ")
    name=name.title()
    while True:
        username=input("Enter username: ")
        username=username.lower()
        if username in e_db:
            print("Username Exists,Choose a Different Username.")
        else:
            break
    while True:
        pwd1=getpass("Enter Password: ")
        pwd2=getpass("Re Enter Password: ")
        if pwd1 != pwd2:
            print("Password Mismatch")
        else:
            break
    e_db[username]=[name,pwd1]
    update_db("employee.pkl",e_db)
    print("User Created Succesfully".center(80))
    
def remove_employee():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    e_db=load_db("employee.pkl")
    print("Remove Employee".center(80))
    print("-"*80)
    username=input("Enter username: ")
    username=username.lower()
    if username in e_db:
        pwd=getpass("Enter Password: ")
        if e_db[username][1]==pwd:
            e_db.pop(username)
            print("User Deleted Succesfully".center(80))
            update_db("employee.pkl",e_db)
    else:
        print("Wrong Username or Password")
        
def view_employees():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    e_db=load_db("employee.pkl")
    print("View Employees".center(80))
    print("-"*80)
    print()
    print("-"*80)
    print("|","Name".center(23),"|","Username".center(24),"|","Password".center(23),"|")
    print("|","-"*23,"|","-"*24,"|","-"*23,"|",sep="-")
    for i in e_db:
        print("|",e_db[i][0].center(23),"|",i.center(24),"|",e_db[i][1].center(23),"|")
    print("-"*80)   
    
#account functions
def view_stock():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    m_db=load_db("medicine.pkl")
    print("Stock".center(80))
    print("-"*80)
    print()
    print("-"*80)
    print("|","Name".center(23),"|","MRP".center(24),"|","Stock".center(23),"|")
    print("|","-"*23,"|","-"*24,"|","-"*23,"|",sep="-")
    for i in m_db:
        print("|",i.center(23),"|",str(m_db[i][0]).center(24),"|",str(m_db[i][1]).center(23),"|")
    print("-"*80)
    
def view_sell():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    s_db=load_db("sell.pkl")
    i_db=load_db("invoice.pkl")
    print("Bill Wise Sell".center(80))
    print("-"*80)
    print()
    print("-"*80)
    print("|","Invoice No.".center(23),"|","Name".center(24),"|","Amount".center(23),"|")
    print("|","-"*23,"|","-"*24,"|","-"*23,"|",sep="-")
    for i in range(1,i_db+1):
        amount=0
        for x in s_db[i][1:]:
            amt=x[1]*x[2]
            amount+=amt
        print("|",str(i).center(23),"|",str(s_db[i][0]).center(24),"|",str(amount).center(23),"|")
    print("-"*80)
    
def view_purchase():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    p_db=load_db("purchase.pkl")
    print("Bill Wise Purchase".center(80))
    print("-"*80)
    print()
    print("-"*80)
    print("|","Party-Invoice".center(37),"|","Amount".center(36),"|")
    print("|","-"*37,"|","-"*36,"|",sep="-")
    for i in p_db:
        amount=0
        for j in p_db[i]:
            amt=j[1]*j[2]
            amount+=amt
        print("|",i.center(37),"|",str(amount).center(36),"|")
    print("-"*80)

#admin functions again
def accounts():
    choice=0
    while choice!="4":
        input("Press Enter to continue.".center(80))
        os.system("cls")
        title()
        print("Accounts Menu".center(80))
        print("-"*80)
        print("1. View Stock")
        print("2. View Bill Wise Sell")
        print("3. View Bill Wise Purchase")
        print("4. Go to Admin Menu")
        choice=input("Enter Your Choice: ")
        if choice == "1":
            view_stock()
        elif choice == "2":
            view_sell()
        elif choice == "3":
            view_purchase()
        elif choice == "4":
            break
        else:
             print("Invalid Choice")
                
#after admin login menu function and admin function driver
def admin():
    choice=0
    while choice!="5":
        input("Press Enter to continue.".center(80))
        os.system("cls")
        title()
        print("Admin Menu".center(80))
        print("-"*80)
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employees")
        print("4. View Accounts")
        print("5. Go to Main Menu")
        choice=input("Enter Your Choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            accounts()
        elif choice == "5":
            break
        else:
             print("Invalid Choice")
 # menu functions               
def admin_login():
        input("Press Enter to continue.".center(80))
        os.system("cls")
        title()
        print("Admin Login".center(80))
        print("-"*80)
        choice=0
        username=input("Username: ")
        password=getpass("Password: ")
        if username=="admin" and password=="admin":
            print("Welcome Admin".center(80))
            admin()
            choice="2"
        else:
            print("Wrong Username or Password")
            while choice !="2" or choice !="1":
                print("1. Try Again")
                print("2. Go to Main Menu")
                choice=input("Enter Your Choice: ")
                if choice == "1":
                    break
                elif choice == "2":
                    break
                else:
                    print("Invalid Choice")
                    
# employee functios
def change_password(username):
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    e_db=load_db("employee.pkl")
    print("Change Password".center(80))
    print("-"*80)
    user=input("Enter Your Username: ")
    pwd=getpass("Enter Existing Password: ")
    if username==user and e_db[username][1]==pwd:
        pwd1=getpass("Enter New Password: ")
        pwd2=getpass("Re Enter New Password: ")
        if pwd1 != pwd2:
            print("Password Mismatch")
        else:
            e_db[username][1]=pwd1
            update_db("employee.pkl",e_db)
            print("Password Changed Succesfully".center(80))
    else:
        print("Wrong Username or Password")
       
    
# sell function to print bill
def view_bill(inv,dr):
    input("Press Enter to continue.".center(80))
    os.system("cls")
    s_db=load_db("sell.pkl")
    i_db=s_db[inv]
    title()
    print("Sell Invoice".center(80))
    print("-"*80)
    print("Name: ",i_db[0])
    print("Referred By: ",dr)
    print("-"*80)
    print("|","Medicine".center(17),"|","Price".center(17),"|","Quantity".center(16),"|","Amount".center(17),"|")
    print("|","-"*17,"|","-"*17,"|","-"*16,"|","-"*17,"|",sep="-")
    amount=0
    for x in i_db[1:]:
        amt=x[1]*x[2]
        amount+=amt
        amt=str(amt)
        price=str(x[1])
        quantity=str(x[2])
        print("|",x[0].center(17),"|",price.center(17),"|",quantity.center(16),"|",amt.center(17),"|")
    print("-"*80)
    print(f"Total Amount is {amount}.".center(80))
    print("-"*80)
    print("Thank You Visit Again.".center(80))
    print("-"*80)
    
# employee function functions again
def sell():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    m_db=load_db("medicine.pkl")
    print("Sell Invoice".center(80))
    print("-"*80)
    s_db=load_db("sell.pkl")
    inv=load_db("invoice.pkl")
    inv+=1;
    name=input("Enter Customer Name: ")
    dr=input("Refered By Dr.: ")
    print(f"Invoice Number is {inv}.")
    s_db[inv]=[name]
    print("-"*80)
    choice=0
    while choice !="2":
        m_name=input("Enter medicine name: ")
        m_name=m_name.title()
        if m_name in m_db:
            mrp=float(input("Enter MRP: "))
            quantity=int(input("Enter Quantity: "))
            if m_db[m_name][1]>=quantity:
                m_db[m_name][1]-=quantity
                s_db[inv].append((m_name,mrp,quantity))
            else:
                print("Out of Stock")
        else:
            print("Medicine Do Not Exist")
        while choice !="1" or choice !="2":
            print("1. Add More")
            print("2. Print Bill")
            choice=input()
            if choice=="2" or choice=="1":
                break
            else:
                print("Invalid Choice")
    update_db("medicine.pkl",m_db)
    update_db("Sell.pkl",s_db)
    update_db("invoice.pkl",inv)
    view_bill(inv,dr)
    
def purchase():
    input("Press Enter to continue.".center(80))
    os.system("cls")
    title()
    m_db=load_db("medicine.pkl")
    print("Purchase Invoice".center(80))
    print("-"*80)
    name=input("Enter Seller Name: ")
    name=name.title()
    inv=input("Enter Invoice Number:")
    p_db=load_db("purchase.pkl")
    if name+"-"+inv not in p_db:
        p_db[name+"-"+inv]=[]
        print("-"*80)
        choice=0
        while choice !="2":
            m_name=input("Enter medicine name: ")
            m_name=m_name.title()
            mrp=float(input("Enter Price: "))
            quantity=int(input("Enter Quantity: "))
            if m_name not in m_db:
                m_db[m_name]=[mrp,quantity]
            else:
                m_db[m_name][1]+=quantity
            p_db[name+"-"+inv].append((m_name,mrp,quantity))
            while choice !="1" or choice !="2":
                print("1. Add More")
                print("2. Go to Employee Menu")
                choice=input()
                if choice=="2" or choice=="1":
                    break
                else:
                    print("Invalid Choice")
        update_db("medicine.pkl",m_db)
        update_db("purchase.pkl",p_db)
        print("Medicines Added Succesfully".center(80))
    else:
        print("Bill Already Uploaded.")
        
# afteremployee login and driver of employee methods
def employee(username):
    choice=0
    while choice!="5":
        input("Press Enter to continue.".center(80))
        os.system("cls")
        title()
        print("Employee Menu".center(80))
        print("-"*80)
        print("1. Sell Medicine")
        print("2. Purchase Medicine")
        print("3. View Stock")
        print("4. Change Password")
        print("5. Go to Main Menu")
        choice=input("Enter Your Choice: ")
        if choice == "1":
            sell()
        elif choice == "2":
            purchase()
        elif choice == "3":
            view_stock()
        elif choice == "4":
            change_password(username)
        elif choice == "5":
            break
        else:
             print("Invalid Choice")
       
    
# menu funcion 
def employee_login():
    choice=0
    e_db=load_db("employee.pkl")
    while choice!="2":
        input("Press Enter to continue.".center(80))
        os.system("cls")
        title()
        print("Employee Login".center(80))
        print("-"*80)
        username=input("Username: ")
        password=getpass("Password: ")
        if username in e_db and password==e_db[username][1]:
            print(f"Welcome {e_db[username][0]}".center(80))
            employee(username)
            choice="2"
        else:
            print("Wrong Username or Password")
            while choice !="2" or choice !="1":
                print("1. Try Again")
                print("2. Go to Main Menu")
                choice=input("Enter Your Choice: ")
                if choice == "1":
                    break
                elif choice == "2":
                    break
                else:
                    print("Invalid Choice")
                    
                    
# driver function for menu
def driver():   
    choice=0
    while choice != 3:
        title()
        print("Main Menu".center(80))
        print("-"*80)
        print("1. Admin Login")
        print("2. Employee Login")
        print("3. Exit")
        choice=input("Enter Your Choice: ")
        if choice == "1":
            admin_login()
        elif choice == "2":
            employee_login()
        elif choice == "3":
            break
        else:
            print("Invalid Choice")
        print("-"*80)
        input("Press Enter to continue.".center(80))
        os.system("cls")
        
#calling driver
driver()