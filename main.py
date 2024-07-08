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
    global filename
    win=Toplevel(root)
    win.title("Send")
    win.geometry("450x560+500+200")
    win.configure(bg="#f4fdfe")
    win.resizable(False,False)

    def select_file():
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select Image File',
                                            filetype=(('file_type','*.txt'),('all files','*.*')))
        
    
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port = 8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("Waiting for any incoming connectoions......")
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")
    #################icon###############
    image_icon1=PhotoImage(file="send.png")
    win.iconphoto(False,image_icon1)
    Sbackground=PhotoImage(file="sender.png")
    Label(win,image=Sbackground).place(x=-2,y=0)

    Mbackground=PhotoImage(file="id.png")
    Label(win,image=Mbackground,bg="#f4fdfe").place(x=0,y=260)

    host=socket.gethostname()
    Label(win,text=f"ID : {host}",bg='white',fg='black').place(x=160,y=280)

    Button(win,text="+ select file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(win,text="SEND",width=8,height=1,font='aial 14 bold',bg="#000",fg="#fff",command=sender).place(x=300,y=150)



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
    Hbackground=PhotoImage(file='background.png')
    Label(win,image=Hbackground).place(x=-2,y=0)

    logo=PhotoImage(file='id.png')
    Label(win,image=logo,bg="#f4fdfe").place(x=10,y=250)
    Label(win,text="Receive",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340)

    Label(win,text="Input Sender id",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340)
    SenderID= Entry(win,width=25,fg="black",border=2,bg='white',font=('arial', 15))
    SenderID.place(x=20,y=370)

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