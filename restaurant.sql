--> GROUP 1

--> Project Milestone 3

--> De Castro, Nico
--> Olano, Kenneth  
--> Ramos, John Miles
--> Tandang, Bernard Jezua


DROP DATABASE IF EXISTS `restaurant`;

CREATE OR REPLACE USER 'restaurant'@'localhost' IDENTIFIED BY 'foodreview';
CREATE DATABASE IF NOT EXISTS `restaurant`;
GRANT ALL ON restaurant.* TO 'restaurant'@'localhost';

USE `restaurant`;
-- CREATE TABLES

-- Creating the CUSTOMER table
CREATE TABLE CUSTOMER(
    email VARCHAR(50) NOT NULL PRIMARY KEY,
    real_name VARCHAR(50) NOT NULL,
    user_name VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    num_reviews INT(5) NOT NULL DEFAULT 0
);

-- Creating the FOOD_ESTABLISHMENT table

CREATE TABLE FOOD_ESTABLISHMENT(
    estab_id INT(5) NOT NULL PRIMARY KEY,
    estab_desc VARCHAR(999),
    estab_name VARCHAR(20) NOT NULL
);

-- Creating the FOOD_ESTABLISHMENT_LOCATION table

CREATE TABLE FOOD_ESTABLISHMENT_LOCATION(
	estab_id INT(5) NOT NULL,
	loc VARCHAR(50) NOT NULL,
	CONSTRAINT PRIMARY KEY(estab_id, loc)
);

-- Creating the FOOD_ESTABLISHMENT_MODE_OF_SERVICE table

CREATE TABLE FOOD_ESTABLISHMENT_MODE_OF_SERVICE(
	estab_id INT(5) NOT NULL,
	serv_mod VARCHAR(50) NOT NULL,
	CONSTRAINT PRIMARY KEY(estab_id, serv_mod)
);

-- Creating the FOOD_ESTABLISHMENT_CONTACT_DETAIL table

CREATE TABLE FOOD_ESTABLISHMENT_CONTACT(
	estab_id INT(5) NOT NULL,
	contact VARCHAR(50) NOT NULL,
	CONSTRAINT PRIMARY KEY(estab_id, contact)
);

-- Creating the FOOD_ITEM table

CREATE TABLE FOOD_ITEM(
    food_id INT(5) NOT NULL PRIMARY KEY,
    food_name VARCHAR(50) NOT NULL,
    food_desc VARCHAR(999) NOT NULL,
    price DECIMAL(10, 2) NOT NULL DEFAULT 0,
    estab_id INT(5),
    CONSTRAINT fooditem_estabid_fk FOREIGN KEY(estab_id) REFERENCES FOOD_ESTABLISHMENT(estab_id) ON DELETE SET NULL
);

-- Creating the FOOD_ITEM_FOOD_TYPE table

CREATE TABLE FOOD_ITEM_FOOD_TYPE(
	food_id INT(5) NOT NULL,
	food_type VARCHAR(50) NOT NULL,
	CONSTRAINT PRIMARY KEY(food_id, food_type)
);

-- Creating the REVIEW table

CREATE TABLE REVIEW(
    review_id INT(5) NOT NULL PRIMARY KEY,
    rating INT(2) NOT NULL DEFAULT 0,
    rev_date DATE NOT NULL DEFAULT CURDATE(),
    rev_stat VARCHAR(999) NOT NULL,
    email VARCHAR(50),
    estab_id INT(5),
    food_id INT(5),
    CONSTRAINT review_email_fk FOREIGN KEY(email) REFERENCES CUSTOMER(email) ON DELETE SET NULL,
    CONSTRAINT review_estabid_fk FOREIGN KEY(estab_id) REFERENCES FOOD_ESTABLISHMENT(estab_id) ON DELETE SET NULL,
    CONSTRAINT review_foodid_fk FOREIGN KEY(food_id) REFERENCES FOOD_ITEM(food_id) ON DELETE SET NULL
);

-- INSERT TABLES

-- Inserting dummy data into the CUSTOMER table
INSERT INTO CUSTOMER(email, real_name, user_name, password, num_reviews) VALUES 
('customer1@email.com', 'Customer One', 'custone', 'password1', 5),
('customer2@email.com', 'Customer Two', 'custtwo', 'password2', 10),
('customer3@email.com', 'Customer Three', 'custthree', 'password3', 15),
('customer4@email.com', 'Customer Four', 'custfour', 'password4', 20),
('customer5@email.com', 'Customer Five', 'custfive', 'password5', 25);

-- Inserting dummy data into the FOOD_ESTABLISHMENT table
INSERT INTO FOOD_ESTABLISHMENT(estab_id, estab_desc, estab_name) VALUES 
(1, 'Fast food restaurant', 'WcDonald'),
(2, 'Casual diner', 'Four Guys'),
(3, 'Fine dining restaurant', 'Fine Diners'),
(4, 'Cafe', 'Cafe Comforts'),
(5, 'Bakery', 'Bakery Bites');

-- Inserting dummy data into the FOOD_ESTABLISHMENT_LOCATION table
INSERT INTO FOOD_ESTABLISHMENT_LOCATION(estab_id, loc) VALUES
(1, 'Tokyo'),
(2, 'Quezon City'),
(3, 'Los Banos'),
(4, 'San Francisco'),
(5, 'Paris');

-- Inserting dummy data into the FOOD_ESTABLISHMENT_MODE_OF_SERVICE table
INSERT INTO FOOD_ESTABLISHMENT_MODE_OF_SERVICE(estab_id, serv_mod) VALUES
(1, 'Take Out'),
(2, 'Dine In'),
(3, 'Dine In'),
(4, 'Pick Up'),
(5, 'Delivery');

-- Inserting dummy data into the FOOD_ESTABLISHMENT_CONTACT_DETAIL table
INSERT INTO FOOD_ESTABLISHMENT_CONTACT(estab_id, contact) VALUES
(1, '+639876543217'),
(2, '+639123516718'),
(3, '+639879193454'),
(4, 'customer@cafecomforts.ph'),
(5, 'bakerybites@shop.ph');

-- Inserting dummy data into the FOOD_ITEM table
INSERT INTO FOOD_ITEM(food_id, food_name, food_desc, price, estab_id) VALUES
(1, 'Cheese WcBurger', 'Classic all-beef patty with cheese, lettuce, tomato, and onion on a toasted bun', 170, 1),
(2, 'Buttermilk Pancakes', 'Stack of fluffy pancakes served with butter and maple syrup', 159, 5),
(3, 'Ham and Cheese Sandwich', 'Classic sandwich with ham, cheese, lettuce, tomato, and mayonnaise on toasted bread', 149, 4),
(4, 'Tapsilog', 'Beef strips with sunny side up and fried rice', 69, 1),
(5, 'Honey Buttered Fish Fillet', 'Fresh fish fillet seasoned with herbs and spices with honey butter sauce', 127, 3), 
(6, 'Pork Sinigang', 'Sour and savory pork soup with vegetables', 100, 3), 
(7, 'Curly Fries', 'Curled up, fried potato strips, lightly salted', 45, 2);

-- Inserting dummy data into the FOOD_ITEM_FOOD_TYPE table
INSERT INTO FOOD_ITEM_FOOD_TYPE(food_id, food_type) VALUES 
(1, 'Breakfast'),
(2, 'Lunch'),
(3, 'Breakfast'),
(4, 'Lunch'),
(5, 'Breakfast'),
(6, 'Dinner'),
(7, 'Dinner');

-- Inserting dummy data into the REVIEW table
INSERT INTO REVIEW(review_id, rating, rev_date, rev_stat, email, estab_id, food_id) VALUES
(1, 5, '2024-05-01', 'Saks lang beh', 'customer1@email.com', 1, 1),
(2, 4, '2020-10-01', 'Goods lang pre', 'customer2@email.com', 1, 4),
(3, 2, '2021-03-16', 'Sarap niya guys', 'customer3@email.com', 2, 7),
(4, 3, '2022-02-06', 'Budget friendly', 'customer4@email.com', 2, 7),
(5, 1, '2023-11-03', 'Mas masarap sa kabila', 'customer5@email.com', 3, 6),
(6, 5, '2024-05-03', 'My favorite place', 'customer1@email.com', 3, 5),
(7, 3, '2023-01-02', 'Okay food', 'customer2@email.com', 4, 3),
(8, 1, '2024-04-03', 'Waiting time is too long for a sandwich', 'customer3@email.com', 4, 3),
(9, 4, '2022-06-12', 'Fluffy pancakes yummy frfr', 'customer4@email.com', 5, 2),
(10, 5, '2024-05-05', 'The best in the country', 'customer5@email.com', 5, 2);




-- UPDATE TABLES

-- Update data from FOOD_ITEM table
UPDATE FOOD_ITEM SET food_name='WcFries', food_desc='Cheesy fries with bacon bits', price=99 WHERE food_id=1;
UPDATE FOOD_ITEM SET food_name='Fried Oreos', food_desc='Oreo bathed in creamy, delicious pancake mix', price=79 WHERE food_id=3;


-- DELETE TABLES
-- Delete a review with a rating less than 3
DELETE FROM REVIEW WHERE rating < 3;
-- Delete a food item with a price greater than 110
DELETE FROM FOOD_ITEM WHERE price > 110;
-- Delete a customer whose number of reviews are less than 10
DELETE FROM CUSTOMER WHERE num_reviews <= 10;


-- BASIC SELECT
-- Basic Select
USE restaurant;
SELECT * FROM CUSTOMER;
SELECT * FROM FOOD_ESTABLISHMENT;
SELECT * FROM FOOD_ESTABLISHMENT_CONTACT;
SELECT * FROM FOOD_ESTABLISHMENT_LOCATION;
SELECT * FROM FOOD_ESTABLISHMENT_MODE_OF_SERVICE;
SELECT * FROM FOOD_ITEM;
SELECT * FROM FOOD_ITEM_FOOD_TYPE;
SELECT * FROM REVIEW;


-- SELECT for Report Generation
-- Select for Report Generation


USE restaurant;

--> 1. View all food establishments;

SELECT * FROM FOOD_ESTABLISHMENT;

--> 2. View all food reviews for an establishment or a food item; 

-- View all food reviews for an establishment given establishment id
SELECT review_id, rating, rev_date, rev_stat, email, (SELECT food_name FROM FOOD_ITEM fi WHERE fi.food_id=r.food_id) food_name, estab_name FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id WHERE r.estab_id=2;

-- View all food reviews for an establishment given establishment name
SELECT review_id, rating, rev_date, rev_stat, email, (SELECT food_name FROM FOOD_ITEM fi WHERE fi.food_id=r.food_id) food_name, estab_name FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id WHERE f.estab_name='Fine Diners';

-- View all food reviews for a food item given food id
SELECT review_id, rating, rev_date, rev_stat, email, food_name, (SELECT estab_name FROM FOOD_ESTABLISHMENT fe WHERE fe.estab_id=r.estab_id) estab_name FROM FOOD_ITEM f JOIN REVIEW r ON f.estab_id=r.estab_id WHERE r.food_id=7;

-- View all food reviews for a food item given food name
SELECT review_id, rating, rev_date, rev_stat, email, food_name, (SELECT estab_name FROM FOOD_ESTABLISHMENT fe WHERE fe.estab_id=r.estab_id) estab_name FROM FOOD_ITEM f JOIN REVIEW r ON f.estab_id=r.estab_id WHERE f.food_name='Pork Sinigang';

--> 3. View all food items from an establishment;

-- View all food items from an establishment given establishment id
SELECT * FROM FOOD_ITEM WHERE estab_id=2;

-- View all food items from an establishment given establishment name
SELECT * FROM FOOD_ITEM WHERE estab_id=(SELECT estab_id FROM FOOD_ESTABLISHMENT where estab_name='WcDonald');

--> 4. View all food items from an establishment that belong to a food type {meat | veg | etc.};

SELECT fi.food_id, food_name, food_desc, price, (SELECT estab_name FROM FOOD_ESTABLISHMENT where estab_id=fi.estab_id) AS estab_name, food_type FROM FOOD_ITEM fi JOIN FOOD_ITEM_FOOD_TYPE ft ON fi.food_id=ft.food_id WHERE estab_id=(SELECT estab_id FROM FOOD_ESTABLISHMENT where estab_name='WcDonald') AND ft.food_type='Breakfast';

--> 5. View all reviews made within a month for an establishment or a food item;

SELECT review_id, rating, rev_date, rev_stat, email, (SELECT estab_name FROM FOOD_ESTABLISHMENT fe WHERE fe.estab_id=r.estab_id) AS estab_name, (SELECT food_name FROM FOOD_ITEM fi WHERE fi.food_id=r.food_id) AS food_name FROM REVIEW r WHERE MONTH(rev_date)=MONTH(CURDATE());

--> 6. View all establishments with a high average rating (rating >= 4). (ratings from 1-5; highest is 5);

SELECT * FROM (SELECT r.estab_id, estab_name, SUM(rating)/COUNT(review_id) AS average_rating FROM FOOD_ESTABLISHMENT f JOIN REVIEW r ON f.estab_id=r.estab_id GROUP BY estab_name ORDER BY average_rating DESC) as estab_ave_rating WHERE average_rating >= 4;

--> 7. View all food items from an establishment arranged according to price;

-- View food items from establishment ordered by price given estab_name
SELECT food_id, food_name, food_desc, price, estab_name FROM FOOD_ITEM fi JOIN FOOD_ESTABLISHMENT fe ON fi.estab_id=fe.estab_id WHERE fe.estab_name='WcDonald' ORDER BY price;

-- View food item from establishment ordered by price given estab_id
SELECT food_id, food_name, food_desc, price, estab_name FROM FOOD_ITEM fi JOIN FOOD_ESTABLISHMENT fe ON fi.estab_id=fe.estab_id WHERE fi.estab_id='1' ORDER BY price;

--> 8. Search food items from any establishment based on a given price range and/or food type.

-- Search food items from any establishment based on a given price range
SELECT food_id, food_name, food_desc, price, (SELECT estab_name FROM FOOD_ESTABLISHMENT fe WHERE fe.estab_id=fi.estab_id) AS estab_name FROM FOOD_ITEM fi WHERE price > 100 AND price < 200 ORDER BY price;

-- Search food items from any establishment based on food type
SELECT fi.food_id, food_name, food_desc, price, (SELECT estab_name FROM FOOD_ESTABLISHMENT fe WHERE fe.estab_id=fi.estab_id) AS estab_name, food_type FROM FOOD_ITEM fi JOIN FOOD_ITEM_FOOD_TYPE ft ON fi.food_id=ft.food_id WHERE food_type='Breakfast';