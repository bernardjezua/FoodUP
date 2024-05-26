from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame13"


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
    x=374.0,
    y=417.0,
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
    x=703.0,
    y=35.0,
    width=67.8702392578125,
    height=37.0
)

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

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    background="#DE1A1A",
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
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
    x=23.0,
    y=354.0,
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
    x=22.0,
    y=207.0,
    width=201.0,
    height=42.0
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

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
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=22.0,
    y=158.0,
    width=201.0,
    height=42.0
)

button_image_hover_6 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

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


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=22.0,
    y=256.0,
    width=201.0,
    height=42.0
)

button_image_hover_7 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

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


button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=22.0,
    y=305.0,
    width=201.0,
    height=42.0
)

button_image_hover_8 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

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


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    525.5,
    366.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=381.0,
    y=330.0,
    width=289.0,
    height=71.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    525.5,
    216.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=381.0,
    y=192.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    377.0,
    173.0,
    anchor="nw",
    text="Food ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    524.5,
    147.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=380.0,
    y=123.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    376.0,
    104.0,
    anchor="nw",
    text="Establishment ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    524.5,
    78.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=380.0,
    y=54.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    376.0,
    35.0,
    anchor="nw",
    text="Review ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    377.0,
    311.0,
    anchor="nw",
    text="Review",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    525.5,
    285.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=381.0,
    y=261.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    377.0,
    242.0,
    anchor="nw",
    text="Rating",
    fill="#D78521",
    font=("Inter", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
