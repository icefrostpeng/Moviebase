import sys
import smtplib
from random import randint
from tkcalendar import Calendar, DateEntry
from datetime import date
from PIL import ImageTk, Image
import PIL
import smtplib
from random import randint
import pymysql
import pymysql.cursors
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import re
import register
import signin
# from signin import vp_start_gui
# from register import *

import hashlib

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


def querys(email, name, age, dob, addr, phno, pass1):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=mypkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        try:
            conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                                   passwd=sql_password, db=sql_main_database,
                                   port=tunnel.local_bind_port)
            cur = conn.cursor()
            sql = "INSERT INTO User (email,name,age,dob,addr,phno,pswd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (email, name, age, dob, addr, phno, pass1)
            cur.execute(sql, val)
            # cur.execute(q)
            conn.commit()
            cur.execute("select * from User")
            result = cur.fetchone()
            print(result)
            # data = pd.read_sql_query(q, conn)
            conn.close()
            print("sucess")
            return 1
        except Exception as e:
            print(e)
            return 0


# ! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 23, 2021 10:01:06 AM IST  platform: Windows NT


# from PIL import ImageTk, Image
# import PIL


def vp_start_gui_reg(data):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = RegOTP(data, root)
    root.mainloop()


w = None


def create_RegOTP(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_RegOTP(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = RegOTP(w)
    return w, top


def destroy_RegOTP():
    global w
    w.destroy()
    w = None


class RegOTP:
    def __init__(self, data, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        # values to be inserted

        email = data[0]
        name = data[1]
        age = data[2]
        dob = data[3]
        addr = data[4]
        phno = data[5]
        pswd = data[6]

        f=open("credentials.txt","a")
        creds=" \n " +email+" : "+pswd
        f.write(creds)
        f.close

        pswd=pswd.encode()
        pswd=hashlib.sha256(pswd).hexdigest()
        print(pswd)

        def random_with_N_digits():
            return randint(100000, 999999)

        def email_generator():
            sender_email = "rushiwatpal123@gmail.com"
            rec_email = email
            print(f'receiver email {email}')
            password = 'Rushi@12345'
            subject = 'Ticket Booker'
            otp = str(random_with_N_digits())
            body = f' \n OTP - {otp}'
            message = f'Subject: {subject}\n\n{body}'
            send_mail(sender_email, password, rec_email, message)
            print(otp)
            return otp

        def send_mail(sender_email, password, rec_email, message):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, rec_email, message)

        otp = email_generator()

        top.geometry("497x525+668+155")
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#000328")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        top.resizable(False, False)
        global img
        img = ImageTk.PhotoImage(file="bg.png")
        self.Background = tk.Label(top, image=img)
        self.Background.place(relx=0, rely=0, height=1000, width=1500)
        self.Background = img

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.08, rely=-0.019, height=222, width=424)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#000328")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 18")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Please check your email to Confirm your registration''')
        self.Label1.configure(wraplength="300")

        def on_click():
            user_otp = self.OTP_e.get()
            if user_otp == otp:
                '''print(email,name,age,dob,addr,phno,pswd)
                pswd=pswd.encode()
                pswd=hashlib.sha256(pswd).hexdigest()
                print(pswd)'''
                t = querys(email, name, age, dob, addr, phno, pswd)
                if t == 1:
                    print('Login Success from email!')
                    root.destroy()
                    signin.vp_start_gui()


                else:
                    print(f'failure from email')

            else:
                messagebox.showinfo("Failure", "Invalid OTP!\n Try again")
                root.destroy()
                register.vp_start_register()
                print('Invalid OTP')

        self.Submit = tk.Button(top, command=on_click)
        self.Submit.place(relx=0.302, rely=0.705, height=54, width=207)
        self.Submit.configure(activebackground="#ececec")
        self.Submit.configure(activeforeground="#000000")
        self.Submit.configure(background="#2ba5ff")
        self.Submit.configure(borderwidth="4")
        self.Submit.configure(disabledforeground="#a3a3a3")
        self.Submit.configure(font="-family {Segoe UI} -size 14")
        self.Submit.configure(foreground="#000000")
        self.Submit.configure(highlightbackground="#d9d9d9")
        self.Submit.configure(highlightcolor="black")
        self.Submit.configure(pady="0")
        self.Submit.configure(text='''Confirm Registration''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.302, rely=0.305, height=81, width=194)
        self.Label2.configure(activebackground="#000040")
        self.Label2.configure(activeforeground="white")
        self.Label2.configure(activeforeground="#000000")
        self.Label2.configure(background="#000328")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Enter OTP from Email''')

        self.OTP_e = tk.Entry(top)
        self.OTP_e.place(relx=0.322, rely=0.476, height=70, relwidth=0.37)
        self.OTP_e.configure(background="white")
     #   self.OTP_e.configure(cursor="fleur")
        self.OTP_e.configure(disabledforeground="#a3a3a3")
        self.OTP_e.configure(font="-family {Leelawadee UI Semilight} -size 23")
        self.OTP_e.configure(foreground="#000000")
        self.OTP_e.configure(insertbackground="black")


if __name__ == '__main__':
    vp_start_gui_reg()


