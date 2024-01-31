from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = [random.choice(letters) for _ in range(12)] + [random.choice(symbols) for _ in range(6)] + [random.choice(numbers) for _ in range(6)]

    random.shuffle(password)
    final_password = "".join(password)
    
    password_input.delete(0, END) 
    password_input.insert(0, final_password) 

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    username = user_input.get()
    password = password_input.get()


    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please make sure you don't have any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"New password details: \nEmail: {username} "
                                   f"\n Password: {password} \n Save?")

        if is_ok:
            with open ('password.txt', 'a') as file:
                file.write(f"{website} | {username} | {password}\n")

            website_input.delete(0, END)
            user_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("ilfedrigo Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
user_text = Label(text="e-mail/username:")
user_text.grid(row=2, column=0)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

website_input = Entry(width=38)
website_input.grid(row=1, column=1, columnspan=2)
user_input = Entry(width=38)
user_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=password_generator)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()