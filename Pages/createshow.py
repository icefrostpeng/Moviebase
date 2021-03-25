#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 04:40:50 PM IST  platform: Windows NT
import sys
from tkcalendar import Calendar,DateEntry
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



def vp_start_gui1(movie_id):
    '''Starting point when module is the main routine.'''
    
    global val, w, root, movie
    movie=movie_id
    root = tk.Tk()
    top = AddShow (root)
    root.mainloop()

w = None
def create_AddUser(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_AddUser(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = AddUser (w)
    return (w, top)


import pymysql
import pymysql.cursors
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import re
import adhome
from tkinter import messagebox

sql_hostname = '127.0.0.1'
mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
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
    
    
def seats(slot_id, capacity):
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
            for i in range(capacity):
                sql = "INSERT INTO seatdet (slot_id,status) VALUES (%s, %s)"
                val = (slot_id, "v")
                cur.execute(sql,val)
                #cur.execute(q)
                conn.commit()
            conn.close()
            print("sucess seats")
            return 1
        except Exception as e:
            print(e)
            return 0



def querys(theater_id, time, showdate, cost, movie_id):
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
            cur.execute("select slot_id from slotdet ORDER BY slot_id DESC LIMIT 1")
            slot_id=cur.fetchone()
            slot_id=slot_id[0]
            print(slot_id)
            slot_id = str(slot_id+1)            
            print((str(slot_id), str(theater_id), str(time), str(showdate), str(cost), str(movie_id)))
            sql = "INSERT INTO slotdet (slot_id, theater_id, timing, dates,cost, movie_id) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (str(slot_id), str(theater_id), str(time), str(showdate), str(cost), str(movie_id))
            cur.execute(sql,val)
            conn.commit()
            conn.close()
            print("success slot")
            return 1,slot_id
        except Exception as e:
        	print(e)
        	return 0,None




def querys2(theater_name):
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
            sql = "SELECT theater_id, capacity FROM theaterdet WHERE theater_name='{0}'".format(str(theater_name))

            cur.execute(sql)
            result = cur.fetchone()
            print(result)
            #data = pd.read_sql_query(q, conn)
            conn.close()
            print("sucess theaterid")
            return result
        except Exception as e:
         	print(e)
         	return 0
         
# print("SELECT theater_id, capacity FROM theaterdet WHERE theater_name='{0}'".format(theater_name))

def  ins(theater_name1, time1,showdate1, cost1):
    print(theater_name1, time1,showdate1, cost1)
    theater_name=theater_name1.get()
    time= time1.get()
    showdate=showdate1.get_date()
    cost=cost1.get()
    
    
    if(len(theater_name)!=0 and len(time)!=0 and len(str(showdate))!=0 and len(cost)!=0):
        regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
        pattern=re.compile(regex)
        print(time)
        print(re.search(pattern,str(time)))
        if pattern.search(time):
            try:
                cost=int(cost)					
                try:
                    result=querys2(theater_name)
                    if result:
                        theater_id, capacity=result                        
                        movie_id="24"
                        t,slot_id=querys(theater_id, time, showdate, str(cost), movie_id)
                        if t==1:
                            z=seats(slot_id, capacity)
                        else:
                            messagebox.showerror("Error", "Could not add a slot")
                        if(t==1):
                            messagebox.showinfo("Success", "Show Creation successfull")
                            root.withdraw()
                            create_AdHome(root)
                        else:
                            messagebox.showerror("UnSucess", "Show Creation Unsuccessfull")
                    else:
                        messagebox.showerror("Error", "Could not find that Theater")
                except Exception as e: print(e)
            except Exception as e: 
                print(e)
                messagebox.showerror("UnSucess", "Enter a number in cost")
        else:
            messagebox.showerror("Error", "time has to be in hh:mm format")
    else:
        messagebox.showerror("Error", "Fields cannot be empty")

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
        
        
        cname=tk.StringVar()
        showtime=tk.StringVar()
        showdate=tk.StringVar()
        cost=tk.StringVar()


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
        self.TSeparator3.configure(orient="vertical")

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
        self.TSeparator4.configure(orient="vertical")

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
        
        self.cal = DateEntry(root,width=30,bg="darkblue",fg="white",year=2021,date_pattern='mm/dd/y')
        self.cal.place(relx=0.203, rely=0.250, height=31, width=171)

        self.time_l = tk.Label(top)
        self.time_l.place(relx=0.203, rely=0.335, height=31, width=284)
        self.time_l.configure(activebackground="#f9f9f9")
        self.time_l.configure(activeforeground="black")
        self.time_l.configure(anchor='w')
        self.time_l.configure(background="#000040")
        self.time_l.configure(disabledforeground="#a3a3a3")
        self.time_l.configure(font="-family {Segoe UI} -size 13")
        self.time_l.configure(foreground="#ffffff")
        self.time_l.configure(highlightbackground="#d9d9d9")
        self.time_l.configure(highlightcolor="black")
        self.time_l.configure(text='''Enter time 24hr clock (hh:mm):''')

        self.theater_name = tk.Entry(top, textvariable=cname)
        self.theater_name.place(relx=0.203, rely=0.51, height=30, relwidth=0.222)
        self.theater_name.configure(background="white")
        self.theater_name.configure(disabledforeground="#a3a3a3")
        self.theater_name.configure(font="TkFixedFont")
        self.theater_name.configure(foreground="#000000")
        self.theater_name.configure(highlightbackground="#d9d9d9")
        self.theater_name.configure(highlightcolor="black")
        self.theater_name.configure(insertbackground="black")
        self.theater_name.configure(selectbackground="blue")
        self.theater_name.configure(selectforeground="white")

        self.time_e = tk.Entry(top, textvariable=showtime)
        self.time_e.place(relx=0.203, rely=0.394, height=30, relwidth=0.12)
        self.time_e.configure(background="white")
        self.time_e.configure(disabledforeground="#a3a3a3")
        self.time_e.configure(font="TkFixedFont")
        self.time_e.configure(foreground="#000000")
        self.time_e.configure(highlightbackground="#d9d9d9")
        self.time_e.configure(highlightcolor="black")
        self.time_e.configure(insertbackground="black")
        self.time_e.configure(selectbackground="blue")
        self.time_e.configure(selectforeground="white")

        self.theater_name_l = tk.Label(top)
        self.theater_name_l.place(relx=0.203, rely=0.466, height=31, width=284)
        self.theater_name_l.configure(activebackground="#f9f9f9")
        self.theater_name_l.configure(activeforeground="black")
        self.theater_name_l.configure(anchor='w')
        self.theater_name_l.configure(background="#000040")
        self.theater_name_l.configure(disabledforeground="#a3a3a3")
        self.theater_name_l.configure(font="-family {Segoe UI} -size 13")
        self.theater_name_l.configure(foreground="#ffffff")
        self.theater_name_l.configure(highlightbackground="#d9d9d9")
        self.theater_name_l.configure(highlightcolor="black")
        self.theater_name_l.configure(text='''Enter Cinema Name:''')
        
        self.cost_l = tk.Label(top)
        self.cost_l.place(relx=0.203, rely=0.550, height=31, width=284)
        self.cost_l.configure(activebackground="#f9f9f9")
        self.cost_l.configure(activeforeground="black")
        self.cost_l.configure(anchor='w')
        self.cost_l.configure(background="#000040")
        self.cost_l.configure(disabledforeground="#a3a3a3")
        self.cost_l.configure(font="-family {Segoe UI} -size 13")
        self.cost_l.configure(foreground="#ffffff")
        self.cost_l.configure(highlightbackground="#d9d9d9")
        self.cost_l.configure(highlightcolor="black")
        self.cost_l.configure(text='''Enter Cost in Rs:''')
        
        self.cost_e = tk.Entry(top, textvariable=cost)
        self.cost_e.place(relx=0.200, rely=0.600, height=30, relwidth=0.122)
        self.cost_e.configure(background="white")
        self.cost_e.configure(disabledforeground="#a3a3a3")
        self.cost_e.configure(font="TkFixedFont")
        self.cost_e.configure(foreground="#000000")
        self.cost_e.configure(highlightbackground="#d9d9d9")
        self.cost_e.configure(highlightcolor="black")
        self.cost_e.configure(insertbackground="black")
        self.cost_e.configure(selectbackground="blue")
        self.cost_e.configure(selectforeground="white")
        
        

        self.CreateShow_b = tk.Button(top, command=lambda: ins(cname, showtime,self.cal, cost))
        self.CreateShow_b.place(relx=0.594, rely=0.7, height=84, width=207)
        self.CreateShow_b.configure(activebackground="#ececec")
        self.CreateShow_b.configure(activeforeground="#000000")
        self.CreateShow_b.configure(background="#77eaea")
        self.CreateShow_b.configure(disabledforeground="#a3a3a3")
        self.CreateShow_b.configure(cursor="hand2")
        self.CreateShow_b.configure(font="-family {Segoe UI} -size 23")
        self.CreateShow_b.configure(foreground="#000000")
        self.CreateShow_b.configure(highlightbackground="#d9d9d9")
        self.CreateShow_b.configure(highlightcolor="black")
        self.CreateShow_b.configure(pady="0")
        self.CreateShow_b.configure(text='''Create Screen''')
        
        

if __name__ == '__main__':
    vp_start_gui()


