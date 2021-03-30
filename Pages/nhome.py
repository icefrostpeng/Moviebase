# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:16:57 2021

@author: Admin
"""
import slots
import sys
from PIL import ImageTk, Image
import PIL
import PIL.Image
global co 
co=0
global d,to
import payment
import search2
import cancelticket
from tkinter import *
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
global movidic,namess,ratings
def query():
	global movidic,namess,ratings
	with SSHTunnelForwarder(
			(ssh_host, ssh_port),
			ssh_username=ssh_user,
			ssh_pkey=mypkey,
			remote_bind_address=(sql_hostname, sql_port)) as tunnel:
		global movidic,namess,ratings
		conn = pymysql.connect(host='127.0.0.1', user=sql_username,
				passwd=sql_password, db=sql_main_database,
				port=tunnel.local_bind_port)
		cur=conn.cursor()
		
		cur.execute("select * from moviedet") #get all movie details present in databse
		arr = list(cur.fetchall())
		dic={}
		val=1
		for i in arr:
			li=list(i[1:7])
			a=str(val)+".jpeg"
			li.insert(0,a)
			dic[i[0]]=li
			val+=1
		movidic=dic #creating global dictionary of movie details 
		tn=[]
		tr=[]
		for i in range(1,6):
			
			q1='select movie_name,rating from moviedet where movie_id={0} and status="r"'.format(i) #movie rating and name for sidebar
			cur.execute(q1)
			arr = list(cur.fetchall())
			
			for i in arr:
				l=list(i)
				tn.append(l[0])
				tr.append(l[1])
		global namess,ratings
		namess=tn
		ratings=tr #saving both in global variables
		#print(namess)
		#print(ratings)
	
def datas():
	global namess,ratings
	return namess,ratings

def queryse(q):
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
def data():
	global movidic
	query()
	m=movidic
	return m
def bookT(name,mem,email,top): #function alled when user tries to book ticket using the movie list in slidebar
	global co,d,namess,ratings
	ky=[]
	for i in d.keys():
		ky.append(i)
	print(d[ky[co]])
	print("yess")
	dic={}
	#get the slotdetails along with the theatre details of the movie which the user selected
	m=queryse(" select theaterdet.theater_id,theaterdet.theater_name,theaterdet.city,theaterdet.theater_add,slotdet.slot_id,slotdet.timing,slotdet.cost,slotdet.dates from theaterdet,slotdet where movie_id={0} and slotdet.theater_id=theaterdet.theater_id order by slotdet.dates".format(ky[co]))
	le=0
	l=[]
	i=0
	print(len(m))
	print(m)
	while(i!=(len(m))):
		print(i)
		if(m[i][7]==m[i+1][7]):
			if(m[i][7] in dic.keys()):
				li=dic[m[i][7]]
				nd={}
				print(li)
				li.append(m[i][:7])
				nd[m[i][7]]=li
				print(li)
				dic.update(nd)
			else:
				dic[m[i][7]]=[m[i][:7]]
		else:
			if(m[i][7] in dic.keys()):
				li=dic[m[i][7]]
				nd={}
				print(li)
				li.append(m[i][:7])
				nd[m[i][7]]=li
				print(li)
				dic.update(nd)
			else:
				dic[m[i][7]]=[m[i][:7]]
		i=i+1
		if(i==(len(m)-1)):
			if(m[i][7] in dic.keys()):
				li=dic[m[i][7]]
				nd={}
				li.append(m[i][:7])
				nd[m[i][7]]=li
				dic.update(nd)
			else:
				dic[m[i][7]]=[m[i][:7]]
			break
	print(dic) #getting the list of slot and thater details based on the date 
	mov=d[ky[co]]
	mov=mov[1:]
	mov.insert(0,ky[co])
	top.destroy()
	print(mov,dic,name,mem,email)
	slots.vp_start_slot(mov,dic,name,mem,email,top,namess,ratings) #calling slot booking gui
def history(name,mem,email,names,rating,root): #when history button is clicked
	root.destroy()
	print(rating)
	cancelticket.vp_start_gui(name,mem,email,names,rating) #call cancel button gui
def vp_start_gui1(name='XYZ',mem='Gold',email='singhsilentsrishti@gmail.com'):
	'''Starting point when module is the main routine.'''
	global val, w, root,d
	root = tk.Tk()
	d=data()
	print(d)
	top = Home (name,mem,email,root)
	root.mainloop()

w = None
def create_Home(rt,*args, **kwargs):
	'''Starting point when module is imported by another module.
	   Correct form of call: 'create_Home(root, *args, **kwargs)' .'''
	global w, w_win, root
	#rt = root
	root = rt
	w = tk.Toplevel (root)
	top = Home (w)
	return w, top

def destroy_Home():
	global w
	w.destroy()
	w = None
def search(var,name,mem,email, top): #when the search button is clicked
	global namess,ratings
	val=var.get()
	if (len(val)!=0): #check if user has entered something to search
		a="select * from moviedet where movie_name LIKE '{0}%'".format(val) #check if the entered value for searching is a movie
		print (a)
		b=queryse(a)
		if(len(b)!=0): #if yes
		    top.destroy()
		    #print(b)
		    search2.vp_start_gui(0,name,mem,email,b,namess,ratings) #then call search2 with starting parameter as 0 indicating its a movie

		else: #else if its not a movie
		    a="select * from theaterdet where theater_name='{0}%'".format(val) #check if the entered value is a theatre
		    print (a)
		    b=queryse(a)
		    if(len(b)!=0): #if yes
		        top.destroy()
		        #print(b)
		        search2.vp_start_gui(1,name,mem,email,b,namess,ratings) #call search2 with 1 as first parameter indicating if it as theatre

		    else: #else conclude a wrong search
		        messagebox.showerror("Error", "No Movie or Theatre found!!!")

	else: #if not
		messagebox.showerror("Error", "Enter something")


def button_functionality(mem): #based on membership status of user disable the buttons
	if mem == 'Gold':
		gold = False
		platinum = True
		diamond = True
	elif mem == 'Platinum':
		gold = False
		platinum = False
		diamond = True
	elif mem == 'Diamond':
		gold = False
		platinum = False
		diamond = False
	else:
		gold = True
		platinum = True
		diamond = True
	return gold, platinum, diamond
class Home():
	global to
	def ahead(self,top): # called when '>' button is clicked from the  slideshow bar 
		global co #global variable used for indicating the navigation bar below
		co=(co+1)%5 #incrementing the value
		ky=[]
		for i in d.keys():
			ky.append(i)#storing all the keys of dic
		print(ky)
		print(d[ky[co]])
		print(d[ky[co]][0])
		img = ImageTk.PhotoImage(PIL.Image.open(d[ky[co]][0]).resize((560, 277), PIL.Image.ANTIALIAS)) #setting new image
		self.Movie_image = tk.Label(top,image = img)
		self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
		self.Movie_image=img
		#changing information of the rest of the labels 
		st="Description : \n"+d[ky[co]][2]
		self.Description_l.configure(text=st)
		strr="Rating : \n"+str(d[ky[co]][3])+"/5"
		self.Rating_l.configure(text=strr)
		stc="Cast : \n"
		lis=d[ky[co]][4].split(',')
		for i in lis:
			stc+=i+"\n"
		self.Cast_l.configure(text=stc)
		stt="Title : "+d[ky[co]][1]
		self.Label8.configure(text=stt)
		stg="Genre : \n"+d[ky[co]][6]
		self.Genre_l.configure(text=stg)
		self.Label9.configure(text=d[ky[co]][5])
		return
	def bac(self,top): # when < button is clicked from slideshow
		global co
		ky=[]
		for i in d.keys():
			ky.append(i)
		if(co==0): #checking if the counter value is 0
		    print(co) #if yes then  dont decrement it further
		else:
		    co-=1 #else decrement it
		    print(co)
		img = ImageTk.PhotoImage(PIL.Image.open(d[ky[co]][0]).resize((560, 277), PIL.Image.ANTIALIAS)) #setting new image
		self.Movie_image = tk.Label(top,image = img)
		self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
		self.Movie_image=img
		#and rest f the labels according to new values
		st="Description : \n"+d[ky[co]][2]
		self.Description_l.configure(text=st)
		strr="Rating : \n"+str(d[ky[co]][3])+"/5"
		self.Rating_l.configure(text=strr)
		stc="Cast : \n"
		lis=d[ky[co]][4].split(',')
		for i in lis:
			stc+=i+"\n"
		self.Cast_l.configure(text=stc)
		stt="Title : "+d[ky[co]][1]
		self.Label8.configure(text=stt)
		stg="Genre : \n"+d[ky[co]][6]
		self.Genre_l.configure(text=stg)
		self.Label9.configure(text=d[ky[co]][5])
		return
	def __init__(self,name='x',mem='Gold',email='s', top=None):
		#query()
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

		top.geometry("1280x686+297+168")
		top.minsize(120, 1)
		top.maxsize(3004, 1913)
		top.resizable(1,  1)
		top.title("New Toplevel")
		top.configure(background="#000040")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="#000000")

		
		top.resizable(False,False)
		img = ImageTk.PhotoImage(file="bg.png")
		self.Background = tk.Label(top,image = img)        
		self.Background.place(relx=0, rely=0, height=1000, width=1500)
		self.Background=img

		self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
		top.configure(menu = self.menubar)


  
  ####################################################################Movies Slider###################################################################
		global d
		global to,co
		to=top
		img = ImageTk.PhotoImage(PIL.Image.open(d[1][0]).resize((560, 277), PIL.Image.ANTIALIAS)) #setting frist image at display
		self.Movie_image = tk.Label(top,image = img)        
		self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
		self.Movie_image=img

		self.Previous_b = tk.Button(top,command=lambda: self.bac(top))
		self.Previous_b.place(relx=0.172, rely=0.277, height=284, width=27)
		self.Previous_b.configure(activebackground="#000040")
		self.Previous_b.configure(activeforeground="white")
		self.Previous_b.configure(activeforeground="#ffffff")
		self.Previous_b.configure(background="#b3eaff")
		self.Previous_b.configure(disabledforeground="#a3a3a3")
		self.Previous_b.configure(font="-family {Segoe UI} -size 20 -weight bold")
		self.Previous_b.configure(foreground="#000000")
		self.Previous_b.configure(highlightbackground="#d9d9d9")
		self.Previous_b.configure(highlightcolor="black")
		self.Previous_b.configure(pady="0")
		self.Previous_b.configure(text='''<''')

		self.Next_b = tk.Button(top,command=lambda: self.ahead(top))
		self.Next_b.place(relx=0.648, rely=0.277, height=284, width=27)
		self.Next_b.configure(activebackground="#000040")
		self.Next_b.configure(activeforeground="white")
		self.Next_b.configure(activeforeground="#ffffff")
		self.Next_b.configure(background="#b3eaff")
		self.Next_b.configure(disabledforeground="#a3a3a3")
		self.Next_b.configure(font="-family {Segoe UI} -size 20 -weight bold")
		self.Next_b.configure(foreground="#000000")
		self.Next_b.configure(highlightbackground="#d9d9d9")
		self.Next_b.configure(highlightcolor="black")
		self.Next_b.configure(pady="0")
		self.Next_b.configure(text='''>''')


#########################################################################################################################################





##########################################################Main##########################################################
		self.Label3 = tk.Label(top)
		self.Label3.place(relx=0.172, rely=0.131, height=48, width=193)
		self.Label3.configure(activebackground="#f9f9f9")
		self.Label3.configure(activeforeground="black")
		self.Label3.configure(background="#000040")
		self.Label3.configure(borderwidth="5")
		self.Label3.configure(disabledforeground="#a3a3a3")
		self.Label3.configure(font="-family {Segoe UI} -size 22")
		self.Label3.configure(foreground="#ffffff")
		self.Label3.configure(highlightbackground="#d9d9d9")
		self.Label3.configure(highlightcolor="black")
		self.Label3.configure(text='''Recommended!''')


		self.Movie_image = tk.Label(top)
		self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
		self.Movie_image.configure(activebackground="#f9f9f9")
		self.Movie_image.configure(activeforeground="black")
		self.Movie_image.configure(background="#d9d9d9")
		self.Movie_image.configure(disabledforeground="#a3a3a3")
		self.Movie_image.configure(foreground="#000000")
		self.Movie_image.configure(highlightbackground="#d9d9d9")
		self.Movie_image.configure(highlightcolor="black")

		self.Book_b = tk.Button(top,command=lambda: bookT(name,mem,email,top))
		self.Book_b.place(relx=0.215, rely=0.752, height=54, width=177)
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
		self.Book_b.configure(text='''Book Ticket!''')

		self.Description_f = tk.LabelFrame(top)
		self.Description_f.place(relx=0.357, rely=0.729, relheight=0.108
		        , relwidth=0.287)
		self.Description_f.configure(relief='groove')
		self.Description_f.configure(foreground="black")
		self.Description_f.configure(background="#d9d9d9")
		#self.Description_f.configure(cursor="fleur")
		self.Description_f.configure(highlightbackground="#d9d9d9")
		self.Description_f.configure(highlightcolor="black")

		self.Description_l = tk.Label(self.Description_f,wraplength=600,justify="left")
		self.Description_l.place(relx=0.008, rely=0.041, height=72, width=360
		        , bordermode='ignore')
		self.Description_l.configure(activebackground="#f9f9f9")
		self.Description_l.configure(activeforeground="black")
		self.Description_l.configure(anchor='nw')
		self.Description_l.configure(background="#000040")
		self.Description_l.configure(disabledforeground="#a3a3a3")
		self.Description_l.configure(font="-family {Segoe UI} -size 12")
		self.Description_l.configure(foreground="#ffffff")
		self.Description_l.configure(highlightbackground="#d9d9d9")
		self.Description_l.configure(highlightcolor="black")
		st="Description : \n"+d[1][2]
		self.Description_l.configure(text=st)

		self.Info_f = tk.LabelFrame(top)
		self.Info_f.place(relx=0.685, rely=0.294, relheight=0.389
		        , relwidth=0.122)
		self.Info_f.configure(relief='groove')
		self.Info_f.configure(foreground="black")
		self.Info_f.configure(background="#000040")
		self.Info_f.configure(highlightbackground="#d9d9d9")
		self.Info_f.configure(highlightcolor="black")

		self.Rating_l = tk.Label(self.Info_f)
		self.Rating_l.place(relx=0.045, rely=0.026, height=50, width=146
		        , bordermode='ignore')
		self.Rating_l.configure(activebackground="#f9f9f9")
		self.Rating_l.configure(activeforeground="black")
		self.Rating_l.configure(background="#000040")
		self.Rating_l.configure(disabledforeground="#a3a3a3")
		self.Rating_l.configure(font="-family {Segoe UI} -size 14")
		self.Rating_l.configure(foreground="#ffffff")
		self.Rating_l.configure(highlightbackground="#d9d9d9")
		self.Rating_l.configure(highlightcolor="black")
		strr="Rating : \n"+str(d[1][3])+"/5"
		self.Rating_l.configure(text=strr)

		self.TSeparator1 = ttk.Separator(self.Info_f)
		self.TSeparator1.place(relx=0.032, rely=0.236, relwidth=1.269
		        , bordermode='ignore')
#####################################################Stars###########################################################


		

#######################################################################################################################################



		self.Cast_l = tk.Label(self.Info_f,wraplength=500)
		self.Cast_l.place(relx=0.045, rely=0.558, height=109, width=145, bordermode='ignore')
		self.Cast_l.configure(activebackground="#f9f9f9")
		self.Cast_l.configure(activeforeground="black")
		self.Cast_l.configure(anchor='nw')
		self.Cast_l.configure(background="#000040")
		self.Cast_l.configure(disabledforeground="#a3a3a3")
		self.Cast_l.configure(font="-family {Segoe UI} -size 12")
		self.Cast_l.configure(foreground="#ffffff")
		self.Cast_l.configure(highlightbackground="#d9d9d9")
		self.Cast_l.configure(highlightcolor="black")
		stc="Cast : \n"
		lis=d[1][4].split(',')
		for i in lis:
			stc+=i+"\n"
		self.Cast_l.configure(text=stc)

		self.Genre_l = tk.Label(self.Info_f)
		self.Genre_l.place(relx=0.045, rely=0.277, height=48, width=145, bordermode='ignore')
		self.Genre_l.configure(activebackground="#f9f9f9")
		self.Genre_l.configure(activeforeground="black")
		self.Genre_l.configure(background="#000040")
		self.Genre_l.configure(disabledforeground="#a3a3a3")
		self.Genre_l.configure(font="-family {Segoe UI} -size 13")
		self.Genre_l.configure(foreground="#ffffff")
		self.Genre_l.configure(highlightbackground="#d9d9d9")
		self.Genre_l.configure(highlightcolor="black")
		stg="Genre : \n"+d[1][6]
		self.Genre_l.configure(text=stg)

		self.TSeparator3 = ttk.Separator(top)
		self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
		self.TSeparator3.configure(orient="vertical")

		self.Label8 = tk.Label(top)
		self.Label8.place(relx=0.172, rely=0.204, height=42, width=547)
		self.Label8.configure(activebackground="#f9f9f9")
		self.Label8.configure(activeforeground="black")
		self.Label8.configure(anchor='w')
		self.Label8.configure(background="#000040")
		self.Label8.configure(disabledforeground="#a3a3a3")
		self.Label8.configure(font="-family {Segoe UI} -size 20")
		self.Label8.configure(foreground="#ffffff")
		self.Label8.configure(highlightbackground="#d9d9d9")
		self.Label8.configure(highlightcolor="black")
		stt="Title : "+d[1][1]
		self.Label8.configure(text=stt)

		self.Label9 = tk.Label(top)
		self.Label9.place(relx=0.60, rely=0.204, height=42, width=547)
		self.Label9.configure(activebackground="#f9f9f9")
		self.Label9.configure(activeforeground="black")
		self.Label9.configure(anchor='w')
		self.Label9.configure(background="#000040")
		self.Label9.configure(disabledforeground="#a3a3a3")
		self.Label9.configure(font="-family {Segoe UI} -size 20")
		self.Label9.configure(foreground="#ffffff")
		self.Label9.configure(highlightbackground="#d9d9d9")
		self.Label9.configure(highlightcolor="black")
		self.Label9.configure(text=d[1][5])
		
####################Membership Function##################################################
		self.membership = mem
		self.Membership_f = tk.LabelFrame(top)
		self.Membership_f.place(relx=0.013, rely=0.219, relheight=0.516, relwidth=0.14)
		self.Membership_f.configure(relief='groove')
		self.Membership_f.configure(foreground="#edea67")
		self.Membership_f.configure(background="#bfe2ff")
		self.Membership_f.configure(highlightbackground="#f3fee2")
		self.Membership_f.configure(highlightcolor="#4bc602")

		self.TSeparator3 = ttk.Separator(top)
		self.TSeparator3.place(relx=0.165, rely=0.168, relheight=0.845)
		self.TSeparator3.configure(orient="vertical")

		# redirect to payment
		def button_click(product):
		    top.destroy()
		    action = 1
		    payment.vp_start_gui_P(name, mem, product, email, action)


		# membership status
		gold, platinum, diamond = button_functionality(mem)

		# Gold Button
		prod_gold = ["Gold", 600]
		self.Gold_b = tk.Button(self.Membership_f, command=lambda: button_click(prod_gold))
		self.Gold_b.place(relx=0.056, rely=0.734, height=84, width=157, bordermode='ignore')
		self.Gold_b.configure(activebackground="#f0df99")
		self.Gold_b.configure(activeforeground="#000000")
		self.Gold_b.configure(background="#ffda04")
		self.Gold_b.configure(borderwidth="9")
		self.Gold_b.configure(disabledforeground="#a3a3a3")
		self.Gold_b.configure(font="-family {Segoe UI} -size 15")
		self.Gold_b.configure(foreground="#000000")
		self.Gold_b.configure(highlightbackground="#d9d9d9")
		self.Gold_b.configure(highlightcolor="black")
		self.Gold_b.configure(pady="0")
		self.Gold_b.configure(text='Gold')
		if gold:
		    self.Gold_b["state"] = "normal"
		else:
		    self.Gold_b["state"] = "disabled"

		# Platinum Button
		prod_platinum = ["Platinum", 800]
		self.Platinum_b = tk.Button(self.Membership_f, command=lambda: button_click(prod_platinum))
		self.Platinum_b.place(relx=0.056, rely=0.452, height=84, width=157, bordermode='ignore')
		self.Platinum_b.configure(activebackground="#707070")
		self.Platinum_b.configure(activeforeground="white")
		self.Platinum_b.configure(activeforeground="#000000")
		self.Platinum_b.configure(background="#d8d8d8")
		self.Platinum_b.configure(borderwidth="9")
		self.Platinum_b.configure(disabledforeground="#a3a3a3")
		self.Platinum_b.configure(font="-family {Segoe UI} -size 15")
		self.Platinum_b.configure(foreground="#000000")
		self.Platinum_b.configure(highlightbackground="#d9d9d9")
		self.Platinum_b.configure(highlightcolor="black")
		self.Platinum_b.configure(pady="0")
		self.Platinum_b.configure(text='''Platinum''')
		if platinum:
		    self.Platinum_b["state"] = "normal"
		else:
		    self.Platinum_b["state"] = "disabled"

		# Diamond Button
		prod_diamond = ["Diamond", 1000]
		self.Diamond_b = tk.Button(self.Membership_f, command=lambda: button_click(prod_diamond))
		self.Diamond_b.place(relx=0.061, rely=0.169, height=84, width=157, bordermode='ignore')
		self.Diamond_b.configure(activebackground="#d9fcff")
		self.Diamond_b.configure(activeforeground="#7070fa")
		self.Diamond_b.configure(background="#2de9f2")
		self.Diamond_b.configure(borderwidth="9")
		self.Diamond_b.configure(disabledforeground="#a3a3a3")
		self.Diamond_b.configure(font="-family {Segoe UI} -size 15")
		self.Diamond_b.configure(foreground="#000000")
		self.Diamond_b.configure(highlightbackground="#d9d9d9")
		self.Diamond_b.configure(highlightcolor="#e9f552")
		self.Diamond_b.configure(highlightthickness="6")
		self.Diamond_b.configure(pady="0")
		self.Diamond_b.configure(text='''Diamond''')
		if diamond:
		    self.Diamond_b["state"] = "normal"
		else:
		    self.Diamond_b["state"] = "disabled"

		# Label in membership block
		self.Join_l = tk.Label(self.Membership_f)
		self.Join_l.place(relx=0.056, rely=0.028, height=41, width=155, bordermode='ignore')
		self.Join_l.configure(activebackground="#f9f9f9")
		self.Join_l.configure(activeforeground="black")
		self.Join_l.configure(background="#bfe2ff")
		self.Join_l.configure(disabledforeground="#a3a3a3")
		self.Join_l.configure(font="-family {Segoe UI} -size 12")
		self.Join_l.configure(foreground="#000000")
		self.Join_l.configure(highlightbackground="#d9d9d9")
		self.Join_l.configure(highlightcolor="black")
		self.Join_l.configure(text=f'Join our Membership plan!')
		self.Join_l.configure(wraplength="150")

####################Sidebar########################################################################
		self.TSeparator4 = ttk.Separator(top)
		self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
		self.TSeparator4.configure(orient="vertical")


		self.Listofmovies_f = tk.LabelFrame(top)
		self.Listofmovies_f.place(relx=0.829, rely=0.157, relheight=0.831
		        , relwidth=0.138)
		self.Listofmovies_f.configure(relief='groove')
		self.Listofmovies_f.configure(font="-family {Segoe UI} -size 17")
		self.Listofmovies_f.configure(foreground="#000000")
		self.Listofmovies_f.configure(text='''List of Movies''')
		self.Listofmovies_f.configure(background="#d7eeff")
		self.Listofmovies_f.configure(highlightbackground="#f0f0f0f0f0f0")
		self.Listofmovies_f.configure(highlightcolor="#646464646464")

		self.page_id = tk.Label(self.Listofmovies_f)
		self.page_id.place(relx=0.04, rely=0.947, height=21, width=166
		        , bordermode='ignore')
		self.page_id.configure(activebackground="#f9f9f9")
		self.page_id.configure(activeforeground="black")
		self.page_id.configure(background="#000040")
		self.page_id.configure(borderwidth="10")
		self.page_id.configure(disabledforeground="#a3a3a3")
		self.page_id.configure(font="-family {Segoe UI} -size 13")
		self.page_id.configure(foreground="#ffffff")
		self.page_id.configure(highlightbackground="#d9d9d9")
		self.page_id.configure(highlightcolor="black")
		self.page_id.configure(text='''1 of 2''')

		namem, rating = datas()
		y=0.07
		for i in range(0,len(namem)):
		                self.Movie1_b = tk.Button(self.Listofmovies_f)
		                self.Movie1_b.place(relx=0.056, rely=y, height=74, width=157, bordermode='ignore')
		                self.Movie1_b.configure(activebackground="#ececec")
		                self.Movie1_b.configure(activeforeground="#000000")
		                self.Movie1_b.configure(anchor='nw')
		                self.Movie1_b.configure(background="#d7eeff")
		                self.Movie1_b.configure(disabledforeground="#a3a3a3")
		                self.Movie1_b.configure(font="-family {Segoe UI} -size 12")
		                self.Movie1_b.configure(foreground="#000000")
		                self.Movie1_b.configure(highlightbackground="#d9d9d9")
		                self.Movie1_b.configure(highlightcolor="black")
		                self.Movie1_b.configure(pady="0")
		                self.Movie1_b.configure(text='''{0} \n\nRating: {1}/5'''.format(namem[i],rating[i]))
		                self.Movie1_b.configure(wraplength="150")
		                y+=0.14

###################################################Search Bar###############################################################################
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

#####################################HOME BAR###################################################
		self.Home_f = tk.LabelFrame(top)
		self.Home_f.place(relx=0.023, rely=0.029, relheight=0.093, relwidth=0.50)
		self.Home_f.configure(relief='groove')
		self.Home_f.configure(foreground="#000000")
		self.Home_f.configure(background="#e8e8ff")
		self.Home_f.configure(highlightbackground="#d9d9d9")
		self.Home_f.configure(highlightcolor="black")

		self.home_inner_f = tk.Frame(self.Home_f)
		self.home_inner_f.place(relx=0.017, rely=0.109, relheight=0.797, relwidth=0.959, bordermode='ignore')
		self.home_inner_f.configure(relief='groove')
		self.home_inner_f.configure(borderwidth="2")
		self.home_inner_f.configure(relief="groove")
		self.home_inner_f.configure(background="#b3eaff")
		self.home_inner_f.configure(highlightbackground="#d9d9d9")
		self.home_inner_f.configure(highlightcolor="black")
		names, rating = datas()
		self.Home_b = tk.Button(self.home_inner_f,command=lambda:history(name,mem,email,names,rating,top))
		self.Home_b.place(relx=0.025, rely=0.0, height=57, width=110)
		self.Home_b.configure(activebackground="#ececec")
		self.Home_b.configure(activeforeground="#000000")
		self.Home_b.configure(background="#000040")
		self.Home_b.configure(disabledforeground="#a3a3a3")
		self.Home_b.configure(font="-family {Segoe UI} -size 12")
		self.Home_b.configure(foreground="#ffffff")
		self.Home_b.configure(highlightbackground="#d9d9d9")
		self.Home_b.configure(highlightcolor="black")
		self.Home_b.configure(pady="0")
		self.Home_b.configure(text='''History''')

		self.Member_l = tk.Label(self.home_inner_f)
		self.Member_l.place(relx=0.262, rely=0.137, height=34, width=352)
		self.Member_l.configure(activebackground="#b3eaff")
		self.Member_l.configure(activeforeground="black")
		self.Member_l.configure(background="#b3eaff")
		self.Member_l.configure(disabledforeground="#a3a3a3")
		self.Member_l.configure(font="-family {Segoe UI} -size 12")
		self.Member_l.configure(foreground="#000000")
		self.Member_l.configure(highlightbackground="#d9d9d9")
		self.Member_l.configure(highlightcolor="black")
		self.Member_l.configure(text=f'Member status {name} has {mem} Membership')
		

if __name__ == '__main__':
	vp_start_gui1()
