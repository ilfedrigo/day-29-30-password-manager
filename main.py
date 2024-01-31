from tkinter import *
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = []
# for char in range (1, nr_letters + 1):
#   password.append(random.choice(letters))

# for char in range (1, nr_symbols + 1):
#   password.append(random.choice(symbols))

# for char in range (1, nr_numbers + 1):
#   password.append(random.choice(numbers))

# final_password = ""
# random.shuffle(password)
# final_password = "".join(password)

# print(final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

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

gen_password_button = Button(text="Generate Password")
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()