from tkinter import Tk, Canvas
from tkinter import *
import pymysql
from functools import partial
import paramiko
import pandas as pd
from tkinter import messagebox
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
global li,count,strv
count=0
li=[]
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
def query():
	with SSHTunnelForwarder(
			(ssh_host, ssh_port),
			ssh_username=ssh_user,
			ssh_pkey=mypkey,
			remote_bind_address=(sql_hostname, sql_port)) as tunnel:
		conn = pymysql.connect(host='127.0.0.1', user=sql_username,
				passwd=sql_password, db=sql_main_database,
				port=tunnel.local_bind_port)
		cur=conn.cursor()
		cur.execute("select seat_id,status from seatdet where slot_id=1")
		arr = list(cur.fetchall())
		arr=dict(arr)
		print(arr)
		cur.close()
		return arr
def quer(seatid,val):
	with SSHTunnelForwarder(
			(ssh_host, ssh_port),
			ssh_username=ssh_user,
			ssh_pkey=mypkey,
			remote_bind_address=(sql_hostname, sql_port)) as tunnel:
		conn = pymysql.connect(host='127.0.0.1', user=sql_username,
				passwd=sql_password, db=sql_main_database,
				port=tunnel.local_bind_port)
		cur=conn.cursor()
		cur.execute("update seatdet set status='{1}' where slot_id=1 and seat_id={0}".format(seatid,val))
		conn.commit()
		return 1
window = Tk()
dic=query()
global fin
fin=[]
def sub():
	global fin
	flag=0
	if(len(fin)==0):
		messagebox.showerror("Error", "No Seats selected")
	else:
		for i in fin:
			if(i[1]=='v'):
				i[1]='o'
				if(quer(i[0],i[1])):
					flag=1
				else:
					flag=0
	if(flag==1):
		messagebox.showinfo("Sucess", "Seats Booked successfully")
	print(query())
def clicked(*args):
	global li,count,strv,fin
	j=args[0]
	print(args[1],args[2])
	if(li[args[0]].cget('bg')=='blue'):
		li[args[0]].configure(background="yellow")
		fin.append([args[1],args[2]])
		count+=1
	else:
		li[args[0]].configure(background="blue")
		count-=1
		fin.remove([args[1],args[2]])
	cou=str(count)
	st="Number of seats selected are : "+cou
	strv.set(st)
	print(fin)
topx=25
topy=25
rightx=75
righty=75
co=0
window.geometry("700x500") 
#c.bind('<Button-1>', clicked)
for key,value in dic.items():
	if(value=='v'):
		playbutton = Button(window,text=(co+1),command=partial(clicked, co,key,value), fg='#ffffff',width=5,height=2,relief=RAISED)
		playbutton.configure(bg='blue')
		playbutton.place(x=topx,y=topy)
		#c.tag_bind("playbutton","<Button-1>",clicked)
		
	elif(value=='i'):
		playbutton = Button(window,text=(co+1),bg='black', fg='#ffffff',width=5,height=2,state=DISABLED,relief=FLAT).place(x=topx,y=topy)

	else:
		playbutton = Button(window,text=(co+1),bg='red', fg='#ffffff',width=5,height=2,state=DISABLED,relief=FLAT).place(x=topx,y=topy)
	li.append(playbutton)
	co+=1
	if(co%10==0):
		topy+=60
		righty+=60
		topx=25
		rightx=75
	elif(co%5==0):
		topx+=80
		rightx+=80
	else:
		topx+=60
		rightx+=60
we=Label(window,text="_____________________________________Screen This Side___________________________________",font="-family {Segoe UI} -size 12").place(x=20,y=280)
blu = Button(window,text = "Available",bg='#0052cc', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=20,y=320)
red = Button(window,text = "BOOKED",bg='red', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=110,y=320)
bla = Button(window,text = "Invalid",bg='black', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=200,y=320)

strv=StringVar()
strv.set("Number of seats selected is : 0")
wel=Label(window,textvariable=strv,font = "Helvetica 16 bold italic").place(x=40,y=380)
b=Button(window,command=sub,text = "Payment",bg='#0052cc', fg='#ffffff',width=8,height=2,relief=RAISED).place(x=100,y=410)
window.mainloop()
