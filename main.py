from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# creating a window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(height=400, width=400, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=logo_img)
canvas.grid(row=1, column=1)

window.mainloop()
