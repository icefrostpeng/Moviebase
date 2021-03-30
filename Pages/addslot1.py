# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:01:22 2021

@author: Elton
"""

#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 23, 2021 05:31:05 PM IST  platform: Windows NT
#called From: Adhome
#Redirects to: Adhome


#########################################################
'''Importing Packages'''
#########################################################
from functools import partial
from tkinter import messagebox
import sys
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
import createshow

import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder

#########################################################
'''Declaring Variables'''
#########################################################

mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
sql_hostname = '127.0.0.1'
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22

#########################################################
'''Query that returns a list of results as per the query string passed to it'''
#########################################################
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



#########################################################
'''Query that returns executes the Query string passed to it'''
#########################################################
def queryn(q):
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
		 conn.commit()
		 conn.close()
		 return 1
	
#########################################################
'''Page Functions'''
#########################################################
	
def back(top):
 	top.destroy()
def vp_start_gui_add_slot():
 	'''Starting point when module is the main routine.'''
 	global val, w, root
 	root = tk.Tk()
 	m=query("Select * from moviedet")
 	top = findmovie (m,root)
 	root.mainloop()

def create_findmovie(rt, *args, **kwargs):
 	'''Starting point when module is imported by another module.
	   Correct form of call: 'create_findmovie(root, *args, **kwargs)' .'''
 	global w, w_win, root
 	#rt = root
 	root = rt
 	w = tk.Toplevel (root)
 	top = findmovie (w)
 	return (w, top)

def destroy_findmovie():
 	global w
 	w.destroy()
 	w = None

def adds(top,movieid):
		print(movieid)
		top.destroy()
		createshow.vp_start_gui_createshow2(movieid)
		
		
#########################################################
''' Tkinter Page'''
#########################################################
class findmovie():
	def __init__(self,b,top=None):
		print(b)
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

		top.geometry("1280x686+212+135")
		top.minsize(120, 1)
		top.maxsize(3004, 1913)
		top.resizable(1,  1)
		top.title("New Toplevel")
		top.configure(background="#000040")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="#000000")
		
		top.resizable(False, False)
		global img
		img = ImageTk.PhotoImage(file="bg.png")
		self.Background = tk.Label(top,image = img)        
		self.Background.place(relx=0, rely=0, height=1000, width=1500)
		self.Background=img
		
		
		self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
		top.configure(menu = self.menubar)

		self.findmovie_b = tk.Button(top,command=lambda:back(top) )
		self.findmovie_b.place(relx=0.0, rely=0.0, height=44, width=100
				, bordermode='ignore')
		self.findmovie_b.configure(activebackground="#b3eaff")
		self.findmovie_b.configure(activeforeground="#000000")
		self.findmovie_b.configure(background="#00205b")
		self.findmovie_b.configure(disabledforeground="#a3a3a3")
		self.findmovie_b.configure(cursor="hand2")
		self.findmovie_b.configure(font="-family {Segoe UI} -size 12")
		self.findmovie_b.configure(foreground="#ffffff")
		self.findmovie_b.configure(highlightbackground="#d9d9d9")
		self.findmovie_b.configure(highlightcolor="black")
		self.findmovie_b.configure(pady="0")
		self.findmovie_b.configure(text='''Back''')

################################################################Result instance############################################################
		y=0.1
		yim=0.095
		yib=0.32
		for i in b:
 			self.Movie1 = tk.Frame(top)
 			self.Movie1.place(relx=0.18, rely=y, relheight=0.138, relwidth=0.621)
 			self.Movie1.configure(relief='groove')
 			self.Movie1.configure(borderwidth="2")
 			self.Movie1.configure(relief="groove")
 			self.Movie1.configure(background="#00002b")
 			self.Image1 = tk.Label(self.Movie1)
 			self.Image1.place(relx=0.025, rely=yim, height=73, width=135)
 			self.Image1.configure(background="#d9d9d9")
 			self.Image1.configure(disabledforeground="#a3a3a3")
 			self.Image1.configure(foreground="#000000")
 			self.Image1.configure(text=i[1])

 			self.Description1 = tk.Label(self.Movie1)
 			self.Description1.place(relx=0.239, rely=yim, height=73, width=573)
 			self.Description1.configure(anchor='nw')
 			self.Description1.configure(background="#00002b")
 			self.Description1.configure(cursor="fleur")
 			self.Description1.configure(disabledforeground="#a3a3a3")
 			self.Description1.configure(font="-family {Segoe UI} -size 12")
 			self.Description1.configure(foreground="#bcfbfe")
 			self.Description1.configure(text=i[2])
				
 			self.Book_b = tk.Button(top,command=partial(adds,top,i[0]))
 			self.Book_b.place(relx=0.60, rely=y+0.02, height=54, width=177)
 			self.Book_b.configure(activebackground="#000040")
 			self.Book_b.configure(activeforeground="white")
 			self.Book_b.configure(activeforeground="#ffffff")
 			self.Book_b.configure(background="#b3eaff")
 			self.Book_b.configure(disabledforeground="#a3a3a3")
 			self.Book_b.configure(cursor="hand2")
 			self.Book_b.configure(font="-family {Segoe UI} -size 14")
 			self.Book_b.configure(foreground="#000000")
 			self.Book_b.configure(highlightbackground="#d9d9d9")
 			self.Book_b.configure(highlightcolor="black")
 			self.Book_b.configure(pady="0")
 			self.Book_b.configure(text='''Select Movie''')
 			y+=0.15
 			yim+=0.03
 			yib+=0.15
		
##############################################################################################################################################

##################################################################scroller########################################################
		self.Previous = tk.Button(top)
		self.Previous.place(relx=0.383, rely=0.933, height=24, width=47)
		self.Previous.configure(activebackground="#ececec")
		self.Previous.configure(activeforeground="#000000")
		self.Previous.configure(background="#b4eafe")
		self.Previous.configure(disabledforeground="#a3a3a3")
		self.Previous.configure(font="-family {Segoe UI} -size 15")
		self.Previous.configure(foreground="#000000")
		self.Previous.configure(highlightbackground="#d9d9d9")
		self.Previous.configure(highlightcolor="black")
		self.Previous.configure(pady="0")
		self.Previous.configure(text='''<''')

		self.Next = tk.Button(top)
		self.Next.place(relx=0.57, rely=0.933, height=24, width=47)
		self.Next.configure(activebackground="#ececec")
		self.Next.configure(activeforeground="#000000")
		self.Next.configure(background="#b4eafe")
		self.Next.configure(disabledforeground="#a3a3a3")
		self.Next.configure(font="-family {Segoe UI} -size 15")
		self.Next.configure(foreground="#000000")
		self.Next.configure(highlightbackground="#d9d9d9")
		self.Next.configure(highlightcolor="black")
		self.Next.configure(pady="0")
		self.Next.configure(text='''>''')

		self.Page_list = tk.Label(top)
		self.Page_list.place(relx=0.43, rely=0.933, height=21, width=164)
		self.Page_list.configure(activebackground="#f0f0f0f0f0f0")
		self.Page_list.configure(background="#000040")
		self.Page_list.configure(disabledforeground="#a3a3a3")
		self.Page_list.configure(font="-family {Segoe UI} -size 12")
		self.Page_list.configure(foreground="#b4eafe")
		self.Page_list.configure(text='''1 of 4''')
		
		#findmoviebar.__init__(self, top=None)

#####################################################################################################################################

if __name__ == '__main__':
 	vp_start_gui()


