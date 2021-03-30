

#########################################################
'''Importing Packages'''
#########################################################
from tkinter import Tk, Canvas
from tkinter import *
import pymysql
from functools import partial
import paramiko
import payment
import pandas as pd
from tkinter import messagebox
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import adhome

#########################################################
'''Declaring Variables'''
#########################################################
global li,count,strv,cosm,dcost,seat
cosm = 0
seat=''
count = 0
li = []
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

#########################################################
'''Query to Update seat status'''
#########################################################
def quer(slotid,seatid,val):
	with SSHTunnelForwarder(
			(ssh_host, ssh_port),
			ssh_username=ssh_user,
			ssh_pkey=mypkey,
			remote_bind_address=(sql_hostname, sql_port)) as tunnel:
		conn = pymysql.connect(host='127.0.0.1', user=sql_username,
				passwd=sql_password, db=sql_main_database,
				port=tunnel.local_bind_port)
		cur=conn.cursor()
		print("update seatdet set status='{0}' where slot_id={1} and seat_id={2}".format(val,slotid,seatid))
		cur.execute("update seatdet set status='{0}' where slot_id={1} and seat_id={2}".format(val,slotid,seatid))
		conn.commit()
		return 1
def quera(email):
	with SSHTunnelForwarder(
			(ssh_host, ssh_port),
			ssh_username=ssh_user,
			ssh_pkey=mypkey,
			remote_bind_address=(sql_hostname, sql_port)) as tunnel:
		conn = pymysql.connect(host='127.0.0.1', user=sql_username,
				passwd=sql_password, db=sql_main_database,
				port=tunnel.local_bind_port)
		cur=conn.cursor()
		cur.execute("select age from User where email='{0}'".format(email))
		arr = list(cur.fetchall())
		cur.close()
		return int(arr[0][0])
    #########################################################
'''Query to Update seat status'''
#########################################################
def query(slotid):
	with SSHTunnelForwarder(
			(ssh_host, ssh_port),
			ssh_username=ssh_user,
			ssh_pkey=mypkey,
			remote_bind_address=(sql_hostname, sql_port)) as tunnel:
		conn = pymysql.connect(host='127.0.0.1', user=sql_username,
				passwd=sql_password, db=sql_main_database,
				port=tunnel.local_bind_port)
		cur=conn.cursor()
		cur.execute("select seat_id,status from seatdet where slot_id={0}".format(slotid))
		arr = list(cur.fetchall())
		arr=dict(arr)
		print(f'{arr} query seats')
		cur.close()
		return arr

global fin,seats
fin=[]
def sub(slotid,top):
	global fin
	flag=0
	chkM=1
	if(len(fin)==0):
		messagebox.showerror("Error", "No Seats selected")
	else:
		
		for i in fin:
			if(i[1]=='i'):
				i[1]='v'
				if(quer(slotid,i[0],i[1])):
					flag=1
				else:
					flag=0
					
	if flag==1:
		sts=''
		for i in range(len(fin)):
			if i==0:
				sts+=str(fin[i][2])
			else:
				sts+=","+str(fin[i][2])
		st="Seats Modified successfully\n Seat number : "+sts
		messagebox.showinfo("Sucess", st)
		top.destroy()
		adhome.vp_start_guih()



#call Payment function vaiables : totalcost=cosm discounted cost=dcost seat number = sts(in string as 12,13) parameters of function ssub has name,mem,email,timing,tdate
def clicked(*args):
	global fin,seat,count,strv
	j=args[0]
	print(args[1],args[2])
	if li[args[0]].cget('bg')=='blue':
		li[args[0]].configure(background="yellow")
		fin.append([args[1],args[2],(args[0]+1)])
		count+=1
		
	else:
		li[args[0]].configure(background="blue")
		count-=1
		
		fin.remove([args[1],args[2],(args[0]+1)])
	cou=str(count)
	
	seat+=str(j+1)+"\t"
	st="Number of seats selected are : "+cou+"\nNew Valid Seats:"+seat
	strv.set(st)
	print(fin)
def creates(slotid):
	window = Tk()
	global strv
	dic=query(slotid)
	topx=25
	topy=25
	rightx=75
	righty=75
	co=0
	window.geometry("700x600") 
	blu = Button(window,text = "Invalid",bg='#0052cc', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=20,y=320)
	red = Button(window,text = "Booked",bg='red', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=110,y=320)
	bla = Button(window,text = "Valid",bg='black', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=200,y=320)

	strv=StringVar()
	strv.set("Number of seats selected is : 0\n ")
	print(strv)
	wel=Label(window,textvariable=strv,font = "Helvetica 16 bold italic",justify="left").place(x=40,y=380)
	
	b=Button(window,command=lambda: sub(slotid,window),text = "MODIFY",bg='#0052cc', fg='#ffffff',width=8,height=2,relief=RAISED).place(x=100,y=480)
	
	#c.bind('<Button-1>', clicked)
	for key,value in dic.items():
		if(value=='i'):
			playbutton = Button(window,text=(co+1),command=partial(clicked, co,key,value), fg='#ffffff',width=5,height=2,relief=RAISED)
			playbutton.configure(bg='blue')
			playbutton.place(x=topx,y=topy)
			#c.tag_bind("playbutton","<Button-1>",clicked)
			
		elif(value=='v'):
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
	window.mainloop()
#creates()
