from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    password = password_entry.get()
    if len(password) == 0:
        password_list = [choice(LETTERS) for char in range(randint(8, 10))] + \
                        [choice(SYMBOLS) for char in range(randint(2, 4))] + \
                        [choice(NUMBERS) for char in range(randint(2, 4))]

        shuffle(password_list)

        password = ''.join(password_list)
        password_entry.insert(0, password)
        pyperclip.copy(password)

# ---------------------------- SEARCH FEATURE  ------------------------------- #

def find_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo("Oops", "Please specify a website!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo("Oops", "No Data File Found")
        else:
            try: # should actually use an if/else here instead
                entry = data[website]
            except KeyError:
                messagebox.showinfo("Oops.", "No details for this website exists")
            else:
                messagebox.showinfo("Results", f"Email: {entry['email']}\nPassword: {entry['password']}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Do not leave any entries empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Generate password button
password_btn = Button(text="Generate Password", highlightthickness=0, command=generate)
password_btn.grid(row=3, column=2)

#Generate Search button
search_btn = Button(text="Search", highlightthickness=0, width=13, command=find_password)
search_btn.grid(row=1, column=2)

# Add button
add_btn = Button(text="Add", highlightthickness=0, width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


#Entry fields
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dummy@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#text on screen = Labels
website_label = Label(text="Website:", font=("Arial", 14 ))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Arial", 14 ))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 14))
password_label.grid(column=0, row=3)




window.mainloop()
