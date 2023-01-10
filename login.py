from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk     #pip install pillow
from tkinter import messagebox
from LPG_booking_system import *
from LPG_booking_system import LPG_Booking

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(r"C:\Users\lenovo\Downloads\cylinder1.jpg")         #image....
        lbl_bg=Label(self.root,image=self.bg)         #image line 
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)    #image line 

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r" ")                         #image....
        img1=img1.resize((100,100),Image.ANTIALIAS)   #image line (21 :30)
        self.photoimage1=ImageTk.PhotoImage(img1)     #image line 
        lblimg1= Label(image=self.photoimage1,bg="black",borderwidth=0)        #image line
        lblimg1.place(x=730,y=175,width=100,height=100)    #image line

        get_str=Label(frame,text="Get Started",font=("times new roman ",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #lable
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=0,y=155)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=100,y=155, width=220)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=0,y=250)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=100,y=250,width=220)

        #=========Icon Image=========
        img2=Image.open(r" ")                         #image....
        img2=img2.resize((25,25),Image.ANTIALIAS)   #image line (21:30)
        self.photoimage2=ImageTk.PhotoImage(img2)     #image line 
        lblimg1= Label(image=self.photoimage2,bg="black",borderwidth=0)        #image line
        lblimg1.place(x=650,y=323,width=25,height=25)    #image line

        
        img3=Image.open(r" ")                         #image....
        img3=img3.resize((25,25),Image.ANTIALIAS)   #image line (21:30)
        self.photoimage3=ImageTk.PhotoImage(img3)     #image line 
        lblimg1= Label(image=self.photoimage3,bg="black",borderwidth=0)        #image line
        lblimg1.place(x=650,y=395,width=25,height=25)    #image line
        
        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman ",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red", activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #registerbutton
        registerbtn=Button(frame,text="New User Register",font=("times new roman ",10,"bold"),borderwidth=0,fg="white",bg="black", activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #forgotpassbtn
        loginbtnp=Button(frame,text="Forget Password",font=("times new roman ",10,"bold"),borderwidth=0,fg="white",bg="black", activeforeground="white",activebackground="black")
        loginbtnp.place(x=10,y=370,width=160)
        
    def login(self):
        self.new_win=Toplevel(self.root)
        self.main_app=LPG_Booking(self.new_win)



if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()      

