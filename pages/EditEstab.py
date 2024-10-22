from pathlib import Path
import sys
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, StringVar
from QueriesAPI import QueriesAPI

db = QueriesAPI()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/editestab"

def on_button_3_click():
    print("button_3 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/DashboardPage.py"], shell=True)
    process.wait()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("GROUP 1 Food & Restaurant Review Application")

eid = StringVar()
ename = StringVar()
edesc = StringVar()
eloc = StringVar()
eservmod = StringVar()
econtact = StringVar()

estab_id = None

def maintainId(*args):
    if(estab_id != None and eid.get() != estab_id and estab_id != ''):
        eid.set(estab_id)

def setId(*args):
    eid.set(estab_id)

eid.trace_add("write", callback=maintainId)
ename.trace_add("write", callback=setId)
edesc.trace_add("write", callback=setId)
eloc.trace_add("write", callback=setId)
eservmod.trace_add("write", callback=setId)
econtact.trace_add("write", callback=setId)

def resetEntries():
    ename.set('')
    edesc.set('')
    eloc.set('')
    eservmod.set('')
    econtact.set('')

def search_button_click():
    if(eid.get().isnumeric()):
        global estab_id
        estab_id = eid.get()
        result = db.select_food_estab_by_id(eid.get())
        if(len(result) == 0):
            resetEntries()
            messagebox.showerror("Search Error", "No establishment with specified ID found")
        else:
            resetEntries()
            messagebox.showinfo("Establishment ID Found", "Matched query results to Establishment ID!")
            ename.set(result[0][2])  # Name
            edesc.set(result[0][1])  # Description
            eloc.set(result[0][4])  # Location
            eservmod.set(result[0][5])  # Modes of Service
            econtact.set(result[0][3])  # Contact
    else:
        messagebox.showinfo("Invalid Input!", "Please check all fields!")
        

def edit_button_click():
    if(eid.get() != "" and ename.get() != "" and edesc.get() != "" and eloc.get() != "" and eservmod.get() != "" and econtact.get() != "" and eid.get().isnumeric()):
        locList = eloc.get().split(",")
        servModList = eservmod.get().split(",")
        contactList = econtact.get().split(",")
        result = db.update_food_estab_by_id(estab_id, ename.get(), edesc.get(), locList, servModList, contactList)
        window.destroy()
        process = subprocess.Popen([sys.executable, "./pages/ViewEstab.py"], shell=True)
        process.wait()
    else:
        messagebox.showinfo("Invalid Input", "Please check all fields!")
    

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

edit_button_image = PhotoImage(
    file=relative_to_assets("button_1.png"))
edit_button = Button(
    image=edit_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: edit_button_click(),
    relief="flat"
)
edit_button.place(
    x=372.0,
    y=439.0,
    width=299.0,
    height=49.0
)

def on_button_2_click():
    print("button_2 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/ViewEstab.py"], shell=True)
    process.wait()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_2_click,
    relief="flat"
)
button_2.place(
    x=703.0,
    y=35.0,
    width=67.8702392578125,
    height=37.0
)

canvas.create_text(
    374.0,
    355.0,
    anchor="nw",
    text="Contact Details",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    374.0,
    289.0,
    anchor="nw",
    text="Modes of Service (Dine In, Take Out, Delivery, Pickup)",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    375.0,
    223.0,
    anchor="nw",
    text="Location",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

# Establishment id
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    482.5,
    60.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=eid
)
entry_6.place(
    x=379.0,
    y=36.0,
    width=207.0,
    height=47.0
)

# Modes of Service
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    523.5,
    330.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=eservmod
)
entry_1.place(
    x=379.0,
    y=306.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    375.0,
    157.0,
    anchor="nw",
    text="Establishment description",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    375.0,
    89.0,
    anchor="nw",
    text="Establishment name",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

# Establishment Name
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    523.5,
    132.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=ename
)
entry_2.place(
    x=379.0,
    y=108.0,
    width=289.0,
    height=47.0
)

# Establishment Description
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    523.5,
    198.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=edesc
)
entry_3.place(
    x=379.0,
    y=174.0,
    width=289.0,
    height=47.0
)

canvas.create_text(
    387.0,
    425.0,
    anchor="nw",
    text="*  Separate multiple values with commas e.g. Take Out,Dine In",
    fill="#B0A6BF",
    font=("Inter Bold", 9 * -1)
)

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

# Location
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    523.5,
    264.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=eloc
)
entry_4.place(
    x=379.0,
    y=240.0,
    width=289.0,
    height=47.0
)

def on_button_4_click():
    print("button_4 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/ViewEstab.py"], shell=True)
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
    x=23.0,
    y=256.0,
    width=201.0,
    height=42.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    background="#DE1A1A",
    highlightthickness=0,
    command=lambda: QueriesAPI().logout(),
    relief="flat"
)
button_5.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    123.0,
    84.0,
    image=image_image_1
)

# Contact Details
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    523.5,
    396.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    highlightthickness=0,
    textvariable=econtact
)
entry_5.place(
    x=379.0,
    y=372.0,
    width=289.0,
    height=47.0
)

def on_button_6_click():
    print("button_6 clicked")
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/ProfilePage.py"], shell=True)
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
    y=208.0,
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
    process = subprocess.Popen([sys.executable, "./pages/ViewFood.py"], shell=True)
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
    y=304.0,
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
    process = subprocess.Popen([sys.executable, "./pages/ViewReview.py"], shell=True)
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
    y=351.0,
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
    376.0,
    17.0,
    anchor="nw",
    text="Establishment id",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

search_button_image = PhotoImage(
    file=relative_to_assets("button_9.png"))
search_button = Button(
    image=search_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: search_button_click(),
    relief="flat"
)
search_button.place(
    x=603.0,
    y=42.0,
    width=67.8702392578125,
    height=37.0
)

window.resizable(False, False)
window.mainloop()
