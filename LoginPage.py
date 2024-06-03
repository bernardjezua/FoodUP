from multiprocessing import process
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import subprocess
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from QueriesAPI import QueriesAPI

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login():
    email = entry_2.get()
    password = entry_1.get()
    if not email or not password:
        messagebox.showerror("Input Error", "Please enter both email and password")
    else:
        api.verify_credentials(email, password, window)

def open_signup():
    window.destroy()
    subprocess.Popen([sys.executable, "SignupPage.py"], shell=True)
    process.wait()
    window.wm_deiconify()
    #SignupPage.main()

api = QueriesAPI()

window = Tk()

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
    20.0,
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
    540,
    81.0,
    anchor="nw",
    text="Login",
    fill="#D78521",
    font=("Inter Bold", 22 * -1)
)

canvas.create_rectangle(
    413.0,
    171.0,
    712.0,
    220.0,
    fill="#F2D398",
    outline="")

# PASSWORD entry
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    562.5,
    272.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_1.place(
    x=418.0,
    y=248.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    432.0,
    187.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=413.0,
    y=376.0,
    width=299.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=345.0,
    y=432.0,
    width=435.0,
    height=33.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    332.0,
    500.0,
    fill="#DE1A1A",
    outline="")

canvas.create_text(
    105,
    150.0,
    anchor="nw",
    text="Welcome to",
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    162.0,
    270.0,
    image=image_image_2
)

# EMAIL entry
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    562.5,
    195.5,
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
    y=171.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    414.0,
    152.0,
    anchor="nw",
    text="Email",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    413.0,
    229.0,
    anchor="nw",
    text="Password",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
#Login BUTTON
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    #command=lambda: QueriesAPI().verify_credentials(entry_2.get(), entry_1.get(), window),
    command=login,
    relief="flat"
)

button_1.place(
    x=413.0,
    y=376.0,
    width=299.0,
    height=49.0
)

# Sign-up button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    background= "#FFFFFF",
    highlightthickness=0,
    #command=lambda: print("button_4 clicked"),
    command=open_signup,
    relief="flat"
)
button_2.place(
    x=345.0,
    y=432.0,
    width=435.0,
    height=33.0
)
# def printRes():
#     print(f'''email:{}\npassword:{}''')
window.resizable(False, False)
window.mainloop()