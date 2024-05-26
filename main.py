from doctest import master
import tkinter as tk
from tkinter import Label, Toplevel, ttk, messagebox, CENTER, NO
import mysql.connector

class FoodReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GROUP 1 Food & Restaurant Review Application")

        # Database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="restaurant",
            password="foodreview",
            database="restaurant"
        )
        self.cursor = self.conn.cursor()

        # Define UI elements
        self.setup_ui()

    def setup_ui(self):
        self.tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Food Establishments')
        self.tab_control.add(self.tab2, text='Food Items')
        self.tab_control.add(self.tab3, text='Reviews')
        self.tab_control.add(self.tab4, text='View All Reports')
        self.tab_control.pack(expand=1, fill='both')

        # Setup tab1 for Food Establishments
        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()
        self.setup_tab4()

    def setup_tab1(self):
        # Label frame for Food Establishments tab
        establishment_frame = ttk.LabelFrame(self.tab1, text="Food Establishments")
        establishment_frame.pack(padx=10, pady=10)

        # Buttons for adding, updating, and deleting establishments
        add_button = ttk.Button(establishment_frame, text="Add Establishment", command=self.add_establishment)
        add_button.pack(pady=5)

        update_button = ttk.Button(establishment_frame, text="Update Establishment", command=self.update_establishment)
        update_button.pack(pady=5)

        delete_button = ttk.Button(establishment_frame, text="Delete Establishment", command=self.delete_establishment)
        delete_button.pack(pady=5)

    def setup_tab2(self):
        # Label frame for Food Items tab
        item_frame = ttk.LabelFrame(self.tab2, text="Food Items")
        item_frame.pack(padx=10, pady=10)

        # Buttons for adding, updating, and deleting establishments
        add_button = ttk.Button(item_frame, text="Add Food Item", command=self.add_food_item)
        add_button.pack(pady=5)

        update_button = ttk.Button(item_frame, text="Update Food Item", command=self.update_food_item)
        update_button.pack(pady=5)

        search_button = ttk.Button(item_frame, text="Search Food Item", command=self.search_food_item)
        search_button.pack(pady=5)

        delete_button = ttk.Button(item_frame, text="Delete Food Item", command=self.delete_food_item)
        delete_button.pack(pady=5)


    def setup_tab3(self):
        # Label frame for Reviews tab
        reviews_frame = ttk.LabelFrame(self.tab3, text="Reviews")
        reviews_frame.pack(padx=10, pady=10)

        # Buttons for adding, updating, and deleting establishments
        add_button = ttk.Button(reviews_frame, text="Add Review", command=self.add_review)
        add_button.pack(pady=5)

        update_button = ttk.Button(reviews_frame, text="Update Review", command=self.update_review)
        update_button.pack(pady=5)

        delete_button = ttk.Button(reviews_frame, text="Delete Review", command=self.delete_review)
        delete_button.pack(pady=5)


    def setup_tab4(self):
        # Label frame for View Reports tab
        view_reports_frame = ttk.LabelFrame(self.tab4, text="View Reports")
        view_reports_frame.pack(padx=10, pady=10)

        table = ttk.Treeview(view_reports_frame)

        table['columns'] = ('establishment_id', 'description', 'establishment_name')

        table.column("#0", width=0,  stretch=NO)
        table.column("establishment_id",anchor=CENTER, width=80)
        table.column("description",anchor=CENTER,width=80)
        table.column("establishment_name",anchor=CENTER,width=80)

        table.heading("#0",text="",anchor=CENTER)
        table.heading("establishment_id",text="Id",anchor=CENTER)
        table.heading("description",text="Description",anchor=CENTER)
        table.heading("establishment_name",text="Name",anchor=CENTER)

        
        # Buttons for viewing reports
        view_all_food_estabs = ttk.Button(view_reports_frame, text="View All Food Establishments", command=lambda: self.select_all_food_estabs(table))
        view_all_food_estabs.pack(pady=5)
        
        table.pack()

        # add_button = ttk.Button(view_reports_frame, text="Add Establishment", command=self.add_establishment)
        # add_button.pack(pady=5)

        # update_button = ttk.Button(view_reports_frame, text="Update Establishment", command=self.update_establishment)
        # update_button.pack(pady=5)

        # delete_button = ttk.Button(view_reports_frame, text="Delete Establishment", command=self.delete_establishment)
        # delete_button.pack(pady=5)


    # Other helper functions
    def select_all_food_estabs(self, table):
        sql_statement = "SELECT * FROM FOOD_ESTABLISHMENT"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        for index,value in enumerate(result):
            table.insert(parent='',index='end',iid=index, text='', values=(value[0],value[1],value[2]))
        print(result)

    def add_establishment(self):
        newWindow = Toplevel(master)
        newWindow.title("Add Establishment")
        newWindow.geometry("200x200")
        newWindow.grab_set()

        
        Label(newWindow, text ="Establishment ID").pack()
        establishment_id = tk.Entry(newWindow, width=30)
        establishment_id.pack( padx=20, pady= 20)
        Label(newWindow, text ="Establishment Name").pack()
        establishment_name = tk.Entry(newWindow, width=30)
        establishment_name.pack( padx=20, pady= 20)
        Label(newWindow, text ="Establishment Location").pack()
        establishment_loc = tk.Text(newWindow,height = 2)
        establishment_loc.pack( padx=20, pady= 20)
        Label(newWindow, text ="Mode of Service").pack()
        serv_mod = tk.Text(newWindow,height=2)
        serv_mod.pack(padx=20, pady= 20)
        Label(newWindow, text ="Contact Detail").pack()
        contact_detail = tk.Text(newWindow, height=2)
        contact_detail.pack( padx=20, pady= 20)
        Label(newWindow, text ="Establishment Description").pack()
        establishment_id = tk.Text(newWindow, height=2)
        establishment_id.pack( padx=20, pady= 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)
  

    def update_establishment(self):
        newWindow = Toplevel(master)
        newWindow.title("Update Establishment")
        newWindow.geometry("200x200")
        newWindow.grab_set()
        Label(newWindow, text ="Enter establishment id:").pack()
        establishment_id = tk.Entry(newWindow, width=30)
        establishment_id.pack( padx=20, pady= 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def delete_establishment(self):
        newWindow = Toplevel(master)
        newWindow.title("Delete Establishment")
        newWindow.geometry("200x200")
        newWindow.grab_set()
        Label(newWindow, text ="Enter establishment id:").pack()
        establishment_id = tk.Entry(newWindow, width=30)
        establishment_id.pack( padx=20, pady= 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def add_food_item(self):
        newWindow = Toplevel(master)
        newWindow.title("Add Food Item")
        newWindow.geometry("400x800")
        newWindow.grab_set()

        Label(newWindow, text ="Food Item ID").pack()
        fooditem_id = tk.Entry(newWindow, width=30)
        fooditem_id.pack(padx=20, pady = 20)
        Label(newWindow, text ="Food Item Name").pack()
        fooditem_name = tk.Entry(newWindow, width=30)
        fooditem_name.pack(padx=20, pady = 20)
        Label(newWindow, text ="Food Item Type").pack()
        fooditem_type = tk.Text(newWindow, height=2)
        fooditem_type.pack(padx=20, pady = 20)
        Label(newWindow, text ="Food Item Price").pack()
        fooditem_price = tk.Entry(newWindow, width=30)
        fooditem_price.pack(padx=20, pady = 20)
        Label(newWindow, text ="Food Item Description").pack()
        fooditem_id = tk.Text(newWindow, height=2)
        fooditem_id.pack(padx=20, pady = 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def update_food_item(self):
        newWindow = Toplevel(master)
        newWindow.title("Update Food Item")
        newWindow.geometry("400x800")
        newWindow.grab_set()

        Label(newWindow, text ="Enter food item id: ").pack()
        fooditem_id = tk.Entry(newWindow, width=30)
        fooditem_id.pack(padx=20, pady = 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def search_food_item(self):
        newWindow = Toplevel(master)
        newWindow.title("Search Food Item")
        newWindow.geometry("400x800")
        newWindow.grab_set()

        Label(newWindow, text ="Enter food item id: ").pack()
        fooditem_id = tk.Entry(newWindow, width=30)
        fooditem_id.pack(padx=20, pady = 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def delete_food_item(self):
        newWindow = Toplevel(master)
        newWindow.title("Delete Food Item")
        newWindow.geometry("400x800")
        newWindow.grab_set()

        Label(newWindow, text ="Enter food item id: ").pack()
        fooditem_id = tk.Entry(newWindow, width=30)
        fooditem_id.pack(padx=20, pady = 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def add_review(self):
        newWindow = Toplevel(master)
        newWindow.title("Update Food Item")
        newWindow.geometry("400x800")
        newWindow.grab_set()

        Label(newWindow, text ="Review ID").pack()
        review_id = tk.Entry(newWindow, width=30)
        review_id.pack(padx=20, pady = 20)
        Label(newWindow, text ="Review Rating").pack()
        review_rating = tk.Entry(newWindow, width=30)
        review_rating.pack(padx=20, pady = 20)
        Label(newWindow, text ="Date of Rating").pack()
        review_rating = tk.Entry(newWindow, width=30)
        review_rating.pack(padx=20, pady = 20)
        Label(newWindow, text ="Review Statement").pack()
        review_rating = tk.Text(newWindow, height=2)
        review_rating.pack(padx=20, pady = 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def update_review(self):
        newWindow = Toplevel(master)
        newWindow.title("Update Review")
        newWindow.geometry("400x800")
        newWindow.grab_set()

        Label(newWindow, text ="Enter review id: ").pack()
        fooditem_id = tk.Entry(newWindow, width=30)
        fooditem_id.pack(padx=20, pady = 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)

    def delete_review(self):
        newWindow = Toplevel(master)
        newWindow.title("Delete Review")
        newWindow.geometry("400x800")
        newWindow.grab_set()

        Label(newWindow, text ="Enter review id: ").pack()
        fooditem_id = tk.Entry(newWindow, width=30)
        fooditem_id.pack(padx=20, pady = 20)
        submitButton = tk.Button(newWindow, text="Submit")
        submitButton.pack(padx=20, pady= 20)


    def run(self):
        self.root.mainloop()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodReviewApp(root)
    app.run()