from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save a data into a data file"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    isok = messagebox.askokcancel(title=f"{website}",
                                  message=f"These are the details you entered: \n Email: {email}\n Password: {password}\n "
                                          f"Is it ok to save?")
    if isok:
        with open("data.txt", "a") as data:
            data.write(f"{website},| {email},| {password}\n")
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
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "amit@gmail.com")  # this method will insert this default text
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass = Button(text="Generate Password")
generate_pass.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
