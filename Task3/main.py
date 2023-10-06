from tkinter import *
import string
import random
from tkinter import messagebox

root=Tk()
root.geometry("800x600")
root.title("PASSWORD GENERATOR")

def getname():
    global name
    name=name_text.get(1.0,"end")
    return name


def getlen():
    global passlen
    passlen = passlen_text.get(1.0, "end")
    try:
        passlen = int(passlen)
        return passlen
    except ValueError as e:
        genpass_text.insert(1.0,"INVALID INPUT!")

def generate():
    name = getname()
    length = getlen()
    characters = string.ascii_letters + string.digits + string.punctuation

    # Clear the existing text in the genpass_text widget
    genpass_text.delete(1.0, "end")

    if name and length:
        password = ''.join(random.choice(characters) for _ in range(length))
        genpass_text.insert(1.0, password)
    else:
        genpass_text.insert(1.0, "INVALID INPUT!")


def reset():
    name=""
    passlen=0
    name_text.delete(1.0,"end")
    passlen_text.delete(1.0,"end")
    genpass_text.delete(1.0,"end")

def accept():
    generated_password = genpass_text.get("1.0", "end-1c")

    messagebox.showinfo("PASSWORD!", generated_password)


# Frame
frame = Frame(root)
frame.pack(expand=True, fill="both")  # Use expand and fill to center the label


# Title
title_label=Label(frame,text="PASSWORD GENERATOR!",font=("arial",20,"bold"),width=40,height=5,borderwidth=2,fg="purple")
title_label.grid(row=0,column=3,columnspan=3,padx=55,sticky='n')

# labels
username_label=Label(frame,text="Enter user name:",font=("arial",15),height=2,pady=5,padx=5)
username_label.grid(row=2,column=2,columnspan=2,sticky="w")
passlen_label=Label(frame,text="Enter password length:",font=("arial",15),height=2,pady=5,padx=5)
passlen_label.grid(row=3,column=2,columnspan=2,sticky="w")
genpass_label=Label(frame,text="Generated password:",font=("arial",15),height=2,padx=5,pady=5)
genpass_label.grid(row=4,column=2,columnspan=2,sticky="w")

# Variables for storing data
name_var=StringVar
pass_var=StringVar
gen_var=StringVar

# entries
name_text=Text(frame,width=40,height=2,font=("arial",15,"bold"),fg="purple")
name_text.grid(row=2,column=4)
passlen_text=Text(frame,width=40,height=2,font=("arial",15,"bold"),fg="purple")
passlen_text.grid(row=3,column=4)
genpass_text=Text(frame,width=40,bg="white",fg="purple",height=2,font=("arial",15,"bold"))
genpass_text.grid(row=4,column=4)

# Buttons
Label(frame,text="").grid(row=5,column=4)

generate_button=Button(frame,text="GENERATE PASSWORD",command=lambda :generate(),font=("arial",15,"bold"),bg="purple",fg="white")
generate_button.grid(row=6,column=4)
Label(frame,text="").grid(row=7,column=4)
accept_button=Button(frame,text="ACCEPT",font=("arial",15,"bold"),command=lambda :accept(),bg="white",fg="purple",borderwidth=2,relief="groove",highlightbackground="purple",highlightcolor="purple")
accept_button.grid(row=8,column=4)
Label(frame,text="").grid(row=9,column=4)
reset_button=Button(frame,text="RESET",font=("arial",15,"bold"),command=lambda :reset(),bg="white",fg="purple",borderwidth=2,relief="groove",highlightbackground="purple",highlightcolor="purple")
reset_button.grid(row=10,column=4)

root.mainloop()
