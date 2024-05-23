import tkinter as tk
from tkinter import ttk, messagebox
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
        self.tab_control.add(self.tab1, text='Food Establishments')
        self.tab_control.add(self.tab2, text='Food Items')
        self.tab_control.add(self.tab3, text='Reviews')
        self.tab_control.pack(expand=1, fill='both')

        # Setup tab1 for Food Establishments
        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()

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


    # Other helper functions
    def add_establishment(self):
        # Code for adding a new food establishment
        messagebox.showinfo("Info", "Add Establishment")

    def update_establishment(self):
        # Code for updating an existing food establishment
        messagebox.showinfo("Info", "Update Establishment")

    def delete_establishment(self):
        # Code for deleting a food establishment
        messagebox.showinfo("Info", "Delete Establishment")

    def add_food_item(self):
        # Code for adding a new food item
        messagebox.showinfo("Info", "Add Food Item")

    def update_food_item(self):
        # Code for updating an existing food item
        messagebox.showinfo("Info", "Update Food Item")

    def search_food_item(self):
        # Code for searching a food item
        messagebox.showinfo("Info", "Search Food Item")

    def delete_food_item(self):
        # Code for deleting a food item
        messagebox.showinfo("Info", "Delete Food Item")

    def add_review(self):
        # Code for adding a new review
        messagebox.showinfo("Info", "Add Review")

    def update_review(self):
        # Code for updating an existing review
        messagebox.showinfo("Info", "Update Review")

    def delete_review(self):
        # Code for deleting a review
        messagebox.showinfo("Info", "Delete Review")


    def run(self):
        self.root.mainloop()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodReviewApp(root)
    app.run()