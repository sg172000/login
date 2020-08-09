from tkinter import *
import os
from PIL import ImageTk

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def logout():
    screen7.destroy()

def session():
  global screen4
  screen8 = Toplevel(screen)
  screen8.bg=ImageTk.PhotoImage(file="3.jpg")
  screen8.bg_image=Label(screen8,image=screen8.bg).place(x=0,y=0,relwidth=1,relheight=1)
  screen8.title("Dashboard")
  screen8.geometry("1199x600+100+50")
  
def login_sucess():
  session()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150*100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Successfull", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.bg=ImageTk.PhotoImage(file="3.jpg")
  screen1.bg_image=Label(screen1,image=screen1.bg).place(x=0,y=0,relwidth=1,relheight=1)
  screen1.title("Register")
  screen1.geometry("1199x600+100+50")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 35, height = 3, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.bg=ImageTk.PhotoImage(file="3.jpg")
  screen2.bg_image=Label(screen2,image=screen2.bg).place(x=0,y=0,relwidth=1,relheight=1)
  screen2.title("Login")
  screen2.geometry("1199x600+100+50")
  Label(screen2, text = "Please enter details below to login",font=("impact",10)).pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ",font=("impact",10,),fg="black",bg="white").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ",font=("impact",10,),fg="black",bg="white").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login",  width = 35, height = 3, command = login_verify,font=("impact",10),fg="black",bg="white").pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  #======bg============
  screen.bg=ImageTk.PhotoImage(file="3.jpg")
  screen.bg_image=Label(screen,image=screen.bg).place(x=0,y=0,relwidth=1,relheight=1)
  screen.title("DOCTOR CURE")
  screen.geometry("1700x700+0+0")
  
  Label(text = "").pack()
  
  title=Label(screen,text="DOCTOR CURE",font=("impact",50,"bold"),fg="light blue",bg="black").place(x=190,y=30)
  Login_Frame=Frame(screen,bg="black")
  Login_Frame.place(x=400,y=150)
  
  Button(text = "Login",bg="light blue",fg="black",bd=0,height="4",width="40",font=("times new roman",13), command = login).place(x=200,y=200)
  Label(text = "").pack()
  Button(text = "Register",bg="light blue",fg="black",bd=0,height="4",width="40",font=("times new roman",13), command = register).place(x=200,y=300)

  screen.mainloop()

main_screen()