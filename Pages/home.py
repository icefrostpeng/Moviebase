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
    

 
import sidebar
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

def button_functionality(mem):
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

#paramiko 
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
    
    #gets Movies from the database
def querys(q):
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
        arr = list(cur.fetchall())
        dic={}
        val=1
        for i in arr:
            li=list(i[1:7])
            a=str(val)+".jpeg"
            li.insert(0,a)
            dic[i[0]]=li
            val+=1
        return dic
    
    #gets all movies
def data():
        m=querys("select * from moviedet")
        return m
    
    #gets list if shows to be shown to the user
def bookT(name,mem,email,top):
    global co,d
    ky=[]
    for i in d.keys():
        ky.append(i)
    print(d[ky[co]])
    print("yess")
    dic={}
    m=query(" select theaterdet.theater_id,theaterdet.theater_name,theaterdet.city,theaterdet.theater_add,slotdet.slot_id,slotdet.timing,slotdet.cost,slotdet.dates from theaterdet,slotdet where movie_id={0} and slotdet.theater_id=theaterdet.theater_id order by slotdet.dates".format(ky[co]))
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

    mov=d[ky[co]]
    mov=mov[1:]
    mov.insert(0,ky[co])
    top.destroy()

    slots.vp_start_slot(mov,dic,name,mem,email,top)
    
    
    
def vp_start_gui1(name='XYZ',mem='a',email='singh@fg.c'):
    '''Starting point when module is the main routine.'''
    global val, w, root,d
    root = tk.Tk()
    d=data()

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

class Home():
    global to
    def ahead(self,top):
        global co
        co=(co+1)%5
        ky=[]
        for i in d.keys():
            ky.append(i)
        print(ky)
        print(d[ky[co]])
        print(d[ky[co]][0])
        img = ImageTk.PhotoImage(Image.open(d[ky[co]][0]).resize((560, 277), Image.ANTIALIAS))
        self.Movie_image = tk.Label(top,image = img)
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image=img
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
    def bac(self,top):
        global co
        ky=[]
        for i in d.keys():
            ky.append(i)
        if(co==0):
            print(co)
        else:
            co-=1
            print(co)
        img = ImageTk.PhotoImage(Image.open(d[ky[co]][0]).resize((560, 277), Image.ANTIALIAS))
        self.Movie_image = tk.Label(top,image = img)
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image=img
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
    def __init__(self,name,mem,email, top=None):
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
        img = ImageTk.PhotoImage(PIL.Image.open(d[1][0]).resize((560, 277), PIL.Image.ANTIALIAS))
        self.Movie_image = tk.Label(top,image = img)        
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image=img

        self.Previous_b = tk.Button(top,command=lambda: self.bac(top))
        self.Previous_b.place(relx=0.172, rely=0.277, height=284, width=27)
        self.Previous_b.configure(activebackground="#000040", activeforeground="#ffffff", background="#b3eaff", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 20 -weight bold", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''<''')

        self.Next_b = tk.Button(top,command=lambda: self.ahead(top))
        self.Next_b.place(relx=0.648, rely=0.277, height=284, width=27)
        self.Next_b.configure(activebackground="#000040", activeforeground="#ffffff", background="#b3eaff", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 20 -weight bold", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''>''')


#########################################################################################################################################





##########################################################Main##########################################################
        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.172, rely=0.131, height=48, width=193)
        self.Label3.configure(activebackground="#f9f9f9", activeforeground="black", background="#000040", borderwidth="5", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 22", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black", text='''Recommended!''')


        self.Movie_image = tk.Label(top)
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Book_b = tk.Button(top,command=lambda: bookT(name,mem,email,top))
        self.Book_b.place(relx=0.215, rely=0.752, height=54, width=177)
        self.Book_b.configure(activebackground="#000040", activeforeground="#ffffff", background="#b3eaff", disabledforeground="#a3a3a3", cursor="hand2", font="-family {Segoe UI} -size 14", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Book Ticket!''')

        self.Description_f = tk.LabelFrame(top)
        self.Description_f.place(relx=0.357, rely=0.729, relheight=0.108
                , relwidth=0.287)
        self.Description_f.configure(relief='groove', foreground="black", background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Description_l = tk.Label(self.Description_f,wraplength=600,justify="left")
        self.Description_l.place(relx=0.008, rely=0.041, height=72, width=360
                , bordermode='ignore')
        self.Description_l.configure(activebackground="#f9f9f9", activeforeground="black", anchor='nw', background="#000040", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
        st="Description : \n"+d[1][2]
        self.Description_l.configure(text=st)

        self.Info_f = tk.LabelFrame(top)
        self.Info_f.place(relx=0.685, rely=0.294, relheight=0.389
                , relwidth=0.122)
        self.Info_f.configure(relief='groove', foreground="black", background="#000040", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Rating_l = tk.Label(self.Info_f)
        self.Rating_l.place(relx=0.045, rely=0.026, height=50, width=146
                , bordermode='ignore')
        self.Rating_l.configure(activebackground="#f9f9f9", activeforeground="black", background="#000040", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 14", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
        strr="Rating : \n"+str(d[1][3])+"/5"
        self.Rating_l.configure(text=strr)

        self.TSeparator1 = ttk.Separator(self.Info_f)
        self.TSeparator1.place(relx=0.032, rely=0.236, relwidth=1.269
                , bordermode='ignore')
#####################################################Stars###########################################################


        

#######################################################################################################################################



        self.Cast_l = tk.Label(self.Info_f,wraplength=500)
        self.Cast_l.place(relx=0.045, rely=0.558, height=109, width=145, bordermode='ignore')
        self.Cast_l.configure(activebackground="#f9f9f9", activeforeground="black", anchor='nw', background="#000040", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
        stc="Cast : \n"
        lis=d[1][4].split(',')
        for i in lis:
            stc+=i+"\n"
        self.Cast_l.configure(text=stc)

        self.Genre_l = tk.Label(self.Info_f)
        self.Genre_l.place(relx=0.045, rely=0.277, height=48, width=145, bordermode='ignore')
        self.Genre_l.configure(activebackground="#f9f9f9", activeforeground="black", background="#000040", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
        stg="Genre : \n"+d[1][6]
        self.Genre_l.configure(text=stg)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
        self.TSeparator3.configure(orient="vertical")

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.172, rely=0.204, height=42, width=547)
        self.Label8.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#000040", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 20", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
        stt="Title : "+d[1][1]
        self.Label8.configure(text=stt)

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.60, rely=0.204, height=42, width=547)
        self.Label9.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#000040", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 20", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black", text=d[1][5])
        
        self.membership = membership
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
            payment.vp_start_gui_P(name, membership, product, email, action)


        # membership status
        gold, platinum, diamond = button_functionality(membership)

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
        

if __name__ == '__main__':
    vp_start_gui1()
