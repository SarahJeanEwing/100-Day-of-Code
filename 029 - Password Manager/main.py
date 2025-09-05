from tkinter import *
import os
from random import randint, choice, shuffle
from tkinter import messagebox
from dotenv import load_dotenv
import pyperclip

load_dotenv()
email_address = os.getenv('EMAIL_ADDRESS')

def show_password_copied_message():
    messagebox.showinfo("Info", "Password has been copied to clipboard")

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    window.after(100, show_password_copied_message)
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == '' or username == '' or password == '':
        messagebox.showwarning("Warning", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel("Information", f"Do you want to save the following information?\n{website}\n{username}\n{password}")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200)
myPass_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100 , image=myPass_image)
canvas.grid(column=1, row=0)

website_label = Label(window, text='Website', width=18)
website_label.grid(column=0, row=1)

website_entry = Entry(window, width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_label = Label(window, text='Email/Username', width=18)
username_label.grid(column=0, row=2)

username_entry = Entry(window, width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, email_address)

password_label = Label(window, text='Password', width=18)
password_label.grid(column=0, row=3)

password_entry = Entry(window, width=22)
password_entry.grid(column=1, row=3)

generate_password_button = Button(window, text='Generate Password', width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(window, text='Add Password', width=37, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2, pady=(0, 20))

window.mainloop()