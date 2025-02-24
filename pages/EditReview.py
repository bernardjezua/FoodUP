from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import subprocess
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, messagebox
from QueriesAPI import QueriesAPI

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/editreview"


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

def on_button_2_click():
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/ViewReview.py"], shell=True)
    process.wait()
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button_2_click(),
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

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    background="#DE1A1A",
    highlightthickness=0,
    command=lambda: QueriesAPI().logout(),
    relief="flat"
)
button_4.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
)

def on_button_5_click():
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/ViewReview.py"], shell=True)
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
    x=23.0,
    y=354.0,
    width=201.0,
    height=42.0
)
def on_button_6_click():
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
    command=lambda: on_button_6_click(),
    relief="flat"
)
button_6.place(
    x=22.0,
    y=207.0,
    width=201.0,
    height=42.0
)

button_image_hover_6 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

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
    process = subprocess.Popen([sys.executable, "./pages/DashboardPage.py"], shell=True)
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
    y=158.0,
    width=201.0,
    height=42.0
)

button_image_hover_7 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

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
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/ViewEstab.py"], shell=True)
    process.wait()

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=lambda: on_button_8_click(),
    relief="flat"
)
button_8.place(
    x=22.0,
    y=256.0,
    width=201.0,
    height=42.0
)

button_image_hover_8 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

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
    window.destroy()
    process = subprocess.Popen([sys.executable, "./pages/ViewFood.py"], shell=True)
    process.wait()
button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    background = "#DE1A1A",
    highlightthickness=0,
    command=lambda: on_button_9_click(),
    relief="flat"
)
button_9.place(
    x=22.0,
    y=305.0,
    width=201.0,
    height=42.0
)

button_image_hover_9 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

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

revid = StringVar()
eid = StringVar()
fid = StringVar()
rating = StringVar()
reviewdesc = StringVar()

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    525.5,
    366.5,
    image=entry_image_1
)
review_entry = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    textvariable=reviewdesc,
    highlightthickness=0
)
review_entry.place(
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
food_id_entry = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    textvariable=fid,
    highlightthickness=0
)
food_id_entry.place(
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
estab_id_entry = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    textvariable=eid,
    highlightthickness=0
)
estab_id_entry.place(
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

canvas.create_text(
    377.0,
    311.0,
    anchor="nw",
    text="Review",
    fill="#D78521",
    font=("Inter", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    525.5,
    285.5,
    image=entry_image_4
)
rating_entry = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    textvariable=rating,
    highlightthickness=0
)
rating_entry.place(
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

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    483.5,
    77.5,
    image=entry_image_5
)
review_id_entry = Entry(
    bd=0,
    bg="#F2D398",
    fg="#000716",
    textvariable=revid,
    highlightthickness=0
)
review_id_entry.place(
    x=380.0,
    y=53.0,
    width=207.0,
    height=47.0
)

def maintainId(*args):
    if(global_reviewid != None and revid.get() != global_reviewid and global_reviewid != ''):
        revid.set(global_reviewid)

def setId(*args):
    revid.set(global_reviewid)

revid.trace_add("write", callback=maintainId)
rating.trace_add("write", callback=setId)
reviewdesc.trace_add("write", callback=setId)
eid.trace_add("write", callback=setId)
fid.trace_add("write", callback=setId)

# SEARCH FUNCTION
global_reviewid = None
def search_review():
    if(revid.get().isnumeric()):
        global global_reviewid
        global_reviewid = revid.get()
        result = QueriesAPI().select_review_by_id(global_reviewid)
        if result != []:
            print(result)
            revid.set(result[0][0])
            rating.set(result[0][1])
            reviewdesc.set(result[0][2])
            print(type(result[0][3]), type(result[0][4]))
            if isinstance(result[0][3], type(None)):
                eid.set('')
            else:
                eid.set(result[0][3])
            if isinstance(result[0][4], type(None)):
                fid.set('')
            else:
                fid.set(result[0][4])
            messagebox.showinfo("Review ID Found", "Matched query results to Review ID!")
        else:
            revid.set('')
            rating.set('')
            reviewdesc.set('')
            eid.set('')
            fid.set('')
            messagebox.showinfo("Review Not Found", "No review was found with the given id!")
    else:
        messagebox.showinfo("Invalid Input!", "Please check all fields!")

#search button
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
search_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: search_review(),
    relief="flat"
)
search_button.place(
    x=604.0,
    y=59.0,
    width=67.8702392578125,
    height=37.0
)

def edit_button_click():
    # Get the values from the StringVars
    new_rating = rating.get()
    new_review_text = reviewdesc.get()
    estab_id = eid.get()
    food_id = fid.get()

    if not new_rating.isdigit() or int(new_rating) < 1 or int(new_rating) > 5:
        messagebox.showinfo("Invalid Input!", "Rating entry must be 1-5 only.")
    elif not (food_id.isdigit() or estab_id.isdigit()):
        messagebox.showinfo("Invalid Input!", "Either Food ID or Establishment ID must be present.")
    elif not new_review_text.strip():
        messagebox.showinfo("Invalid Input!", "Review cannot be empty.")
    else:
        QueriesAPI().update_review(global_reviewid, new_rating, new_review_text, estab_id, food_id)
        revid.set(global_reviewid)
        window.destroy()
        process = subprocess.Popen([sys.executable, "./pages/ViewReview.py"], shell=True)
        process.wait()

#edit button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: edit_button_click(),
    relief="flat"
)
button_1.place(
    x=374.0,
    y=417.0,
    width=299.0,
    height=49.0
)

canvas.create_text(
    376.0,
    34.0,
    anchor="nw",
    text="Review ID",
    fill="#D78521",
    font=("Inter", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
