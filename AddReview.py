from pathlib import Path
import subprocess
import sys
from OperationFunctions import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from QueriesAPI import QueriesAPI


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/addreview"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
    background = "#DE1A1A",
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
#add review button
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: QueriesAPI().add_review(entry_3, entry_5, entry_4, entry_2, window),
    relief="flat"
)
button_2.place(
    x=372.0,
    y=393.0,
    width=299.0,
    height=49.0
)
def on_entry_1_click(): #back
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    736.9351196289062,
    53.5,
    image=entry_image_1
)
entry_1 = Button(
    image=entry_image_1,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=lambda: on_entry_1_click(),
    relief="flat"
)
entry_1.place(
    x=708.0,
    y=35.0,
    width=57.8702392578125,
    height=35.0
)

def on_button_3_click():
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=lambda: on_button_3_click(),
    relief="flat"
)
button_3.place(
    x=23.0,
    y=354.0,
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
    command=lambda:on_button_4_click(),
    relief="flat"
)
button_4.place(
    x=22.0,
    y=207.0,
    width=201.0,
    height=42.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

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
    window.destroy()
    process = subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)
    process.wait()
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=lambda: on_button_5_click(),
    relief="flat"
)
button_5.place(
    x=22.0,
    y=158.0,
    width=201.0,
    height=42.0
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

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

def on_button_6_click():
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
    command=lambda: on_button_6_click(),
    relief="flat"
)
button_6.place(
    x=22.0,
    y=256.0,
    width=201.0,
    height=42.0
)

button_image_hover_6 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_6_hover(e):
    button_6.config(
        image=button_image_hover_6
    )
def button_6_leave(e):
    button_6.config(
        image=button_image_6
    )

button_6.bind('<Enter>', button_6_hover)
button_6.bind('<Leave>', button_6_leave)

def on_button_7_click():
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
    process.wait()
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=lambda: on_button_7_click(),
    relief="flat"
)
button_7.place(
    x=22.0,
    y=305.0,
    width=201.0,
    height=42.0
)

button_image_hover_7 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

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


entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    521.5,
    324.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=377.0,
    y=288.0,
    width=289.0,
    height=71.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    521.5,
    103.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=377.0,
    y=79.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    373.0,
    60.0,
    anchor="nw",
    text="Rating",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    373.0,
    269.0,
    anchor="nw",
    text="Review",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    521.5,
    243.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=377.0,
    y=219.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    373.0,
    199.0,
    anchor="nw",
    text="Establishment ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    521.5,
    173.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=377.0,
    y=149.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    373.0,
    130.0,
    anchor="nw",
    text="Food ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
