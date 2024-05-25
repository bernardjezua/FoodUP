from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame11"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x500")
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
    background= '#DE1A1A',
    borderwidth=0,
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
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=23.0,
    y=354.0,
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
    x=22.0,
    y=207.0,
    width=201.0,
    height=42.0
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

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
    x=22.0,
    y=158.0,
    width=201.0,
    height=42.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

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
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=22.0,
    y=256.0,
    width=201.0,
    height=42.0
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

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
    y=305.0,
    width=201.0,
    height=42.0
)

button_image_hover_6 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

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


canvas.create_rectangle(
    282.0,
    222.0,
    776.0,
    478.0,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    282.0,
    149.0,
    776.0,
    212.0,
    fill="#F0F0F0",
    outline="")

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
    x=686.0,
    y=168.0,
    width=80.0,
    height=26.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    515.0,
    188.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=450.0,
    y=176.0,
    width=130.0,
    height=24.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    363.0,
    188.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=298.0,
    y=176.0,
    width=130.0,
    height=24.0
)

canvas.create_text(
    294.0,
    157.0,
    anchor="nw",
    text="Search Food ID",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    444.0,
    157.0,
    anchor="nw",
    text="Search Establishment ID",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    599.0,
    157.0,
    anchor="nw",
    text="View by",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

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
    x=626.0,
    y=102.0,
    width=150.0,
    height=30.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=454.0,
    y=102.0,
    width=150.0,
    height=30.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=282.0,
    y=102.0,
    width=150.0,
    height=30.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    658.0,
    48.0,
    image=image_image_2
)

canvas.create_text(
    282.0,
    31.0,
    anchor="nw",
    text="Reviews",
    fill="#D78521",
    font=("Inter Bold", 25 * -1)
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=596.0,
    y=175.0,
    width=80.0,
    height=25.736572265625
)
window.resizable(False, False)
window.mainloop()
