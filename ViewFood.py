from pathlib import Path
import re
import sys
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, ttk, CENTER, NO, StringVar, OptionMenu, font

from QueriesAPI import QueriesAPI


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame17"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

view_food = Tk()

w = 800
h = 500 

# get screen width and height
ws = view_food.winfo_screenwidth() 
hs = view_food.winfo_screenheight()

# calculate x and y coordinates for the Tk root view_food
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
view_food.geometry('%dx%d+%d+%d' % (w, h, x, y))
view_food.configure(bg = "#FFFFFF")


canvas = Canvas(
    view_food,
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
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=23.0,
    y=305.0,
    width=201.0,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    background="#DE1A1A",
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=86.0,
    y=460.0,
    width=75.0,
    height=19.354839324951172
)

canvas.create_rectangle(
    276.0,
    225.0,
    770.0,
    480.0,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    276.0,
    146.0,
    770.0,
    212.0,
    fill="#F0F0F0",
    outline="")

def on_button_3_click():
    print("button_3 clicked")
    view_food.destroy()
    process = subprocess.Popen([sys.executable, "DeleteFood.py"], shell=True)
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
    x=620.0,
    y=104.0,
    width=150.0,
    height=30.0
)

def on_button_4_click():
    print("button_4 clicked")
    view_food.destroy()
    process = subprocess.Popen([sys.executable, "EditFood.py"], shell=True)
    process.wait()

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_4_click,
    relief="flat"
)
button_4.place(
    x=448.0,
    y=104.0,
    width=150.0,
    height=30.0
)

def on_button_5_click():
    print("button_5 clicked")
    view_food.destroy()
    process = subprocess.Popen([sys.executable, "AddFood.py"], shell=True)
    process.wait()

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_5_click,
    relief="flat"
)
button_5.place(
    x=276.0,
    y=104.0,
    width=150.0,
    height=30.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    652.0,
    50.0,
    image=image_image_2
)


canvas.create_text(
    638.0,
    47.0,
    anchor="nw",
    text=f"{QueriesAPI().count_food_item()}",
    fill="#FFFFFF",
    font=("Inter Bold", 18)
)

canvas.create_text(
    276.0,
    33.0,
    anchor="nw",
    text="Food Items",
    fill="#D78521",
    font=("Inter Bold", 25 * -1)
)

def on_button_6_click():
    view_food.destroy()
    process = subprocess.Popen([sys.executable, "ProfilePage.py"], shell=True)
    process.wait()

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_6_click,
    relief="flat"
)
button_6.place(
    x=23.0,
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
    view_food.destroy()
    process = subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)

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
    x=23.0,
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
    view_food.destroy()
    process = subprocess.Popen([sys.executable, "ViewEstab.py"], shell=True)
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
    x=23.0,
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
    view_food.destroy()
    process = subprocess.Popen([sys.executable, "ViewReview.py"], shell=True)
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
    x=23.0,
    y=353.0,
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




#################
canvas.create_rectangle(
    276.0,
    218.0,
    770.0,
    480.0,
    fill="#F0F0F0",
    outline="")

table = ttk.Treeview()
table['columns'] = ('food_id', 'food_name', 'food_desc', 'food_type', 'price', 'estab_name')
table.column("#0", width=0,  stretch=NO)
table.column("food_id",anchor=CENTER,width=40)
table.column("food_name",anchor=CENTER,minwidth=50)
table.column("food_desc",anchor=CENTER,minwidth=90)
table.column("food_type",anchor=CENTER,minwidth=50)
table.column("price",anchor=CENTER,minwidth=30)
table.column("estab_name",anchor=CENTER,minwidth=90)

# Scrollbars
horzScrollBar = ttk.Scrollbar(view_food, 
                           orient ="horizontal", 
                           command = table.xview)
horzScrollBar.place(
    x=276,
    y=480,
    width=494,
    height=20
)
vertScrollBar = ttk.Scrollbar(view_food, 
                           orient ="vertical", 
                           command = table.yview)
vertScrollBar.place(
    x=770,
    y=218,
    width=20,
    height=262
)
table.configure(xscrollcommand = horzScrollBar.set)
table.configure(yscrollcommand = vertScrollBar.set)

# Disable resizing of columns
table.bind('<Button-1>', 'break')

#ascSort = True
sortTable = 0
sortText = StringVar()
sortText.set("Price (₱) —")
def toggleSort(event):
    region = table.identify_region(event.x, event.y)
    if region == "heading":
        column = table.identify_column(event.x)
        if(column == "#5"):
            global sortTable
            if(sortTable == 2):
                sortTable = 0
                table.heading("price",text=f"{"Price (₱) —"}",anchor=CENTER)
            elif(sortTable == 0):
                sortTable+=1
                #sortText.set("Price (₱) ↑")
                table.heading("price",text=f"{"Price (₱) ↑"}",anchor=CENTER)
            else:
                table.heading("price",text=f"{"Price (₱) ↓"}",anchor=CENTER)
                #sortText.set("Price (₱) ↓")
                sortTable+=1
            print("toggled")
            update_table_search_id()


table.bind("<Button-1>", toggleSort)
table.heading("#0",text="",anchor=CENTER)
table.heading("food_id",text="Id",anchor=CENTER)
table.heading("food_name",text="Name",anchor=CENTER)
table.heading("food_desc",text="Description",anchor=CENTER)
table.heading("food_type",text="Food Type",anchor=CENTER)
table.heading("price",text=f"{sortText.get()}",anchor=CENTER)
table.heading("estab_name",text="Establishment Name",anchor=CENTER)
table.place(
    x=276,
    y=218,
    width=494,
    height=262
)


canvas.create_rectangle(
    276.0,
    151.0,
    770.0,
    208.0,
    fill="#F0F0F0",
    outline="")

db = QueriesAPI()
result = db.select_all_food_item()
for index,value in enumerate(result):
    table.insert(parent='',index='end',iid=index, text='', values=(value[0],value[1],value[2],value[4],value[3], value[5]))


def clear_all(tableToClear):
   for item in tableToClear.get_children():
      tableToClear.delete(item)


options = [
    "Any",
    "Breakfast",
    "Lunch",
    "Dinner",
]

fiv = StringVar()
fev = StringVar()
minv = StringVar()
maxv = StringVar()
clicked = StringVar()

def update_table_search_id(*args):
    clear_all(table)
    if(bool(re.search(r'[^\d]', fiv.get())) or bool(re.search(r'[^\d]', fev.get())) or bool(re.search(r'[^\d]', minv.get()))) or bool(re.search(r'[^\d]', maxv.get())):
        print("non-numeric input")
        result = []
    else:
        result = db.select_food_item_spec(fiv.get(), fev.get(), minv.get(), maxv.get(), clicked.get(), sortTable)
        
    for index, value in enumerate(result):
        table.insert(parent='',index='end',iid=index, text='', values=(value[0],value[1],value[2],value[4],value[3], value[5]))

            
        

fiv.trace_add("write", callback=update_table_search_id)
fev.trace_add("write", callback=update_table_search_id)
minv.trace_add("write", callback=update_table_search_id)
maxv.trace_add("write", callback=update_table_search_id)
clicked.trace_add("write", callback=update_table_search_id)
clicked.set("Any")

foodid_field = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    textvariable=fiv
)
foodid_field.place(
    x=292.0,
    y=175.0,
    width=90.0,
    height=24.0
)



# button_image_3 = PhotoImage(
#     file=relative_to_assets("button_3.png"))

# clicked = StringVar()
# def update_table_filter(*args):
#     clear_all(table)
#     result = db.select_food_estab_by_rating(clicked.get())
#     if(clicked.get() == "Any"):
#         for index,value in enumerate(result):
#             table.insert(parent='',index='end',iid=index, text='',values=(value[0],value[1],value[2],value[3],value[4]))
#     else:
#         for index,value in enumerate(result):
#             table.insert(parent='',index='end',iid=index, text='',values=(value[0],value[1],value[2],value[3],value[4]))
    

# clicked.trace_add("write", callback=update_table_filter)
# clicked.set("Any")
foodtype_dd = OptionMenu(canvas,
    clicked,
    *options,
)
foodtype_dd.configure(
    bd=0,
    activebackground="#FFFFFF",
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
foodtype_dd.place(
    x=680.0,
    y=174.0,
    width=80.0,
    height=26.0
)
###############
# entry_image_2 = PhotoImage(
#     file=relative_to_assets("estabid_field.png"))
# entry_bg_2 = canvas.create_image(
#     510.0,
#     189.0,
#     image=entry_image_2
# )
estabid_field = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=fev
)
estabid_field.place(
    x=400.0,
    y=177.0,
    width=100.0,
    height=24.0
)

canvas.create_text(
    289.0,
    158.0,
    anchor="nw",
    text="Search Food ID",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    400.0,
    158.0,
    anchor="nw",
    text="Search Establishment ID",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    540.0,
    158.0,
    anchor="nw",
    text="Min Price",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)
minprice_field = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=minv
)
minprice_field.place(
    x=540.0,
    y=175.0,
    width=50.0,
    height=24.0
)

canvas.create_text(
    600.0,
    158.0,
    anchor="nw",
    text="Max Price",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)

maxprice_field = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=maxv
)
maxprice_field.place(
    x=600.0,
    y=175.0,
    width=50.0,
    height=24.0
)


canvas.create_text(
    680.0,
    158.0,
    anchor="nw",
    text="Type",
    fill="#DE1A1A",
    font=("Inter", 11 * -1)
)
view_food.resizable(False, False)
view_food.mainloop()