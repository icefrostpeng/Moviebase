# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:12:02 2021

@author: Elton
"""

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
class Homebar:
    def __init__(self,uname, mem, top=None):
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

        self.Home_b = tk.Button(self.home_inner_f)
        self.Home_b.place(relx=0.025, rely=0.0, height=54, width=77)
        self.Home_b.configure(activebackground="#ececec")
        self.Home_b.configure(activeforeground="#000000")
        self.Home_b.configure(background="#000040")
        self.Home_b.configure(disabledforeground="#a3a3a3")
        self.Home_b.configure(font="-family {Segoe UI} -size 12")
        self.Home_b.configure(foreground="#ffffff")
        self.Home_b.configure(highlightbackground="#d9d9d9")
        self.Home_b.configure(highlightcolor="black")
        self.Home_b.configure(pady="0")
        self.Home_b.configure(text='''Home''')

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
        self.Member_l.configure(text=f'Member status {uname} has {mem} Membership')


##################################################################################################################################################
