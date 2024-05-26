from pathlib import Path
import sys
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, CENTER, NO, StringVar, OptionMenu
from QueriesAPI import QueriesAPI

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame10"

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
    y=256.0,
    width=201.0,
    height=42.0
)

# table
canvas.create_rectangle(
    276.0,
    218.0,
    770.0,
    480.0,
    fill="#F0F0F0",
    outline="")

table = ttk.Treeview()
table['columns'] = ('estab_id', 'estab_name', 'estab_desc', 'serv_mod', 'loc', 'contact')
table.column("#0", width=0,  stretch=NO)
table.column("estab_id",anchor=CENTER, width=20)
table.column("estab_name",anchor=CENTER,width=80)
table.column("estab_desc",anchor=CENTER,width=80)
table.column("serv_mod",anchor=CENTER,width=80)
table.column("loc",anchor=CENTER,width=80)
table.column("contact",anchor=CENTER,width=80)

table.heading("#0",text="",anchor=CENTER)
table.heading("estab_id",text="Id",anchor=CENTER)
table.heading("estab_name",text="Name",anchor=CENTER)
table.heading("estab_desc",text="Description",anchor=CENTER)
table.heading("serv_mod",text="Modes of Service",anchor=CENTER)
table.heading("loc",text="Location",anchor=CENTER)
table.heading("contact",text="Contact",anchor=CENTER)
table.place(
    x=276,
    y=218,
    width=494,
    height=262
)
db = QueriesAPI()
result = db.select_all_food_estabs()
for index,value in enumerate(result):
    table.insert(parent='',index='end',iid=index, text='', values=(value[0],value[2],value[1],value[5],value[4],value[3]))


canvas.create_rectangle(
    276.0,
    151.0,
    770.0,
    208.0,
    fill="#F0F0F0",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    432.0,
    187.0,
    image=entry_image_1
)

def clear_all(tableToClear):
   for item in tableToClear.get_children():
      tableToClear.delete(item)

sv = StringVar()
def update_table_search_id(*args):
    clear_all(table)
    result = db.select_food_estab_by_id(sv.get())
    for index,value in enumerate(result):
        table.insert(parent='',index='end',iid=index, text='', values=(value[0],value[2],value[1],value[5],value[4],value[3]))

sv.trace_add("write", callback=update_table_search_id)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=sv
)
entry_1.place(
    x=292.0,
    y=175.0,
    width=280.0,
    height=24.0
)

options = [
    "Filter",
    "Rating >= 4",
    "5",
    "4",
    "3",
    "2",
    "1",
]

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

clicked = StringVar()
clicked.set("Filter")
button_drop_3 = OptionMenu(canvas,
    clicked,
    *options
)
button_drop_3.configure(
    bd=0,
    activebackground="#FFFFFF",
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
button_drop_3.place(
    x=608.0,
    y=174.0,
    width=130.0,
    height=26.0
)
# button_3 = Button(
#     image=button_image_3,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_3 clicked"),
#     relief="flat"
# )
# button_3.place(
#     x=608.0,
#     y=174.0,
#     width=130.0,
#     height=26.0
# )

def on_button_4_click():
    print("button_4 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "DeleteEstab.py"], shell=True)
    process.wait()

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_4_click(),
    relief="flat"
)
button_4.place(
    x=620.0,
    y=104.0,
    width=150.0,
    height=30.0
)

def on_button_5_click():
    print("button_5 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "EditEstab.py"], shell=True)
    process.wait()

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_5_click(),
    relief="flat"
)
button_5.place(
    x=448.0,
    y=104.0,
    width=150.0,
    height=30.0
)

def on_button_6_click():
    print("button_6 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "AddEstab.py"], shell=True)
    process.wait()

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_6_click(),
    relief="flat"
)
button_6.place(
    x=276.0,
    y=104.0,
    width=150.0,
    height=30.0
)

canvas.create_rectangle(
    534.0,
    23.0,
    770.0,
    78.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    276.0,
    18.0,
    anchor="nw",
    text="Food\nEstablishments",
    fill="#D78521",
    font=("Inter Bold", 25 * -1)
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
    x=24.0,
    y=208.0,
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
    process = subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)
    process.wait()

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
    x=24.0,
    y=159.0,
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
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
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
    x=24.0,
    y=304.0,
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
    process = subprocess.Popen([sys.executable, "ReviewMenu.py"], shell=True)
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
    x=24.0,
    y=351.0,
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


canvas.create_text(
    287.0,
    159.0,
    anchor="nw",
    text="Search Establishment ID",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    609.0,
    159.0,
    anchor="nw",
    text="Filter by Rating",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
