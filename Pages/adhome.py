#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 02:49:35 PM IST  platform: Windows NT


# This Program is the home page for the admin console. It has options to add, remove and modify the databases.

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
    
import deletemovie 
from modifymovie import *
from createmovie import *
from createuser import *
from modifyusers import *
from modifyseats import *
from deltheater import *
import addslot1


#Navigation functions
def vp_start_guih():
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	top = AdHome (root)
	root.mainloop()
from modifycinema import *
from createcinema import *
from deluser import *
w = None

def create_AdHome(rt, *args, **kwargs):
	'''Starting point when module is imported by another module.
	   Correct form of call: 'create_AdHome(root, *args, **kwargs)' .'''
	global w, w_win, root
	#rt = root
	root = rt
	w = tk.Toplevel (root)
	top = AdHome (w)
	return (w, top)

def destroy_AdHome():
	global w
	w.destroy()
	w = None

class AdHome:
	
#ADD REMOVE AND MODIFY SELECTION FUNTIONS
########################################
	def addOptions(self):
		print('1')
		global flag 
		flag=1
		self.Modify_b['state'] = tk.DISABLED
		self.Delete_b['state'] = tk.DISABLED
		self.User_b['state'] = tk.NORMAL
		self.Movie_b['state'] = tk.NORMAL
		self.Cinema_b['state'] = tk.NORMAL
		self.Show_b['state'] = tk.NORMAL
		self.Button1['state'] = tk.DISABLED
		print('1')
		
	def modifyOptions(self):
		print('1')
		global flag
		flag=2
		self.Add_b['state'] = tk.DISABLED
		self.Delete_b['state'] = tk.DISABLED
		self.User_b['state'] = tk.NORMAL
		self.Movie_b['state'] = tk.NORMAL
		self.Cinema_b['state'] = tk.NORMAL
		self.Show_b['state'] = tk.DISABLED
		self.Button1['state'] = tk.NORMAL
		print('1')
		return flag
	def deleteOptions(self):
		print('1')
		global flag
		flag=3
		self.Modify_b['state'] = tk.DISABLED
		self.Add_b['state'] = tk.DISABLED
		self.User_b['state'] = tk.NORMAL
		self.Movie_b['state'] = tk.NORMAL
		self.Cinema_b['state'] = tk.NORMAL
		self.Show_b['state'] = tk.DISABLED
		self.Button1['state'] = tk.DISABLED
		print('1')
		return flag
	def button4(self):
		print('1')
		self.Add_b['state'] = tk.NORMAL
		self.Modify_b['state'] = tk.NORMAL
		self.Delete_b['state'] = tk.NORMAL
		self.User_b['state'] = tk.DISABLED
		self.Movie_b['state'] = tk.DISABLED
		self.Cinema_b['state'] = tk.DISABLED
		self.Show_b['state'] = tk.DISABLED
		self.Button1['state'] = tk.DISABLED
		print('1')
		
#######################################################

#SELECTS THE RESPECTIVE ITEM TO ADD REMOVE OR MODIFY

	def buttonmo(self):
		if flag==3:
			print('1')
			root.destroy()
			deletemovie.vp_start_gui_deletemovie()
		elif flag==2:
			root.destroy()
			vp_start_gui_mod()
			print("try with delete")
		else:
			root.destroy()
			vp_start_gui_create()
			print("try with delete")
			
	def buttonus(self):
		if flag==3:
			print('3')
			root.destroy()
			vp_start_gui_deluser()
			
		elif flag==2:
			root.destroy()
			vp_start_gui_modifyusers()
			print("modify works")
		else:
			root.destroy()
			vp_start_gui_createuser()
			print("user works")
			
	def buttonci(self):
		if flag==3:
			print('1')
			root.destroy()
			vp_start_gui_deltheater()
			
		elif flag==2:
			root.destroy()
			vp_start_gui_cinema()
			print("modify works")
		else:
			root.destroy()
			vp_start_gui_createcinema()
			print("user works")
			
	def buttonsh(self):
		if flag==3:
			print('1')
			
		elif flag==2:
			print('2')
		else:
			root.destroy()
			addslot1.vp_start_gui_add_slot()
			print("user works")
			
	def buttonsc(self):
		if flag==3:
			print('1')
			
		elif flag==2:
			print('2')
			root.destroy()
			vp_start_gui_modifyseats()
			print("modifyyyy works")
			
		else:
			
			print("user works")
			
####################################################################            
			#This is the Page 
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
		top.title("Admin Homepage")
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

		self.Add_b = tk.Button(top,command =lambda:self.addOptions())
		self.Add_b.place(relx=0.211, rely=0.204, height=104, width=247)
		self.Add_b.configure(activebackground="#ececec")
		self.Add_b.configure(activeforeground="#000000")
		self.Add_b.configure(background="#95f1f7")
		self.Add_b.configure(disabledforeground="#a3a3a3")
		self.Add_b.configure(cursor="hand2")
		self.Add_b.configure(font="-family {Segoe UI} -size 23")
		self.Add_b.configure(foreground="#000000")
		self.Add_b.configure(highlightbackground="#d9d9d9")
		self.Add_b.configure(highlightcolor="black")
		self.Add_b.configure(pady="0")
		self.Add_b.configure(text='''Add''')

		self.Modify_b = tk.Button(top,command =lambda:self.modifyOptions())
		self.Modify_b.place(relx=0.211, rely=0.423, height=114, width=247)
		self.Modify_b.configure(activebackground="#ececec")
		self.Modify_b.configure(activeforeground="#000000")
		self.Modify_b.configure(background="#ff8040")
		self.Modify_b.configure(disabledforeground="#a3a3a3")
		self.Modify_b.configure(cursor="hand2")
		self.Modify_b.configure(font="-family {Segoe UI} -size 23")
		self.Modify_b.configure(foreground="#000000")
		self.Modify_b.configure(highlightbackground="#d9d9d9")
		self.Modify_b.configure(highlightcolor="black")
		self.Modify_b.configure(pady="0")
		self.Modify_b.configure(text='''Modify''')

		self.Delete_b = tk.Button(top,command =lambda:self.deleteOptions())
		self.Delete_b.place(relx=0.211, rely=0.641, height=124, width=247)
		self.Delete_b.configure(activebackground="#ececec")
		self.Delete_b.configure(activeforeground="#000000")
		self.Delete_b.configure(background="#d32c38")
		self.Delete_b.configure(disabledforeground="#a3a3a3")
		self.Delete_b.configure(cursor="hand2")
		self.Delete_b.configure(font="-family {Segoe UI} -size 23")
		self.Delete_b.configure(foreground="#000000")
		self.Delete_b.configure(highlightbackground="#d9d9d9")
		self.Delete_b.configure(highlightcolor="black")
		self.Delete_b.configure(pady="0")
		self.Delete_b.configure(text='''Delete''')

		self.User_b = tk.Button(top,state=tk.DISABLED,command=lambda:self.buttonus())
		self.User_b.place(relx=0.633, rely=0.175, height=74, width=157)
		self.User_b.configure(activebackground="#ececec")
		self.User_b.configure(activeforeground="#000000")
		self.User_b.configure(background="#b3ffff")
		self.User_b.configure(disabledforeground="#a3a3a3")
		self.User_b.configure(cursor="hand2")
		self.User_b.configure(font="-family {Segoe UI} -size 16")
		self.User_b.configure(foreground="#000000")
		self.User_b.configure(highlightbackground="#d9d9d9")
		self.User_b.configure(highlightcolor="black")
		self.User_b.configure(pady="0")
		self.User_b.configure(text='''User''')

		self.Movie_b = tk.Button(top,state=tk.DISABLED,command=lambda:self.buttonmo())
		self.Movie_b.place(relx=0.633, rely=0.306, height=74, width=157)
		self.Movie_b.configure(activebackground="#ececec")
		self.Movie_b.configure(activeforeground="#000000")
		self.Movie_b.configure(background="#57fd53")
		self.Movie_b.configure(disabledforeground="#a3a3a3")
		self.Movie_b.configure(cursor="hand2")
		self.Movie_b.configure(font="-family {Segoe UI} -size 17")
		self.Movie_b.configure(foreground="#000000")
		self.Movie_b.configure(highlightbackground="#d9d9d9")
		self.Movie_b.configure(highlightcolor="black")
		self.Movie_b.configure(pady="0")
		self.Movie_b.configure(text='''Movie''')

		self.Cinema_b = tk.Button(top,state=tk.DISABLED,command=lambda:self.buttonci())
		self.Cinema_b.place(relx=0.633, rely=0.437, height=74, width=157)
		self.Cinema_b.configure(activebackground="#ececec")
		self.Cinema_b.configure(activeforeground="#000000")
		self.Cinema_b.configure(background="#d382ee")
		self.Cinema_b.configure(disabledforeground="#a3a3a3")
		self.Cinema_b.configure(cursor="hand2")
		self.Cinema_b.configure(font="-family {Segoe UI} -size 17")
		self.Cinema_b.configure(foreground="#000000")
		self.Cinema_b.configure(highlightbackground="#d9d9d9")
		self.Cinema_b.configure(highlightcolor="black")
		self.Cinema_b.configure(pady="0")
		self.Cinema_b.configure(text='''Cinema''')

		self.Show_b = tk.Button(top,state=tk.DISABLED,command=lambda:self.buttonsh())
		self.Show_b.place(relx=0.633, rely=0.569, height=74, width=157)
		self.Show_b.configure(activebackground="#ececec")
		self.Show_b.configure(activeforeground="#000000")
		self.Show_b.configure(background="#660455")
		self.Show_b.configure(disabledforeground="#a3a3a3")
		self.Show_b.configure(cursor="hand2")
		self.Show_b.configure(font="-family {Segoe UI} -size 17")
		self.Show_b.configure(foreground="#ffffff")
		self.Show_b.configure(highlightbackground="#d9d9d9")
		self.Show_b.configure(highlightcolor="black")
		self.Show_b.configure(pady="0")
		self.Show_b.configure(text='''Show''')

		self.Back_b = tk.Button(top,command =lambda:self.button4())
		self.Back_b.place(relx=0.648, rely=0.845, height=64, width=147)
		self.Back_b.configure(activebackground="#ececec")
		self.Back_b.configure(activeforeground="#000000")
		self.Back_b.configure(background="#b71730")
		self.Back_b.configure(disabledforeground="#a3a3a3")
		self.Back_b.configure(cursor="hand2")
		self.Back_b.configure(font="-family {Segoe UI} -size 18")
		self.Back_b.configure(foreground="#000000")
		self.Back_b.configure(highlightbackground="#d9d9d9")
		self.Back_b.configure(highlightcolor="black")
		self.Back_b.configure(pady="0")
		self.Back_b.configure(text='''<Back''')

		img = ImageTk.PhotoImage(PIL.Image.open("Logo.png").resize((90, 90), PIL.Image.ANTIALIAS))
		#img = ImageTk.PhotoImage(file="Logo.png")
		self.Logo_image = tk.Label(top)
		self.Logo_image.place(relx=0.172, rely=0.015, height=92, width=124)
		self.Logo_image.configure(image=img)
		self.Logo_image=img


		self.Title_l = tk.Label(top)
		self.Title_l.place(relx=0.32, rely=0.044, height=61, width=372)
		self.Title_l.configure(activebackground="#f9f9f9")
		self.Title_l.configure(activeforeground="black")
		self.Title_l.configure(background="#000040")
		self.Title_l.configure(disabledforeground="#a3a3a3")
		self.Title_l.configure(font="-family {Segoe UI} -size 22")
		self.Title_l.configure(foreground="#ffffff")
		self.Title_l.configure(highlightbackground="#d9d9d9")
		self.Title_l.configure(highlightcolor="black")
		self.Title_l.configure(text='''Theatre Buzz Admin Page''')

		self.Label2 = tk.Label(top)
		self.Label2.place(relx=0.484, rely=0.452, height=91, width=93)
		self.Label2.configure(activebackground="#f9f9f9")
		self.Label2.configure(activeforeground="black")
		self.Label2.configure(background="#000040")
		self.Label2.configure(disabledforeground="#a3a3a3")
		self.Label2.configure(font="-family {Segoe UI} -size 24")
		self.Label2.configure(foreground="#aafbfb")
		self.Label2.configure(highlightbackground="#d9d9d9")
		self.Label2.configure(highlightcolor="black")
		self.Label2.configure(text='''>>''')

		self.Button1 = tk.Button(top,state=tk.DISABLED,command=lambda:self.buttonsc())
		self.Button1.place(relx=0.633, rely=0.7, height=74, width=157)
		self.Button1.configure(activebackground="#ececec")
		self.Button1.configure(activeforeground="#000000")
		self.Button1.configure(background="#ff8000")
		self.Button1.configure(disabledforeground="#a3a3a3")
		self.Button1.configure(cursor="hand2")
		self.Button1.configure(font="-family {Segoe UI} -size 19")
		self.Button1.configure(foreground="#000000")
		self.Button1.configure(highlightbackground="#d9d9d9")
		self.Button1.configure(highlightcolor="black")
		self.Button1.configure(pady="0")
		self.Button1.configure(text='''Screen''')
if __name__ == '__main__':
	vp_start_guih()


