
import tkinter as tk
import re

window=tk.Tk()
window.title("Password Checker tool")
window.geometry("450x400")
#Main logic for the password checker
def check():
    if enter.get()=="":
        label["text"]=("Password is Empty! Please Enter the Password")
    elif len(enter.get()) < 8:
        label["text"]=("Weak Password: Password should contain at least 8 character")
        label.config(fg="red")
    elif not re.search("[A-Z]", enter.get()):
        label["text"]=("Weak Password: Password should contain Uppercase letter")
        label.config(fg="red")
    elif not re.search("[a-z]", enter.get()):
        label["text"]=("Weak Password: Password should contain Lowercase letter")
        label.config(fg="red")
    elif not re.search("[0-9]", enter.get()):
        label["text"]=("Weak Password: Password should contain Lowercase letter")
        label.config(fg="red")
    elif not re.search(r"[!@#$%^&*()_+[\]{};:/\\\"<>?,.]+", enter.get()):
        label["text"]=("Weak Password: Password should contain Special character")
        label.config(fg="red")
    else:
        label["text"]=("Strong Password: You have got the strong password ")
        label.config(fg="green")

Maintext=tk.Label(window,text="Check Password Strength",font=("helvitica",15,"bold"),fg=("Blue"))
Maintext.pack()

text=tk.Label(window, text=" Enter your Password ", font=("helvitica",10,"bold"))
text.pack(padx=20,pady=20)

#Box to enter the password
enter=tk.Entry(window,relief="solid",width=30)
enter.pack()
#Button to check the password
button=tk.Button(window,text="Check",command=check,bg="#42c2f5",height=1,relief="solid")
button.pack(padx=10,pady=5)

#Space to show the results
label=tk.Label(text="",height=4, font=("helvitica",10,"bold"))
label.place(x=50,y=180)
window.mainloop()
