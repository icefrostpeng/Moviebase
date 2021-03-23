# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:15:38 2021

@author: Admin
"""

import sys
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


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Register (root)
    root.mainloop()

w = None
def create_Register(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Register(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Register (w)
    return (w, top)

def destroy_Register():
    global w
    w.destroy()
    w = None

class Register:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("497x804+552+110")#1280x686
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#000328")

        self.email_l = tk.Label(top)
        self.email_l.place(relx=0.163, rely=0.100, height=22, width=183)
        self.email_l.configure(anchor='w')
        self.email_l.configure(background="#000000")
        self.email_l.configure(disabledforeground="#a3a3a3")
        self.email_l.configure(font="-family {Segoe UI} -size 12")
        self.email_l.configure(foreground="#ffffff")
        self.email_l.configure(padx="6")
        self.email_l.configure(text='''Enter your email id:''')

        self.email_e = tk.Entry(top)
        self.email_e.place(relx=0.163, rely=0.150, height=20, relwidth=0.551)
        self.email_e.configure(background="white")
        self.email_e.configure(disabledforeground="#a3a3a3")
        self.email_e.configure(font="TkFixedFont")
        self.email_e.configure(foreground="#000000")
        self.email_e.configure(insertbackground="black")

        self.username_e = tk.Entry(top)
        self.username_e.place(relx=0.163, rely=0.250, height=20, relwidth=0.551)
        self.username_e.configure(background="white")
        #self.username_e.configure(cursor="fleur")
        self.username_e.configure(disabledforeground="#a3a3a3")
        self.username_e.configure(font="TkFixedFont")
        self.username_e.configure(foreground="#000000")
        self.username_e.configure(insertbackground="black")

        self.username_l = tk.Label(top)
        self.username_l.place(relx=0.161, rely=0.200, height=21, width=150)
        self.username_l.configure(activeforeground="#000328")
        self.username_l.configure(anchor='w')
        self.username_l.configure(background="#000328")
        self.username_l.configure(disabledforeground="#a3a3a3")
        self.username_l.configure(font="-family {Segoe UI} -size 12")
        self.username_l.configure(foreground="#ffffff")
        self.username_l.configure(text='''Enter username:''')

        self.password_l = tk.Label(top)
        self.password_l.place(relx=0.165, rely=0.300, height=31, width=149)
        self.password_l.configure(anchor='w')
        self.password_l.configure(background="#000328")
        #self.password_l.configure(cursor="fleur")
        self.password_l.configure(disabledforeground="#a3a3a3")
        self.password_l.configure(font="-family {Segoe UI} -size 12")
        self.password_l.configure(foreground="#ffffff")
        self.password_l.configure(text='''Enter password:''')

        self.password_e = tk.Entry(top)
        self.password_e.place(relx=0.163, rely=0.350, height=20, relwidth=0.551)
        self.password_e.configure(background="white")
        #self.password_e.configure(cursor="fleur")
        self.password_e.configure(disabledforeground="#a3a3a3")
        self.password_e.configure(font="TkFixedFont")
        self.password_e.configure(foreground="#000000")
        self.password_e.configure(insertbackground="black")

        self.confirm_l = tk.Label(top)
        self.confirm_l.place(relx=0.163, rely=0.400, height=32, width=149)
        self.confirm_l.configure(activeforeground="#000328")
        self.confirm_l.configure(anchor='w')
        self.confirm_l.configure(background="#000328")
        self.confirm_l.configure(disabledforeground="#a3a3a3")
        self.confirm_l.configure(font="-family {Segoe UI} -size 12")
        self.confirm_l.configure(foreground="#ffffff")
        self.confirm_l.configure(text='''Confirm Password:''')

        self.confirm_e = tk.Entry(top)
        self.confirm_e.place(relx=0.163, rely=0.450, height=20, relwidth=0.551)
        self.confirm_e.configure(background="white")
        #self.confirm_e.configure(cursor="fleur")
        self.confirm_e.configure(disabledforeground="#a3a3a3")
        self.confirm_e.configure(font="TkFixedFont")
        self.confirm_e.configure(foreground="#000000")
        self.confirm_e.configure(insertbackground="black")

        self.dob = tk.Label(top)
        self.dob.place(relx=0.163, rely=0.500, height=31, width=171)
        self.dob.configure(anchor='w')
        self.dob.configure(background="#000328")
        self.dob.configure(disabledforeground="#a3a3a3")
        self.dob.configure(font="-family {Segoe UI} -size 12")
        self.dob.configure(foreground="#ffffff")
        self.dob.configure(text='''Enter Date of Birth''')

        self.cal = DateEntry(root,width=30,bg="darkblue",fg="white",year=2010)
        self.cal.place(relx=0.163, rely=0.550, height=31, width=171)

        self.address_l = tk.Label(top)
        self.address_l.place(relx=0.163, rely=0.600, height=31, width=171)
        self.address_l.configure(anchor='w')
        self.address_l.configure(background="#000328")
        self.address_l.configure(disabledforeground="#a3a3a3")
        self.address_l.configure(font="-family {Segoe UI} -size 12")
        self.address_l.configure(foreground="#ffffff")
        self.address_l.configure(text='''Enter Address''')

        self.address_e = tk.Entry(top)
        self.address_e.place(relx=0.163, rely=0.650, height=20, relwidth=0.551)
        self.address_e.configure(background="white")
        #self.address_e.configure(cursor="fleur")
        self.address_e.configure(disabledforeground="#a3a3a3")
        self.address_e.configure(font="TkFixedFont")
        self.address_e.configure(foreground="#000000")
        self.address_e.configure(insertbackground="black")

        self.mobileno_l = tk.Label(top)
        self.mobileno_l.place(relx=0.163, rely=0.700, height=31, width=185)
        self.mobileno_l.configure(anchor='w')
        self.mobileno_l.configure(background="#000328")
        self.mobileno_l.configure(disabledforeground="#a3a3a3")
        self.mobileno_l.configure(font="-family {Segoe UI} -size 12")
        self.mobileno_l.configure(foreground="#ffffff")
        self.mobileno_l.configure(text='''Enter your mobile number''')

        self.mobileno_e = tk.Entry(top)
        self.mobileno_e.place(relx=0.163, rely=0.750, height=20, relwidth=0.551)
        self.mobileno_e.configure(background="white")
        #self.mobileno_e.configure(cursor="fleur")
        self.mobileno_e.configure(disabledforeground="#a3a3a3")
        self.mobileno_e.configure(font="TkFixedFont")
        self.mobileno_e.configure(foreground="#000000")
        self.mobileno_e.configure(insertbackground="black")

        self.age_warning = tk.Label(top)
        self.age_warning.place(relx=0.170, rely=0.81, height=21, width=100)
        self.age_warning.configure(background="#000328")
        #self.age_warning.configure(cursor="fleur")
        self.age_warning.configure(disabledforeground="#a3a3a3")
        self.age_warning.configure(foreground="#ffffff")
        self.age_warning.configure(text='''age confirmation''')

        self.checkAge = tk.Checkbutton(top)
        self.checkAge.place(relx=0.584, rely=0.781, relheight=0.081
                , relwidth=0.203)
        self.checkAge.configure(activebackground="#ececec")
        self.checkAge.configure(activeforeground="#000000")
        self.checkAge.configure(background="#000328")
        self.checkAge.configure(cursor="hand2")
        self.checkAge.configure(disabledforeground="#a3a3a3")
        self.checkAge.configure(foreground="#ffffff")
        self.checkAge.configure(highlightbackground="#d9d9d9")
        self.checkAge.configure(highlightcolor="black")
        self.checkAge.configure(justify='left')
        self.checkAge.configure(text='''18+''')
        
        
        
        
        self.Submit = tk.Button(top)
        self.Submit.place(relx=0.300, rely=0.875, height=54, width=177)
        self.Submit.configure(activebackground="#ececec")
        self.Submit.configure(activeforeground="#000000")
        self.Submit.configure(background="#2ba5ff")
        self.Submit.configure(borderwidth="4")
        self.Submit.configure(cursor="hand2")
        self.Submit.configure(disabledforeground="#a3a3a3")
        self.Submit.configure(font="-family {Segoe UI} -size 14")
        self.Submit.configure(foreground="#000000")
        self.Submit.configure(highlightbackground="#d9d9d9")
        self.Submit.configure(highlightcolor="black")
        self.Submit.configure(pady="0")
        self.Submit.configure(text='''Register''')
        

if __name__ == '__main__':
    vp_start_gui()