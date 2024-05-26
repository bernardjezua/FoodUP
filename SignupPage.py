from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame1"


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
    command=lambda: print("button_1 clicked"),
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
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=9.0,
    y=18.0,
    width=106.0,
    height=44.0
)

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
    highlightthickness=0
)
entry_3.place(
    x=418.0,
    y=327.0,
    width=289.0,
    height=47.0
)

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
