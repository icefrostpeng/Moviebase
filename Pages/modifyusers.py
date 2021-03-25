# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:02:56 2021

@author: Elton
"""

#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 04:20:35 PM IST  platform: Windows NT

from functools import partial
import sys
from datetime import date
from PIL import ImageTk, Image
import PIL
from tkcalendar import Calendar,DateEntry
try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

try:
	import ttk
	py3 = False
except ImportError:
	import tkinter.ttk as ttk
	py3 = True
from tkinter import *
#from home import *

#from Deletemoviebar import Deletemoviebar

import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
sql_hostname = '127.0.0.1'
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22
from adhome import *

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = AddMovie (root)
    root.mainloop()
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def querys(em,name,age,dob,addr,phno,pswd):
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
            sql = "UPDATE User SET name = %s,age = %s,dob = %s,addr = %s,phno = %s, pswd = %s WHERE email='{0}'".format(em)
            val = (name,age,dob,addr,phno,pswd)
            cur.execute(sql,val)
            #cur.execute(q)
            conn.commit()
        	#data = pd.read_sql_query(q, conn)
            conn.close()
            print("success")
            return 1
        except Exception as e:
        	print(e)
        	return 0


def  ins(emails,usern,pass1,addre,mobi,cal):
    email=emails.get()
    username=usern.get()
    passs1=pass1.get()
    addres=addre.get()
    mob=mobi.get()
    print(len(email), len(username), len(passs1), len(addres), len(mob))
    if(len(email)!=0 and len(username)!=0 and len(passs1)!=0 and len(addres)!=0 and len(mob)!=0):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)):
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)
            if(re.search(pat, passs1)):
                    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
                    if(Pattern.match(mob) and len(mob)==10):
                        dob=cal.get_date()
                        age=str(calculateAge(cal.get_date()))						
                        dob=str(dob)						
                        try:
                            print(email,username,age,dob,addres,mob,passs1)
                            t=querys(email,username,age,dob,addres,mob,passs1)
                            if(t==1):
                                messagebox.showinfo("Sucess", "Updation successfull")
                                root.withdraw()
                                create_AdHome(root)
                                
                            else:
                                messagebox.showerror("UnSucess", "Updation Unsuccessfull")
                        except Exception as e: print(e)
                    else:
                        messagebox.showerror("Error", "Mobile Number Invalid")
            else:
                messagebox.showerror("Error", "Enter a strong Password")
        else:
        	messagebox.showerror("Error", "Invalid Email Id")
    else:
        messagebox.showerror("Error", "Fields cannot be empty")
    print(age)

w = None
def create_AddMovie(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_AddUser(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = AddMovie (w)
    return (w, top)

def destroy_AddMovie():
    global w
    w.destroy()
    w = None

class AddMovie:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1280x686+280+126")
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#000040")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
        self.TSeparator3.configure(orient="vertical")

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
        self.TSeparator4.configure(orient="vertical")

        self.uid=tk.StringVar()
        self.em=tk.StringVar()
        self.usern=tk.StringVar()
        self.pass1=tk.StringVar()
        self.ad=tk.StringVar()
        self.mob=tk.StringVar()

<<<<<<< HEAD

=======
>>>>>>> 0aeb174a7ebdc7d2ffef804e056ce022fbf14476
        img = ImageTk.PhotoImage(PIL.Image.open("Logo.png").resize((90, 90), PIL.Image.ANTIALIAS))
        #img = ImageTk.PhotoImage(file="Logo.png")
        self.Logo_image = tk.Label(top)
        self.Logo_image.place(relx=0.172, rely=0.015, height=92, width=124)
        self.Logo_image.configure(image=img)
        self.Logo_image=img
<<<<<<< HEAD
=======
        
        '''self.Logo_image = tk.Label(top)
        self.Logo_image.place(relx=0.234, rely=0.029, height=92, width=124)
        self.Logo_image.configure(background="#d9d9d9")
        self.Logo_image.configure(disabledforeground="#a3a3a3")
        self.Logo_image.configure(foreground="#000000")
        self.Logo_image.configure(text=''Label'')'''
>>>>>>> 0aeb174a7ebdc7d2ffef804e056ce022fbf14476

        self.Title_l = tk.Label(top)
        self.Title_l.place(relx=0.359, rely=0.044, height=61, width=372)
        self.Title_l.configure(background="#000040")
        self.Title_l.configure(disabledforeground="#a3a3a3")
        self.Title_l.configure(font="-family {Segoe UI} -size 22")
        self.Title_l.configure(foreground="#ffffff")
        self.Title_l.configure(text='''Theatre Buzz Admin Page''')

        self.Username_l = tk.Label(top)
        
        self.Username_l.place(relx=0.203, rely=0.475, height=30, relwidth=0.222)
        self.Username_l.configure(anchor='w')
        self.Username_l.configure(background="#000040")
        self.Username_l.configure(disabledforeground="#a3a3a3")
        self.Username_l.configure(font="-family {Segoe UI} -size 13")
        self.Username_l.configure(foreground="#ffffff")
        self.Username_l.configure(text='''Enter Username:''')

        self.password_l = tk.Label(top)
        self.password_l.place(relx=0.203, rely=0.335, height=31, width=284)
        self.password_l.configure(anchor='w')
        self.password_l.configure(background="#000040")
        self.password_l.configure(disabledforeground="#a3a3a3")
        self.password_l.configure(font="-family {Segoe UI} -size 13")
        self.password_l.configure(foreground="#ffffff")
        self.password_l.configure(text='''Enter password:''')

        self.username_e = tk.Entry(top,textvariable=self.usern)
        self.username_e.place(relx=0.203, rely=0.525, height=30, relwidth=0.222)
        self.username_e.configure(background="white")
        self.username_e.configure(disabledforeground="#a3a3a3")
        self.username_e.configure(font="TkFixedFont")
        self.username_e.configure(foreground="#000000")
        self.username_e.configure(insertbackground="black")

        self.password_e = tk.Entry(top,textvariable=self.pass1)
        self.password_e.place(relx=0.203, rely=0.394, height=30, relwidth=0.222)
        self.password_e.configure(background="white")
        self.password_e.configure(disabledforeground="#a3a3a3")
        self.password_e.configure(font="TkFixedFont")
        self.password_e.configure(foreground="#000000")
        self.password_e.configure(insertbackground="black")

        self.email_l = tk.Label(top)
        self.email_l.place(relx=0.203, rely=0.204, height=31, width=284)
        self.email_l.configure(anchor='w')
        self.email_l.configure(background="#000040")
        self.email_l.configure(disabledforeground="#a3a3a3")
        self.email_l.configure(font="-family {Segoe UI} -size 13")
        self.email_l.configure(foreground="#ffffff")
        self.email_l.configure(text='''Enter Email Address:''')

        self.email_e = tk.Entry(top,textvariable=self.em)
        self.email_e.place(relx=0.203, rely=0.262, height=30, relwidth=0.222)
        self.email_e.configure(background="white")
        self.email_e.configure(disabledforeground="#a3a3a3")
        self.email_e.configure(font="TkFixedFont")
        self.email_e.configure(foreground="#000000")
        self.email_e.configure(insertbackground="black")

        self.address_l = tk.Label(top)
        self.address_l.place(relx=0.203, rely=0.598, height=31, width=284)
        self.address_l.configure(anchor='w')
        self.address_l.configure(background="#000040")
        self.address_l.configure(disabledforeground="#a3a3a3")
        self.address_l.configure(font="-family {Segoe UI} -size 13")
        self.address_l.configure(foreground="#ffffff")
        self.address_l.configure(text='''Enter Address''')

        self.address_e = tk.Entry(top,textvariable=self.ad)
        self.address_e.place(relx=0.203, rely=0.656, height=30, relwidth=0.222)
        self.address_e.configure(background="white")
        self.address_e.configure(disabledforeground="#a3a3a3")
        self.address_e.configure(font="TkFixedFont")
        self.address_e.configure(foreground="#000000")
        self.address_e.configure(insertbackground="black")

        self.mobile_l = tk.Label(top)
        self.mobile_l.place(relx=0.203, rely=0.729, height=31, width=284)
        self.mobile_l.configure(anchor='w')
        self.mobile_l.configure(background="#000040")
        self.mobile_l.configure(disabledforeground="#a3a3a3")
        self.mobile_l.configure(font="-family {Segoe UI} -size 13")
        self.mobile_l.configure(foreground="#ffffff")
        self.mobile_l.configure(text='''Enter Mobile number:''')

        self.mobile_e = tk.Entry(top,textvariable=self.mob)
        self.mobile_e.place(relx=0.203, rely=0.787, height=30, relwidth=0.222)
        self.mobile_e.configure(background="white")
        self.mobile_e.configure(disabledforeground="#a3a3a3")
        self.mobile_e.configure(font="TkFixedFont")
        self.mobile_e.configure(foreground="#000000")
        self.mobile_e.configure(insertbackground="black")

        self.dob_l = tk.Label(top)
        self.dob_l.place(relx=0.563, rely=0.204, height=32, width=221)
        self.dob_l.configure(anchor='w')
        self.dob_l.configure(background="#000040")
        self.dob_l.configure(disabledforeground="#a3a3a3")
        self.dob_l.configure(font="-family {Segoe UI} -size 13")
        self.dob_l.configure(foreground="#ffffff")
        self.dob_l.configure(text='''Enter user Date of Bith''')
        
                
        self.cal = DateEntry(root,width=30,bg="darkblue",fg="white",year=2010,date_pattern='mm/dd/y')
        self.cal.place(relx=0.563, rely=0.250, height=31, width=171)

        self.Createuser_b = tk.Button(top,command= lambda: ins(self.em,self.usern,self.pass1,self.ad,self.mob,self.cal))
        self.Createuser_b.place(relx=0.594, rely=0.7, height=84, width=207)
        self.Createuser_b.configure(activebackground="#ececec")
        self.Createuser_b.configure(activeforeground="#000000")
        self.Createuser_b.configure(background="#77eaea")
        self.Createuser_b.configure(disabledforeground="#a3a3a3")
        self.Createuser_b.configure(cursor="hand2")
        self.Createuser_b.configure(font="-family {Segoe UI} -size 23")
        self.Createuser_b.configure(foreground="#000000")
        self.Createuser_b.configure(highlightbackground="#d9d9d9")
        self.Createuser_b.configure(highlightcolor="black")
        self.Createuser_b.configure(pady="0")
        self.Createuser_b.configure(text='''Modify User''')
        
        self.Get_info_b = tk.Button(top, command=lambda: self.getinfo())
        self.Get_info_b.place(relx=0.594, rely=0.47, height=84, width=207)
        self.Get_info_b.configure(activebackground="#ececec")
        self.Get_info_b.configure(activeforeground="#000000")
        self.Get_info_b.configure(background="#77eaea")
        self.Get_info_b.configure(disabledforeground="#a3a3a3")
        self.Get_info_b.configure(cursor="hand2")
        self.Get_info_b.configure(font="-family {Segoe UI} -size 23")
        self.Get_info_b.configure(foreground="#000000")
        self.Get_info_b.configure(highlightbackground="#d9d9d9")
        self.Get_info_b.configure(highlightcolor="black")
        self.Get_info_b.configure(pady="0")
        self.Get_info_b.configure(text='''Get Info''')
        
    def querysd(self,user):
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
                cur.execute("select email, name, dob, addr, phno, mem, pswd from User WHERE email='{0}'".format(user))
                values=cur.fetchone()
                print(values)
                #cur.execute(q)
                conn.commit()
            	#data = pd.read_sql_query(q, conn)
                conn.close()
                print("success")
                return values
            except Exception as e:
            	print(e)
            	return None
    
    def getinfo(self):        						

                user=self.em.get()
                if len(user):
                    result=self.querysd(user)
                    if(result):
                        self.em.set(result[0])
                        self.usern.set(result[1])
                        self.ad.set(result[3])
                        self.mob.set(result[4])
                        self.pass1.set(result[6])
                        year,month,day=result[2].split("-")
                        self.cal = DateEntry(root,width=30,bg="darkblue",fg="white",year=int(year),month=int(month),day=int(day),date_pattern='mm/dd/y')
                        self.cal.place(relx=0.563, rely=0.250, height=31, width=171)

                else:
                    messagebox.showerror("UnSucess", "Couldnt find user")
    


if __name__ == '__main__':
    vp_start_gui()


