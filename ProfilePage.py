import multiprocessing
from pathlib import Path
import sys
import subprocess
import mysql.connector
from QueriesAPI import QueriesAPI
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame3"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Define a function for logout
def logout():
    # children = multiprocessing.active_children()
    # print(children)
    # for child in children:
    #     child.terminate()
    window.destroy() 
    subprocess.Popen([sys.executable, "LoginPage.py"], shell=True)

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
    246.0,
    500.0,
    fill="#DE1A1A",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    123.0,
    84.0,
    image=image_image_1
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
    x=23.0,
    y=207.0,
    width=201.0,
    height=42.0
)

button_image_hover_1 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(
        image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
        image=button_image_1
    )

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)

def on_button_2_click():
    print("button_2 clicked")
    window.destroy()
    subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)
    

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_2_click,
    relief="flat"
)
button_2.place(
    x=23.0,
    y=158.0,
    width=201.0,
    height=42.0
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)

def on_button_3_click():
    print("button_3 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
    process.wait()

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_3_click,
    relief="flat"
)
button_3.place(
    x=23.0,
    y=256.0,
    width=201.0,
    height=42.0
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


def on_button_4_click():
    print("button_4 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
    process.wait()

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_4_click,
    relief="flat"
)
button_4.place(
    x=23.0,
    y=303.0,
    width=201.0,
    height=42.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)

def on_button_5_click():
    print("button_5 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_5_click,
    relief="flat"
)
button_5.place(
    x=23.0,
    y=350.0,
    width=201.0,
    height=42.0
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_5.png"))

def button_5_hover(e):
    button_5.config(
        image=button_image_hover_5
    )
def button_5_leave(e):
    button_5.config(
        image=button_image_5
    )

button_5.bind('<Enter>', button_5_hover)
button_5.bind('<Leave>', button_5_leave)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    #command=lambda: print("button_6 clicked"),
    command=logout,
    relief="flat"
)
button_6.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
)

canvas.create_text(
    279.0,
    41.0,
    anchor="nw",
    text="My Profile",
    fill="#D78521",
    font=("Inter Bold", 32 * -1)
)

# Initialize QueriesAPI and get the logged-in user's email
queries_api = QueriesAPI()


# Fetch user details and display them
user_details = queries_api.fetch_user_details()
print("User details:", user_details)
if user_details:
    real_name = user_details[0][2]
    username = user_details[0][1]
    email = user_details[0][0]
    label_real_name = Label(window, text=f"Name: {real_name}", bg="#DE1A1A", font=("Inter", 14))
    label_real_name.place(x=279, y=100)

    label_username = Label(window, text=f"Username: {username}", bg="#DE1A1A", font=("Inter", 14))
    label_username.place(x=279, y=140)

    label_email = Label(window, text=f"Email: {email}", bg="#DE1A1A", font=("Inter", 14))
    label_email.place(x=279, y=180)
else:
    label_no_user = Label(window, text="No user details found.", bg="#DE1A1A", font=("Inter", 14))
    label_no_user.place(x=279, y=100)

window.resizable(False, False)
window.mainloop()