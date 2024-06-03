from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import mysql.connector
import subprocess
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from QueriesAPI import QueriesAPI, DuplicateEmailError

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame1"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_account():
    name = entry_1.get()
    username = entry_2.get()
    email = entry_4.get()
    password = entry_3.get()

    # Check if any of the required fields are empty
    if not (name and username and email and password):
        messagebox.showerror("Missing Information", "Please fill in all required fields.")
        return

    # Checking if '@' is present in the email
    if '@' not in email:
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return
    
    try:
        api.create_account(email, name, username, password, window)
    except DuplicateEmailError as e:
        messagebox.showerror("Duplicate Email", str(e))
    except mysql.connector.errors.IntegrityError as e:
        if e.errno == 1062:  # Duplicate entry error
            messagebox.showerror("Duplicate Email", "The email address you provided is already registered. Please use a different email address.")
        else:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"An error occurred: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def go_back_to_login():
    window.destroy()
    subprocess.Popen([sys.executable, "LoginPage.py"], shell=True)

api = QueriesAPI()

window = Tk()
window.title("GROUP 1 Food & Restaurant Review Application")

w = 800
h = 500 

# get screen width and height
ws = window.winfo_screenwidth() 
hs = window.winfo_screenheight()

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    332.0,
    500.0,
    fill="#DE1A1A",
    outline="")

canvas.create_text(
    100.0,
    150.0,
    anchor="nw",
    text="Welcome to",
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    162.0,
    270.0,
    image=image_image_1
)

canvas.create_text(
    525,
    31.0,
    anchor="nw",
    text="Sign up",
    fill="#D78521",
    font=("Inter Bold", 22 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    #command=lambda: QueriesAPI().create_account(entry_4.get(), entry_2.get(), entry_1.get(), entry_3.get(), window),
    command=create_account,
    relief="flat"
)
button_1.place(
    x=413.0,
    y=409.0,
    width=299.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    bg = "#DE1A1A",
    borderwidth=0,
    highlightthickness=0,
    #command=lambda: print("button_2 clicked"),
    command=go_back_to_login,
    relief="flat"
)
button_2.place(
    x=9.0,
    y=18.0,
    width=106.0,
    height=44.0
)

# Name
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    562.5,
    197.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=418.0,
    y=173.0,
    width=289.0,
    height=47.0
)

# Username entry
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    562.5,
    120.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=418.0,
    y=96.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    414.0,
    77.0,
    anchor="nw",
    text="Name",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    414.0,
    154.0,
    anchor="nw",
    text="Username",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

# PASSWORD entry
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    562.5,
    351.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_3.place(
    x=418.0,
    y=327.0,
    width=289.0,
    height=47.0
)

# EMAIL entry
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    562.5,
    274.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=418.0,
    y=250.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    414.0,
    231.0,
    anchor="nw",
    text="Email",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    413.0,
    308.0,
    anchor="nw",
    text="Password",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

window.resizable(False, False)
window.mainloop()