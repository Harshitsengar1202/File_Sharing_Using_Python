from tkinter import *
import socket
from  tkinter import filedialog
from tkinter import messagebox
import os


#######################MAINWINDOW##########################

root=Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

#########################FUNCTIONS####################

def Send():
    win=Toplevel(root)
    win.title("Send")
    win.geometry("450x560+500+200")
    win.configure(bg="#f4fdfe")
    win.resizable(False,False)
    #################icon###############
    image_icon1=PhotoImage(file="send.png")
    win.iconphoto(False,image_icon1)
    Sbackground=PhotoImage(file="sender.png")
    



    win.mainloop()

def Receive():
    win=Toplevel(root)
    win.title("Receive")
    win.geometry("450x560+500+200")
    win.configure(bg="#f4fdfe")
    win.resizable(False,False)
    #################icon###############
    image_icon2=PhotoImage(file="receive.png")
    win.iconphoto(False,image_icon2)


    win.mainloop()

#########################ICON#################

image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)


Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)


########################SENDBUTTON##################

send_image=PhotoImage(file="Send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)
Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=67,y=200)

########################RECEIVEBUTTON##################

receive_image=PhotoImage(file="receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=308,y=200)

########################BACKGROUND#######################
background=PhotoImage(file="background.png")
Label(root,image=background).place(x=-2,y=323)






root.mainloop()