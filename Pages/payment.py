#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 10:33:09 AM IST  platform: Windows NT

import sys

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
import sys
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

class Search:
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

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
        self.TSeparator3.configure(orient="vertical")

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
        self.TSeparator4.configure(orient="vertical")

        self.Frame_f = tk.Frame(top)
        self.Frame_f.place(relx=0.18, rely=0.364, relheight=0.443
                , relwidth=0.621)
        self.Frame_f.configure(relief='groove')
        self.Frame_f.configure(borderwidth="2")
        self.Frame_f.configure(relief="groove")
        self.Frame_f.configure(background="#00002b")
        self.Frame_f.configure(highlightbackground="#d9d9d9")
        self.Frame_f.configure(highlightcolor="black")

        self.Product_l = tk.Label(self.Frame_f)
        self.Product_l.place(relx=0.038, rely=0.099, height=113, width=764)
        self.Product_l.configure(activebackground="#f9f9f9")
        self.Product_l.configure(activeforeground="black")
        self.Product_l.configure(anchor='nw')
        self.Product_l.configure(background="#00002b")
        self.Product_l.configure(disabledforeground="#a3a3a3")
        self.Product_l.configure(font="-family {Segoe UI} -size 16")
        self.Product_l.configure(foreground="#bcfbfe")
        self.Product_l.configure(highlightbackground="#d9d9d9")
        self.Product_l.configure(highlightcolor="black")
        self.Product_l.configure(text='''Product_Name''')

        self.Cost_l = tk.Label(self.Frame_f)
        self.Cost_l.place(relx=0.553, rely=0.099, height=88, width=267)
        self.Cost_l.configure(activebackground="#f9f9f9")
        self.Cost_l.configure(activeforeground="black")
        self.Cost_l.configure(background="#00002b")
        self.Cost_l.configure(cursor="fleur")
        self.Cost_l.configure(disabledforeground="#a3a3a3")
        self.Cost_l.configure(font="-family {Segoe UI} -size 19")
        self.Cost_l.configure(foreground="#aaffff")
        self.Cost_l.configure(highlightbackground="#d9d9d9")
        self.Cost_l.configure(highlightcolor="black")
        self.Cost_l.configure(text='''Cost''')

        self.Cancel_b = tk.Button(self.Frame_f)
        self.Cancel_b.place(relx=0.553, rely=0.724, height=44, width=117)
        self.Cancel_b.configure(activebackground="#ececec")
        self.Cancel_b.configure(activeforeground="#000000")
        self.Cancel_b.configure(background="#eb0214")
        self.Cancel_b.configure(disabledforeground="#a3a3a3")
        self.Cancel_b.configure(font="-family {Segoe UI} -size 12")
        self.Cancel_b.configure(foreground="#000000")
        self.Cancel_b.configure(highlightbackground="#d9d9d9")
        self.Cancel_b.configure(highlightcolor="black")
        self.Cancel_b.configure(pady="0")
        self.Cancel_b.configure(text='''Cancel''')

        self.Pay_b = tk.Button(self.Frame_f)
        self.Pay_b.place(relx=0.742, rely=0.691, height=54, width=157)
        self.Pay_b.configure(activebackground="#ececec")
        self.Pay_b.configure(activeforeground="#000000")
        self.Pay_b.configure(background="#00c6c6")
        self.Pay_b.configure(cursor="fleur")
        self.Pay_b.configure(disabledforeground="#a3a3a3")
        self.Pay_b.configure(font="-family {Segoe UI} -size 22")
        self.Pay_b.configure(foreground="#000000")
        self.Pay_b.configure(highlightbackground="#d9d9d9")
        self.Pay_b.configure(highlightcolor="black")
        self.Pay_b.configure(pady="0")
        self.Pay_b.configure(text='''Pay''')
        
        Searchbar.__init__(self, top=None)
        Memberbar.__init__(self, mem, top=None)
        Homebar.__init__(self,name,mem, top=None)
        Sidebar.__init__(self, top=None)


if __name__ == '__main__':
    vp_start_gui()


