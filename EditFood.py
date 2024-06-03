from pathlib import Path
import sys, subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, messagebox

from QueriesAPI import QueriesAPI


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/editfood"


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
    background="#DE1A1A",
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
#edit button

def edit_button_click():
    if(entry_6.get() != "" and fname.get() != "" and fprice.get() != "" and ftype.get() != "" and estid.get() != "" and fdesc.get() != "" and entry_6.get().isnumeric() and estid.get().isnumeric()):
        QueriesAPI().update_food_item(entry_6.get(), fname.get(), fprice.get(), ftype.get(), estid.get(), fdesc.get())
        window.destroy()
        process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
        process.wait()
    else:
        messagebox.showinfo("Invalid Input", "Please check all fields!")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: edit_button_click(),
    relief="flat"
)
button_2.place(
    x=372.0,
    y=431.0,
    width=299.0,
    height=49.0
)

def on_button_3_click():
    print("button_3 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
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
    x=703.0,
    y=35.0,
    width=67.8702392578125,
    height=37.0
)

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
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_4_click,
    relief="flat"
)
button_4.place(
    x=24.0,
    y=305.0,
    width=201.0,
    height=42.0
)

def on_button_5_click():
    print("button_5 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ProfilePage.py"], shell=True)
    process.wait()

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_5_click,
    relief="flat"
)
button_5.place(
    x=24.0,
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

def on_button_6_click():
    window.destroy()
    process = subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)
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
    x=24.0,
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
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_7_click,
    relief="flat"
)
button_7.place(
    x=24.0,
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

def on_button_8_click():
    print("button_8 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
    process.wait()

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=on_button_8_click,
    relief="flat"
)
button_8.place(
    x=24.0,
    y=353.0,
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


canvas.create_text(
    372.0,
    221.0,
    anchor="nw",
    text="Food type (Breakfast, Lunch, Dinner)",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    373.0,
    157.0,
    anchor="nw",
    text="Price",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

fname = StringVar()
fprice = StringVar()
ftype = StringVar()
estid = StringVar()
fdesc = StringVar()

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    521.5,
    197.5,
    image=entry_image_1
)
#food price field
entry_1 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=fprice
)
entry_1.place(
    x=377.0,
    y=173.0,
    width=289.0,
    height=47.0
    
)
#food desc field
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    521.5,
    263.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=ftype
)
entry_2.place(
    x=377.0,
    y=239.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    373.0,
    352.0,
    anchor="nw",
    text="Food description",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    373.0,
    90.0,
    anchor="nw",
    text="Food name",
    fill="#D78521",
    font=("Inter", 14 * -1)
)
#foodname field
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    521.5,
    133.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=fname
)
entry_3.place(
    x=377.0,
    y=109.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    372.0,
    288.0,
    anchor="nw",
    text="Establishment ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

#estab id field
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    521.5,
    328.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=estid
)
entry_4.place(
    x=377.0,
    y=304.0,
    width=289.0,
    height=47.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    521.5,
    393.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=fdesc
)
entry_5.place(
    x=377.0,
    y=369.0,
    width=289.0,
    height=47.0
)
#SEARCH BUTTON

def searchfood():
    if(entry_6.get().isnumeric()):
        result = QueriesAPI().select_food_item_byid(entry_6.get())
        if result != []:
            print(result)
            fname.set(result[0][0])
            fprice.set(result[0][2])
            ftype.set(result[0][3])
            estid.set(result[0][4])
            fdesc.set(result[0][1])
        else:
            fname.set('')
            fprice.set('')
            ftype.set('')
            estid.set('')
            fdesc.set('')
            messagebox.showinfo("Food Not Found", "No food item was found with the given id!")
    else:
        messagebox.showinfo("Invalid Input!", "Please check all fields!")



button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: searchfood(),
    relief="flat"
)
button_9.place(
    x=601.0,
    y=48.0,
    width=67.8702392578125,
    height=37.0
)
#search field
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    480.5,
    66.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=377.0,
    y=42.0,
    width=207.0,
    height=47.0
)

canvas.create_text(
    373.0,
    23.0,
    anchor="nw",
    text="Food ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)
window.resizable(False, False)
window.mainloop()