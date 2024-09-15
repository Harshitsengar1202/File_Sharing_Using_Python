from tkinter import *
from tkinter import ttk
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
import threading

####################### MAIN WINDOW ##########################

root = Tk()
root.title("File-Transfer")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)

######################### SEND TAB ####################

send_frame = Frame(notebook, bg="#f4fdfe")
notebook.add(send_frame, text="Send")

# Initialize filename
filename = None

selected_file_label = Label(send_frame, text="", bg="#f4fdfe", fg="black", font=('arial', 12))
selected_file_label.place(x=160, y=120)

def select_file():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select File',
                                          filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
    if filename:
        selected_file_label.config(text=os.path.basename(filename))  # Display the selected file name

def sender():
    if not filename:
        messagebox.showerror("Error", "Please select a file to send.")
        return
    
    try:
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print("Waiting for incoming connections...")
        conn, addr = s.accept()
        print(f"Connection established with {addr}")

        with open(filename, 'rb') as file:
            file_data = file.read(1024)
            while file_data:
                conn.send(file_data)
                file_data = file.read(1024)
        print("Data has been transmitted successfully")
        messagebox.showinfo("Success", "File sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Failed to send file: {e}")
    finally:
        s.close()

# UI Elements for Send Tab
Button(send_frame, text="+ select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file).place(x=160, y=150)
Button(send_frame, text="SEND", width=8, height=1, font='arial 14 bold', bg="#000", fg="#fff", command=lambda: threading.Thread(target=sender).start()).place(x=300, y=150)

# Display Host ID
host = socket.gethostname()
Label(send_frame, text=f"ID : {host}", bg='white', fg='black').place(x=160, y=280)

######################### RECEIVE TAB ####################

receive_frame = Frame(notebook, bg="#f4fdfe")
notebook.add(receive_frame, text="Receive")

def receiver():
    ID = SenderID.get()
    filename1 = incoming_file.get()
    if not ID or not filename1:
        messagebox.showerror("Error", "Please provide Sender ID and filename.")
        return

    try:
        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        with open(filename1, 'wb') as file:
            file_data = s.recv(1024)
            while file_data:
                file.write(file_data)
                file_data = s.recv(1024)
        print("File has been received successfully")
        messagebox.showinfo("Success", "File received successfully!")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Failed to receive file: {e}")
    finally:
        s.close()

# UI Elements for Receive Tab
Label(receive_frame, text="Input Sender ID", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=40)
SenderID = Entry(receive_frame, width=25, fg="black", border=2, bg='white', font=('arial', 15))
SenderID.place(x=20, y=70)
SenderID.focus()

Label(receive_frame, text="Filename for the incoming file:", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=120)
incoming_file = Entry(receive_frame, width=25, fg="black", border=2, bg='white', font=('arial', 15))
incoming_file.place(x=20, y=150)

image_icon1 = PhotoImage(file="arrow.png")
Button(receive_frame, text="Receive", compound=LEFT, image=image_icon1, width=130, bg="#39c790", font="arial 14 bold", command=lambda: threading.Thread(target=receiver).start()).place(x=20, y=200)

######################### ICON #################

image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

Label(root, text="File Transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").place(x=20, y=30)

######################## BACKGROUND #######################
background = PhotoImage(file="background.png")
Label(root, image=background).place(x=-2, y=323)

root.mainloop()
