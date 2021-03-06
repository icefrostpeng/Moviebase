#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 04:20:35 PM IST  platform: Windows NT


#called by adhome
#redirects to adhome
#########################################################
'''Importing Packages'''
#########################################################

from functools import partial
import sys
from PIL import ImageTk, Image
import PIL
import adhome
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
#from home import *

#from Deletemoviebar import Deletemoviebar

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
'''Page Functions'''
#########################################################
def vp_start_gui_create():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = AddMovie (root)
    root.mainloop()

w = None
def create_AddMovie(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_AddUser(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = AddMovie (w)
    return (w, top)

def destroy_AddMovie():
    global w
    w.destroy()
    w = None


#########################################################
'''Query to insert details into movie'''
#########################################################
def querys(movname, descr, rating, cast, age_rating, genre, poster ):
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
            cur.execute("select movie_id from moviedet ORDER BY movie_id DESC LIMIT 1")
            movie_id=cur.fetchone()
            movie_id=movie_id[0]+1
            print(movie_id)
            sql = "INSERT INTO moviedet (movie_id, movie_name,descr,rating,cast,age_rat,genre,posterx) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
            val = (movie_id, movname, descr, rating, cast, age_rating, genre, poster)
            cur.execute(sql,val)
            #cur.execute(q)
            conn.commit()
        	#data = pd.read_sql_query(q, conn)
            conn.close()
            print("success")
            return 1
        except Exception as e:
        	print(e)
        	return 0

#########################################################
'''Validate and Insert movie'''
#########################################################

def  ins(movname1, descr1, cast1, poster1, RatingSpinbox1, ageratingcombo, genrecombo ):
    movname=movname1.get()
    descr=descr1.get()
    rating=RatingSpinbox1.get()
    cast=cast1.get()
    age_rating=ageratingcombo.get()
    poster=poster1.get()
    genre=genrecombo.get()
    print(movname,descr,rating,cast,age_rating,poster,genre)
    if(len(movname)!=0 and len(descr)!=0 and len(rating)!=0 and len(cast)!=0 and len(age_rating)!=0 and len(genre)!=0 and len(poster)!=0):						
        try:
            t=querys(movname, descr, rating, cast, age_rating, genre, poster)
            if(t==1):
                messagebox.showinfo("Sucess", "Registration successfull")
                root.withdraw()
                adhome.create_AdHome(root)
            else:
                messagebox.showerror("UnSucess", "Registration Unsuccessfull")

        except Exception as e: print(e)

    else:
        messagebox.showerror("Error", "Fields cannot be empty")
    root.destroy()
    adhome.vp_start_guih()


#########################################################
''' Tkinter Page'''
#########################################################
class AddMovie:
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
        
        movname=tk.StringVar()
        descr=tk.StringVar()
        age_rating=tk.StringVar()
        rating=tk.StringVar()
        genre=tk.StringVar()
        poster=tk.StringVar()
        cast=tk.StringVar()

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

        self.Movie_l = tk.Label(top)
        self.Movie_l.place(relx=0.203, rely=0.204, height=31, width=284)
        self.Movie_l.configure(activebackground="#f9f9f9")
        self.Movie_l.configure(activeforeground="black")
        self.Movie_l.configure(anchor='w')
        self.Movie_l.configure(background="#000040")
        self.Movie_l.configure(disabledforeground="#a3a3a3")
        self.Movie_l.configure(font="-family {Segoe UI} -size 13")
        self.Movie_l.configure(foreground="#ffffff")
        self.Movie_l.configure(highlightbackground="#d9d9d9")
        self.Movie_l.configure(highlightcolor="black")
        self.Movie_l.configure(text='''Enter Movie name:''')

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
        self.Desc_l.configure(text='''Enter description:''')

        self.Moviename_e = tk.Entry(top, textvariable=movname)
        self.Moviename_e.place(relx=0.203, rely=0.262, height=30, relwidth=0.222)

        self.Moviename_e.configure(background="white")
        self.Moviename_e.configure(disabledforeground="#a3a3a3")
        self.Moviename_e.configure(font="TkFixedFont")
        self.Moviename_e.configure(foreground="#000000")
        self.Moviename_e.configure(highlightbackground="#d9d9d9")
        self.Moviename_e.configure(highlightcolor="black")
        self.Moviename_e.configure(insertbackground="black")
        self.Moviename_e.configure(selectbackground="blue")
        self.Moviename_e.configure(selectforeground="white")

        self.Desc_e = tk.Entry(top, textvariable=descr)
        self.Desc_e.place(relx=0.203, rely=0.394, height=30, relwidth=0.222)
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
        self.rating_l.configure(cursor="hand2")
        self.rating_l.configure(disabledforeground="#a3a3a3")
        self.rating_l.configure(font="-family {Segoe UI} -size 13")
        self.rating_l.configure(foreground="#ffffff")
        self.rating_l.configure(highlightbackground="#d9d9d9")
        self.rating_l.configure(highlightcolor="black")
        self.rating_l.configure(text='''Enter Rating:''')

        self.cast_l = tk.Label(top)
        self.cast_l.place(relx=0.203, rely=0.554, height=31, width=284)
        self.cast_l.configure(activebackground="#f9f9f9")
        self.cast_l.configure(activeforeground="black")
        self.cast_l.configure(anchor='w')
        self.cast_l.configure(background="#000040")
        self.cast_l.configure(disabledforeground="#a3a3a3")
        self.cast_l.configure(font="-family {Segoe UI} -size 13")
        self.cast_l.configure(foreground="#ffffff")
        self.cast_l.configure(highlightbackground="#d9d9d9")
        self.cast_l.configure(highlightcolor="black")
        self.cast_l.configure(text='''Enter Cast:''')

        self.cast_e = tk.Entry(top, textvariable=cast)
        self.cast_e.place(relx=0.203, rely=0.612, height=30, relwidth=0.222)
        self.cast_e.configure(background="white")
        self.cast_e.configure(disabledforeground="#a3a3a3")
        self.cast_e.configure(font="TkFixedFont")
        self.cast_e.configure(foreground="#000000")
        self.cast_e.configure(highlightbackground="#d9d9d9")
        self.cast_e.configure(highlightcolor="black")
        self.cast_e.configure(insertbackground="black")
        self.cast_e.configure(selectbackground="blue")
        self.cast_e.configure(selectforeground="white")

        self.Agerating_l = tk.Label(top)
        self.Agerating_l.place(relx=0.203, rely=0.685, height=31, width=284)
        self.Agerating_l.configure(activebackground="#f9f9f9")
        self.Agerating_l.configure(activeforeground="black")
        self.Agerating_l.configure(anchor='w')
        self.Agerating_l.configure(background="#000040")
        self.Agerating_l.configure(disabledforeground="#a3a3a3")
        self.Agerating_l.configure(font="-family {Segoe UI} -size 13")
        self.Agerating_l.configure(foreground="#ffffff")
        self.Agerating_l.configure(highlightbackground="#d9d9d9")
        self.Agerating_l.configure(highlightcolor="black")
        self.Agerating_l.configure(text='''Enter Age Rating:''')

        self.Genre_l = tk.Label(top)
        self.Genre_l.place(relx=0.203, rely=0.758, height=33, width=111)
        self.Genre_l.configure(activebackground="#f9f9f9")
        self.Genre_l.configure(activeforeground="black")
        self.Genre_l.configure(anchor='w')
        self.Genre_l.configure(background="#000040")
        self.Genre_l.configure(disabledforeground="#a3a3a3")
        self.Genre_l.configure(cursor="hand2")
        self.Genre_l.configure(font="-family {Segoe UI} -size 13")
        self.Genre_l.configure(foreground="#ffffff")
        self.Genre_l.configure(highlightbackground="#d9d9d9")
        self.Genre_l.configure(highlightcolor="black")
        self.Genre_l.configure(text='''Enter Genre:''')


        self.RatingSpinbox1 = tk.Spinbox(top, from_=1.0, to=5.0)
        self.RatingSpinbox1.place(relx=0.305, rely=0.481, relheight=0.044
                , relwidth=0.034)
        self.RatingSpinbox1.configure(activebackground="#f9f9f9")
        self.RatingSpinbox1.configure(background="white")
        self.RatingSpinbox1.configure(buttonbackground="#d9d9d9")
        self.RatingSpinbox1.configure(disabledforeground="#a3a3a3")
        self.RatingSpinbox1.configure(font="TkDefaultFont")
        self.RatingSpinbox1.configure(foreground="black")
        self.RatingSpinbox1.configure(highlightbackground="black")
        self.RatingSpinbox1.configure(highlightcolor="black")
        self.RatingSpinbox1.configure(insertbackground="black")
        self.RatingSpinbox1.configure(selectbackground="blue")
        self.RatingSpinbox1.configure(selectforeground="white")

        self.ageratingcombo = ttk.Combobox(top, textvariable=age_rating)
        self.ageratingcombo.place(relx=0.336, rely=0.685, relheight=0.045
                , relwidth=0.088)
        self.ageratingcombo.configure(font="-family {Segoe UI} -size 12")
        self.ageratingcombo.configure(takefocus="")
        self.ageratingcombo['values']=('U', 'U/A', 'A')
        self.ageratingcombo.current(1)
        

        self.Genrecombo = ttk.Combobox(top, textvariable= genre)
        self.Genrecombo.place(relx=0.336, rely=0.758, relheight=0.045
                , relwidth=0.088)
        self.Genrecombo.configure(takefocus="")
        self.Genrecombo['values']=('Horror', 'Comedy', 'Action','Suspense', 'Drama')
        self.Genrecombo.current(1)
        
        
        self.Poster_l = tk.Label(top)
        self.Poster_l.place(relx=0.500, rely=0.335, height=31, width=284)
        self.Poster_l.configure(activebackground="#f9f9f9")
        self.Poster_l.configure(activeforeground="black")
        self.Poster_l.configure(anchor='w')
        self.Poster_l.configure(background="#000040")
        self.Poster_l.configure(disabledforeground="#a3a3a3")
        self.Poster_l.configure(font="-family {Segoe UI} -size 13")
        self.Poster_l.configure(foreground="#ffffff")
        self.Poster_l.configure(highlightbackground="#d9d9d9")
        self.Poster_l.configure(highlightcolor="black")
        self.Poster_l.configure(text='''Enter Poster''')
        
        self.Poster_e = tk.Entry(top, textvariable=poster)
        self.Poster_e.place(relx=0.500, rely=0.394, height=30, relwidth=0.222)
        self.Poster_e.configure(background="white")
        self.Poster_e.configure(disabledforeground="#a3a3a3")
        self.Poster_e.configure(font="TkFixedFont")
        self.Poster_e.configure(foreground="#000000")
        self.Poster_e.configure(highlightbackground="#d9d9d9")
        self.Poster_e.configure(highlightcolor="black")
        self.Poster_e.configure(insertbackground="black")
        self.Poster_e.configure(selectbackground="blue")
        self.Poster_e.configure(selectforeground="white")

        
        self.Createuser_b = tk.Button(top, command=lambda: ins(movname, descr, cast, poster, self.RatingSpinbox1, self.ageratingcombo, self.Genrecombo))
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
        self.Createuser_b.configure(text='''Create Movie''')

if __name__ == '__main__':
    vp_start_gui_create()


