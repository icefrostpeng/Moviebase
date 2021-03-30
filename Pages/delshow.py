# #! /usr/bin/env python
# #  -*- coding: utf-8 -*-
# #
# # GUI module generated by PAGE version 6.0.1
# #  in conjunction with Tcl version 8.6
# #    Mar 24, 2021 05:24:22 PM IST  platform: Windows NT


# #

# import sys

# try:
#     import Tkinter as tk
# except ImportError:
#     import tkinter as tk

# try:
#     import ttk
#     py3 = False
# except ImportError:
#     import tkinter.ttk as ttk
#     py3 = True


# def vp_start_gui():
#     '''Starting point when module is the main routine.'''
#     global val, w, root
#     root = tk.Tk()
#     top = Search (root)
#     root.mainloop()

# w = None
# def create_Search(rt, *args, **kwargs):
#     '''Starting point when module is imported by another module.
#        Correct form of call: 'create_Search(root, *args, **kwargs)' .'''
#     global w, w_win, root
#     #rt = root
#     root = rt
#     w = tk.Toplevel (root)
#     top = Search (w)
#     return (w, top)

# def destroy_Search():
#     global w
#     w.destroy()
#     w = None

# class Search:
#     def __init__(self, top=None):
#         '''This class configures and populates the toplevel window.
#            top is the toplevel containing window.'''
#         _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
#         _fgcolor = '#000000'  # X11 color: 'black'
#         _compcolor = '#d9d9d9' # X11 color: 'gray85'
#         _ana1color = '#d9d9d9' # X11 color: 'gray85'
#         _ana2color = '#ececec' # Closest X11 color: 'gray92'
#         self.style = ttk.Style()
#         if sys.platform == "win32":
#             self.style.theme_use('winnative')
#         self.style.configure('.',background=_bgcolor)
#         self.style.configure('.',foreground=_fgcolor)
#         self.style.configure('.',font="TkDefaultFont")
#         self.style.map('.',background=
#             [('selected', _compcolor), ('active',_ana2color)])

#         top.geometry("1280x686+212+135")
#         top.minsize(120, 1)
#         top.maxsize(3004, 1913)
#         top.resizable(1,  1)
#         top.title("New Toplevel")
#         top.configure(background="#000040")
#         top.configure(highlightbackground="#d9d9d9")
#         top.configure(highlightcolor="#000000")

#         self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
#         top.configure(menu = self.menubar)

#         self.TSeparator3 = ttk.Separator(top)
#         self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
#         self.TSeparator3.configure(orient="vertical")

#         self.TSeparator4 = ttk.Separator(top)
#         self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
#         self.TSeparator4.configure(orient="vertical")
        
#         self.Logo_image = tk.Label(top)
#         self.Logo_image.place(relx=0.234, rely=0.029, height=92, width=124)
#         self.Logo_image.configure(activebackground="#f9f9f9")
#         self.Logo_image.configure(activeforeground="black")
#         self.Logo_image.configure(background="#d9d9d9")
#         self.Logo_image.configure(disabledforeground="#a3a3a3")
#         self.Logo_image.configure(foreground="#000000")
#         self.Logo_image.configure(highlightbackground="#d9d9d9")
#         self.Logo_image.configure(highlightcolor="black")
#         self.Logo_image.configure(text='''Label''')

#         self.Title_l = tk.Label(top)
#         self.Title_l.place(relx=0.359, rely=0.044, height=61, width=372)
#         self.Title_l.configure(activebackground="#f9f9f9")
#         self.Title_l.configure(activeforeground="black")
#         self.Title_l.configure(background="#000040")
#         self.Title_l.configure(disabledforeground="#a3a3a3")
#         self.Title_l.configure(font="-family {Segoe UI} -size 22")
#         self.Title_l.configure(foreground="#ffffff")
#         self.Title_l.configure(highlightbackground="#d9d9d9")
#         self.Title_l.configure(highlightcolor="black")
#         self.Title_l.configure(text='''Theatre Buzz Admin Page''')


#         self.Movie1 = tk.Frame(top)
#         self.Movie1.place(relx=0.18, rely=0.364, relheight=0.137, relwidth=0.621)

#         self.Movie1.configure(relief='groove')
#         self.Movie1.configure(borderwidth="2")
#         self.Movie1.configure(relief="groove")
#         self.Movie1.configure(background="#00002b")
#         self.Movie1.configure(highlightbackground="#d9d9d9")
#         self.Movie1.configure(highlightcolor="black")

#         self.Description1 = tk.Label(self.Movie1)
#         self.Description1.place(relx=0.025, rely=0.106, height=32, width=764)
#         self.Description1.configure(activebackground="#f9f9f9")
#         self.Description1.configure(activeforeground="black")
#         self.Description1.configure(anchor='nw')
#         self.Description1.configure(background="#00002b")
#         self.Description1.configure(disabledforeground="#a3a3a3")
#         self.Description1.configure(font="-family {Segoe UI} -size 12")
#         self.Description1.configure(foreground="#bcfbfe")
#         self.Description1.configure(highlightbackground="#d9d9d9")
#         self.Description1.configure(highlightcolor="black")
#         self.Description1.configure(text='''Name of cinema with address''')

#         self.Label3 = tk.Label(self.Movie1)
#         self.Label3.place(relx=0.038, rely=0.638, height=21, width=54)
#         self.Label3.configure(activebackground="#f9f9f9")
#         self.Label3.configure(activeforeground="black")
#         self.Label3.configure(background="#d9d9d9")
#         self.Label3.configure(disabledforeground="#a3a3a3")
#         self.Label3.configure(foreground="#000000")
#         self.Label3.configure(highlightbackground="#d9d9d9")
#         self.Label3.configure(highlightcolor="black")
#         self.Label3.configure(text='''timings''')

#         self.Label4 = tk.Label(self.Movie1)
#         self.Label4.place(relx=0.138, rely=0.638, height=21, width=55)
#         self.Label4.configure(activebackground="#f9f9f9")
#         self.Label4.configure(activeforeground="black")
#         self.Label4.configure(background="#d9d9d9")
#         self.Label4.configure(disabledforeground="#a3a3a3")
#         self.Label4.configure(foreground="#000000")
#         self.Label4.configure(highlightbackground="#d9d9d9")
#         self.Label4.configure(highlightcolor="black")
#         self.Label4.configure(text='''timings''')

# if __name__ == '__main__':
#     vp_start_gui()


