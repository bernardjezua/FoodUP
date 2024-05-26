from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame16"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


sort = Tk()

sort.geometry("287x222")
sort.configure(bg = "#FFFFFF")


canvas = Canvas(
    sort,
    bg = "#FFFFFF",
    height = 222,
    width = 287,
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
    x=156.0,
    y=176.0,
    width=118.0,
    height=26.0
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
    x=19.0,
    y=176.0,
    width=118.0,
    height=26.0
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
    x=80.000244140625,
    y=89.0,
    width=129.999755859375,
    height=26.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    180.0,
    140.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=155.0,
    y=128.0,
    width=50.0,
    height=24.0
)



canvas.create_text(
    142.0,
    133.0,
    anchor="nw",
    text="-",
    fill="#DE1A1A",
    font=("Inter Bold", 11 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    110.0,
    140.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=85.0,
    y=128.0,
    width=50.0,
    height=24.0
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
    x=80.0,
    y=52.0,
    width=130.0,
    height=26.0
)

canvas.create_text(
    88.0,
    17.0,
    anchor="nw",
    text="Sort Price by",
    fill="#D78521",
    font=("Inter Bold", 18 * -1)
)
sort.resizable(False, False)
sort.mainloop()
