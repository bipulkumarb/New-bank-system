#imports
from tkinter import *
import os
from tkinter import font
from PIL import ImageTk, Image

#Main Screen
master = Tk()
master.title('Banking Management')

#Functions
def finish_reg():
    name = temp_name.get()
    aadhar=temp_aadhar.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password1.get()
    conform_password = temp_conform_password.get()
    all_accounts = os.listdir()
    date=temp_date.get()
    mobile=temp_mobile.get()
    address=temp_add.get()

    if name == "" or age == "" or gender == "" or password == ""or conform_password==""  or date=="" or mobile=="" or address=="" or aadhar=="":
        notif.config(fg="red",text="All fields requried * ")
        return

    if conform_password == password:
        
        for name_check in all_accounts:
            if name == name_check:
               notif.config(fg="red",text="Account already exists")
               return
            else:
                if mobile.isnumeric() and mobile.__len__() == 10 :
                    new_file = open(name,"w")
                    new_file.write(name+'\n')
                    new_file.write(password+'\n')
                    new_file.write(age+'\n')
                    new_file.write(gender+'\n')
                    new_file.write(date+'\n')
                    new_file.write(aadhar+'\n')
                    new_file.write(mobile+'\n')
                    new_file.write(address+'\n')
                    new_file.write('0')
                    new_file.close()
                    notif.config(fg="green", text="Account has been created")
                else:
                    notif.config(fg="red",text="Invalid mobile number")    
                    return
    else:
        notif.config(fg="red",text="password and con_pass are not same ")    
        return        

def register():
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    global temp_date
    global temp_mobile
    global temp_password1
    global temp_add
    global temp_conform_password
    global temp_aadhar
    temp_aadhar = StringVar()
    temp_add = StringVar()
    temp_mobile = StringVar()
    temp_date = StringVar()
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password1 = StringVar()
    temp_password = StringVar()
    temp_conform_password = StringVar()
    
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text="Please enter your details below to register", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',12)).grid(row=4,sticky=W)
    Label(register_screen, text="Con_pass", font=('Calibri',12)).grid(row=5,sticky=W)
    Label(register_screen, text="Date", font=('Calibri',12)).grid(row=6,sticky=W)
    Label(register_screen, text="Mobile:", font=('Calibri',12)).grid(row=7,sticky=W)
    Label(register_screen, text="Address", font=('Calibri',12)).grid(row=8,sticky=W)
    Label(register_screen, text="Aadhar No", font=('Calibri',12)).grid(row=9,sticky=W)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=11,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0,padx=10)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0,padx=10)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0,padx=10)
    Entry(register_screen,textvariable=temp_password1,show="*").grid(row=4,column=0,padx=10)
    Entry(register_screen,textvariable=temp_conform_password,show="*").grid(row=5,column=0,padx=10)
    Entry(register_screen,textvariable=temp_date).grid(row=6,column=0,padx=10)
    Entry(register_screen,textvariable=temp_mobile).grid(row=7,column=0,padx=10)
    Entry(register_screen,textvariable=temp_add).grid(row=8,column=0,padx=10)
    Entry(register_screen,textvariable=temp_aadhar).grid(row=9,column=0,padx=10)
    
    #Buttons
    Button(register_screen, text="Register", command = finish_reg, font=('Calibri',12)).grid(row=12,sticky=N,pady=10)

def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password  = file_data[1]
            file.close()
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                #Labels
                Label(account_dashboard, text="Account Dashboard", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+name, font=('Calibri',12)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details",font=('Calibri',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="Deposit",font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard, text="Withdraw",font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password incorrect!!")
                return
    login_notif.config(fg="red", text="No account found !!")

def deposit():
    #Vars
    global amount
    global date1
    global amount1
    global date
    global deposit_notif
    global current_balance_label
    date = StringVar()
    amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[8]
    file.close()
    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')

    #Label
    Label(deposit_screen, text="Deposit", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance : Rs"+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(deposit_screen, text="Date ", font=('Calibri',12)).grid(row=3,sticky=W)
    deposit_notif = Label(deposit_screen,font=('Calibri',12))
    deposit_notif.grid(row=4, sticky=N,pady=5)

    #Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2,column=1)
    Entry(deposit_screen, textvariable=date).grid(row=3,column=1)

    
    #Button
    Button(deposit_screen,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=5,sticky=W,pady=5)


def finish_deposit():

    global name1
    global age1
    global gender1
    global aadhar1


    file = open(login_name,"r")
    file_data=file.read()
    user_details=file_data.split('\n')
    details_age=user_details[2]
    details_name=user_details[0]
    details_gender=user_details[3]
    details_aadhar=user_details[7]
    details_balance=user_details[8]
    file.close()


    amount1=amount.get()
    balance=details_balance
    date1=date.get()
    name1=details_name
    age1=details_age
    gender1=details_gender
    aadhar1=details_aadhar


    print(amount1)
    print(date1)

    if amount.get() == "" or date1 == "":
        deposit_notif.config(text='All field is required!',fg="red")
        return
    else:
        f=open("111.txt","a")
        f.write(f"Date :  {date1} , Name :  {name1} , Age :  {age1} , Gender :  {gender1} , Aadhar No : {aadhar1} , Deposited : {amount1}  , Total Balance before deposit :  {balance}......:  \n")
        f.close()


    if float(amount.get()) <=0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[8]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs"+str(updated_balance),fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')
 
def withdraw():
     #Vars
    global withdraw_amount
    global amount2
    global datew
    global date2
    global withdraw_notif
    global current_balance_label
    datew= StringVar()
    withdraw_amount = StringVar()
    file   = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[8]
    file.close()
    #Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')
    #Label
    Label(withdraw_screen, text="Withdraw", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : Rs"+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(withdraw_screen, text="Date : ", font=('Calibri',12)).grid(row=3,sticky=W)
    withdraw_notif = Label(withdraw_screen,font=('Calibri',12))
    withdraw_notif.grid(row=5, sticky=N,pady=5)

    #Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2,column=1)
    Entry(withdraw_screen, textvariable=datew).grid(row=3,column=1)

    #Button
    Button(withdraw_screen,text="Finish",font=('Calibri',12),command=finish_withdraw).grid(row=4,sticky=W,pady=5)

def finish_withdraw():

    global name2
    global age2
    global gender2
    global balance1
    global aadhar2
    global date2


    file = open(login_name,"r")
    file_data=file.read()
    user_details=file_data.split('\n')
    details_age=user_details[2]
    details_name=user_details[0]
    details_gender=user_details[3]
    details_aadhar=user_details[7]
    details_balance=user_details[8]
    file.close()


    amount2=withdraw_amount.get()
    balance1=details_balance
    date2=datew.get()
    name2=details_name
    age2=details_age
    gender2=details_gender
    aadhar2=details_aadhar


    print(amount2)
    print(date2)

    if withdraw_amount.get() == "" or date2=="":
        withdraw_notif.config(text='All field is required!',fg="red")
        return

    else:
        f=open("222.txt","a")
        f.write(f"Date :  {date2} , Name :  {name2} , Age :  {age2} , Gender :  {gender2} , Aadhar No : {aadhar2} , Deposited : {amount2}  , Total Balance before withdrawn  :  {balance1}......:  \n")
        f.close()
    


    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[8]

    if float(withdraw_amount.get()) >float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs"+str(updated_balance),fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')
    

def personal_details():
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_date = user_details[4]
    details_aadhar =user_details[5]
    details_mobile=user_details[6]
    details_add=user_details[7]
    details_balance = user_details[8]
    file.close()
    #Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    #Labels
    Label(personal_details_screen, text="Personal Details", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text="Name    : "+details_name, font=('Calibri',12)).grid(row=1,sticky=W,padx=10)
    Label(personal_details_screen, text="Age     : "+details_age, font=('Calibri',12)).grid(row=2,sticky=W,padx=10)
    Label(personal_details_screen, text="Gender  : "+details_gender, font=('Calibri',12)).grid(row=3,sticky=W,padx=10)
    Label(personal_details_screen, text="Balance :Rs"+details_balance, font=('Calibri',12)).grid(row=4,sticky=W,padx=10)
    Label(personal_details_screen, text="Date    :"+details_date, font=('Calibri',12)).grid(row=6,sticky=W,padx=10)
    # Label(personal_details_screen, text="Mobile:"+details_mobile, font=('Calibri',12)).grid(row=7,sticky=W)
    Label(personal_details_screen, text="Address :"+details_add, font=('Calibri',12)).grid(row=8,sticky=W,padx=10)
    Label(personal_details_screen, text="Aadhar  :"+details_aadhar, font=('Calibri',12)).grid(row=7,sticky=W,padx=10)


def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Login to your account", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=('Calibri',12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=10)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=10)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=10)

def finish_con():
    name = temp_contact_name.get()
    problem=temp_contact_problem.get()
    phone = temp_contact_phone.get()
    date= temp_contact_date.get()
    if name=="" or phone=="" or date=="" or problem=="":
        notif.config(fg="red",text="All fields are required")
        return

    else:
        
        new_file= open(date,"w")
        new_file.write(date+'\n')
        new_file.write(name+'\n')
        new_file.write(phone+'\n')
        new_file.write(problem+'\n')
        new_file.close()
        notif.config(fg="green",text="Your complain is submitted")   


def contact():
    global temp_contact_phone
    global notif
    global temp_contact_name
    global temp_contact_problem
    global temp_contact_date
    temp_contact_problem=StringVar()
    temp_contact_date= StringVar()
    temp_contact_name=StringVar()
    temp_contact_phone=StringVar()
    contact_screen = Toplevel(master)
    contact_screen.title('Contact Us')
    Label(contact_screen, text="Our E-mail_id", font=('Calibri',12)).grid(row=0,sticky=W)
    Label(contact_screen, text="Our Phone Number", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(contact_screen, text="Address", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(contact_screen, text="turnbull124@gmail.com", font=('Calibri',12)).grid(row=0,column=1,padx=5)
    Label(contact_screen, text="0123456789", font=('Calibri',12)).grid(row=1,column=1,padx=5)
    Label(contact_screen, text="13, Baker Street , London", font=('Calibri',12)).grid(row=2,column=1,padx=5)
    Label(contact_screen, text="OR", font=('Calibri',12)).grid(row=3,column=0,padx=5)
    Label(contact_screen, text="Enter Your Name", font=('Calibri',12)).grid(row=4,sticky=W)
    Entry(contact_screen, textvariable=temp_contact_name).grid(row=4,column=1,padx=10)
    Label(contact_screen, text="Enter Your Phone Number", font=('Calibri',12)).grid(row=5,sticky=W)
    Entry(contact_screen, textvariable=temp_contact_phone).grid(row=5,column=1,padx=10)
    Label(contact_screen, text="Enter Date and Time in(( dd-mm-yyyy-HH-MM AM/PM) Format", font=('Calibri',12)).grid(row=6,sticky=W)
    Entry(contact_screen, textvariable=temp_contact_date).grid(row=6,column=1,padx=10)
    Label(contact_screen, text="Enter Your Problem", font=('Calibri',12)).grid(row=7,sticky=W)
    Entry(contact_screen, textvariable=temp_contact_problem).grid(row=7,column=1,padx=10)
    notif = Label(contact_screen, font=('Calibri',12))
    notif.grid(row=8,sticky=N,pady=10)


    #Buttons
    Button(contact_screen, text="Submit", command = finish_con, font=('Calibri',12)).grid(row=9,sticky=N,pady=10)


def conform_new_password():
    global con_old_password
    global con_new_password
    con_old_password=StringVar()
    # con_old_password=old_password.get()
    con_new_password=new_password.get()
    all_accounts =os.listdir()
    con_for_name= for_name.get()


    
    for name in all_accounts:
        if name == forgot_name:
            file = open(name,"r+")
            file_data = file.read()
            file_data = file_data.split('\n')
            con_old_password = file_data[1]
            file.close()
            print("fhjkh") 
            print(con_old_password)
            print(con_new_password)  

    
    if con_old_password==con_new_password:
        print("asd")
        forgot1_notif.config(fg="red",text='New password cannot be same as old Password')
        return
    else:
        print("asdf")
        

        for name in all_accounts:
           print(con_for_name)
           print("mnb")
           file = open(con_for_name, 'r+')
           file_data = file.read()
           details = file_data.split('\n')
           con_old_password = details[1]
           print("x")
           print(con_old_password)
           print("mnbv")
           print(con_for_name)
           print("z1")
           print(name)

           file_data = file_data.replace(con_old_password, str(con_new_password))
           file.seek(0)
           file.truncate(0)
           file.write(file_data)
           file.close()
           forgot1_notif.config(fg="green",text='Password Updated')
           return

def forgot_session():
    global forgot_name
    global new_password
    global forgot_aad
    global old_password
    global forgot1_notif
    global forgot_gender
    old_password= StringVar()
    forgot_name=for_name.get()
    new_password= StringVar()
    forgot_aad=for_aad.get()
    forgot_gender=for_gender.get()
    all_accounts =os.listdir()

    for name in all_accounts:
        if name == forgot_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            f_name = file_data[0]
            print(f_name)

            f_gender = file_data[3]
            f_aad = file_data[5]
            print(f_gender)
            print(f_aad)
            
            print("123")
            if f_name==forgot_name and f_aad ==forgot_aad and f_gender==forgot_gender:
                forgot_dashboard = Toplevel(master)
                forgot_dashboard.title('Forgot Password')
                print("aad")

                Label(forgot_dashboard, text="Enter your new Password",font=('Calibri',12)).grid(row=0,sticky=W)

                Entry(forgot_dashboard,textvariable=new_password).grid(row=0,column=1)
                forgot1_notif= Label(forgot_dashboard, font=('Calibri',12))
                forgot1_notif.grid(row=1,sticky=N)

                Button(forgot_dashboard,text="Submit",command=conform_new_password, width=15,font=('Calibri',12)).grid(row=2,sticky=N)
                print("nvjh")

            else:
                forgot_notif.config(fg="red",text="Invalid Instruction")
                return
            forgot_notif.config(fg='green',text="Account Found")
            return
        forgot_notif.config(fg='red',text=" No Account Found")  
          
            


def forgot():
    global for_aad
    global forgot_notif
    global for_name
    global for_gender
    for_name =StringVar()
    for_gender = StringVar()
    for_aad = StringVar()
    forgot_screen = Toplevel(master)
    forgot_screen.title('Forgot Password')
    Label(forgot_screen, text="Enter Name", font=('Calibri',12)).grid(row=0,sticky=W)
    Entry(forgot_screen, textvariable=for_name).grid(row=0,column=1,padx=10)
    Label(forgot_screen, text="Enter Aadhar Number", font=('Calibri',12)).grid(row=1,sticky=W)
    Entry(forgot_screen, textvariable=for_aad).grid(row=1,column=1,padx=10)
    Label(forgot_screen, text="Enter Gender", font=('Calibri',12)).grid(row=2,sticky=W)
    Entry(forgot_screen, textvariable=for_gender).grid(row=2,column=1,padx=10)
    forgot_notif= Label(forgot_screen, font=('Calibri',12))
    forgot_notif.grid(row=3,sticky=N)
    Button(forgot_screen,text="Submit",command=forgot_session, width=15,font=('Calibri',12)).grid(row=4,sticky=N)



#Image import
img = Image.open('1.jpg')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "Bank of Mrizapur", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "One of the most trusted bank of India", font=('Calibri',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text="Register", font=('Calibri',12),width=20,command=register).grid(row=3,sticky=N,pady=5)
Button(master, text="Login", font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N,pady=5)
Button(master, text="Contact us", font=('Calibri',12),width=20,command=contact).grid(row=5,sticky=N,pady=5)
Button(master, text="Forgot Password", font=('Calibri',12),width=20,command=forgot).grid(row=6,sticky=N,pady=5)


master.mainloop()