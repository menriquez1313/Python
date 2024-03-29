from email import message
from email.mime import image
from textwrap import indent
from tkinter import *
from tkinter import messagebox 
from random import choice, randint, shuffle
from turtle import title
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END) #clears password entry if regenerating a new password
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_numbers + password_symbols

    password_list += choice(numbers)

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    # password += chare
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
    messagebox.showinfo(title="Password Copied", message="Password has been clipped!")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="OOPS", message="Please fill in the blank fields. \nThank You!")
    
    else:
        try:
            with open("data.json","r") as data_file:
                #reads old data
                data = json.load(data_file)
                    
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else: 
            #updating old data with new data
            data.update(new_data)
            
            with open("data.json","w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
                
        finally: 
            #data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exits.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hero@email.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

#button 
search = Button(text="Search", width=14, command=find_password)
search.grid(column=2, row=1)
generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(column=2, row=3)
add = Button(text="Add", width=35, command=save)
add.grid(column=1, row=4, columnspan=2)
window.mainloop()