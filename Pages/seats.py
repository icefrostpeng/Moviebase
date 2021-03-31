from tkinter import Tk, Canvas
from tkinter import *
import pymysql
from functools import partial
import paramiko
import payment
import nhome
import pandas as pd
from tkinter import messagebox
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
global li,count,strv,cosm,dcost
cosm = 0
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
		cur.execute("select age from User where email='{0}'".format(email)) #fetch age of the user
		arr = list(cur.fetchall())
		cur.close()
		return int(arr[0][0])
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
		cur.execute("select seat_id,status from seatdet where slot_id={0}".format(slotid)) #select all seat details of the user selected slots
		arr = list(cur.fetchall())
		arr=dict(arr)
		print(f'{arr} query seats')
		cur.close()
		return arr

global fin
fin=[]
def sub(window,l,slotid,name,mem,email,timing,tdate,cinemaNAd): #fucntion called when user clicks on payment after selecting seats
	global fin,cosm,dcost
	flag=0
	chkM=1
	if(len(fin)==0): #check if user has selected any seats
		messagebox.showerror("Error", "No Seats selected") #if not display error
	else:
		if(l[5]=='A'):#check if user selected movie is an adult movie
			age=quera(email) #if yes check age of the user
			print(age)
			if(age<18): #if age is less than 18 dont allow the user to book the ticket
				chkM=0
				messagebox.showerror("Error", "Adult Movie and your age is Less than 18")
				window.destroy()
				nhome.vp_start_gui1(name, mem, email) #send user back to home page
			elif(age>18 and len(fin)>1): #if user is above 18 but is booking more than one ticket
				messagebox.showinfo("Adult Movie", "You are booking an adult movie so please ensure all the Pals with you are 18+\nAnd do carry Age Proofs of all the peoples")
		if(chkM==1):
			for i in fin:
				if(i[1]=='v'):#convert user selected seats from valid to occupied
					i[1]='o'
					flag=1
	if flag==1:#check if the age criteria is satisfied
		sts=''
		for i in range(len(fin)):
			if i==0:
				sts+=str(fin[i][2])
			else:
				sts+=","+str(fin[i][2])
		#st="Seats Booked successfully\n Seat number : "+sts
		#messagebox.showinfo("Sucess", st)
		print(name,mem,email,timing,tdate,str(cosm),str(dcost),sts,cinemaNAd)
		#return(name, mem, email, timing, tdate, str(cosm), str(dcost), sts, cinemaNAd)
		tickets = 'Tickets'
		dbv=[]
		for i in fin:

			i.insert(2,slotid)
			i=i[:-1]
			dbv.append(i)
		print(f'{dbv} check')
		prod = [tickets, str(dcost),timing, tdate, str(cosm), sts, cinemaNAd, dbv]
		action = 2

		window.destroy()

		payment.vp_start_gui_P(name, mem, prod, email,action) #display payment page

def backh(window,name,mem,email):
	window.destroy()
	nhome.vp_start_gui1(name,mem,email)
#call Payment function vaiables : totalcost=cosm discounted cost=dcost seat number = sts(in string as 12,13) parameters of function ssub has name,mem,email,timing,tdate
def clicked(*args): #called when user selects a seat
	global li,count,strv,fin,cosm,dcost
	j=args[0]
	print(args[1],args[2])
	cost=args[6]
	mem=args[4]
	name=args[3]
	email=args[5]
	print(name,mem,email,cost)
	if li[args[0]].cget('bg')=='blue': #check if the clicked seat is valid seat and not selected earlier
		li[args[0]].configure(background="yellow") #if yes then change color to signify selection
		fin.append([args[1],args[2],(args[0]+1)]) #append it in the list where all selected seats are stored
		count+=1
		cosm+=cost#calculate cost
	else:
		li[args[0]].configure(background="blue")#if that seat has been selected earlier change it to blue to signify diselection
		count-=1
		cosm-=cost
		fin.remove([args[1],args[2],(args[0]+1)]) #remove it from the list
	cou=str(count)
	#strv=args[3]
	#calculate discounts based on the membership of user
	if(mem=='Gold'):
		dcost=0.9*cosm
	elif(mem=='Platinum'):
		dcost=cosm*0.85
	elif(mem=='Diamond'):
		dcost=cosm*0.8
	else:
		dcost=cosm
	costss=str(cosm)
	st="Number of seats selected are : "+cou+"\nTotal cost :"+costss+"\nDiscounted Costs :"+str(dcost)
	strv.set(st)
	print(fin)
	print(cosm,dcost)
def creates(l,di,slotid,name,mem,email,cost,tdate):
	window = Tk()
	global strv
	dic=query(slotid)#get list of seat details based on slotid
	topx=25
	topy=25
	rightx=75
	righty=75
	co=0
	window.geometry("700x600") 
	blu = Button(window,text = "Available",bg='#0052cc', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=20,y=320)
	red = Button(window,text = "BOOKED",bg='red', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=110,y=320)
	bla = Button(window,text = "Invalid",bg='black', fg='#ffffff',width=7,height=1,disabledforeground="white",state=DISABLED,relief=FLAT).place(x=200,y=320)

	strv=StringVar()
	strv.set("Number of seats selected is : 0\nTotal cost: 0")
	wel=Label(window,textvariable=strv,font = "Helvetica 16 bold italic",justify="left").place(x=40,y=380)
	cinemaNAd=di[1]+", "+di[3]+", "+di[2]
	b=Button(window,command=lambda: sub(window,l,slotid,name,mem,email,di[5],tdate,cinemaNAd),text = "Payment",bg='#0052cc', fg='#ffffff',width=8,height=2,relief=RAISED).place(x=100,y=480)
	b1=Button(window,command=lambda: backh(window,name,mem,email),text = "Back",bg='#0034dd', fg='#ffffff',width=8,height=2,relief=RAISED).place(x=300,y=480)
	
	#display the seating arrangements
	#c.bind('<Button-1>', clicked)
	for key,value in dic.items():
		if(value=='v'):
			playbutton = Button(window,text=(co+1),command=partial(clicked, co,key,value,name,mem,email,cost), fg='#ffffff',width=5,height=2,relief=RAISED)
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
	window.mainloop()
#creates()
