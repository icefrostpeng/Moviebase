from tkcalendar import Calendar, DateEntry
from datetime import date
from PIL import ImageTk, Image
import PIL
import pymysql
import pymysql.cursors
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import re
import sys
import smtplib
from random import randint
import membershipallocation
import home

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

import searchbar
# from memberbar import Memberbar
import homebar
import sidebar

from tkinter import messagebox

# ! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 10:33:09 AM IST  platform: Windows NT
""" 
import sys
import smtplib
from random import randint
from membershipallocation import *
from home import *
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

from searchbar import Searchbar
#from memberbar import Memberbar
from homebar import Homebar
from sidebar import Sidebar """
#####################################
sql_hostname = '127.0.0.1'
mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22


def querys(mem, email):
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
            # sql = f'UPDATE User set mem = {mem} where email = {email}';
            # UPDATE table_name SET field1 = new-value1, field2 = new-value2
            # [WHERE Clause]
            #######
            print(f'From querys {mem} {email}')
            sql = 'UPDATE User set mem = "{0}" where email = "{1}" '.format(mem, email)
            print(sql)
            # val = (mem, email)
            # sql = "INSERT INTO User (email,name,age,dob,addr,phno,pswd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            # val = (email, name, age, dob, addr, phno, pass1)
            cur.execute(sql)
            #############
            # cur.execute(sql)
            # cur.execute(q)
            conn.commit()
            conn.close()
            return 1
        except Exception as e:
            return 0


########################################
def vp_start_gui_P(name='XYZ', mem='a', product=[], email='abc@gmail.com'):
    '''Starting point when module is the main routine.'''
    if product is None:
        product = []
    global val, w, root
    root = tk.Tk()
    top = Payment(name, mem, product, email, root)
    root.mainloop()


w = None


def create_Payment(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Search(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Payment(w)
    return w, top


def destroy_Payment():
    global w
    w.destroy()
    w = None


class Payment:
    def __init__(self, name, mem, product, email, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1280x686+212+135")
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#000040")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.165, rely=0.168, relheight=0.845)
        self.TSeparator3.configure(orient="vertical")

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.818, rely=0.168, relheight=0.835)
        self.TSeparator4.configure(orient="vertical")

        self.Frame_f = tk.Frame(top)
        self.Frame_f.place(relx=0.18, rely=0.364, relheight=0.443, relwidth=0.621)
        self.Frame_f.configure(relief='groove')
        self.Frame_f.configure(borderwidth="2")
        self.Frame_f.configure(relief="groove")
        self.Frame_f.configure(background="#00002b")
        self.Frame_f.configure(highlightbackground="#d9d9d9")
        self.Frame_f.configure(highlightcolor="black")

        # Product name label
        self.Product_l = tk.Label(self.Frame_f)
        self.Product_l.place(relx=0.038, rely=0.099, height=113, width=764)
        self.Product_l.configure(activebackground="#f9f9f9")
        self.Product_l.configure(activeforeground="black")
        self.Product_l.configure(anchor='nw')
        self.Product_l.configure(background="#00002b")
        self.Product_l.configure(disabledforeground="#a3a3a3")
        self.Product_l.configure(font="-family {Segoe UI} -size 16")
        self.Product_l.configure(foreground="#bcfbfe")
        self.Product_l.configure(highlightbackground="#d9d9d9")
        self.Product_l.configure(highlightcolor="black")
        self.Product_l.configure(text='''Product_Name''')

        # Product
        print(f'From payment {product[0]} {product[1]}')
        self.Product_name = tk.Label(self.Frame_f)
        self.Product_name.place(relx=0.038, rely=0.3, height=113, width=764)
        self.Product_name.configure(activebackground="#f9f9f9")
        self.Product_name.configure(activeforeground="black")
        self.Product_name.configure(anchor='nw')
        self.Product_name.configure(background="#00002b")
        self.Product_name.configure(disabledforeground="#a3a3a3")
        self.Product_name.configure(font="-family {Segoe UI} -size 16")
        self.Product_name.configure(foreground="#bcfbfe")
        self.Product_name.configure(highlightbackground="#d9d9d9")
        self.Product_name.configure(highlightcolor="black")
        self.Product_name.configure(text=f'{product[0]} Membership')

        # Cost label
        self.Cost_l = tk.Label(self.Frame_f)
        self.Cost_l.place(relx=0.553, rely=0.039, height=50, width=267)
        self.Cost_l.configure(activebackground="#f9f9f9")
        self.Cost_l.configure(activeforeground="black")
        self.Cost_l.configure(background="#00002b")
        #self.Cost_l.configure(cursor="fleur")
        self.Cost_l.configure(disabledforeground="#a3a3a3")
        self.Cost_l.configure(font="-family {Segoe UI} -size 19")
        self.Cost_l.configure(foreground="#aaffff")
        self.Cost_l.configure(highlightbackground="#d9d9d9")
        self.Cost_l.configure(highlightcolor="black")
        self.Cost_l.configure(text='''Cost''')

        # Cost to be payed
        self.Cost_value = tk.Label(self.Frame_f)
        self.Cost_value.place(relx=0.553, rely=0.2, height=88, width=267)
        self.Cost_value.configure(activebackground="#f9f9f9")
        self.Cost_value.configure(activeforeground="black")
        self.Cost_value.configure(background="#00002b")
        #self.Cost_value.configure(cursor="fleur")
        self.Cost_value.configure(disabledforeground="#a3a3a3")
        self.Cost_value.configure(font="-family {Segoe UI} -size 19")
        self.Cost_value.configure(foreground="#aaffff")
        self.Cost_value.configure(highlightbackground="#d9d9d9")
        self.Cost_value.configure(highlightcolor="black")
        self.Cost_value.configure(text=product[1])

        def button_clicked(membership):
            top.destroy()
            print(f'From button {email}')
            email_generator('M')
            t = querys(membership, email)
            if t == 1:
                print('success')
            else:
                print('failure')
            membershipallocation.vp_start_gui_mem_allocation(membership, name, email)

        def button_home():
            print(f'from button {name} {mem} {email} and this is {product[0]}')
            top.destroy()
            home.vp_start_gui1(name, mem, email)

        self.Cancel_b = tk.Button(self.Frame_f, command=button_home)
        self.Cancel_b.place(relx=0.553, rely=0.724, height=44, width=117)
        self.Cancel_b.configure(activebackground="#ececec")
        self.Cancel_b.configure(activeforeground="#000000")
        self.Cancel_b.configure(background="#eb0214")
        self.Cancel_b.configure(disabledforeground="#a3a3a3")
        self.Cancel_b.configure(cursor="hand2")
        self.Cancel_b.configure(font="-family {Segoe UI} -size 12")
        self.Cancel_b.configure(foreground="#000000")
        self.Cancel_b.configure(highlightbackground="#d9d9d9")
        self.Cancel_b.configure(highlightcolor="black")
        self.Cancel_b.configure(pady="0")
        self.Cancel_b.configure(text='Cancel')

        self.Pay_b = tk.Button(self.Frame_f, command=lambda: button_clicked(product[0]))
        self.Pay_b.place(relx=0.742, rely=0.691, height=54, width=157)
        self.Pay_b.configure(activebackground="#ececec")
        self.Pay_b.configure(activeforeground="#000000")
        self.Pay_b.configure(background="#00c6c6")
        self.Pay_b.configure(cursor="hand2")
        self.Pay_b.configure(disabledforeground="#a3a3a3")
        self.Pay_b.configure(font="-family {Segoe UI} -size 22")
        self.Pay_b.configure(foreground="#000000")
        self.Pay_b.configure(highlightbackground="#d9d9d9")
        self.Pay_b.configure(highlightcolor="black")
        self.Pay_b.configure(pady="0")
        self.Pay_b.configure(text='Pay')

        searchbar.Searchbar.__init__(self,name,mem,email, top=None)
        homebar.Homebar.__init__(self, name, mem, top=None)
        sidebar.Sidebar.__init__(self, top=None)

        def random_with_N_digits():
            return randint(100000, 999999)

        def email_generator(action):
            sender_email = "rushiwatpal123@gmail.com"
            rec_email = email
            password = 'Rushi@12345'
            subject = 'Theatre Buzz'

            if action == 'O':
                otp = str(random_with_N_digits())
                body = f' \n OTP - {otp}'
                message = f'Subject: {subject}\n\n{body}'
                send_mail(sender_email, password, rec_email, message)
                user_otp = str(input('Enter your OTP: '))
                if user_otp == otp:
                    print('Login Success!')
                else:
                    print('Invalid OTP')

            elif action == 'T':
                body = f'Congratulations your ticket has been booked successfully\n\n' \
                       f'Cinema name: {cinema}\n' \
                       f'Movie name: {movie}\n' \
                       f'Slot: {slot}\n' \
                       f'seat number: {seat_number}'
                message = f'Subject: {subject}\n\n{body}'
                send_mail(sender_email, password, rec_email, message)
                print('Mail sent successfully')

            elif action == 'M':
                body = f'Congratulation for having {product[0]} Membership'
                message = f'Subject: {subject}\n\n{body}'
                send_mail(sender_email, password, rec_email, message)

            else:
                print('Invalid input!')

        def send_mail(sender_email, password, rec_email, message):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, rec_email, message)



