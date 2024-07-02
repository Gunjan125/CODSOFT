import random 
import string
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x350')
root.title("Password Generator")
root.configure(bg='light blue')


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    
top_frame = tk.Frame(root, bg='light blue', padx=20, pady=20)
top_frame.grid(row=0,column=0,columnspan=2 )

middle_frame=tk.Frame(root,bg='light blue',padx=20,pady=20)
middle_frame.grid(row=1,column=0)
    
lower_frame=tk.Frame(root,bg='light blue', padx=20, pady=20)
lower_frame.grid(row=2,column=0,columnspan=2 )

reslt_frame=tk.Frame(root,bg='light blue', padx=20, pady=20)
reslt_frame.grid(row=3,column=0,columnspan=2 )

    
Label = tk.Label(top_frame, text="Password Generator", bd=7,font=('Times New Roman', 16, 'bold'), bg='light blue', fg='dark blue')
Label.grid(row=0,columnspan=1)

Label1=tk.Label(middle_frame,text="Enter Lenght of Password", font=('Times New Roman', 16, 'bold'), bg='light blue',fg='white')
Label1.grid(row=1,column=0)

entry = tk.Entry(root, width=30,)
entry.grid(row=1,column=1,pady=10)

def clear_previous_text():
    for widget in reslt_frame.winfo_children():
        widget.destroy()
def show_input():
    clear_previous_text()
    try:
        length = int(entry.get())
        if length>0 :
            all_characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choices(all_characters, k=length))

            Label2=tk.Label(reslt_frame,text=f"Generated Password is: {password}", font=('Times New Roman', 16, 'bold'), bg='light blue', fg='dark blue')
            Label2.grid(row=3,column=1)

        else:
            Label2=tk.Label(reslt_frame,text="Please Enter correct password length!", font=('Times New Roman', 16, 'bold'), bg='light blue', fg='dark blue')
            Label2.grid(row=3,column=1)
    except:
            Label2=tk.Label(reslt_frame,text="Length should be in number!", font=('Times New Roman', 16, 'bold'), bg='light blue', fg='dark blue')
            Label2.grid(row=3,column=1)




button = tk.Button(lower_frame, text="Generate",font=('Times New Roman', 16), command=show_input,bg='white', fg='black', relief='flat', width=10,height=2)
button.grid(row=2,pady=10)


center_window(root)
root.mainloop()