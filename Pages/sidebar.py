# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:22:08 2021

@author: Elton
"""
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder

import sys
from PIL import ImageTk, Image
import PIL
global co
co=0
global d,to
d={0:['1.jpeg',5,'horror'],1:['2.jpeg',4,'horror'],2:['3.jpeg',3,'horror'],3:['4.jpeg',5,'horror'],4:['5.jpeg',2,'horror']}
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
		data = pd.read_sql_query(q, conn)
		conn.close()
		return data

name=[]
rating=[]
for i in range(1,6):
    q1='select movie_name from moviedet where movie_id={0} and status="r"'.format(i)
    v1=query(q1)
    v1=v1.replace('movie_name' ,'')
    print(v1)
    if v1.empty:
        continue
    else:
        name.append(v1)
    q2='select rating from moviedet where movie_id={0} and status="r"'.format(i)
    v2=query(q2)
    print(v2)
    if v2.empty:
        continue
    else:
        rating.append(v2)
#print(name)
#print(rating)


class Sidebar:
    def __init__(self, top=None):
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

        self.Movie1_b = tk.Button(self.Listofmovies_f)
        self.Movie1_b.place(relx=0.056, rely=0.07, height=74, width=157
                , bordermode='ignore')
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
        self.Movie1_b.configure(text='''Movie name \n\nRating: 5/5''')
        self.Movie1_b.configure(wraplength="150")

####################################################################################################################
