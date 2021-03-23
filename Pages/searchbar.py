# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:43:11 2021

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
class Searchbar:
    ###############################################Search##########################################################################################
    def __init__(self, top=None):
        self.Search_f = tk.LabelFrame(top)
        self.Search_f.place(relx=0.609, rely=0.044, relheight=0.06
                , relwidth=0.322)
        self.Search_f.configure(relief='groove')
        self.Search_f.configure(foreground="black")
        self.Search_f.configure(background="#e8e8ff")
        self.Search_f.configure(highlightbackground="#d9d9d9")
        self.Search_f.configure(highlightcolor="black")
    
    
        self.Search_b = tk.Button(self.Search_f)
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
    
        self.Search_e = tk.Entry(self.Search_f)
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

###############################################################################################################################################