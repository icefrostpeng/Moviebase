#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 05:09:10 PM IST  platform: Windows NT

from functools import partial
from tkinter import messagebox
import sys
import adhome
from PIL import ImageTk, Image
import PIL
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
import adhome
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
global co,mod,wil,flag
flag=1
wil=[]
co=0
mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
sql_hostname = '127.0.0.1'
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22
def query(q):
	with SSHTunnelForwarder(
			(ssh_host, ssh_port),
			ssh_username=ssh_user,
			ssh_pkey=mypkey,
			remote_bind_address=(sql_hostname, sql_port)) as tunnel:
		conn = pymysql.connect(host='127.0.0.1', user=sql_username,
				passwd=sql_password, db=sql_main_database,
				port=tunnel.local_bind_port)
		cur=conn.cursor()
		cur.execute(q)
		result=cur.fetchone()
		conn.close()
		return result
    
def vp_start_gui_deltheater():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = delcinema (root)
    root.mainloop()

w = None
def create_delcinema(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_delcinema(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = delcinema (w)
    return (w, top)

def destroy_delcinema():
    global w
    w.destroy()
    w = None
    
def delete_theater(theater):
    tname=theater.get()
    try:
        print("Delete FROM theaterdet where theater_name='{0}'".format(tname))
        q=query("Delete FROM theaterdet where theater_name='{0}'".format(tname))
        print(q)
    except Exception as e:
        print(e)
        messagebox.showerror("Failed", "Could not Delete the theater")
    root.destroy()
    adhome.vp_start_guih()
    

class delcinema:
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
        
        theater=tk.StringVar()

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
        self.TSeparator3.configure(orient="vertical")

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
        self.TSeparator4.configure(orient="vertical")

        self.Logo_image = tk.Label(top)
        self.Logo_image.place(relx=0.234, rely=0.029, height=92, width=124)
        self.Logo_image.configure(activebackground="#f9f9f9")
        self.Logo_image.configure(activeforeground="black")
        self.Logo_image.configure(background="#d9d9d9")
        self.Logo_image.configure(disabledforeground="#a3a3a3")
        self.Logo_image.configure(foreground="#000000")
        self.Logo_image.configure(highlightbackground="#d9d9d9")
        self.Logo_image.configure(highlightcolor="black")
        self.Logo_image.configure(text='''Label''')

        self.Title_l = tk.Label(top)
        self.Title_l.place(relx=0.359, rely=0.044, height=61, width=372)
        self.Title_l.configure(activebackground="#f9f9f9")
        self.Title_l.configure(activeforeground="black")
        self.Title_l.configure(background="#000040")
        self.Title_l.configure(disabledforeground="#a3a3a3")
        self.Title_l.configure(font="-family {Segoe UI} -size 22")
        self.Title_l.configure(foreground="#ffffff")
        self.Title_l.configure(highlightbackground="#d9d9d9")
        self.Title_l.configure(highlightcolor="black")
        self.Title_l.configure(text='''Theatre Buzz Admin Page''')

        self.Message_l = tk.Label(top)
        self.Message_l.place(relx=0.219, rely=0.233, height=281, width=694)
        self.Message_l.configure(activebackground="#f9f9f9")
        self.Message_l.configure(activeforeground="black")
        self.Message_l.configure(background="#000040")
        self.Message_l.configure(disabledforeground="#a3a3a3")
        self.Message_l.configure(font="-family {Segoe UI} -size 18")
        self.Message_l.configure(foreground="#ffffff")
        self.Message_l.configure(highlightbackground="#d9d9d9")
        self.Message_l.configure(highlightcolor="black")
        self.Message_l.configure(text='''Sorry There are shows lined up with current movie. Hence cannot be deleted. Try deleting the shows first!/Do you want to delete xyz Movie?''')
        self.Message_l.configure(wraplength="600")
        
        self.Theater_l = tk.Label(top)
        self.Theater_l.place(relx=0.203, rely=0.554, height=31, width=284)
        self.Theater_l.configure(activebackground="#f9f9f9")
        self.Theater_l.configure(activeforeground="black")
        self.Theater_l.configure(anchor='w')
        self.Theater_l.configure(background="#000040")
        self.Theater_l.configure(disabledforeground="#a3a3a3")
        self.Theater_l.configure(font="-family {Segoe UI} -size 13")
        self.Theater_l.configure(foreground="#ffffff")
        self.Theater_l.configure(highlightbackground="#d9d9d9")
        self.Theater_l.configure(highlightcolor="black")
        self.Theater_l.configure(text='''Enter the name of Theater you want to Delete''')

        self.Theater_e = tk.Entry(top, textvariable=theater)
        self.Theater_e.place(relx=0.203, rely=0.612, height=30, relwidth=0.222)
        self.Theater_e.configure(background="white")
        self.Theater_e.configure(disabledforeground="#a3a3a3")
        self.Theater_e.configure(font="TkFixedFont")
        self.Theater_e.configure(foreground="#000000")
        self.Theater_e.configure(highlightbackground="#d9d9d9")
        self.Theater_e.configure(highlightcolor="black")
        self.Theater_e.configure(insertbackground="black")
        self.Theater_e.configure(selectbackground="blue")
        self.Theater_e.configure(selectforeground="white")

        self.delcinema_b = tk.Button(top, command=lambda: delete_theater(theater))
        self.delcinema_b.place(relx=0.594, rely=0.7, height=84, width=207)
        self.delcinema_b.configure(activebackground="#ececec")
        self.delcinema_b.configure(activeforeground="#000000")
        self.delcinema_b.configure(background="#77eaea")
        self.delcinema_b.configure(cursor="hand2")
        self.delcinema_b.configure(disabledforeground="#a3a3a3")
        self.delcinema_b.configure(font="-family {Segoe UI} -size 23")
        self.delcinema_b.configure(foreground="#000000")
        self.delcinema_b.configure(highlightbackground="#d9d9d9")
        self.delcinema_b.configure(highlightcolor="black")
        self.delcinema_b.configure(pady="0")
        self.delcinema_b.configure(text='''Delete Theater''')

if __name__ == '__main__':
    vp_start_gui_deltheater()


