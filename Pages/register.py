import sys
import smtplib
from random import randint
from tkcalendar import Calendar, DateEntry
from datetime import date
from PIL import ImageTk, Image
import PIL
from regd import *
import pymysql
import pymysql.cursors
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import re

import logging

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import *
from tkinter import messagebox

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True
sql_hostname = '127.0.0.1'
mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22

logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('register.py initiated')

def calculateAge(birthDate):
    today = date.today() #check date on which the user is trying to register
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) #calculate age with refernce to current date
    return age


def ins(emails, usern, pass1, pass2, addre, mobi, cal,var):
	#storing all textbox values in variables
    email = emails.get()
    username = usern.get()
    passs1 = pass1.get()
    passs2 = pass2.get()
    addres = addre.get()
    mob = mobi.get()

    if len(email) != 0 and len(username) != 0 and len(passs1) != 0 and len(passs2) != 0 and len(addres) != 0 and len(
            mob) != 0 and var.get()!=0: #check if user has entered all fields
        regex = '^[a-zA-Z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email): #check if email entered is in correct format i.e xyz@abc.com
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" 
            pat = re.compile(reg)
            if re.search(pat, passs1): #check if password entered by user is strong enough i.e with one upper case one lower case,one no.and one spcl char
                if passs1 == passs2: #both the passwords entered are same
                    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
                    if Pattern.match(mob) and len(mob) == 10: # check if mobile number is valid or not
                        dob = cal.get_date()
                        age = str(calculateAge(cal.get_date())) # calculate the useres age based on dob 
                        dob = str(dob)
                        try:
                            print(email, username, age, dob, addres, mob, passs1)
                            pass_value = [email, username, age, dob, addres, mob, passs1]

                            
                            root.destroy() #destroy current page

                            vp_start_gui_reg(pass_value) # pass values to the next otp page
                        except Exception as e:
                            logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
                            logging.warning('Couldnt load OTP page')
                            print(e)
                    else:
                        messagebox.showerror("Error", "Mobile Number Invalid") #show error accordingly
                        logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
                        logging.warning('Entered invalid mobile Number')
                else:
                    messagebox.showerror("Error", "Both passwords do not match")
                    logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
                    logging.warning('Passwords in both the fields do not match')
            else:
                messagebox.showerror("Error", "Enter a strong Password")
                logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
                logging.warning('User hasnt chosen a strong password')
        else:
            messagebox.showerror("Error", "Invalid Email Id")
            logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            logging.warning('Invalid Email')
    else:
        messagebox.showerror("Error", "Fields cannot be empty")
        logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('Fields are empty')
    return


def vp_start_register():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Register(root)
    root.mainloop()


w = None


def create_Register(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Register(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Register(w)
    return w, top


def destroy_Register():
    global w
    w.destroy()
    w = None


class Register:
    def ageagreement(self, age):
        if age < 18:
            x = "I agree that my age is below 18"
            return x
        if age > 18:
            x = " I agree that my age is above 18"
            return x

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'


        top.geometry("477x686+532+10")#1280x686
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#000328")

        top.resizable(False, False)
        global img
        img = ImageTk.PhotoImage(file="bg.png") #setting the bg color
        self.Background = tk.Label(top, image=img)
        self.Background.place(relx=0, rely=0, height=1000, width=1500)
        self.Background = img

        self.email_l = tk.Label(top)
        self.email_l.place(relx=0.163, rely=0.100, height=22, width=183)
        self.email_l.configure(anchor='w')
        self.email_l.configure(background="#000000")
        self.email_l.configure(disabledforeground="#a3a3a3")
        self.email_l.configure(font="-family {Segoe UI} -size 12")
        self.email_l.configure(foreground="#ffffff")
        self.email_l.configure(padx="6")
        self.email_l.configure(text='''Enter your email id:''')

        em = tk.StringVar() #email textbox
        self.email_e = tk.Entry(top, textvariable=em)
        self.email_e.place(relx=0.163, rely=0.150, height=20, relwidth=0.551)
        self.email_e.configure(background="white")
        self.email_e.configure(disabledforeground="#a3a3a3")
        self.email_e.configure(font="TkFixedFont")
        self.email_e.configure(foreground="#000000")
        self.email_e.configure(insertbackground="black")

        usern = tk.StringVar()
        self.username_e = tk.Entry(top, textvariable=usern) #username textbox
        self.username_e.place(relx=0.163, rely=0.250, height=20, relwidth=0.551)
        self.username_e.configure(background="white")
        # self.username_e.configure(cursor="fleur")
        self.username_e.configure(disabledforeground="#a3a3a3")
        self.username_e.configure(font="TkFixedFont")
        self.username_e.configure(foreground="#000000")
        self.username_e.configure(insertbackground="black")

        self.username_l = tk.Label(top)
        self.username_l.place(relx=0.161, rely=0.200, height=21, width=150)
        self.username_l.configure(activeforeground="#000328")
        self.username_l.configure(anchor='w')
        self.username_l.configure(background="#000328")
        self.username_l.configure(disabledforeground="#a3a3a3")
        self.username_l.configure(font="-family {Segoe UI} -size 12")
        self.username_l.configure(foreground="#ffffff")
        self.username_l.configure(text='''Enter username:''')

        self.password_l = tk.Label(top)
        self.password_l.place(relx=0.165, rely=0.300, height=31, width=149)
        self.password_l.configure(anchor='w')
        self.password_l.configure(background="#000328")
        # self.password_l.configure(cursor="fleur")
        self.password_l.configure(disabledforeground="#a3a3a3")
        self.password_l.configure(font="-family {Segoe UI} -size 12")
        self.password_l.configure(foreground="#ffffff")
        self.password_l.configure(text='''Enter password:''')

        pass1 = tk.StringVar()
        self.password_e = tk.Entry(top, textvariable=pass1) #password1
        self.password_e.place(relx=0.163, rely=0.350, height=20, relwidth=0.551)
        self.password_e.configure(background="white")
        self.password_e.configure(show="*") #hide the passwords
        self.password_e.configure(disabledforeground="#a3a3a3")
        self.password_e.configure(font="TkFixedFont")
        self.password_e.configure(foreground="#000000")
        self.password_e.configure(insertbackground="black")

        self.confirm_l = tk.Label(top)
        self.confirm_l.place(relx=0.163, rely=0.400, height=32, width=149)
        self.confirm_l.configure(activeforeground="#000328")
        self.confirm_l.configure(anchor='w')
        self.confirm_l.configure(background="#000328")
        self.confirm_l.configure(disabledforeground="#a3a3a3")
        self.confirm_l.configure(font="-family {Segoe UI} -size 12")
        self.confirm_l.configure(foreground="#ffffff")
        self.confirm_l.configure(text='''Confirm Password:''')

        pass2 = tk.StringVar()
        self.confirm_e = tk.Entry(top, textvariable=pass2) #confirm password textbox
        self.confirm_e.place(relx=0.163, rely=0.450, height=20, relwidth=0.551)
        self.confirm_e.configure(background="white")
        self.confirm_e.configure(show="*")
        self.confirm_e.configure(disabledforeground="#a3a3a3")
        self.confirm_e.configure(font="TkFixedFont")
        self.confirm_e.configure(foreground="#000000")
        self.confirm_e.configure(insertbackground="black")

        self.dob = tk.Label(top)
        self.dob.place(relx=0.163, rely=0.500, height=31, width=171) #dob
        self.dob.configure(anchor='w')
        self.dob.configure(background="#000328")
        self.dob.configure(disabledforeground="#a3a3a3")
        self.dob.configure(font="-family {Segoe UI} -size 12")
        self.dob.configure(foreground="#ffffff")
        self.dob.configure(text='''Enter Date of Birth''')

        self.cal = DateEntry(root, width=30, bg="darkblue", fg="white", year=2020, date_pattern='mm/dd/y')
        self.cal.place(relx=0.163, rely=0.550, height=31, width=171)

        self.address_l = tk.Label(top)
        self.address_l.place(relx=0.163, rely=0.600, height=31, width=171)
        self.address_l.configure(anchor='w')
        self.address_l.configure(background="#000328")
        self.address_l.configure(disabledforeground="#a3a3a3")
        self.address_l.configure(font="-family {Segoe UI} -size 12")
        self.address_l.configure(foreground="#ffffff")
        self.address_l.configure(text='''Enter Address''')

        ad = tk.StringVar()
        self.address_e = tk.Entry(top, textvariable=ad) #address
        self.address_e.place(relx=0.163, rely=0.650, height=20, relwidth=0.551)
        self.address_e.configure(background="white")
        # self.address_e.configure(cursor="fleur")
        self.address_e.configure(disabledforeground="#a3a3a3")
        self.address_e.configure(font="TkFixedFont")
        self.address_e.configure(foreground="#000000")
        self.address_e.configure(insertbackground="black")

        self.mobileno_l = tk.Label(top)
        self.mobileno_l.place(relx=0.163, rely=0.700, height=31, width=185) 
        self.mobileno_l.configure(anchor='w')
        self.mobileno_l.configure(background="#000328")
        self.mobileno_l.configure(disabledforeground="#a3a3a3")
        self.mobileno_l.configure(font="-family {Segoe UI} -size 12")
        self.mobileno_l.configure(foreground="#ffffff")
        self.mobileno_l.configure(text='''Enter your mobile number''')

        mob = tk.StringVar()
        self.mobileno_e = tk.Entry(top, textvariable=mob) #mobile number
        self.mobileno_e.place(relx=0.163, rely=0.750, height=20, relwidth=0.551)
        self.mobileno_e.configure(background="white")
        # self.mobileno_e.configure(cursor="fleur")
        self.mobileno_e.configure(disabledforeground="#a3a3a3")
        self.mobileno_e.configure(font="TkFixedFont")
        self.mobileno_e.configure(foreground="#000000")
        self.mobileno_e.configure(insertbackground="black")

        

        # dob=datetime.strptime(date_str2, '%m/%d/%y')
        var = IntVar() #confirming information
        self.checkAge = tk.Checkbutton(top, text="I confirm that all the above information is true to my knowledge",foreground="white",selectcolor="black", variable=var, onvalue=1, offvalue=0)
        self.checkAge.place(relx=0.1, rely=0.79, relheight=0.051, relwidth=0.9)
        #self.checkAge.place(relx=0.484, rely=0.781, relheight=0.081, relwidth=0.403)
        self.checkAge.configure(activebackground="#ececec")
        self.checkAge.configure(activeforeground="#000000")
        self.checkAge.configure(background="#000328")
        self.checkAge.configure(disabledforeground="#a3a3a3")
        self.checkAge.configure(cursor="hand2")
        self.checkAge.configure(highlightbackground="#d9d9d9")
        self.checkAge.configure(highlightcolor="black")
        self.checkAge.configure(justify='left')

        

        # self.LabelAge=tk.Label(top,text=age)

        self.Submit = tk.Button(top, command=lambda: ins(em, usern, pass1, pass2, ad, mob, self.cal,var))
        self.Submit.place(relx=0.300, rely=0.875, height=54, width=177)
        self.Submit.configure(activebackground="#ececec")
        self.Submit.configure(activeforeground="#000000")
        self.Submit.configure(background="#2ba5ff")
        self.Submit.configure(borderwidth="4")
        self.Submit.configure(cursor="hand2")
        self.Submit.configure(disabledforeground="#a3a3a3")
        self.Submit.configure(font="-family {Segoe UI} -size 14")
        self.Submit.configure(foreground="#000000")
        self.Submit.configure(highlightbackground="#d9d9d9")
        self.Submit.configure(highlightcolor="black")
        self.Submit.configure(pady="0")
        self.Submit.configure(text='Register')

        logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('register.py GUI created')


if __name__ == '__main__':
    vp_start_register()

