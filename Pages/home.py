import sys
from PIL import ImageTk, Image
import PIL
global co
co=0
global d,to
d={0:['1.jpeg',5,'horror'],1:['2.jpeg',4,'horror'],2:['3.jpeg',3,'horror'],3:['4.jpeg',5,'horror'],4:['5.jpeg',2,'horror']}
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



def vp_start_gui1(name='XYZ',mem='a',email='singh@fg.c'):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Home (name,mem,email,root)
    root.mainloop()

w = None
def create_Home(rt,*args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Home(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Home (w)
    return (w, top)

def destroy_Home():
    global w
    w.destroy()
    w = None

class Home:
    global to
    def ahead(self,top):
        global co
        co=(co+1)%5
        print(co)
        print(d[co][0])
        img = ImageTk.PhotoImage(Image.open(d[co][0]).resize((560, 277), Image.ANTIALIAS))
        self.Movie_image = tk.Label(top,image = img)
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image=img
        return
    def bac(self,top):
        global co
        if(co==0):
        	print(co)
        else:
        	co-=1
        	print(co)
        img = ImageTk.PhotoImage(Image.open(d[co][0]).resize((560, 277), Image.ANTIALIAS))
        self.Movie_image = tk.Label(top,image = img)
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image=img
        return
    def __init__(self,name,mem,email, top=None):
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

        top.geometry("1280x686+297+168")
        top.minsize(120, 1)
        top.maxsize(3004, 1913)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#000040")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")


        img = ImageTk.PhotoImage(file="bg.png")
        self.Background = tk.Label(top,image = img)        
        self.Background.place(relx=0, rely=0, height=900, width=1200)
        self.Background=img

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



############################################################################Membership###############################################################

        self.Membership_f = tk.LabelFrame(top)
        self.Membership_f.place(relx=0.013, rely=0.219, relheight=0.516
                , relwidth=0.14)
        self.Membership_f.configure(relief='groove')
        self.Membership_f.configure(foreground="#edea67")
        self.Membership_f.configure(background="#bfe2ff")
        self.Membership_f.configure(highlightbackground="#f3fee2")
        self.Membership_f.configure(highlightcolor="#4bc602")

        self.Platinum_b = tk.Button(self.Membership_f)
        self.Platinum_b.place(relx=0.061, rely=0.452, height=84, width=157
                , bordermode='ignore')
        self.Platinum_b.configure(activebackground="#707070")
        self.Platinum_b.configure(activeforeground="white")
        self.Platinum_b.configure(activeforeground="#000000")
        self.Platinum_b.configure(background="#d8d8d8")
        self.Platinum_b.configure(borderwidth="9")
        self.Platinum_b.configure(disabledforeground="#a3a3a3")
        self.Platinum_b.configure(cursor="hand2")
        self.Platinum_b.configure(font="-family {Segoe UI} -size 15")
        self.Platinum_b.configure(foreground="#000000")
        self.Platinum_b.configure(highlightbackground="#d9d9d9")
        self.Platinum_b.configure(highlightcolor="black")
        self.Platinum_b.configure(pady="0")
        self.Platinum_b.configure(text='''Platinum''')

        self.Gold_b = tk.Button(self.Membership_f)
        self.Gold_b.place(relx=0.061, rely=0.734, height=84, width=157
                , bordermode='ignore')
        self.Gold_b.configure(activebackground="#f0df99")
        self.Gold_b.configure(activeforeground="#000000")
        self.Gold_b.configure(background="#ffda04")
        self.Gold_b.configure(borderwidth="9")
        self.Gold_b.configure(disabledforeground="#a3a3a3")
        self.Gold_b.configure(cursor="hand2")
        self.Gold_b.configure(font="-family {Segoe UI} -size 15")
        self.Gold_b.configure(foreground="#000000")
        self.Gold_b.configure(highlightbackground="#d9d9d9")
        self.Gold_b.configure(highlightcolor="black")
        self.Gold_b.configure(pady="0")
        self.Gold_b.configure(text='''Gold''')

        self.Diamond_b = tk.Button(self.Membership_f)
        self.Diamond_b.place(relx=0.061, rely=0.169, height=84, width=157
                , bordermode='ignore')
        self.Diamond_b.configure(activebackground="#d9fcff")
        self.Diamond_b.configure(activeforeground="#7070fa")
        self.Diamond_b.configure(background="#2de9f2")
        self.Diamond_b.configure(borderwidth="9")
        self.Diamond_b.configure(disabledforeground="#a3a3a3")
        self.Diamond_b.configure(cursor="hand2")
        self.Diamond_b.configure(font="-family {Segoe UI} -size 15")
        self.Diamond_b.configure(foreground="#000000")
        self.Diamond_b.configure(highlightbackground="#d9d9d9")
        self.Diamond_b.configure(highlightcolor="#e9f552")
        self.Diamond_b.configure(highlightthickness="6")
        self.Diamond_b.configure(pady="0")
        self.Diamond_b.configure(text='''Diamond''')

        self.Join_l = tk.Label(self.Membership_f)
        self.Join_l.place(relx=0.056, rely=0.028, height=41, width=155
                , bordermode='ignore')
        self.Join_l.configure(activebackground="#f9f9f9")
        self.Join_l.configure(activeforeground="black")
        self.Join_l.configure(background="#bfe2ff")
        self.Join_l.configure(disabledforeground="#a3a3a3")
        self.Join_l.configure(font="-family {Segoe UI} -size 12")
        self.Join_l.configure(foreground="#000000")
        self.Join_l.configure(highlightbackground="#d9d9d9")
        self.Join_l.configure(highlightcolor="black")
        self.Join_l.configure(text='''Join our Membership plan!''')
        self.Join_l.configure(wraplength="150")


#######################################################################################################################################################



############################################Home#####################################################################
        self.Home_f = tk.LabelFrame(top)
        self.Home_f.place(relx=0.023, rely=0.029, relheight=0.092, relwidth=0.55)

        self.Home_f.configure(relief='groove')
        self.Home_f.configure(foreground="#000000")
        self.Home_f.configure(background="#e8e8ff")
        self.Home_f.configure(highlightbackground="#d9d9d9")
        self.Home_f.configure(highlightcolor="black")

        self.home_inner_f = tk.Frame(self.Home_f)
        self.home_inner_f.place(relx=0.017, rely=0.130, relheight=0.700
                , relwidth=0.959, bordermode='ignore')
        self.home_inner_f.configure(relief='groove')
        self.home_inner_f.configure(borderwidth="2")
        self.home_inner_f.configure(relief="groove")
        self.home_inner_f.configure(background="#b3eaff")
        self.home_inner_f.configure(highlightbackground="#d9d9d9")
        self.home_inner_f.configure(highlightcolor="black")

        self.Home_b = tk.Button(self.home_inner_f)
        self.Home_b.place(relx=0.0, rely=0.0, height=40, width=75)
        self.Home_b.configure(activebackground="#ececec")
        self.Home_b.configure(activeforeground="#000000")
        self.Home_b.configure(background="#000040")
        self.Home_b.configure(disabledforeground="#a3a3a3")
        self.Home_b.configure(cursor="hand2")
        self.Home_b.configure(font="-family {Segoe UI} -size 12")
        self.Home_b.configure(foreground="#ffffff")
        self.Home_b.configure(highlightbackground="#d9d9d9")
        self.Home_b.configure(highlightcolor="black")
        self.Home_b.configure(pady="0")
        self.Home_b.configure(text='''Home''')



        self.Member_l = tk.Label(self.home_inner_f)
        self.Member_l.place(relx=0.262, rely=0.137, height=34, width=400)
        self.Member_l.configure(activebackground="#b3eaff")
        self.Member_l.configure(activeforeground="black")
        self.Member_l.configure(background="#b3eaff")
        self.Member_l.configure(disabledforeground="#a3a3a3")
        self.Member_l.configure(font="-family {Segoe UI} -size 12")
        self.Member_l.configure(foreground="#000000")
        self.Member_l.configure(highlightbackground="#d9d9d9")
        self.Member_l.configure(highlightcolor="black")
        st=str(name+",your membership status is : "+mem)
        self.Member_l.configure(text=st)
  
        
  ########################################################################################################################################
  
  ####################################################################Movies Slider###################################################################
        global d
        global to
        to=top
        img = ImageTk.PhotoImage(Image.open(d[0][0]).resize((560, 277), Image.ANTIALIAS))
        self.Movie_image = tk.Label(top,image = img)        
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image=img

        self.Previous_b = tk.Button(top,command=lambda: self.bac(top))
        self.Previous_b.place(relx=0.172, rely=0.277, height=284, width=27)
        self.Previous_b.configure(activebackground="#000040")
        self.Previous_b.configure(activeforeground="white")
        self.Previous_b.configure(activeforeground="#ffffff")
        self.Previous_b.configure(background="#b3eaff")
        self.Previous_b.configure(disabledforeground="#a3a3a3")
        self.Previous_b.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Previous_b.configure(foreground="#000000")
        self.Previous_b.configure(highlightbackground="#d9d9d9")
        self.Previous_b.configure(highlightcolor="black")
        self.Previous_b.configure(pady="0")
        self.Previous_b.configure(text='''<''')

        self.Next_b = tk.Button(top,command=lambda: self.ahead(top))
        self.Next_b.place(relx=0.648, rely=0.277, height=284, width=27)
        self.Next_b.configure(activebackground="#000040")
        self.Next_b.configure(activeforeground="white")
        self.Next_b.configure(activeforeground="#ffffff")
        self.Next_b.configure(background="#b3eaff")
        self.Next_b.configure(disabledforeground="#a3a3a3")
        self.Next_b.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Next_b.configure(foreground="#000000")
        self.Next_b.configure(highlightbackground="#d9d9d9")
        self.Next_b.configure(highlightcolor="black")
        self.Next_b.configure(pady="0")
        self.Next_b.configure(text='''>''')


#########################################################################################################################################

#############################################################Search###############################################################

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

########################################################################################################################################



##########################################################Main##########################################################
        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.172, rely=0.131, height=48, width=193)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#000040")
        self.Label3.configure(borderwidth="5")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 22")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Recommended!''')


        self.Movie_image = tk.Label(top)
        self.Movie_image.place(relx=0.202, rely=0.286, height=277, width=560)
        self.Movie_image.configure(activebackground="#f9f9f9")
        self.Movie_image.configure(activeforeground="black")
        self.Movie_image.configure(background="#d9d9d9")
        self.Movie_image.configure(disabledforeground="#a3a3a3")
        self.Movie_image.configure(foreground="#000000")
        self.Movie_image.configure(highlightbackground="#d9d9d9")
        self.Movie_image.configure(highlightcolor="black")

        self.Book_b = tk.Button(top)
        self.Book_b.place(relx=0.215, rely=0.752, height=54, width=177)
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

        self.Description_f = tk.LabelFrame(top)
        self.Description_f.place(relx=0.357, rely=0.729, relheight=0.108
                , relwidth=0.287)
        self.Description_f.configure(relief='groove')
        self.Description_f.configure(foreground="black")
        self.Description_f.configure(background="#d9d9d9")
        #self.Description_f.configure(cursor="fleur")
        self.Description_f.configure(highlightbackground="#d9d9d9")
        self.Description_f.configure(highlightcolor="black")

        self.Description_l = tk.Label(self.Description_f)
        self.Description_l.place(relx=0.008, rely=0.041, height=72, width=360
                , bordermode='ignore')
        self.Description_l.configure(activebackground="#f9f9f9")
        self.Description_l.configure(activeforeground="black")
        self.Description_l.configure(anchor='nw')
        self.Description_l.configure(background="#000040")
        self.Description_l.configure(disabledforeground="#a3a3a3")
        self.Description_l.configure(font="-family {Segoe UI} -size 12")
        self.Description_l.configure(foreground="#ffffff")
        self.Description_l.configure(highlightbackground="#d9d9d9")
        self.Description_l.configure(highlightcolor="black")
        self.Description_l.configure(text='''Description''')

        self.Info_f = tk.LabelFrame(top)
        self.Info_f.place(relx=0.685, rely=0.294, relheight=0.389
                , relwidth=0.122)
        self.Info_f.configure(relief='groove')
        self.Info_f.configure(foreground="black")
        self.Info_f.configure(background="#000040")
        self.Info_f.configure(highlightbackground="#d9d9d9")
        self.Info_f.configure(highlightcolor="black")

        self.Rating_l = tk.Label(self.Info_f)
        self.Rating_l.place(relx=0.045, rely=0.026, height=27, width=146
                , bordermode='ignore')
        self.Rating_l.configure(activebackground="#f9f9f9")
        self.Rating_l.configure(activeforeground="black")
        self.Rating_l.configure(background="#000040")
        self.Rating_l.configure(disabledforeground="#a3a3a3")
        self.Rating_l.configure(font="-family {Segoe UI} -size 14")
        self.Rating_l.configure(foreground="#ffffff")
        self.Rating_l.configure(highlightbackground="#d9d9d9")
        self.Rating_l.configure(highlightcolor="black")
        self.Rating_l.configure(text='''Rating''')

        self.TSeparator1 = ttk.Separator(self.Info_f)
        self.TSeparator1.place(relx=0.032, rely=0.236, relwidth=1.269
                , bordermode='ignore')
#####################################################Stars###########################################################


        self.Star1 = tk.Label(self.Info_f)
        self.Star1.place(relx=0.173, rely=0.154, height=14, width=16
                , bordermode='ignore')
        self.Star1.configure(activebackground="#f9f9f9")
        self.Star1.configure(activeforeground="black")
        self.Star1.configure(background="#000040")
        self.Star1.configure(disabledforeground="#a3a3a3")
        self.Star1.configure(foreground="#000000")
        self.Star1.configure(highlightbackground="#d9d9d9")
        self.Star1.configure(highlightcolor="black")

        self.Star2 = tk.Label(self.Info_f)
        self.Star2.place(relx=0.301, rely=0.154, height=14, width=17
                , bordermode='ignore')
        self.Star2.configure(activebackground="#f9f9f9")
        self.Star2.configure(activeforeground="black")
        self.Star2.configure(background="#000040")
        self.Star2.configure(disabledforeground="#a3a3a3")
        self.Star2.configure(foreground="#000000")
        self.Star2.configure(highlightbackground="#d9d9d9")
        self.Star2.configure(highlightcolor="black")

        self.Star3 = tk.Label(self.Info_f)
        self.Star3.place(relx=0.436, rely=0.154, height=14, width=16
                , bordermode='ignore')
        self.Star3.configure(activebackground="#f9f9f9")
        self.Star3.configure(activeforeground="black")
        self.Star3.configure(background="#000040")
        self.Star3.configure(disabledforeground="#a3a3a3")
        self.Star3.configure(foreground="#000000")
        self.Star3.configure(highlightbackground="#d9d9d9")
        self.Star3.configure(highlightcolor="black")

        self.Star4 = tk.Label(self.Info_f)
        self.Star4.place(relx=0.564, rely=0.154, height=14, width=16
                , bordermode='ignore')
        self.Star4.configure(activebackground="#f9f9f9")
        self.Star4.configure(activeforeground="black")
        self.Star4.configure(background="#000040")
        self.Star4.configure(disabledforeground="#a3a3a3")
        self.Star4.configure(foreground="#000000")
        self.Star4.configure(highlightbackground="#d9d9d9")
        self.Star4.configure(highlightcolor="black")

        self.Star5 = tk.Label(self.Info_f)
        self.Star5.place(relx=0.699, rely=0.154, height=14, width=16
                , bordermode='ignore')
        self.Star5.configure(activebackground="#f9f9f9")
        self.Star5.configure(activeforeground="black")
        self.Star5.configure(background="#000040")
        self.Star5.configure(disabledforeground="#a3a3a3")
        self.Star5.configure(foreground="#000000")
        self.Star5.configure(highlightbackground="#d9d9d9")
        self.Star5.configure(highlightcolor="black")

#######################################################################################################################################


        self.TSeparator2 = ttk.Separator(self.Info_f)
        self.TSeparator2.place(relx=0.006, rely=0.528, relwidth=1.224
                , bordermode='ignore')

        self.Cast_l = tk.Label(self.Info_f)
        self.Cast_l.place(relx=0.045, rely=0.558, height=109, width=145
                , bordermode='ignore')
        self.Cast_l.configure(activebackground="#f9f9f9")
        self.Cast_l.configure(activeforeground="black")
        self.Cast_l.configure(anchor='nw')
        self.Cast_l.configure(background="#000040")
        self.Cast_l.configure(disabledforeground="#a3a3a3")
        self.Cast_l.configure(font="-family {Segoe UI} -size 12")
        self.Cast_l.configure(foreground="#ffffff")
        self.Cast_l.configure(highlightbackground="#d9d9d9")
        self.Cast_l.configure(highlightcolor="black")
        self.Cast_l.configure(text='''Cast''')

        self.Genre_l = tk.Label(self.Info_f)
        self.Genre_l.place(relx=0.045, rely=0.277, height=48, width=145
                , bordermode='ignore')
        self.Genre_l.configure(activebackground="#f9f9f9")
        self.Genre_l.configure(activeforeground="black")
        self.Genre_l.configure(background="#000040")
        self.Genre_l.configure(disabledforeground="#a3a3a3")
        self.Genre_l.configure(font="-family {Segoe UI} -size 13")
        self.Genre_l.configure(foreground="#ffffff")
        self.Genre_l.configure(highlightbackground="#d9d9d9")
        self.Genre_l.configure(highlightcolor="black")
        self.Genre_l.configure(text='''Genre''')

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.165, rely=0.168,  relheight=0.845)
        self.TSeparator3.configure(orient="vertical")

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.172, rely=0.204, height=42, width=547)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#000040")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 20")
        self.Label8.configure(foreground="#ffffff")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Title''')

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.60, rely=0.204, height=42, width=547)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#000040")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI} -size 20")
        self.Label9.configure(foreground="#ffffff")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''UA/A''')
        
        
        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.818, rely=0.168,  relheight=0.835)
        self.TSeparator4.configure(orient="vertical")


#################################################################SideBar######################################

        self.Listofmovies_f = tk.LabelFrame(top)
        self.Listofmovies_f.place(relx=0.829, rely=0.157, relheight=0.831
                , relwidth=0.138)
        self.Listofmovies_f.configure(relief='groove')
        self.Listofmovies_f.configure(font="-family {Segoe UI} -size 17")
        self.Listofmovies_f.configure(foreground="#000000")
        self.Listofmovies_f.configure(text='''List of Movies''')
        self.Listofmovies_f.configure(background="#d7eeff")
        self.Listofmovies_f.configure(highlightbackground="#f0f0f0f0f0f0")
        self.Listofmovies_f.configure(highlightcolor="#646464646464")

        self.page_id = tk.Label(self.Listofmovies_f)
        self.page_id.place(relx=0.04, rely=0.947, height=21, width=166
                , bordermode='ignore')
        self.page_id.configure(activebackground="#f9f9f9")
        self.page_id.configure(activeforeground="black")
        self.page_id.configure(background="#000040")
        self.page_id.configure(borderwidth="10")
        self.page_id.configure(disabledforeground="#a3a3a3")
        self.page_id.configure(font="-family {Segoe UI} -size 13")
        self.page_id.configure(foreground="#ffffff")
        self.page_id.configure(highlightbackground="#d9d9d9")
        self.page_id.configure(highlightcolor="black")
        self.page_id.configure(text='''1 of 2''')

        self.Movie1_b = tk.Button(self.Listofmovies_f)
        self.Movie1_b.place(relx=0.056, rely=0.07, height=74, width=157
                , bordermode='ignore')
        self.Movie1_b.configure(activebackground="#ececec")
        self.Movie1_b.configure(activeforeground="#000000")
        self.Movie1_b.configure(anchor='nw')
        self.Movie1_b.configure(background="#d7eeff")
        self.Movie1_b.configure(disabledforeground="#a3a3a3")
        self.Movie1_b.configure(font="-family {Segoe UI} -size 12")
        self.Movie1_b.configure(foreground="#000000")
        self.Movie1_b.configure(highlightbackground="#d9d9d9")
        self.Movie1_b.configure(highlightcolor="black")
        self.Movie1_b.configure(pady="0")
        self.Movie1_b.configure(text='''Movie name \n\nRating: 5/5''')
        self.Movie1_b.configure(wraplength="150")

####################################################################################################################
        

if __name__ == '__main__':
    vp_start_gui1()
