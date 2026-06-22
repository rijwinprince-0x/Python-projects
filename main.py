from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for _ in range(randint(8,10))]
    password_symbols =[choice(symbols) for _ in range(randint(2,4))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]

    password_list= password_letters + password_symbols + password_numbers
    shuffle([password_list])

    password ="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    u_password=password_entry.get()

    if len(website) == 0 or len(u_password) == 0 or len(email)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}"f"\nPassword: {u_password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{email}|{u_password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Rijwin's Password Manager and Generator")
window.config(padx=50, pady=50)

# Configure columns to allow expansion and proper spacing
window.columnconfigure(0, weight=0) # Column 0 (Labels) stays tight to content
window.columnconfigure(1, weight=1) # Column 1 (Entries) expands evenly
window.columnconfigure(2, weight=0) # Column 2 (Generate Button) stays tight to content

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=(0, 20)) # Added padding below logo

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5) # Align right (east)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5) # Stretch east-west
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew", padx=(0, 10), pady=5) # Stretch to edge of col 1

# Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew", pady=5) # Stretch to fill col 2

add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=10)

window.mainloop()
