#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 22, 2021 10:52:48 AM IST  platform: Windows NT
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from PIL import *
from PIL import ImageTk, Image
import PIL

import hashlib
import logging

import sys

from nhome import *
from register import *
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

logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Signin.py initiated')

mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
# if you want to use ssh password use - ssh_password='your ssh password', bellow

sql_hostname = '127.0.0.1'
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22
def query(q):
	try:
		with SSHTunnelForwarder(
				(ssh_host, ssh_port),
				ssh_username=ssh_user,
				ssh_pkey=mypkey,
				remote_bind_address=(sql_hostname, sql_port)) as tunnel:
			try:
				conn = pymysql.connect(host='127.0.0.1', user=sql_username,
						passwd=sql_password, db=sql_main_database,
						port=tunnel.local_bind_port)
				logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
				logging.warning('Connection made to the MYSQL server and the database')
				data = pd.read_sql_query(q, conn)
				conn.close()
				return data
			except:
				data=[]
				# enter the excetion in log as dtabase error
				logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - WARNING - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
				logging.warning('Connection to MYSQL server/DB couldnt be established')
				return data
	except:
		data=[]
		# enter the excetion in log
		logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - WARNING - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
		logging.warning('SSH Tunnel couldnt be created')
		return data
def login(ema,passw):
    print("1")
    '''logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - DEBUG - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('1')'''
    df = query('select name,mem from User where email="{0}" and pswd="{1}"'.format(ema,passw))
    print(df)
    '''logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - DEBUG - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning(df)'''
    if(df.empty):
        return 0,0
    else:
        return df['name'][0],df['mem'][0]


def cal(root,em,pas):

    ema=em.get()
    passw=pas.get()
    if len(ema)==0 or len(passw)==0:
        messagebox.showerror("Error", "Email or Password cannot be empty")
        logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - WARNING - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('Email or Password fields are empty')
    else:
        passw=passw.encode()
        passw=hashlib.sha256(passw).hexdigest()
        print(passw)
        name,mem=login(ema,passw)
        if name!=0:
            if mem is None:
                mem='None'
            logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            logging.warning('Signin successful for '+str(ema))
            root.destroy()
            print(f'from sign in {name} {mem} {ema}')
            vp_start_gui1(name,mem,ema)
        else:
            messagebox.showerror("Error", "Invalid Credentails!!!")
            logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - WARNING - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            logging.warning('Signin unsuccessful for '+str(ema))
            em.set("")
            pas.set("")
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Signin (root)
    root.mainloop()

w = None
def create_Signin(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Signin(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Signin (w)
    return (w, top)

def destroy_Signin():
    global w
    w.destroy()
    w = None

class Signin:
    global to
    def regi(self,event):
        global to
        to.destroy()
        vp_start_register()
    def __init__(self, top=None):
        global to
        to=top
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("427x677+660+210")
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1,  1)
        top.title("Login")
        top.configure(background="#000328")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(False,False)

        global img
        img = ImageTk.PhotoImage(file="bg.png")
        self.Background = tk.Label(top,image = img)
        self.Background.place(relx=0, rely=0, height=1000, width=1500)
        self.Background=img


        img = ImageTk.PhotoImage(PIL.Image.open("Logo.png").resize((150, 200), PIL.Image.ANTIALIAS))
        #img = ImageTk.PhotoImage(file="Logo.png")
        self.Logo_image = tk.Label(top)
        self.Logo_image.place(relx=0.280, rely=0.025, height=150, width=200)
        self.Logo_image.configure(image=img)
       # self.Logo_image=img

        em=tk.StringVar()
        self.email_e = tk.Entry(top,textvariable=em)
        self.email_e.place(relx=0.234, rely=0.355, height=30, relwidth=0.548)
        self.email_e.configure(background="white")
        self.email_e.configure(disabledforeground="#a3a3a3")
        self.email_e.configure(font="TkFixedFont")
        self.email_e.configure(foreground="#000000")
        self.email_e.configure(highlightbackground="#d9d9d9")
        self.email_e.configure(highlightcolor="black")
        self.email_e.configure(insertbackground="black")
        self.email_e.configure(selectbackground="blue")
        self.email_e.configure(selectforeground="white")

        self.email_l = tk.Label(top)
        self.email_l.place(relx=0.211, rely=0.31, height=21, width=124)
        self.email_l.configure(activebackground="#f9f9f9")
        self.email_l.configure(activeforeground="black")
        self.email_l.configure(background="#000328")
        self.email_l.configure(disabledforeground="#a3a3a3")
        self.email_l.configure(font="-family {Segoe UI} -size 12")
        self.email_l.configure(foreground="#ffffff")
        self.email_l.configure(highlightbackground="#d9d9d9")
        self.email_l.configure(highlightcolor="black")
        self.email_l.configure(text='''Email address:''')

        pas=tk.StringVar()
        self.password_e = tk.Entry(top,textvariable=pas)
        self.password_e.place(relx=0.234, rely=0.517, height=30, relwidth=0.548)
        self.password_e.configure(background="white")
        self.password_e.configure(show="*")
        self.password_e.configure(disabledforeground="#a3a3a3")
        self.password_e.configure(font="TkFixedFont")
        self.password_e.configure(foreground="#000000")
        self.password_e.configure(highlightbackground="#d9d9d9")
        self.password_e.configure(highlightcolor="black")
        self.password_e.configure(insertbackground="black")
        self.password_e.configure(selectbackground="blue")
        self.password_e.configure(selectforeground="white")

        self.password_l = tk.Label(top)
        self.password_l.place(relx=0.187, rely=0.473, height=21, width=104)
        self.password_l.configure(activebackground="#f9f9f9")
        self.password_l.configure(activeforeground="black")
        self.password_l.configure(background="#000328")
        self.password_l.configure(disabledforeground="#a3a3a3")
        self.password_l.configure(font="-family {Segoe UI} -size 12")
        self.password_l.configure(foreground="#ffffff")
        self.password_l.configure(highlightbackground="#d9d9d9")
        self.password_l.configure(highlightcolor="black")
        self.password_l.configure(text='''Password:''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.656, rely=0.62, height=21, width=74)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#000328")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(cursor="hand2")
        self.Label3.configure(font="-family {Segoe UI} -size 12 -underline 1")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Signup''')
        self.Label3.bind('<Button>',self.regi)

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.187, rely=0.62, height=21, width=174)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#000328")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(cursor="hand2")
        self.Label4.configure(font="-family {Segoe UI} -size 12")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Don't have an Account?''')


        self.Submit = tk.Button(top,command=lambda: cal(top,em,pas))
        self.Submit.place(relx=0.300, rely=0.675, height=54, width=177)
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
        self.Submit.configure(text='Sign In')

        logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(name)s - INFO - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning('Signin.py GUI created')

if __name__ == '__main__':
    vp_start_gui()





