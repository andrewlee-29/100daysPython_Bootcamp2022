DEFAULT_EMAIL = "Sample email"


from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list += [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    # print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # copy the password to clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(password)== 0 or len(website)== 0:
        messagebox.showwarning(message="You did not input the website or password. Please enter the info!!")
    else:
        is_ok =messagebox.askokcancel(title=website,message=f"Your username/email is : {username}\n Your passowrd is :{password} Do you want to save?")
        if is_ok:
            with open("data.txt","a")  as file:
                file.write(f"{website}|{username}|{password}\n ")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

#LockIcon
canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=1,column=2)

#Website label
website_label = Label(text="Website: ")
website_label.grid(row=2,column=1)

website_entry = Entry(width=35)
website_entry.grid(row=2,column=2,columnspan=2)
#select the entry when the app started
website_entry.focus()

#Email/username label
username_label = Label(text="Email/Username: ")
username_label.grid(row=3,column=1)

username_entry = Entry(width=35)
username_entry.grid(row=3,column=2,columnspan=2)
#insert the email
username_entry.insert(0,DEFAULT_EMAIL)
#Password Label
password_label = Label(text="Password: ")
password_label.grid(row=4,column=1)

password_entry = Entry(width=21)
password_entry.grid(row=4,column=2)

# generate button
generate_button = Button(text="Generate",width=10,command=generate_pw)
generate_button.grid(row=4,column=3)

# Add button
add_button = Button(text="Add",width=35,command=save_password)
add_button.grid(row=5,column=2)

window.mainloop()