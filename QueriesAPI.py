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
            print('search contains non-numeric chars')
            return []
        else:
            sql_statement = f"SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod) FROM FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id={id} GROUP BY estab_id"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result

    def select_food_estab_by_id_rating(self, id, rating):
        if(id == None and rating == 'Filter'):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT f.estab_id, COALESCE(SUM(rating)/COUNT(review_id), 'N/A') AS average_rating FROM FOOD_ESTABLISHMENT f LEFT JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE GROUP BY estab_id ORDER BY estab_id"
        elif(id != None and bool(re.search(r'[^\d]', id))):
            print('search contains non-numeric chars')
            return []
        elif(id == None and rating != 'Filter'):
            if(rating == "High Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 4 GROUP BY estab_id ORDER BY average_rating DESC"
            elif(rating == "Average Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 2.5 AND average_rating < 4 GROUP BY estab_id ORDER BY average_rating DESC"
            else:
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating < 2.5 GROUP BY estab_id ORDER BY average_rating DESC"
        elif(id != None):
            if(rating == "Filter"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT f.estab_id, COALESCE(SUM(rating)/COUNT(review_id), 'N/A') AS average_rating FROM FOOD_ESTABLISHMENT f LEFT JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s GROUP BY estab_id ORDER BY estab_id"
            elif(rating == "High Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s AND average_rating >= 4 GROUP BY estab_id ORDER BY average_rating DESC"
            elif(rating == "Average Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s AND average_rating >= 2.5 AND average_rating < 4 GROUP BY estab_id ORDER BY average_rating DESC"
            else:
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s AND average_rating < 2.5 GROUP BY estab_id ORDER BY average_rating DESC"
            self.cursor.execute(sql_statement, [id])
            result = self.cursor.fetchall()
            return result
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result

    def count_food_estab(self):
        sql_statement = f"SELECT COUNT(estab_id) FROM FOOD_ESTABLISHMENT;"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()[0][0]
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

    def add_food_estab(self, estab_name, estab_desc, loc, serv_mod, contact):
        sql_statement = 'SELECT estab_id FROM FOOD_ESTABLISHMENT ORDER BY estab_id DESC'
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        newId = result[0][0] + 1

        for i in loc: 
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_LOCATION(estab_id, loc) VALUES (%s, %s)'
            self.cursor.execute(sql_statement, (newId,  i))
        for i in serv_mod:
           sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_MODE_OF_SERVICE(estab_id, serv_mod) VALUES (%s, %s)'
           self.cursor.execute(sql_statement, (newId,  i))

        for i in contact:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_CONTACT(estab_id, contact) VALUES (%s, %s)'
            self.cursor.execute(sql_statement, (newId,  i))

        sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT(estab_id, estab_desc, estab_name) VALUES  (%s, %s, %s)'
        self.cursor.execute(sql_statement, (newId, estab_desc, estab_name))

        self.conn.commit()
        addedFoodEstab = self.select_food_estab_by_id(str(newId))
        return addedFoodEstab

        
    # ----- UPDATE STATEMENTS -----
    def update_food_estab_by_id(self, id, estab_name, estab_desc, loc, serv_mod, contact):
        sql_statement = 'UPDATE FOOD_ESTABLISHMENT SET estab_desc=%s, estab_name=%s WHERE estab_id=%s'
        self.cursor.execute(sql_statement, (estab_desc, estab_name, id))

        sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_CONTACT WHERE estab_id=%s'
        self.cursor.execute(sql_statement, [id])
        sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_LOCATION WHERE estab_id=%s'
        self.cursor.execute(sql_statement, [id])
        sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s'
        self.cursor.execute(sql_statement, [id])

        for contactDetail in contact:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_CONTACT(estab_id, contact) VALUES(%s, %s)'
            self.cursor.execute(sql_statement, (id, contactDetail))

        for location in loc:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_LOCATION(estab_id, loc) VALUES(%s, %s)'
            self.cursor.execute(sql_statement, (id, location))

        for modeOfService in serv_mod:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_MODE_OF_SERVICE(estab_id, serv_mod) VALUES(%s, %s)'
            self.cursor.execute(sql_statement, (id, modeOfService))

        self.conn.commit()
        updatedFoodEstab = self.select_food_estab_by_id(id)
        return updatedFoodEstab


    # ----- DELETE STATEMENTS -----
    def delete_food_estab_by_id(self, id):
        result = self.select_food_estab_by_id(id)
        if(result == []):
            messagebox.showerror("Delete Error", "Establishment with specified ID not found!")
            return []
        else:
            sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT WHERE estab_id=%s'
            self.cursor.execute(sql_statement, [id])
            sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_CONTACT WHERE estab_id=%s'
            self.cursor.execute(sql_statement, [id])
            sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_LOCATION WHERE estab_id=%s'
            self.cursor.execute(sql_statement, [id])
            sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s'
            self.cursor.execute(sql_statement, [id])
            self.conn.commit()
            messagebox.showinfo("Delete Establishment", "Successfully deleted establishment!")
            return

    def __del__(self):
        self.cursor.close()
        self.conn.close()
