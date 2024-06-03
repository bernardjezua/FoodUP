from pathlib import Path
import re, sys, subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, CENTER, NO, StringVar, OptionMenu, font
from QueriesAPI import QueriesAPI


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame11"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

view_review = Tk()

w = 800
h = 500 

# get screen width and height
ws = view_review.winfo_screenwidth() 
hs = view_review.winfo_screenheight()

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
view_review.geometry('%dx%d+%d+%d' % (w, h, x, y))
view_review.configure(bg = "#FFFFFF")

canvas = Canvas(
    view_review,
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
    #command=lambda: print("button_1 clicked"),
    command=lambda: QueriesAPI().logout(view_review),
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
    background = "#DE1A1A",
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

def on_button_3_click():
    print("button_3 clicked")
    view_review.destroy()
    process = subprocess.Popen([sys.executable, "ProfilePage.py"], shell=True)
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


table = ttk.Treeview()
table['columns'] = ('review_id', 'rating', 'rev_date', 'rev_stat', 'email', 'estab_id', 'food_id')
table.column("#0", width=0,  stretch=NO)
table.column("review_id",anchor=CENTER,width=40)
table.column("rating",anchor=CENTER,minwidth=50)
table.column("rev_date",anchor=CENTER,minwidth=90)
table.column("rev_stat",anchor=CENTER,minwidth=50)
table.column("email",anchor=CENTER,minwidth=70)
table.column("estab_id",anchor=CENTER,minwidth=90)
table.column("food_id",anchor=CENTER,minwidth=90)

# Scrollbars
horzScrollBar = ttk.Scrollbar(view_review, orient ="horizontal", command = table.xview)
horzScrollBar.place(
    x=276,
    y=480,
    width=494,
    height=20
)
vertScrollBar = ttk.Scrollbar(view_review, orient ="vertical", command = table.yview)
vertScrollBar.place(
    x=770,
    y=218,
    width=20,
    height=262
)
table.configure(xscrollcommand = horzScrollBar.set)
table.configure(yscrollcommand = vertScrollBar.set)

table.bind('<Button-1>', 'break')
table.heading("#0",text="",anchor=CENTER)
table.heading("review_id",text="Id",anchor=CENTER)
table.heading("rating",text="Rating",anchor=CENTER)
table.heading("rev_date",text="Date",anchor=CENTER)
table.heading("rev_stat",text="Review",anchor=CENTER)
table.heading("email",text="Email",anchor=CENTER)
table.heading("estab_id",text="Establishment Name",anchor=CENTER)
table.heading("food_id",text="Food Name",anchor=CENTER)
table.place(
    x=276,
    y=218,
    width=494,
    height=262
)

db = QueriesAPI()
result = db.select_all_food_reviews()
for index,value in enumerate(result):
    table.insert(parent='',index='end',iid=index, text='', values=(value[0],value[1],value[2],value[3], value[4], value[5], value[6]))

def on_button_4_click():
    print("button_4 clicked")
    view_review.destroy()
    subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)

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

def on_button_5_click():
    print("button_5 clicked")
    view_review.destroy()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
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


def on_button_6_click():
    print("button_6 clicked")
    view_review.destroy()
    process = subprocess.Popen([sys.executable, "ViewFood.py"], shell=True)
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

def clear_all(tableToClear):
   for item in tableToClear.get_children():
      tableToClear.delete(item)


fiv = StringVar()
fev = StringVar()

months = ["Any","Current Month", "Last 3 Months", "Last 6 Months", "Last Year"]

mfil = StringVar()
mfil.set("Any")
view_by_month = OptionMenu(canvas,
    mfil,
    *months,
)
view_by_month.configure(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
view_by_month.place(
    x=606.0,
    y=175.0,
    width=125.0,
    height=26.0
)

def update_table_search_id(*args):
    clear_all(table)
    if(bool(re.search(r'[^\d]', fiv.get())) or bool(re.search(r'[^\d]', fev.get()))):
        print("non-numeric input")
        result = []
    else:
        result = db.select_food_review_spec(fiv.get(), fev.get(), mfil.get())
    
    print("Number of results fetched:", len(result))
    for index, value in enumerate(result):
        table.insert(parent='',index='end',iid=index, text='', values=(value[0],value[1],value[2],value[3], value[4], value[5], value[6]))

fiv.trace_add("write", callback=update_table_search_id)
fev.trace_add("write", callback=update_table_search_id)
mfil.trace_add("write", callback=update_table_search_id)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    515.0,
    188.0,
    image=entry_image_1
)
estabid_field = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    textvariable=fev,
    highlightthickness=0
)
estabid_field.place(
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
foodid_field = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    textvariable=fiv,
    highlightthickness=0
)
foodid_field.place(
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
    609.0,
    157.0,
    anchor="nw",
    text="Filter Date",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

def on_button_8_click():
    print("button_8 clicked")
    view_review.destroy()
    process = subprocess.Popen([sys.executable, "DeleteReview.py"], shell=True)
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
    x=626.0,
    y=102.0,
    width=150.0,
    height=30.0
)

def on_button_9_click():
    print("button_9 clicked")
    view_review.destroy()
    process = subprocess.Popen([sys.executable, "EditReview.py"], shell=True)
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
    x=454.0,
    y=102.0,
    width=150.0,
    height=30.0
)

def on_button_10_click():
    print("button_10 clicked")
    view_review.destroy()
    process = subprocess.Popen([sys.executable, "AddReview.py"], shell=True)
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
    608.0,
    47.0,
    anchor="nw",
    text=f"{QueriesAPI().count_food_reviews()}",
    fill="#FFFFFF",
    font=("Inter Bold", 18)
)

canvas.create_text(
    282.0,
    31.0,
    anchor="nw",
    text="Reviews",
    fill="#D78521",
    font=("Inter Bold", 25 * -1)
)

view_review.resizable(False, False)
view_review.mainloop()
