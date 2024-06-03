from datetime import datetime
import subprocess
import sys
from tkinter import messagebox
import mysql.connector
import re
import os
from cryptography.fernet import Fernet

class DuplicateEmailError(Exception):
    pass

class EncryptionHelper:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt(self, plaintext):
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        try:
            decrypted_data = self.cipher.decrypt(ciphertext.encode())
            return decrypted_data.decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            return None
        
class QueriesAPI():
    logged_user = ()
    
    def __init__(self):
        self.conn = mysql.connector.connect(
                host="localhost",
                user="restaurant",
                password="foodreview",
                database="restaurant"
            )
        self.cursor = self.conn.cursor()

        # Load or generate encryption key
        self.encryption_key = self.load_or_generate_key()
        self.encryption_helper = EncryptionHelper(self.encryption_key)

    def load_or_generate_key(self):
        key_file_path = "encryption_key.txt"
        
        if os.path.exists(key_file_path):
            # Load the key from the file and convert it to bytes
            with open(key_file_path, "rb") as key_file:
                return key_file.read()
        else:
            # Generate a new key and save it to the file
            key = Fernet.generate_key()
            with open(key_file_path, "wb") as key_file:
                key_file.write(key)
            return key

    def logout(self):
        QueriesAPI.logged_user = None
        os.remove("data_file.txt")
        messagebox.showinfo("Logout", "User logged out successfully!")
        subprocess.Popen([sys.executable, "./pages/LoginPage.py"], shell=True)
        sys.exit()
    
    # def get_logged_user_email(self):
        
    def count_food_estab(self):
        sql_statement = f"SELECT COUNT(estab_id) FROM FOOD_ESTABLISHMENT;"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()[0][0]
        return result
    
    def fetch_user_details(self):
        data_file = open("data_file.txt", "r")
        try:
            read_text = data_file.read()
            print(f"text: {read_text}")
            email = self.encryption_helper.decrypt(read_text)
            print(email)
            
            sql_statement = f'''SELECT email, real_name, user_name, num_reviews FROM customer WHERE email = "{email}";'''
            self.cursor.execute(sql_statement)
            result = self.cursor.fetchall()
            data_file.close()
            return result
        except Exception as e:
            messagebox.showerror("Error in file", f"{e}")

    # ----- SELECT STATEMENTS -----
    def select_all_food_estabs(self):
        sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod) FROM FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE GROUP BY estab_id"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result
    
    def select_food_estab_by_id_rating(self, id, rating, sorting):
        if(sorting==0): #if 0, sort by id asc
            orderclause = " ORDER BY estab_id"
        elif(sorting== 1): #if 1, sort by average_rating asc
            orderclause = " ORDER BY average_rating"
        elif(sorting== 2): #if 2, sort by average_rating desc
            orderclause = " ORDER BY average_rating DESC"

        if(id == None and rating == 'Filter'):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT f.estab_id, COALESCE(SUM(rating)/COUNT(review_id), 'N/A') AS average_rating FROM FOOD_ESTABLISHMENT f LEFT JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE GROUP BY estab_id"
        elif(id != None and bool(re.search(r'[^\d]', id))):
            print('search contains non-numeric chars')
            return []
        elif(id == None and rating != 'Filter'):
            if(rating == "High Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 4 GROUP BY estab_id"
            elif(rating == "Average Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 2.5 AND average_rating < 4 GROUP BY estab_id"
            else:
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating < 2.5 GROUP BY estab_id"
        elif(id != None):
            if(rating == "Filter"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT f.estab_id, COALESCE(SUM(rating)/COUNT(review_id), 'N/A') AS average_rating FROM FOOD_ESTABLISHMENT f LEFT JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s GROUP BY estab_id"
            elif(rating == "High Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s AND average_rating >= 4 GROUP BY estab_id"
            elif(rating == "Average Rating"):
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s AND average_rating >= 2.5 AND average_rating < 4 GROUP BY estab_id"
            else:
                sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s AND average_rating < 2.5 GROUP BY estab_id"
            sql_statement = sql_statement + orderclause
            self.cursor.execute(sql_statement, [id])
            result = self.cursor.fetchall()
            return result
        sql_statement = sql_statement + orderclause
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result
    
    def select_email_by_revid(self, review_id, email):
        self.cursor.execute(f"SELECT email FROM review WHERE review_id = {review_id} AND email = '{email}'")
        result = self.cursor.fetchall()
        return result

    def select_all_food_ids(self):
        self.cursor.execute("SELECT food_id FROM food_item")
        food_ids = [row[0] for row in self.cursor.fetchall()]
        return food_ids

    def select_all_estab_ids(self):
        self.cursor.execute("SELECT estab_id FROM food_establishment")
        estab_ids = [row[0] for row in self.cursor.fetchall()]
        return estab_ids

    def select_all_review_ids(self):
        self.cursor.execute("SELECT review_id FROM review")
        review_ids = [row[0] for row in self.cursor.fetchall()]
        return review_ids

    # ----- FOOD REVIEW FUNCTIONS -----
    def select_all_food_reviews(self):
        sql_statement = "SELECT r.review_id, r.rating, r.rev_date, r.rev_stat, r.email, fe.estab_name, fi.food_name FROM review r LEFT JOIN food_item fi ON r.food_id=fi.food_id LEFT JOIN food_establishment fe ON r.estab_id=fe.estab_id GROUP BY r.review_id;"
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
    
    def select_review_by_id(self, review_id):
        self.cursor.execute(f"SELECT review_id, rating, rev_stat, estab_id, food_id FROM review WHERE review_id = {review_id}")
        result = self.cursor.fetchall()
        return result
    
    def count_food_reviews(self):
        sql_statement = f"SELECT COUNT(review_id) FROM review;"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()[0][0]
        return result
    
    def select_food_review_spec(self, food_id, estab_id, month_filter):
        whereclause = ""
        if(food_id != '' or estab_id != '' or month_filter != 'Any'):
            whereclause = "WHERE "
            if(food_id != ''):
                whereclause += f"r.food_id = {food_id} AND "
            if(estab_id != ''):
                whereclause += f"r.estab_id = {estab_id} AND "
            if(month_filter == 'Current Month'):
                whereclause += f"MONTH(r.rev_date) = MONTH(CURDATE()) AND YEAR(r.rev_date) = YEAR(CURDATE())"
            elif(month_filter == 'Last 3 Months'):
                whereclause += f"r.rev_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)"
            elif(month_filter == 'Last 6 Months'):
                whereclause += f"r.rev_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)"
            elif(month_filter == 'Last Year'):
                whereclause += f"r.rev_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)"
            
            # Remove the last ' AND ' if it exists
            if whereclause.endswith(' AND '):
                whereclause = whereclause[:-5]

        sql_statement = f"SELECT r.review_id, r.rating, r.rev_date, r.rev_stat, r.email, fe.estab_name, fi.food_name FROM review r LEFT JOIN food_item fi ON r.food_id=fi.food_id LEFT JOIN food_establishment fe ON r.estab_id=fe.estab_id {whereclause}"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result

    def select_food_estab_by_rating(self, rating):
        if(rating == "Filter"):
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod) FROM FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE GROUP BY estab_id"
        elif(rating == "High Rating"):
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 4 GROUP BY estab_id ORDER BY average_rating DESC"
        elif(rating == "Average Rating"):
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating >= 2.5 AND average_rating < 4 GROUP BY estab_id ORDER BY average_rating DESC"
        else:
            sql_statement = "SELECT estab_id, estab_desc, estab_name, GROUP_CONCAT(DISTINCT contact), GROUP_CONCAT(DISTINCT loc), GROUP_CONCAT(DISTINCT serv_mod), average_rating FROM (SELECT r.estab_id, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_id) t NATURAL JOIN FOOD_ESTABLISHMENT NATURAL JOIN FOOD_ESTABLISHMENT_CONTACT NATURAL JOIN FOOD_ESTABLISHMENT_LOCATION NATURAL JOIN FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE average_rating < 2.5 GROUP BY estab_id ORDER BY average_rating DESC"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result

    def select_all_food_item(self):
        sql_statement = f"SELECT food_id, food_name, food_desc, price, GROUP_CONCAT(DISTINCT food_type), estab_name FROM food_item NATURAL JOIN food_item_food_type NATURAL JOIN food_establishment GROUP BY food_id;"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result
    
    def select_food_item_byid(self, foodid):
        sql_statement = f"SELECT food_name, food_desc, price, GROUP_CONCAT(DISTINCT food_type), estab_id FROM food_item NATURAL JOIN food_item_food_type NATURAL JOIN food_establishment WHERE food_id = {foodid} GROUP BY food_id;"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result
    
    def count_food_item(self):
        sql_statement = f"SELECT COUNT(food_id) FROM food_item;"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()[0][0]
        
        return result
    
    def select_food_item_spec(self, foodid, estabid, minp, maxp, type, sorting):
        whereclause = ""
        orderclause = ""
        if(foodid != '' or estabid != '' or minp != '' or maxp != '' or type != "Any"):
            whereclause = "WHERE "
            if(foodid != ''):
                if(estabid != ''):
                    whereclause = whereclause + f"food_id = {foodid} AND "
                else:
                    whereclause = whereclause + f"food_id = {foodid}"
            
            if(estabid != ''):
                whereclause = whereclause + f"estab_id = {estabid}"

            if((minp != '' or maxp != '')):
                if(foodid != '' or estabid != ''):
                    whereclause = whereclause + " AND price BETWEEN "
                else:
                    whereclause = whereclause + "price BETWEEN "
                    
                if(minp != ''):
                    whereclause = whereclause + f"{minp} AND "
                else:
                    whereclause = whereclause + f"0 AND "
                
                if(maxp != ''):
                    whereclause = whereclause + f"{maxp}"
                else:
                    maxquery = "SELECT MAX(price) from food_item;"
                    self.cursor.execute(maxquery)
                    max = self.cursor.fetchall()
                    whereclause = whereclause + f"{max[0][0]}"
            if(type != "Any"):
                if(foodid != '' or estabid != '' or minp != '' or maxp != ''):
                    whereclause = whereclause + " AND food_type = "
                else:
                    whereclause = whereclause + " food_type = "

                if(type == "Breakfast"):
                    whereclause = whereclause + '''"Breakfast"'''
                elif(type == "Lunch"):
                    whereclause = whereclause + '''"Lunch"'''
                elif (type == "Dinner"):
                    whereclause = whereclause + '''"Dinner"'''
        if(sorting==0): #if 0, sort by id asc
            orderclause = "ORDER BY food_id"
        elif(sorting== 1): #if 1, sort by price asc
            orderclause = "ORDER BY price"
        elif(sorting== 2): #if 2, sort by price desc
            orderclause = orderclause + "ORDER BY price DESC"

        sql_statement = f"SELECT food_id, food_name, food_desc, price, GROUP_CONCAT(DISTINCT food_type), estab_name FROM food_item NATURAL JOIN food_item_food_type NATURAL JOIN food_establishment {whereclause} GROUP BY food_id {orderclause};"
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        return result

    def verify_credentials(self, email, password, login_window):
        # Retrieve the stored email and password
        sql_statement = "SELECT email, password FROM CUSTOMER WHERE email = %s"
        self.cursor.execute(sql_statement, (email,))
        user_record = self.cursor.fetchone()

        if user_record:
            stored_email, stored_password = user_record
            # Decrypt the stored password
            decrypted_password = self.encryption_helper.decrypt(stored_password)
            # Compare the decrypted password with the provided password
            if decrypted_password == password:
                data_file = open("data_file.txt", "w")
                QueriesAPI.logged_user = (stored_email,)
                messagebox.showinfo("Login", "User logged in successfully!")
                #encrypt email then write to an external text file
                encrypted_email = self.encryption_helper.encrypt(email)
                data_file.write(encrypted_email)
                login_window.destroy()
                subprocess.Popen([sys.executable, "./pages/DashboardPage.py"], shell=True)
                data_file.close()
                return QueriesAPI.logged_user
            else:
                # If the credentials do not match, show an error message
                messagebox.showerror("Login Error", "Invalid email or password")
        else:
            messagebox.showwarning("Login Warning", "Account does not exist. Please register.")

        return None

    # ----- INSERT STATEMENTS -----
    def create_account(self, email, real_name, username, password, register_window):
        email = email.strip()

        # Check if email is already registered
        check_email_query = "SELECT COUNT(*) FROM CUSTOMER WHERE email = %s"
        self.cursor.execute(check_email_query, (email,))
        result = self.cursor.fetchone()
        if result[0] > 0:
            messagebox.showerror("Duplicate Email", "The email address you provided is already registered.")
            return


        # Encrypt the password before saving it
        encrypted_password = self.encryption_helper.encrypt(password)
        sql_statement = "INSERT INTO CUSTOMER (email, real_name, user_name, password, num_reviews) VALUES (%s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql_statement, (email, real_name, username, encrypted_password, 0))
            self.conn.commit()
            messagebox.showinfo("Register", "Account created successfully!")
            register_window.destroy()
            subprocess.Popen([sys.executable, "./pages/LoginPage.py"], shell=True)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")

    def add_review(self, rating, food_id, estab_id, review, window):
        # Check if either food_id or estab_id is provided
        if food_id == '' and estab_id == '':
            messagebox.showerror("Invalid Input", "Either Food ID or Estab ID should be provided!")
            return

        # Fetch the user details
        user_details = self.fetch_user_details()
        if user_details is None or len(user_details) == 0:
            messagebox.showerror("Invalid User", "The user is not logged in or does not exist.")
            return

        # Assuming user_details is a list of tuples
        email = user_details[0][0]
        maxquery = "SELECT MAX(review_id) from REVIEW;"
        self.cursor.execute(maxquery)
        max = self.cursor.fetchall()
        # Checks if there are no reviews, if none, default is 1
        if isinstance(max[0][0], type(None)):
            reviewid = 1
        else:
            reviewid = max[0][0] + 1

        # Converted food IDs and estab IDs from list to set
        food_id_list = self.select_all_food_ids()
        estab_id_list = self.select_all_estab_ids()
        food_id_set = set()
        estab_id_set = set()

        for i in food_id_list:
            food_id_set.add(i)

        for j in estab_id_list:
            estab_id_set.add(j)

        # Check if food_id and estab_id are valid
        if food_id != '' and food_id in food_id_set:
            messagebox.showerror("Invalid Food ID", "The food ID is not present in the database.")
            return
        if estab_id != '' and estab_id in estab_id_set:
            messagebox.showerror("Invalid Establishment ID", "The establishment ID is not present in the database.")
            return

        datereviewed = datetime.now().strftime("%Y-%m-%d")

        # Prepare the SQL statement
        food_id = 'NULL' if food_id == '' else food_id
        estab_id = 'NULL' if estab_id == '' else estab_id

        reviewInsert = f'''INSERT INTO REVIEW(review_id, rating, rev_date, rev_stat, email, estab_id, food_id) VALUES ({reviewid}, {rating}, '{datereviewed}', '{review}', '{email}', {estab_id}, {food_id})'''

        # Insert review into the database
        try:
            self.cursor.execute(reviewInsert)
            self.conn.commit()

            # Count the number of reviews
            review_count = self.count_reviews()

            # Update the num_reviews column for the logged-in user
            self.cursor.execute(f"UPDATE customer SET num_reviews = {review_count} WHERE email = '{email}'")
            self.conn.commit()

            messagebox.showinfo("Success", "Review added successfully!")

        except mysql.connector.Error:
            messagebox.showerror("Database Error", f"One or both of the IDs is not present in the database.")

    def add_food_estab(self, estab_name, estab_desc, loc, serv_mod, contact):
        sql_statement = 'SELECT estab_id FROM FOOD_ESTABLISHMENT ORDER BY estab_id DESC'
        self.cursor.execute(sql_statement)
        result = self.cursor.fetchall()
        if(result == []):
            newId = 1
        else:
            newId = result[0][0] + 1
        

        for i in loc: 
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_LOCATION(estab_id, loc) VALUES (%s, %s)'
            self.cursor.execute(sql_statement, (newId,  i.strip()))
        for i in serv_mod:
           sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_MODE_OF_SERVICE(estab_id, serv_mod) VALUES (%s, %s)'
           self.cursor.execute(sql_statement, (newId,  i.strip()))

        for i in contact:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_CONTACT(estab_id, contact) VALUES (%s, %s)'
            self.cursor.execute(sql_statement, (newId,  i.strip()))

        sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT(estab_id, estab_desc, estab_name) VALUES  (%s, %s, %s)'
        self.cursor.execute(sql_statement, (newId, estab_desc.strip(), estab_name.strip()))

        self.conn.commit()
        addedFoodEstab = self.select_food_estab_by_id(str(newId))
        return addedFoodEstab

    def add_food(self, name_text, price_text, type_text, esid_text, desc_text, window):
        maxquery = "SELECT MAX(food_id) from food_item;"
        self.cursor.execute(maxquery)
        max = self.cursor.fetchall()
        if isinstance(max[0][0], type(None)):
            foodid = 1
        else:
            foodid = max[0][0] + 1
        foodname = name_text.get()
        foodprice = price_text.get()
        foodtype = [type_text.get()]
        estabid = esid_text.get()
        fooddesc = desc_text.get("1.0",'end-1c')
        foodtype_quarray = []

        if(estabid != ''):
            self.cursor.execute(f"SELECT * FROM food_establishment WHERE estab_id = {estabid}")
            estab_query = self.cursor.fetchall()
            if(estab_query == []):
                messagebox.showerror("Establishment Not Found", f"No establishment was found with the entered id!")
                return

        if(',' in foodtype[0]):
            foodtypearray = foodtype[0].replace(" ", "").split(',')
            for i in foodtypearray:
                i = i.capitalize()
                foodtype_quarray.append(f'''INSERT INTO FOOD_ITEM_FOOD_TYPE(food_id, food_type) VALUES ({foodid}, "{i}");''')
        else:
            foodtype_quarray.append(f'''INSERT INTO FOOD_ITEM_FOOD_TYPE(food_id, food_type) VALUES ({foodid},"{foodtype[0]}");''')

        foodInsert = f'''INSERT INTO FOOD_ITEM(food_id, food_name, food_desc, price, estab_id) VALUES ({foodid}, "{foodname}", "{fooddesc}", {foodprice}, {estabid});'''

        try:
            self.cursor.execute(foodInsert)
            for i in foodtype_quarray:
                print(i)
                self.cursor.execute(i)
            self.conn.commit()
            messagebox.showinfo("Add Food", "Food posted!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        
    # ----- UPDATE STATEMENTS -----
    def update_review(self, review_id, new_rating, new_review_text, estab_id, food_id):
        # Check if user is logged in
        user_details = self.fetch_user_details()
        if user_details is None or len(user_details) == 0:
            messagebox.showerror("Invalid User", "The user is not logged in or does not exist.")
            return
        email = user_details[0][0]
        print(email)

        # Check if user is an admin or not
        if not self.admin_perms_check(review_id):
            messagebox.showerror("Permission Denied", "You do not have permission to update this review.")
            return

        # Converted food IDs and estab IDs from list to set
        food_id_list = self.select_all_food_ids()
        estab_id_list = self.select_all_estab_ids()
        food_id_set = set()
        estab_id_set = set()

        for i in food_id_list:
            food_id_set.add(i)

        for j in estab_id_list:
            estab_id_set.add(j)

        # Check if food_id and estab_id are valid
        if food_id != '' and food_id in food_id_set:
            messagebox.showerror("Invalid Food ID", "The Food ID is not present in the database.")
            return
        if estab_id != '' and estab_id in estab_id_set:
            messagebox.showerror("Invalid Establishment ID", "The establishment ID is not present in the database.")
            return
        
        # Check if estab_id or food_id is an empty string
        estab_id = None if estab_id == "" else estab_id
        food_id = None if food_id == "" else food_id

        # SQL query to update the review
        sql_statement = """UPDATE REVIEW
                        SET rating = %s, rev_stat = %s, estab_id = %s, food_id = %s
                        WHERE review_id = %s"""
        try:
            self.cursor.execute(sql_statement, (new_rating, new_review_text, estab_id, food_id, review_id))
            self.conn.commit()
            messagebox.showinfo("Update Review", "Review updated successfully!")
            return
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def update_food_item(self, foodid, name, price, type, estid, desc):
        if(estid != ''):
            self.cursor.execute(f"SELECT * FROM food_establishment WHERE estab_id = {estid}")
            estab_query = self.cursor.fetchall()
            if(estab_query == []):
                messagebox.showerror("Establishment Not Found", f"No establishment was found with the entered id!")
                return
            
        update_fooditem = f'''UPDATE food_item SET food_name = "{name}", food_desc = "{desc}", price = {price}, estab_id = {estid} WHERE food_id = {foodid};'''
        update_foodtype = []
        foodtypearray = type.replace(" ", "").split(',')

        existing_ft_query = f'''SELECT food_type FROM food_item_food_type WHERE food_id = {foodid};'''
        self.cursor.execute(existing_ft_query)
        existing_ft = self.cursor.fetchall()

        if(len(existing_ft) < len(foodtypearray)):
            counter = 0
            for i in range(0, len(existing_ft)):
                update_foodtype.append(f'''UPDATE food_item_food_type SET food_type = "{foodtypearray[i].capitalize()}" WHERE food_id = {foodid} AND food_type = "{existing_ft[i][0]}";''')
                counter+=1
            for i in range (counter, len(foodtypearray)):
                update_foodtype.append(f'''INSERT INTO FOOD_ITEM_FOOD_TYPE(food_id, food_type) VALUES ({foodid},"{foodtypearray[i].capitalize()}");''')
        elif(len(existing_ft) > len(foodtypearray)):
            counter = 0
            for i in range(counter, len(foodtypearray)):
                if(counter <= len(existing_ft)):
                    update_foodtype.append(f'''UPDATE food_item_food_type SET food_type = "{foodtypearray[i].capitalize()}" WHERE food_id = {foodid} AND food_type = "{existing_ft[i][0]}";''')
                    counter+=1
                else:
                    break
            print(len(existing_ft))
            for j in range(counter, len(existing_ft)):
                print("DELETEs")
                update_foodtype.append(f'''DELETE FROM food_item_food_type WHERE food_id = {foodid} AND food_type = "{existing_ft[j][0]}";''')
        elif(len(existing_ft) == len(foodtypearray)):
            for i in range(0, len(existing_ft)):
                update_foodtype.append(f'''UPDATE food_item_food_type SET food_type = "{foodtypearray[i].capitalize()}" WHERE food_id = {foodid} AND food_type = "{existing_ft[i][0]}";''')
            
        try:
            print(update_foodtype)
            self.cursor.execute(update_fooditem)
            for i in update_foodtype:
                self.cursor.execute(i)
            self.conn.commit()
            messagebox.showinfo("Edit Food", "Food updated!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def update_food_estab_by_id(self, id, estab_name, estab_desc, loc, serv_mod, contact):
        sql_statement = 'UPDATE FOOD_ESTABLISHMENT SET estab_desc=%s, estab_name=%s WHERE estab_id=%s'
        self.cursor.execute(sql_statement, (estab_desc.strip(), estab_name.strip(), id))

        sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_CONTACT WHERE estab_id=%s'
        self.cursor.execute(sql_statement, [id])
        sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_LOCATION WHERE estab_id=%s'
        self.cursor.execute(sql_statement, [id])
        sql_statement = 'DELETE FROM FOOD_ESTABLISHMENT_MODE_OF_SERVICE WHERE estab_id=%s'
        self.cursor.execute(sql_statement, [id])

        for contactDetail in contact:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_CONTACT(estab_id, contact) VALUES(%s, %s)'
            self.cursor.execute(sql_statement, (id, contactDetail.strip()))

        for location in loc:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_LOCATION(estab_id, loc) VALUES(%s, %s)'
            self.cursor.execute(sql_statement, (id, location.strip()))

        for modeOfService in serv_mod:
            sql_statement = 'INSERT INTO FOOD_ESTABLISHMENT_MODE_OF_SERVICE(estab_id, serv_mod) VALUES(%s, %s)'
            self.cursor.execute(sql_statement, (id, modeOfService.strip()))

        self.conn.commit()
        messagebox.showinfo("Establishment Updated", "Updated details of establishment.")
        updatedFoodEstab = self.select_food_estab_by_id(id)
        return updatedFoodEstab


    # ----- DELETE STATEMENTS -----
    def admin_perms_check(self, review_id):
        # Fetch the details of the logged-in user
        user_details = self.fetch_user_details()
        if user_details is None or len(user_details) == 0:
            messagebox.showerror("Invalid User", "The user is not logged in or does not exist.")
            return False

        # Assuming user_details is a list of tuples
        user_email = user_details[0][0]

        # Fetch the details of the review
        review_details = self.select_email_by_revid(review_id, user_email)
        if review_details:
            review_email = review_details[0][0]
        else:
            review_email = None

        # If the user is an admin, they can delete any review
        if 'admin' in user_email:
            return True

        # If the user is not an admin, they can only delete their own reviews
        if user_email == review_email:
            return True
        return False
    
    def isAdmin(self):
        user_details = self.fetch_user_details()
        user_email = user_details[0][0]
        if user_details is None or len(user_details) == 0:
            messagebox.showerror("Invalid User", "The user is not logged in or does not exist.")
            return False
        if 'admin' in user_email:
            return True
        return False
    
    def count_reviews(self):
        # Fetch user details
        user_details = self.fetch_user_details()
        email = user_details[0][0]

        # Check if user is admin
        if 'admin' in email:
            # Execute SQL query to count the total number of reviews
            self.cursor.execute("SELECT COUNT(*) FROM review")
            total_reviews = self.cursor.fetchone()[0]
            return total_reviews
        else:
            # If user is not admin, count the number of reviews made by the user
            self.cursor.execute(f"SELECT COUNT(*) FROM review WHERE email = '{email}'")
            user_reviews = self.cursor.fetchone()[0]
            return user_reviews
    
    def delete_review(self, review_id):
        if not review_id.isdigit():
            return "Review ID must be a number."

        # Check if the user has permission to delete the review
        if not self.admin_perms_check(review_id):
            messagebox.showerror("Permission Denied", "You do not have permission to delete this review.")
            return

        if(review_id != ''):
            self.cursor.execute(f"SELECT * FROM review WHERE review_id = {review_id}")
            review_search = self.cursor.fetchall()
            if(review_search != []):
                # Delete the review
                self.cursor.execute(f"DELETE FROM review WHERE review_id = '{review_id}'")
                self.conn.commit()

                # Count the number of reviews
                review_count = self.count_reviews()

                # Update the num_reviews column for the logged-in user
                user_details = self.fetch_user_details()
                email = user_details[0][0]
                sql_statement = 'UPDATE customer SET num_reviews = %s WHERE email = %s'
                self.cursor.execute(sql_statement, (review_count, email))
                self.conn.commit()

                messagebox.showinfo("Success", "Review deleted successfully!")
                return None
            else:
                return "No review was found with the entered id!"
        else:
            return "Review ID cannot be empty."

    def delete_food_item(self, foodid):
        if(foodid != ''):
            self.cursor.execute(f"SELECT * FROM food_item WHERE food_id = {foodid}")
            food_search = self.cursor.fetchall()
            if(food_search != []):
                delete_fi = f'''DELETE FROM food_item WHERE food_id = "{foodid}";'''
                delete_fift = f'''DELETE FROM food_item_food_type WHERE food_id = "{foodid};"'''               
                try:
                    self.cursor.execute(delete_fi)
                    self.cursor.execute(delete_fift)
                    self.conn.commit()
                    messagebox.showinfo("Delete Food", "Food deleted!")
                    return True
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error: {err}")
            else:
                return False
                
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