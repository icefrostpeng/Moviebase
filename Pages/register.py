import sys
from tkcalendar import Calendar,DateEntry
from datetime import date
from PIL import ImageTk, Image
import PIL
import datetime

import pymysql
import pymysql.cursors
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import re
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
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
def querys(email,name,age,dob,addr,phno,pass1):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=mypkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        try:
            conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                    passwd=sql_password, db=sql_main_database,
                    port=tunnel.local_bind_port)
            cur=conn.cursor()
            sql = "INSERT INTO User (email,name,age,dob,addr,phno,pswd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (email,name,age,dob,addr,phno,pass1)
            cur.execute(sql,val)
            #cur.execute(q)
            conn.commit()
            cur.execute("select * from User")
            result = cur.fetchone()
            print(result)
            #data = pd.read_sql_query(q, conn)
            conn.close()
            print("sucess")
            return 1
        except Exception as e:
            print(e)
            return 0
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def  ins(emails,usern,pass1,pass2,addre,mobi,cal):
    email=emails.get()
    username=usern.get()
    passs1=pass1.get()
    passs2=pass2.get()
    addres=addre.get()
    mob=mobi.get()
    if len(email)!=0 and len(username)!=0 and len(passs1)!=0 and len(passs2)!=0 and len(addres)!=0 and len(mob)!=0:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)
            if re.search(pat, passs1):
                if passs1==passs2:
                    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
                    if(Pattern.match(mob) and len(mob)==10):
                        dob=cal.get_date()
                        age=str(calculateAge(cal.get_date()))
                        dob=str(dob)
                        try:
                            print(email,username,age,dob,addres,mob,passs1)
                            t=querys(email,username,age,dob,addres,mob,passs1)
                            if(t==1):
                                messagebox.showinfo("Sucess", "Registration successfull")
                            else:
                                messagebox.showerror("UnSucess", "Registration Unsuccessfull")
                        except Exception as e: print(e)
                    else:
                        messagebox.showerror("Error", "Mobile Number Invalid")
                else:
                    messagebox.showerror("Error", "Both passwords do not match")
            else:
                messagebox.showerror("Error", "Enter a strong Password")
        else:
            messagebox.showerror("Error", "Invalid Email Id")
    else:
        messagebox.showerror("Error", "Fields cannot be empty")
    
    
def vp_start_register():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Register (root)
    root.mainloop()

w = None
def create_Register(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Register(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Register (w)
    return (w, top)

def destroy_Register():
    global w
    w.destroy()
    w = None



class Register:
    def ageagreement(self,age):
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
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("497x804+552+110")#1280x686
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#000328")
        
        
        top.resizable(False,False)
        global img
        img = ImageTk.PhotoImage(file="bg.png")
        self.Background = tk.Label(top,image = img)        
        self.Background.place(relx=0, rely=0, height=1000, width=1500)
        self.Background=img

        self.email_l = tk.Label(top)
        self.email_l.place(relx=0.163, rely=0.100, height=22, width=183)
        self.email_l.configure(anchor='w')
        self.email_l.configure(background="#000000")
        self.email_l.configure(disabledforeground="#a3a3a3")
        self.email_l.configure(font="-family {Segoe UI} -size 12")
        self.email_l.configure(foreground="#ffffff")
        self.email_l.configure(padx="6")
        self.email_l.configure(text='''Enter your email id:''')

        em=tk.StringVar()
        self.email_e = tk.Entry(top,textvariable=em)
        self.email_e.place(relx=0.163, rely=0.150, height=20, relwidth=0.551)
        self.email_e.configure(background="white")
        self.email_e.configure(disabledforeground="#a3a3a3")
        self.email_e.configure(font="TkFixedFont")
        self.email_e.configure(foreground="#000000")
        self.email_e.configure(insertbackground="black")

        usern=tk.StringVar()
        self.username_e = tk.Entry(top,textvariable=usern)
        self.username_e.place(relx=0.163, rely=0.250, height=20, relwidth=0.551)
        self.username_e.configure(background="white")
        #self.username_e.configure(cursor="fleur")
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
        #self.password_l.configure(cursor="fleur")
        self.password_l.configure(disabledforeground="#a3a3a3")
        self.password_l.configure(font="-family {Segoe UI} -size 12")
        self.password_l.configure(foreground="#ffffff")
        self.password_l.configure(text='''Enter password:''')

        pass1=tk.StringVar()
        self.password_e = tk.Entry(top,textvariable=pass1)
        self.password_e.place(relx=0.163, rely=0.350, height=20, relwidth=0.551)
        self.password_e.configure(background="white")
        #self.password_e.configure(cursor="fleur")
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

        pass2=tk.StringVar()
        self.confirm_e = tk.Entry(top,textvariable=pass2)
        self.confirm_e.place(relx=0.163, rely=0.450, height=20, relwidth=0.551)
        self.confirm_e.configure(background="white")
        #self.confirm_e.configure(cursor="fleur")
        self.confirm_e.configure(disabledforeground="#a3a3a3")
        self.confirm_e.configure(font="TkFixedFont")
        self.confirm_e.configure(foreground="#000000")
        self.confirm_e.configure(insertbackground="black")

        self.dob = tk.Label(top)
        self.dob.place(relx=0.163, rely=0.500, height=31, width=171)
        self.dob.configure(anchor='w')
        self.dob.configure(background="#000328")
        self.dob.configure(disabledforeground="#a3a3a3")
        self.dob.configure(font="-family {Segoe UI} -size 12")
        self.dob.configure(foreground="#ffffff")
        self.dob.configure(text='''Enter Date of Birth''')

        self.cal = DateEntry(root,width=30,bg="darkblue",fg="white",year=2020)
        self.cal.place(relx=0.163, rely=0.550, height=31, width=171)

        self.address_l = tk.Label(top)
        self.address_l.place(relx=0.163, rely=0.600, height=31, width=171)
        self.address_l.configure(anchor='w')
        self.address_l.configure(background="#000328")
        self.address_l.configure(disabledforeground="#a3a3a3")
        self.address_l.configure(font="-family {Segoe UI} -size 12")
        self.address_l.configure(foreground="#ffffff")
        self.address_l.configure(text='''Enter Address''')

        ad=tk.StringVar()
        self.address_e = tk.Entry(top,textvariable=ad)
        self.address_e.place(relx=0.163, rely=0.650, height=20, relwidth=0.551)
        self.address_e.configure(background="white")
        #self.address_e.configure(cursor="fleur")
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

        mob=tk.StringVar()
        self.mobileno_e = tk.Entry(top,textvariable=mob)
        self.mobileno_e.place(relx=0.163, rely=0.750, height=20, relwidth=0.551)
        self.mobileno_e.configure(background="white")
        #self.mobileno_e.configure(cursor="fleur")
        self.mobileno_e.configure(disabledforeground="#a3a3a3")
        self.mobileno_e.configure(font="TkFixedFont")
        self.mobileno_e.configure(foreground="#000000")
        self.mobileno_e.configure(insertbackground="black")

        self.age_warning = tk.Label(top)
        self.age_warning.place(relx=0.170, rely=0.81, height=21, width=100)
        self.age_warning.configure(background="#000328")
        #self.age_warning.configure(cursor="fleur")
        self.age_warning.configure(disabledforeground="#a3a3a3")
        self.age_warning.configure(foreground="#ffffff")
        self.age_warning.configure(text='''I confirm''')

        #self.LabelAge=tk.Label(top,text="I confirm")
        #ob=datetime.strftime(date_str2, '%m/%d/%y')

        self.checkAge=tk.Checkbutton(top,text="My age is above 18",foreground="red")
        self.checkAge.place(relx=0.484,rely=0.781,relheight=0.051,relwidth=0.404)
        self.checkAge.configure(activebackground="#ececec")
        self.checkAge.configure(activeforeground="#000000")
        self.checkAge.configure(background="#000328")
        self.checkAge.configure(disabledforeground="#a3a3a3")
        #self.checkAge.configure(foreground="#ffffff")
        self.checkAge.configure(highlightbackground="#d9d9d9")
        self.checkAge.configure(highlightcolor="black")
        self.checkAge.configure(justify='left')

        self.checkAge1 = tk.Checkbutton(top, text="My age is below 18", foreground="red")
        self.checkAge1.place(relx=0.484, rely=0.820, relheight=0.051, relwidth=0.404)
        self.checkAge1.configure(activebackground="#ececec")
        self.checkAge1.configure(activeforeground="#000000")
        self.checkAge1.configure(background="#000328")
        self.checkAge1.configure(disabledforeground="#a3a3a3")
        # self.checkAge.configure(foreground="#ffffff")
        self.checkAge1.configure(highlightbackground="#d9d9d9")
        self.checkAge1.configure(highlightcolor="black")
        self.checkAge1.configure(justify='left')








        self.Submit = tk.Button(top,command= lambda: ins(em,usern,pass1,pass2,ad,mob,self.cal))
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
        self.Submit.configure(text='''Register''')



if __name__ == '__main__':
    vp_start_register()

