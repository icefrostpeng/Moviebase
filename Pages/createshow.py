#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 04:40:50 PM IST  platform: Windows NT

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
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = AddShow (root)
    root.mainloop()

w = None
def create_AddShow(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_AddShow(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = AddShow (w)
    return (w, top)

def destroy_AddShow():
    global w
    w.destroy()
    w = None
    
    
# def seats(slot_id,status, capacity):
#     with SSHTunnelForwarder(
#             (ssh_host, ssh_port),
#             ssh_username=ssh_user,
#             ssh_pkey=mypkey,
#             remote_bind_address=(sql_hostname, sql_port)) as tunnel:
#         try:
#             conn = pymysql.connect(host='127.0.0.1', user=sql_username,
#                     passwd=sql_password, db=sql_main_database,
#                     port=tunnel.local_bind_port)
#             cur=conn.cursor()
#             for i in range(capacity):
#                 sql = "INSERT INTO seatdet (slot_id,status) VALUES (%s, %s)"
#                 val = (slot_id,status)
#                 cur.execute(sql,val)
#                 #cur.execute(q)
#                 conn.commit()
#                 #cur.execute("select * from User")
#                 #result = cur.fetchone()
#                 #print(result)
#                 #data = pd.read_sql_query(q, conn)
#             conn.close()
#             print("sucess")
#             return 1
#         except Exception as e:
#             print(e)
#             return 0

# slot_id=input("write slot id:")
# status=input("write status :")
# seats(slot_id,status, capacity)

# def querys(cname,city,caddress,capacity):
#     with SSHTunnelForwarder(
#         	(ssh_host, ssh_port),
#         	ssh_username=ssh_user,
#         	ssh_pkey=mypkey,
#         	remote_bind_address=(sql_hostname, sql_port)) as tunnel:
#         try:
#         	conn = pymysql.connect(host='127.0.0.1', user=sql_username,
#         			passwd=sql_password, db=sql_main_database,
#         			port=tunnel.local_bind_port)
#         	cur=conn.cursor()
#         	sql = "INSERT INTO slotdet (theater_id,theater_name,city,theater_add, capacity) VALUES (%s, %s, %s, %s, %s)"
#         	val = ("28",cname, city, caddress, capacity)
#         	cur.execute(sql,val)
#         	#cur.execute(q)
#         	conn.commit()
#         	cur.execute("select * from User")
#         	result = cur.fetchone()
#         	print(result)
#         	#data = pd.read_sql_query(q, conn)
#         	conn.close()
#         	print("sucess")
#         	return 1
#         except Exception as e:
#         	print(e)
#         	return 0





# def  ins(name, cityname, address, capacity_s):
#     cname=name.get()
#     city=cityname.get()
#     caddress=address.get()
#     capacity=capacity_s.get()
#     if(len(cname)!=0 and len(caddress)!=0 and len(city)!=0):	
#         print(str(cname),str(city),str(caddress) , str(capacity))					
#         try:
#             t=querys(str(cname),str(city),str(caddress) , str(capacity))
#             if(t==1):
#                 messagebox.showinfo("Success", "Cinema Creation successfull")
#                 root.withdraw()
#                 create_AdHome(root)
#             else:
#                 messagebox.showerror("UnSucess", "Cinema Creation Unsuccessfull")

#         except Exception as e: print(e)

#     else:
#         messagebox.showerror("Error", "Fields cannot be empty")

class AddShow:
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
        
        
        em=tk.StringVar()
        usern=tk.StringVar()
        pass1=tk.StringVar()
        ad=tk.StringVar()
        mob=tk.StringVar()

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

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

        self.Show_date_l = tk.Label(top)
        self.Show_date_l.place(relx=0.203, rely=0.204, height=31, width=284)
        self.Show_date_l.configure(activebackground="#f9f9f9")
        self.Show_date_l.configure(activeforeground="black")
        self.Show_date_l.configure(anchor='w')
        self.Show_date_l.configure(background="#000040")
        self.Show_date_l.configure(disabledforeground="#a3a3a3")
        self.Show_date_l.configure(font="-family {Segoe UI} -size 13")
        self.Show_date_l.configure(foreground="#ffffff")
        self.Show_date_l.configure(highlightbackground="#d9d9d9")
        self.Show_date_l.configure(highlightcolor="black")
        self.Show_date_l.configure(text='''Enter Date:''')

        self.Desc_l = tk.Label(top)
        self.Desc_l.place(relx=0.203, rely=0.335, height=31, width=284)
        self.Desc_l.configure(activebackground="#f9f9f9")
        self.Desc_l.configure(activeforeground="black")
        self.Desc_l.configure(anchor='w')
        self.Desc_l.configure(background="#000040")
        self.Desc_l.configure(disabledforeground="#a3a3a3")
        self.Desc_l.configure(font="-family {Segoe UI} -size 13")
        self.Desc_l.configure(foreground="#ffffff")
        self.Desc_l.configure(highlightbackground="#d9d9d9")
        self.Desc_l.configure(highlightcolor="black")
        self.Desc_l.configure(text='''Enter time 24hr clock (hh:mm):''')

        self.Moviename_e = tk.Entry(top)
        self.Moviename_e.place(relx=0.203, rely=0.51, height=30, relwidth=0.222)
        self.Moviename_e.configure(background="white")
        self.Moviename_e.configure(disabledforeground="#a3a3a3")
        self.Moviename_e.configure(font="TkFixedFont")
        self.Moviename_e.configure(foreground="#000000")
        self.Moviename_e.configure(highlightbackground="#d9d9d9")
        self.Moviename_e.configure(highlightcolor="black")
        self.Moviename_e.configure(insertbackground="black")
        self.Moviename_e.configure(selectbackground="blue")
        self.Moviename_e.configure(selectforeground="white")

        self.Desc_e = tk.Entry(top)
        self.Desc_e.place(relx=0.203, rely=0.394, height=30, relwidth=0.12)
        self.Desc_e.configure(background="white")
        self.Desc_e.configure(disabledforeground="#a3a3a3")
        self.Desc_e.configure(font="TkFixedFont")
        self.Desc_e.configure(foreground="#000000")
        self.Desc_e.configure(highlightbackground="#d9d9d9")
        self.Desc_e.configure(highlightcolor="black")
        self.Desc_e.configure(insertbackground="black")
        self.Desc_e.configure(selectbackground="blue")
        self.Desc_e.configure(selectforeground="white")

        self.rating_l = tk.Label(top)
        self.rating_l.place(relx=0.203, rely=0.466, height=31, width=284)
        self.rating_l.configure(activebackground="#f9f9f9")
        self.rating_l.configure(activeforeground="black")
        self.rating_l.configure(anchor='w')
        self.rating_l.configure(background="#000040")
        self.rating_l.configure(disabledforeground="#a3a3a3")
        self.rating_l.configure(font="-family {Segoe UI} -size 13")
        self.rating_l.configure(foreground="#ffffff")
        self.rating_l.configure(highlightbackground="#d9d9d9")
        self.rating_l.configure(highlightcolor="black")
        self.rating_l.configure(text='''Enter Cinema Name:''')

        self.Createuser_b = tk.Button(top)
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
        self.Createuser_b.configure(text='''Create Screen''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.203, rely=0.583, height=41, width=262)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#000040")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Enter Screen No.''')

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.336, rely=0.598, relheight=0.047
                , relwidth=0.042)
        self.TCombobox1.configure(takefocus="")

if __name__ == '__main__':
    vp_start_gui()

