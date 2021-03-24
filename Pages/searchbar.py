# -*- coding: utf-8 -*-

from tkinter import messagebox
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import sys
from PIL import ImageTk, Image
from search2 import *
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
		arr=list(cur.fetchall())
		l=[]
		for i in arr:
		    l.append(list(i))
		conn.close()
		return l

def search(var,name,mem,email, top):
	val=var.get()
	if (len(val)!=0):
		a="select * from moviedet where movie_name LIKE '{0}%'".format(val)
		print (a)
		b=query(a)
		if(len(b)!=0):
			top.destroy()
			#print(b)
			vp_start_gui(0,name,mem,email,b)
			
		else:
			a="select * from theaterdet where theater_name='{0}%'".format(val)
			print (a)
			b=query(a)
			if(len(b)!=0):
				top.destroy()
				#print(b)
				search2.vp_start_gui(1,name,mem,email,b)
				
			else:
				messagebox.showerror("Error", "No Movie or Theatre found!!!")
			
	else:
	    messagebox.showerror("Error", "Enter something")

	
	


class Searchbar():

	###############################################Search##########################################################################################
	def __init__(self,name,mem,email, top=None):
		print(top)
		self.Search_f = tk.LabelFrame(top)
		self.Search_f.place(relx=0.609, rely=0.044, relheight=0.06
		        , relwidth=0.322)
		self.Search_f.configure(relief='groove')
		self.Search_f.configure(foreground="black")
		self.Search_f.configure(background="#e8e8ff")
		self.Search_f.configure(highlightbackground="#d9d9d9")
		self.Search_f.configure(highlightcolor="black")
		var=StringVar()
		self.Search_e = tk.Entry(self.Search_f,textvariable=var)
		self.Search_e.place(relx=0.25, rely=0.1, height=38, relwidth=0.745
		        , bordermode='ignore')
		self.Search_e.configure(background="white")
		self.Search_e.configure(disabledforeground="#a3a3a3")
		self.Search_e.configure(font="-family {Segoe UI} -size 12")
		self.Search_e.configure(foreground="#000000")
		self.Search_e.configure(highlightbackground="#d9d9d9")
		self.Search_e.configure(highlightcolor="black")
		self.Search_e.configure(insertbackground="black")
		self.Search_e.configure(selectbackground="blue")
		self.Search_e.configure(selectforeground="white")
		print("here")

		self.Search_b = tk.Button(self.Search_f,command=lambda:search(var,name,mem,email, top) )
		self.Search_b.place(relx=0.0, rely=0.0, height=44, width=100
		        , bordermode='ignore')
		self.Search_b.configure(activebackground="#b3eaff")
		self.Search_b.configure(activeforeground="#000000")
		self.Search_b.configure(background="#00205b")
		self.Search_b.configure(disabledforeground="#a3a3a3")
		self.Search_b.configure(cursor="hand2")
		self.Search_b.configure(font="-family {Segoe UI} -size 12")
		self.Search_b.configure(foreground="#ffffff")
		self.Search_b.configure(highlightbackground="#d9d9d9")
		self.Search_b.configure(highlightcolor="black")
		self.Search_b.configure(pady="0")
		self.Search_b.configure(text='''Search''')
###############################################################################################################################################
