"""Manage a password of user"""
import json
import random
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    """Generates a random password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------Search Functionality -----------------------------#
def search():
    """THis method help to email and password for a search website"""
    search_query = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            content = json.load(data_file, )
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="File Not Found")
    else:
        if search_query in content:
            search_query_email = content[search_query]["email"]
            search_query_password = content[search_query]["password"]
            messagebox.showinfo(title=f"{search_query}",
                                message=f"Email:{search_query_email}\n Password:{search_query_password} ")
        else:
            messagebox.showwarning(title="Error",message="No detail found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
"""Here we want to add our data into a json format we will perfom read ,write and update operation on 
    json data .
    json data is  like dictionary key:value .In value it has nested list and dictionary
    for read we use json.load()
    for write we use :json.dump()=> it take data we want to write and a file name in which we want to dump our data
    for update we use :json.update()
"""


def save():
    """Save a data into a data file"""
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    passwd = password_entry.get()
    json_data = {
        website: {
            "email": email,
            "password": passwd
        }
    }

    if len(website) <= 0 or len(email) <= 0 or len(passwd) <= 0:
        messagebox.showwarning(title="warning", message="Please provide value to all fields")
    else:
        # isok = messagebox.askokcancel(title=f"{website}", message=f"These are the details you entered: \n Email: {
        # email}\n Password: {passwd}\n " f"Is it ok to save?") if isok:
        try:
            with open("data.json", "r") as file:
                # json.dump(json_data, file, indent=4,) # writing a json data into a file
                # readed_data = json.load(file)  # reading a json data from a file it returns a Python dictionary
                # print(readed_data)
                # data.write(f"{website},| {email},| {passwd}\n")
                # steps to update a data
                # step 1 read a  old data from a file
                old_data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(json_data, file, indent=4)
        else:
            # step 2: update old data to new_data
            old_data.update(json_data)
            #     step 3 write new_data to file
            with open("data.json", "w") as file:
                json.dump(old_data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# creating a window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # provide a padding
canvas = Canvas(height=200, width=200, highlightthickness=0)  # canvas height and width
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # providing  a x-y coordinate for image
canvas.grid(row=0, column=1)  # layout our image on screen

# Labels
website_label = Label(text="Website:", font=("Arial", 16, "normal"))
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/UserName:", font=("Arial", 16, "normal"))
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 16, "normal"))
password_label.grid(row=3, column=0)

# entrys
website_entry = Entry()
website_entry.focus()
website_entry.grid(row=1, column=1, )

email_entry = Entry(width=35)
email_entry.insert(0, "amit@gmail.com")  # this method will insert this default text
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass = Button(text="Generate Password", command=password_generator)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)
window.mainloop()
