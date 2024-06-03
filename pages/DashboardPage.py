from pathlib import Path
import sys
import os
import subprocess
import mysql.connector
from QueriesAPI import QueriesAPI

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame2"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("GROUP 1 Food & Restaurant Review Application")

w = 800  # width for the Tk root
h = 500  # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth()  # width of the screen
hs = window.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.configure(bg = "#DE1A1A")

canvas = Canvas(
    window,
    bg = "#DE1A1A",
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
    800.0,
    500.0,
    fill="#DE1A1A",
    outline="")

def on_button_1_click():
    print("button_1 clicked")
    window.withdraw()
    process = subprocess.Popen([sys.executable, "ProfilePage.py"], shell=True)
    process.wait()
    window.wm_deiconify()
    window.destroy()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    bg="#D78521",
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_1_click, 
    relief="flat"
)
button_1.place(
    x=86.0,
    y=190.0,
    width=308.0,
    height=111.0
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
    window.withdraw()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()
    window.wm_deiconify()
    window.destroy()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    bg="#D78521",
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_2_click,
    relief="flat"
)
button_2.place(
    x=406.0,
    y=313.0,
    width=308.0,
    height=111.0
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
    window.withdraw()
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
    process.wait()
    window.wm_deiconify()
    window.destroy()

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    bg="#D78521",
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_3_click,
    relief="flat"
)
button_3.place(
    x=86.0,
    y=313.0,
    width=308.0,
    height=111.0
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
    window.withdraw()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
    process.wait()
    window.wm_deiconify()
    window.destroy()

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))

button_4 = Button(
    image=button_image_4,
    bg="#D78521",
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_4_click,
    relief="flat"
)
button_4.place(
    x=406.0,
    y=190.0,
    width=308.0,
    height=111.0
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


button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    bg = "#DE1A1A",
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    #command=lambda: print("button_5 clicked"),
    command=lambda: QueriesAPI().logout(),
    relief="flat"
)
button_5.place(
    x=37.0,
    y=451.0,
    width=75.0,
    height=19.354839324951172
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    275.0,
    103.0,
    image=image_image_1
)

canvas.create_text(
    345.0,
    76.0,
    anchor="nw",
    text="Dashboard",
    fill="#FFFFFF",
    font=("Inter Black", 39 * -1)
)


window.resizable(False, False)
window.mainloop()