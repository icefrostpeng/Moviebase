#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 11:55:08 AM IST  platform: Windows NT

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


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = IfnotAdult (root)
    root.mainloop()

w = None
def create_IfnotAdult(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_IfnotAdult(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = IfnotAdult (w)
    return (w, top)

def destroy_IfnotAdult():
    global w
    w.destroy()
    w = None

class IfnotAdult:
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

        top.geometry("1280x686+263+199")
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

        self.Movie1 = tk.Frame(top)
        self.Movie1.place(relx=0.18, rely=0.233, relheight=0.62, relwidth=0.621)
        self.Movie1.configure(relief='groove')
        self.Movie1.configure(borderwidth="2")
        self.Movie1.configure(relief="groove")
        self.Movie1.configure(background="#00002b")
        self.Movie1.configure(cursor="fleur")
        self.Movie1.configure(highlightbackground="#d9d9d9")
        self.Movie1.configure(highlightcolor="black")

        self.Description1 = tk.Label(self.Movie1)
        self.Description1.place(relx=0.39, rely=0.165, height=82, width=163)
        self.Description1.configure(activebackground="#f9f9f9")
        self.Description1.configure(activeforeground="black")
        self.Description1.configure(background="#00002b")
        self.Description1.configure(disabledforeground="#a3a3a3")
        self.Description1.configure(font="-family {Segoe UI} -size 22")
        self.Description1.configure(foreground="#bcfbfe")
        self.Description1.configure(highlightbackground="#d9d9d9")
        self.Description1.configure(highlightcolor="black")
        self.Description1.configure(text='''Sorry!!!!''')
        self.Description1.configure(wraplength="600")

        self.Label2 = tk.Label(self.Movie1)
        self.Label2.place(relx=0.126, rely=0.4, height=121, width=593)
        self.Label2.configure(background="#00002b")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 17")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''It seems that you are under 18 and trying to book a ticket for an adult movie. Sending you to Home page''')
        self.Label2.configure(wraplength="600")

        self.Continue_b = tk.Button(self.Movie1)
        self.Continue_b.place(relx=0.629, rely=0.8, height=44, width=227)
        self.Continue_b.configure(activebackground="#ececec")
        self.Continue_b.configure(activeforeground="#000000")
        self.Continue_b.configure(background="#b4eafe")
        self.Continue_b.configure(disabledforeground="#a3a3a3")
        self.Continue_b.configure(font="-family {Segoe UI} -size 14")
        self.Continue_b.configure(foreground="#000000")
        self.Continue_b.configure(highlightbackground="#d9d9d9")
        self.Continue_b.configure(highlightcolor="black")
        self.Continue_b.configure(pady="0")
        self.Continue_b.configure(text='''Home''')

if __name__ == '__main__':
    vp_start_gui()

