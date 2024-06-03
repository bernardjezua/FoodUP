from pathlib import Path
import subprocess
import sys
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, END
from QueriesAPI import QueriesAPI

db = QueriesAPI()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame4"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def delete_button_clicked():
    if(entry_1.get() == ''):
        messagebox.showerror("Delete Error", "Enter Establishment ID first")
        return
    db.delete_food_estab_by_id(entry_1.get())
    entry_1.delete(0, END)


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
    246.0,
    500.0,
    fill="#DE1A1A",
    outline="")

def on_button_1_click():
    print("button_1 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_1_click,
    relief="flat"
)
button_1.place(
    x=24.0,
    y=351.0,
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
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
    process.wait()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_2_click,
    relief="flat"
)
button_2.place(
    x=24.0,
    y=304.0,
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
    process = subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)
    process.wait()

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_3_click,
    relief="flat"
)
button_3.place(
    x=24.0,
    y=159.0,
    width=201.0,
    height=42.0
)

def on_button_4_click():
    print("button_4 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ProfilePage.py"], shell=True)
    process.wait()

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_4_click,
    relief="flat"
)
button_4.place(
    x=24.0,
    y=208.0,
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
    borderwidth=0,
    background="#DE1A1A",
    highlightthickness=0,
    command=lambda: db.logout(),
    relief="flat"
)
button_5.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
)

def on_button_6_click():
    print("button_6 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
    process.wait()

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_6_click,
    relief="flat"
)
button_6.place(
    x=23.0,
    y=256.0,
    width=201.0,
    height=42.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    123.0,
    84.0,
    image=image_image_1
)

canvas.create_text(
    374.0,
    157.0,
    anchor="nw",
    text="Establishment id",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    522.5,
    200.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=378.0,
    y=176.0,
    width=289.0,
    height=47.0
)

def on_button_7_click():
    print("button_7 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
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
    x=703.0,
    y=35.0,
    width=67.8702392578125,
    height=37.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: delete_button_clicked(),
    relief="flat"
)
button_8.place(
    x=372.0,
    y=254.0,
    width=299.0,
    height=49.0
)
window.resizable(False, False)
window.mainloop()
