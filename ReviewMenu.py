from pathlib import Path
import sys
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame15"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
    x=299.0,
    y=107.0,
    width=201.0,
    height=42.0
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
    x=540.0,
    y=107.0,
    width=201.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=540.0,
    y=158.0,
    width=201.0,
    height=42.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=299.0,
    y=158.0,
    width=201.0,
    height=42.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=23.0,
    y=350.0,
    width=201.0,
    height=42.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    background="#DE1A1A",
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
)

canvas.create_text(
    299.0,
    45.0,
    anchor="nw",
    text="Reviews",
    fill="#D78521",
    font=("Inter Bold", 32 * -1)
)

def on_button_7_click():
    print("button_7 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ProfilePage.py"], shell=True)
    process.wait()

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_7_click,
    relief="flat"
)
button_7.place(
    x=22.0,
    y=203.0,
    width=201.0,
    height=42.0
)

button_image_hover_7 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_7_hover(e):
    button_7.config(
        image=button_image_hover_7
    )
def button_7_leave(e):
    button_7.config(
        image=button_image_7
    )

button_7.bind('<Enter>', button_7_hover)
button_7.bind('<Leave>', button_7_leave)

def on_button_8_click():
    print("button_8 clicked")
    window.destroy()

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_8_click,
    relief="flat"
)
button_8.place(
    x=22.0,
    y=154.0,
    width=201.0,
    height=42.0
)

button_image_hover_8 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_8_hover(e):
    button_8.config(
        image=button_image_hover_8
    )
def button_8_leave(e):
    button_8.config(
        image=button_image_8
    )

button_8.bind('<Enter>', button_8_hover)
button_8.bind('<Leave>', button_8_leave)

def on_button_9_click():
    print("button_9 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
    process.wait()

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_9_click,
    relief="flat"
)
button_9.place(
    x=22.0,
    y=252.0,
    width=201.0,
    height=42.0
)

button_image_hover_9 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_9_hover(e):
    button_9.config(
        image=button_image_hover_9
    )
def button_9_leave(e):
    button_9.config(
        image=button_image_9
    )

button_9.bind('<Enter>', button_9_hover)
button_9.bind('<Leave>', button_9_leave)

def on_button_10_click():
    print("button_10 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
    process.wait()

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_10_click,
    relief="flat"
)
button_10.place(
    x=22.0,
    y=301.0,
    width=201.0,
    height=42.0
)

button_image_hover_10 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

def button_10_hover(e):
    button_10.config(
        image=button_image_hover_10
    )
def button_10_leave(e):
    button_10.config(
        image=button_image_10
    )

button_10.bind('<Enter>', button_10_hover)
button_10.bind('<Leave>', button_10_leave)

window.resizable(False, False)
window.mainloop()
