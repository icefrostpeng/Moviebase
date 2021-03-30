#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 04:29:51 PM IST  platform: Windows NT



#########################################################
'''Importing Packages'''
#########################################################
import sys

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
from tkinter import messagebox

import pymysql
import pymysql.cursors
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import re

from adhome import *

#########################################################
'''Declaring Variables'''
#########################################################
sql_hostname = '127.0.0.1'
mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22



#########################################################
'''Query to get new theater id and insert a new row in theaterdet'''
#########################################################
def querys(cname,city,caddress,capacity):
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
            cur.execute("select theater_id from theaterdet ORDER BY theater_id DESC LIMIT 1") #Gets latest theaterid
            theater_id=cur.fetchone()
            theater_id=theater_id[0]+1
            sql = "INSERT INTO theaterdet (theater_id,theater_name,city,theater_add, capacity) VALUES (%s, %s, %s, %s, %s)"
            val = (theater_id,cname, city, caddress, capacity)
            cur.execute(sql,val)
            #cur.execute(q)
            conn.commit()
        	#data = pd.read_sql_query(q, conn)
            conn.close()
            print("sucess")
            return 1
        except Exception as e:
        	print(e)
        	return 0



#########################################################
'''Calls, vaidates and performs the query'''
#########################################################

def  ins(name, cityname, address, capacity_s):
    cname=name.get()
    city=cityname.get()
    caddress=address.get()
    capacity=capacity_s.get()
    if(len(cname)!=0 and len(caddress)!=0 and len(city)!=0):	
        print(str(cname),str(city),str(caddress) , str(capacity))					
        try:
            t=querys(str(cname),str(city),str(caddress) , str(capacity))
            if(t==1):
                messagebox.showinfo("Success", "Cinema Creation successfull")
                root.withdraw()
                adhome.create_AdHome(root)
            else:
                messagebox.showerror("UnSucess", "Cinema Creation Unsuccessfull")

        except Exception as e: print(e)

    else:
        messagebox.showerror("Error", "Fields cannot be empty")

#########################################################
'''Page Functions'''
#########################################################
def vp_start_gui_createcinema():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = AddCinema (root)
    root.mainloop()

w = None
def create_AddCinema(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_AddCinema(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = AddCinema (w)
    return (w, top)

def destroy_AddCinema():
    global w
    w.destroy()
    w = None


#########################################################
''' Tkinter Page'''
#########################################################
class AddCinema:
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



        cname=tk.StringVar()
        city=tk.StringVar()
        caddress=tk.StringVar()
        capacity=tk.StringVar()


        
        img = ImageTk.PhotoImage(PIL.Image.open("Logo.png").resize((90, 90), PIL.Image.ANTIALIAS))
        #img = ImageTk.PhotoImage(file="Logo.png")
        self.Logo_image = tk.Label(top)
        self.Logo_image.place(relx=0.172, rely=0.015, height=92, width=124)
        self.Logo_image.configure(image=img)
        self.Logo_image=img

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

        self.Theatre_l = tk.Label(top)
        self.Theatre_l.place(relx=0.203, rely=0.204, height=31, width=284)
        self.Theatre_l.configure(activebackground="#f9f9f9")
        self.Theatre_l.configure(activeforeground="black")
        self.Theatre_l.configure(anchor='w')
        self.Theatre_l.configure(background="#000040")
        self.Theatre_l.configure(disabledforeground="#a3a3a3")
        self.Theatre_l.configure(font="-family {Segoe UI} -size 13")
        self.Theatre_l.configure(foreground="#ffffff")
        self.Theatre_l.configure(highlightbackground="#d9d9d9")
        self.Theatre_l.configure(highlightcolor="black")
        self.Theatre_l.configure(text='''Enter Cinema name:''')
        
        self.capacity_l = tk.Label(top)
        self.capacity_l.place(relx=0.203, rely=0.598, height=31, width=284)
        self.capacity_l.configure(anchor='w')
        self.capacity_l.configure(background="#000040")
        self.capacity_l.configure(disabledforeground="#a3a3a3")
        self.capacity_l.configure(font="-family {Segoe UI} -size 13")
        self.capacity_l.configure(foreground="#ffffff")
        self.capacity_l.configure(text='''Enter Address''')

        
        self.capacity_s = tk.Spinbox(top, from_=1.0, to=5.0)
        self.capacity_s.place(relx=0.205, rely=0.656, relheight=0.044
                , relwidth=0.034)
        self.capacity_s.configure(activebackground="#f9f9f9")
        self.capacity_s.configure(background="white")
        self.capacity_s.configure(buttonbackground="#d9d9d9")
        self.capacity_s.configure(disabledforeground="#a3a3a3")
        self.capacity_s.configure(font="TkDefaultFont")
        self.capacity_s.configure(foreground="black")
        self.capacity_s.configure(highlightbackground="black")
        self.capacity_s.configure(highlightcolor="black")
        self.capacity_s.configure(insertbackground="black")
        self.capacity_s.configure(selectbackground="blue")
        self.capacity_s.configure(selectforeground="white")

        self.City_l = tk.Label(top)
        self.City_l.place(relx=0.203, rely=0.335, height=31, width=284)
        self.City_l.configure(activebackground="#f9f9f9")
        self.City_l.configure(activeforeground="black")
        self.City_l.configure(anchor='w')
        self.City_l.configure(background="#000040")
        self.City_l.configure(disabledforeground="#a3a3a3")
        self.City_l.configure(font="-family {Segoe UI} -size 13")
        self.City_l.configure(foreground="#ffffff")
        self.City_l.configure(highlightbackground="#d9d9d9")
        self.City_l.configure(highlightcolor="black")
        self.City_l.configure(text='''Enter City''')

        self.Cinemaname_e = tk.Entry(top, textvariable=cname)
        self.Cinemaname_e.place(relx=0.203, rely=0.262, height=30
                , relwidth=0.222)
        self.Cinemaname_e.configure(background="white")
        self.Cinemaname_e.configure(disabledforeground="#a3a3a3")
        self.Cinemaname_e.configure(font="TkFixedFont")
        self.Cinemaname_e.configure(foreground="#000000")
        self.Cinemaname_e.configure(highlightbackground="#d9d9d9")
        self.Cinemaname_e.configure(highlightcolor="black")
        self.Cinemaname_e.configure(insertbackground="black")
        self.Cinemaname_e.configure(selectbackground="blue")
        self.Cinemaname_e.configure(selectforeground="white")

        self.City_e = tk.Entry(top, textvariable=city)
        self.City_e.place(relx=0.203, rely=0.394, height=30, relwidth=0.222)
        self.City_e.configure(background="white")
        self.City_e.configure(disabledforeground="#a3a3a3")
        self.City_e.configure(font="TkFixedFont")
        self.City_e.configure(foreground="#000000")
        self.City_e.configure(highlightbackground="#d9d9d9")
        self.City_e.configure(highlightcolor="black")
        self.City_e.configure(insertbackground="black")
        self.City_e.configure(selectbackground="blue")
        self.City_e.configure(selectforeground="white")
        
        
        self.address_l = tk.Label(top)
        self.address_l.place(relx=0.203, rely=0.598, height=31, width=284)
        self.address_l.configure(anchor='w')
        self.address_l.configure(background="#000040")
        self.address_l.configure(disabledforeground="#a3a3a3")
        self.address_l.configure(font="-family {Segoe UI} -size 13")
        self.address_l.configure(foreground="#ffffff")
        self.address_l.configure(text='''Enter Address''')

        self.address_e = tk.Entry(top,textvariable=caddress)
        self.address_e.place(relx=0.203, rely=0.656, height=30, relwidth=0.222)
        self.address_e.configure(background="white")
        self.address_e.configure(disabledforeground="#a3a3a3")
        self.address_e.configure(font="TkFixedFont")
        self.address_e.configure(foreground="#000000")
        self.address_e.configure(insertbackground="black")

        self.capacity_l = tk.Label(top)
        self.capacity_l.place(relx=0.203, rely=0.498, height=31, width=284)
        self.capacity_l.configure(anchor='w')
        self.capacity_l.configure(background="#000040")
        self.capacity_l.configure(disabledforeground="#a3a3a3")
        self.capacity_l.configure(font="-family {Segoe UI} -size 13")
        self.capacity_l.configure(foreground="#ffffff")
        self.capacity_l.configure(text='''Enter Capacity''')

        
        self.capacity_s = tk.Spinbox(top, from_=1.0, to=60, textvariable=capacity)
        self.capacity_s.place(relx=0.205, rely=0.556, relheight=0.044
                , relwidth=0.034)
        self.capacity_s.configure(activebackground="#f9f9f9")
        self.capacity_s.configure(background="white")
        self.capacity_s.configure(buttonbackground="#d9d9d9")
        self.capacity_s.configure(disabledforeground="#a3a3a3")
        self.capacity_s.configure(font="TkDefaultFont")
        self.capacity_s.configure(foreground="black")
        self.capacity_s.configure(highlightbackground="black")
        self.capacity_s.configure(highlightcolor="black")
        self.capacity_s.configure(insertbackground="black")
        self.capacity_s.configure(selectbackground="blue")
        self.capacity_s.configure(selectforeground="white")

        self.Createcinema_b = tk.Button(top, command=lambda: ins(cname,city,caddress,capacity))
        self.Createcinema_b.place(relx=0.594, rely=0.7, height=84, width=207)
        self.Createcinema_b.configure(activebackground="#ececec")
        self.Createcinema_b.configure(activeforeground="#000000")
        self.Createcinema_b.configure(background="#77eaea")
        self.Createcinema_b.configure(disabledforeground="#a3a3a3")
        self.Createcinema_b.configure(cursor="hand2")
        self.Createcinema_b.configure(font="-family {Segoe UI} -size 23")
        self.Createcinema_b.configure(foreground="#000000")
        self.Createcinema_b.configure(highlightbackground="#d9d9d9")
        self.Createcinema_b.configure(highlightcolor="black")
        self.Createcinema_b.configure(pady="0")
        self.Createcinema_b.configure(text='''Create Cinema''')


if __name__ == '__main__':
    vp_start_gui_createcinema()


