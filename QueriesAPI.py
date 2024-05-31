from datetime import datetime
import subprocess
import sys
from tkinter import messagebox
import mysql.connector
import re
import shortuuid


def generateID():
    return shortuuid.ShortUUID(alphabet="0123456789").random(length=5)


logged_user = None
class QueriesAPI():
    logged_user = None
    def __init__(self):
        self.conn = mysql.connector.connect(
                host="localhost",
                user="restaurant",
                password="foodreview",
                database="restaurant"
            )
        self.cursor = self.conn.cursor()

    # ----- SELECT STATEMENTS -----
    def select_all_food_estabs(self):
        sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod) FROM FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE GROUP BY estab_id"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result
    
    def select_food_estab_by_id(self, id):
        if(id == ''):
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod) FROM FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE GROUP BY estab_id"
        elif(bool(re.search(r'[^\d]', id))):
            print('contains non-numeric chars')
            return []
        else:
            sql_statement = f"SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod) FROM FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id={id} GROUP BY estab_id"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result
    
    def select_food_estab_by_rating(self, rating):
        if(rating == "Filter"):
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod) FROM FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE GROUP BY estab_id"
        elif(rating == "High Rating"):
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 4 GROUP BY estab_id ORDER BY average_rating DESC"
        elif(rating == "Average Rating"):
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 2.5 AND average_rating < 4 GROUP BY estab_id ORDER BY average_rating DESC"
        else:
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating < 2.5 GROUP BY estab_id ORDER BY average_rating DESC"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result


    def verify_credentials(self, email, password, login_window): #------LOG IN VERIFICATION------#
        sql_statement = "SELECT email FROM CUSTOMER WHERE email = %s AND password = %s"
        self.cursor.execute(sql_statement, (email, password))
        logged_user = self.cursor.fetchone()

        if logged_user:
            #self.user_session = {"email": email, "user_name": result[0], "real_name": result[1]}
            print(logged_user[0])
            messagebox.showinfo("Login", "User logged in successfully!")
            login_window.destroy()
            subprocess.Popen([sys.executable, "DashboardPage.py"], shell=True)
            return logged_user
        else:
            messagebox.showerror("Login Error", "Invalid email or password")

    def logout(self):
        logged_user = None
        messagebox.showinfo("Logout", "User logged out successfully!")

    # ----- INSERT STATEMENTS -----
    def create_account(self, email, real_name, username, password, register_window):
        sql_statement = "INSERT INTO CUSTOMER (email, real_name, user_name, password, num_reviews) VALUES (%s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql_statement, (email, real_name, username, password, 0))
            self.conn.commit()
            messagebox.showinfo("Register", "Account created successfully!")
            register_window.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Register Error", f"Error: {err}")

    def add_review(self, rate_text, food_text, estab_text, review_text, addrev_window):
        #print(f"Rating: {rate_text.get()}\nFood ID: {food_text.get()}\nEstab ID: {estab_text.get()}\nReview: {review_text.get('1.0', 'end-1c')}")
        reviewid = generateID()
        rating = rate_text.get()
        foodid = food_text.get()
        estabid = estab_text.get()
        review = review_text.get('1.0', 'end-1c')
        datereviewed = datetime.now().strftime("%Y-%m-%d")
        email =logged_user[0]
        reviewInsert = f'''INSERT INTO REVIEW(review_id, rating, rev_date, rev_stat, email, estab_id, food_id) VALUES ({reviewid}, {rating}, '{datereviewed}', '{review}', '{email}', {estabid}, {foodid})'''
        
        try:
            self.cursor.execute(reviewInsert)
            self.conn.commit()
            messagebox.showinfo("Add Review", "Review posted!")
            print(reviewInsert)
            addrev_window.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        
    # ----- UPDATE STATEMENTS -----


    # ----- DELETE STATEMENTS -----

    def __del__(self):
        self.cursor.close()
        self.conn.close()
