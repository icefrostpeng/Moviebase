#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 09:14:49 AM IST  platform: Windows NT

import sys
import seats
from functools import partial
#from searchbar import Searchbar
import searchbar
import memberbar
import homebar
import sidebar
global dic
from datetime import date
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


def vp_start_slot(l,m,name='XYZ',mem='a',email='singh@fg.c',top=None):
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = tk.Tk()
	top = Slots (l,m,name,mem,email,root)
	root.mainloop()

w = None
def create_Slots(rt, *args, **kwargs):
	'''Starting point when module is imported by another module.
	   Correct form of call: 'create_Slots(root, *args, **kwargs)' .'''
	global w, w_win, root
	#rt = root
	root = rt
	w = tk.Toplevel (root)
	top = Slots (w)
	return (w, top)

def destroy_Slots():
	global w
	w.destroy()
	w = None
def slotb(l,i,slotid,name,mem,email,cost,datess,top):
	top.destroy()
	seats.creates(l,i,slotid,name,mem,email,cost,datess)
class Slots( memberbar.Memberbar, homebar.Homebar):
	def __init__(self, l,m,name,mem,email,top=None):
		global dic
		dic=m
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

		self.Recommended_l = tk.Label(top)
		self.Recommended_l.place(relx=0.172, rely=0.131, height=48, width=204)
		self.Recommended_l.configure(activebackground="#f9f9f9")
		self.Recommended_l.configure(activeforeground="black")
		self.Recommended_l.configure(background="#000040")
		self.Recommended_l.configure(borderwidth="5")
		self.Recommended_l.configure(disabledforeground="#a3a3a3")
		self.Recommended_l.configure(font="-family {Segoe UI} -size 22")
		self.Recommended_l.configure(foreground="#ffffff")
		self.Recommended_l.configure(highlightbackground="#d9d9d9")
		self.Recommended_l.configure(highlightcolor="black")
		self.Recommended_l.configure(text="Movie : "+l[1])

		self.TSeparator3 = ttk.Separator(top)
		self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
		self.TSeparator3.configure(orient="vertical")

		self.TSeparator4 = ttk.Separator(top)
		self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
		self.TSeparator4.configure(orient="vertical")

		

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
		self.Page_list.configure(activeforeground="black")
		self.Page_list.configure(background="#000040")
		self.Page_list.configure(disabledforeground="#a3a3a3")
		self.Page_list.configure(font="-family {Segoe UI} -size 12")
		self.Page_list.configure(foreground="#b4eafe")
		self.Page_list.configure(highlightbackground="#d9d9d9")
		self.Page_list.configure(highlightcolor="black")
		self.Page_list.configure(text='''1 of 4''')
		today=date.today()
		g=[]
		for i in m:
			da=i.split('-')
			dat=date(int(da[0]),int(da[1]),int(da[2]))
			if(dat==today):
				g=m[i]
				das=da[2]+"/"+da[1]
				break
		if(len(g)==0):
			key=next(iter(m))
			print(key)
			da=key.split('-')
			dat=date(int(da[0]),int(da[1]),int(da[2]))
			
			g=m[key]
			das=da[2]+"/"+da[1]
		print(g)
		#st=today.strftime("%d")+"/"+today.strftime("%m")
		self.Label2 = tk.Label(top)
		self.Label2.place(relx=0.461, rely=0.248, height=51, width=74)
		self.Label2.configure(background="#000040")
		self.Label2.configure(disabledforeground="#a3a3a3")
		self.Label2.configure(font="-family {Segoe UI} -size 16")
		self.Label2.configure(foreground="#bbfcff")
		self.Label2.configure(text=das)

		self.Button1 = tk.Button(top)
		self.Button1.place(relx=0.391, rely=0.262, height=44, width=47)
		self.Button1.configure(activebackground="#ececec")
		self.Button1.configure(activeforeground="#000000")
		self.Button1.configure(background="#5bedf9")
		self.Button1.configure(disabledforeground="#a3a3a3")
		self.Button1.configure(font="-family {Segoe UI} -size 18")
		self.Button1.configure(foreground="#000000")
		self.Button1.configure(highlightbackground="#d9d9d9")
		self.Button1.configure(highlightcolor="black")
		self.Button1.configure(pady="0")
		self.Button1.configure(text='''<''')

		self.Button2 = tk.Button(top)
		self.Button2.place(relx=0.555, rely=0.262, height=44, width=47)
		self.Button2.configure(activebackground="#ececec")
		self.Button2.configure(activeforeground="#000000")
		self.Button2.configure(background="#5bedf9")
		self.Button2.configure(disabledforeground="#a3a3a3")
		self.Button2.configure(font="-family {Segoe UI} -size 18")
		self.Button2.configure(foreground="#000000")
		self.Button2.configure(highlightbackground="#d9d9d9")
		self.Button2.configure(highlightcolor="black")
		self.Button2.configure(pady="0")
		self.Button2.configure(text='''>''')
		dy=0.1
		ty=0.364
		for i in g:
			print(i)
			self.Movie1 = tk.Frame(top)
			self.Movie1.place(relx=0.18, rely=ty, relheight=0.137, relwidth=0.621)
			self.Movie1.configure(relief='groove')
			self.Movie1.configure(borderwidth="2")
			self.Movie1.configure(relief="groove")
			self.Movie1.configure(background="#00002b")
			self.Movie1.configure(highlightbackground="#d9d9d9")
			self.Movie1.configure(highlightcolor="black")
			self.Description1 = tk.Label(self.Movie1,wraplength=300, justify="left")
			self.Description1.place(relx=0.025, rely=dy, height=160, width=490)
			self.Description1.configure(activebackground="#f9f9f9")
			self.Description1.configure(activeforeground="black")
			self.Description1.configure(anchor='nw')
			self.Description1.configure(background="#00002b")
			self.Description1.configure(cursor="fleur")
			self.Description1.configure(disabledforeground="#a3a3a3")
			self.Description1.configure(font="-family {Segoe UI} -size 13")
			self.Description1.configure(foreground="#bcfbfe")
			self.Description1.configure(highlightbackground="#d9d9d9")
			self.Description1.configure(highlightcolor="black")
			ste="Cinema Hall : "+i[1]+"\t\tCost :"+str(i[6])+"\nAddress "+i[2]+","+i[3]+":\nTiming: "+i[5]
			self.Description1.configure(text=ste)
			
			
			self.Book_b = tk.Button(top,command=partial(slotb,l,i,i[4],name,mem,email,i[6],das,top))
			self.Book_b.place(relx=0.60, rely=ty+0.02, height=54, width=177)
			self.Book_b.configure(activebackground="#000040")
			self.Book_b.configure(activeforeground="white")
			self.Book_b.configure(activeforeground="#ffffff")
			self.Book_b.configure(background="#b3eaff")
			self.Book_b.configure(disabledforeground="#a3a3a3")
			self.Book_b.configure(cursor="hand2")
			self.Book_b.configure(font="-family {Segoe UI} -size 14")
			self.Book_b.configure(foreground="#000000")
			self.Book_b.configure(highlightbackground="#d9d9d9")
			self.Book_b.configure(highlightcolor="black")
			self.Book_b.configure(pady="0")
			self.Book_b.configure(text='''Book Ticket!''')
			ty+=0.14
		
		
		self.Fast_l = tk.Label(top)
		self.Fast_l.place(relx=0.18, rely=0.262, height=31, width=64)
		self.Fast_l.configure(activebackground="#f0f0f0f0f0f0")
		self.Fast_l.configure(background="#ffff80")
		self.Fast_l.configure(disabledforeground="#a3a3a3")
		self.Fast_l.configure(foreground="#000000")
		self.Fast_l.configure(text='''Fast Filling''')

		self.Sold_l = tk.Label(top)
		self.Sold_l.place(relx=0.242, rely=0.262, height=31, width=64)
		self.Sold_l.configure(activebackground="#f0f0f0f0f0f0")
		self.Sold_l.configure(background="#b90000")
		self.Sold_l.configure(disabledforeground="#a3a3a3")
		self.Sold_l.configure(foreground="#000000")
		self.Sold_l.configure(text='''Sold Out''')

		self.Available_f = tk.Label(top)
		self.Available_f.place(relx=0.305, rely=0.262, height=31, width=67)
		self.Available_f.configure(background="#00d200")
		self.Available_f.configure(disabledforeground="#a3a3a3")
		self.Available_f.configure(foreground="#000000")
		self.Available_f.configure(text='''Available''')
		

		
		#Searchbar.__init__(self,name='x',mem='s',email='s', top=None)
		memberbar.Memberbar.__init__(self, name, mem, email, root)
		homebar.Homebar.__init__(self,name,mem, top)
		sidebar.Sidebar.__init__(self, top)

if __name__ == '__main__':
	vp_start_gui()


