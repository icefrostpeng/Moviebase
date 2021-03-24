# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:06:12 2021

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


############################################Membership#########################################################
def button_functionality(mem):
    if mem == 'Gold':
        gold = False
        platinum = True
        diamond = True
    elif mem == 'Silver':
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


class Memberbar:
    def __init__(self, membership, top=None):
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

        gold, platinum, diamond = button_functionality(membership)

        self.Gold_b = tk.Button(self.Membership_f)
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
            print('true')
        else:
            self.Gold_b["state"] = "disabled"
            print('false')

        self.Platinum_b = tk.Button(self.Membership_f)
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
            print('true')
        else:
            self.Platinum_b["state"] = "disabled"
            print('false')

        self.Diamond_b = tk.Button(self.Membership_f)
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
            print('true')
        else:
            self.Diamond_b["state"] = "disabled"
            print('false')

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

    ######################################################################################################################################################

