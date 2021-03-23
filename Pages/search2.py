#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 23, 2021 05:31:05 PM IST  platform: Windows NT

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

from searchbar import Searchbar
from memberbar import Memberbar
from homebar import Homebar
from sidebar import Sidebar


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Search (root)
    root.mainloop()

w = None
def create_Search(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Search(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Search (w)
    return (w, top)

def destroy_Search():
    global w
    w.destroy()
    w = None

class Search(Searchbar, Memberbar, Homebar):
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

        top.geometry("1280x686+212+135")
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#000040")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")
        
        top.resizable(False, False)
        global img
        img = ImageTk.PhotoImage(file="bg.png")
        self.Background = tk.Label(top,image = img)        
        self.Background.place(relx=0, rely=0, height=1000, width=1500)
        self.Background=img
        
        
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



################################################################Result instance############################################################
        self.Movie1 = tk.Frame(top)
        self.Movie1.place(relx=0.18, rely=0.233, relheight=0.138, relwidth=0.621)

        self.Movie1.configure(relief='groove')
        self.Movie1.configure(borderwidth="2")
        self.Movie1.configure(relief="groove")
        self.Movie1.configure(background="#00002b")

        self.Image1 = tk.Label(self.Movie1)
        self.Image1.place(relx=0.025, rely=0.095, height=73, width=135)
        self.Image1.configure(background="#d9d9d9")
        self.Image1.configure(disabledforeground="#a3a3a3")
        self.Image1.configure(foreground="#000000")
        self.Image1.configure(text='''image''')

        self.Description1 = tk.Label(self.Movie1)
        self.Description1.place(relx=0.239, rely=0.095, height=73, width=573)
        self.Description1.configure(anchor='nw')
        self.Description1.configure(background="#00002b")
        self.Description1.configure(cursor="fleur")
        self.Description1.configure(disabledforeground="#a3a3a3")
        self.Description1.configure(font="-family {Segoe UI} -size 12")
        self.Description1.configure(foreground="#bcfbfe")
        self.Description1.configure(text='''description''')

##############################################################################################################################################

##################################################################scroller########################################################
        self.Previous = tk.Button(top)
        self.Previous.place(relx=0.383, rely=0.933, height=24, width=47)
        self.Previous.configure(activebackground="#ececec")
        self.Previous.configure(activeforeground="#000000")
        self.Previous.configure(background="#b4eafe")
        self.Previous.configure(disabledforeground="#a3a3a3")
        self.Previous.configure(font="-family {Segoe UI} -size 15")
        self.Previous.configure(foreground="#000000")
        self.Previous.configure(highlightbackground="#d9d9d9")
        self.Previous.configure(highlightcolor="black")
        self.Previous.configure(pady="0")
        self.Previous.configure(text='''<''')

        self.Next = tk.Button(top)
        self.Next.place(relx=0.57, rely=0.933, height=24, width=47)
        self.Next.configure(activebackground="#ececec")
        self.Next.configure(activeforeground="#000000")
        self.Next.configure(background="#b4eafe")
        self.Next.configure(disabledforeground="#a3a3a3")
        self.Next.configure(font="-family {Segoe UI} -size 15")
        self.Next.configure(foreground="#000000")
        self.Next.configure(highlightbackground="#d9d9d9")
        self.Next.configure(highlightcolor="black")
        self.Next.configure(pady="0")
        self.Next.configure(text='''>''')

        self.Page_list = tk.Label(top)
        self.Page_list.place(relx=0.43, rely=0.933, height=21, width=164)
        self.Page_list.configure(activebackground="#f0f0f0f0f0f0")
        self.Page_list.configure(background="#000040")
        self.Page_list.configure(disabledforeground="#a3a3a3")
        self.Page_list.configure(font="-family {Segoe UI} -size 12")
        self.Page_list.configure(foreground="#b4eafe")
        self.Page_list.configure(text='''1 of 4''')
        
        Searchbar.__init__(self, top=None)
        Memberbar.__init__(self, top=None)
        Homebar.__init__(self, top=None)
        Sidebar.__init__(self, top=None)
#####################################################################################################################################

if __name__ == '__main__':
    vp_start_gui()


