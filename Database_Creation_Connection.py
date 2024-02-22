#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector as connector

# Connect to MySQL
connection = connector.connect(user="root", password="")
cursor = connection.cursor()

# Create database
cursor.execute("DROP DATABASE IF EXISTS little_lemon_db_1")  # Optional: remove this line if you don't want to drop the existing database
cursor.execute("CREATE DATABASE little_lemon_db_1")
cursor.execute("USE little_lemon_db_1")


# In[7]:


# Create Tables
create_menuitems_table = """
CREATE TABLE IF NOT EXISTS MenuItems (
  ItemID INT AUTO_INCREMENT,
  Name VARCHAR(200),
  Type VARCHAR(100),
  Price DECIMAL(10,2),
  PRIMARY KEY (ItemID)
);
"""

create_menus_table = """
CREATE TABLE IF NOT EXISTS Menus (
  MenuID INT AUTO_INCREMENT,
  Cuisine VARCHAR(100),
  PRIMARY KEY (MenuID)
);
"""

create_employees_table = """
CREATE TABLE IF NOT EXISTS Employees (
  EmployeeID INT AUTO_INCREMENT,
  Name VARCHAR(255),
  Role VARCHAR(100),
  Address VARCHAR(255),
  Contact_Number VARCHAR(20),
  Email VARCHAR(255),
  Annual_Salary DECIMAL(10,2),
  PRIMARY KEY (EmployeeID)
);
"""

create_bookings_table = """
CREATE TABLE IF NOT EXISTS Bookings (
  BookingID INT AUTO_INCREMENT,
  TableNo INT,
  GuestFirstName VARCHAR(100) NOT NULL,
  GuestLastName VARCHAR(100) NOT NULL,
  BookingSlot TIME NOT NULL,
  EmployeeID INT,
  FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
  PRIMARY KEY (BookingID)
);
"""

create_menuitems_menus_table = """
CREATE TABLE IF NOT EXISTS MenuItems_Menus (
  MenuItemID INT,
  MenuID INT,
  FOREIGN KEY (MenuItemID) REFERENCES MenuItems(ItemID),
  FOREIGN KEY (MenuID) REFERENCES Menus(MenuID),
  PRIMARY KEY (MenuItemID, MenuID)
);
"""

create_orders_table = """
CREATE TABLE IF NOT EXISTS Orders (
  OrderID INT AUTO_INCREMENT,
  TableNo INT,
  MenuID INT,
  BookingID INT,
  BillAmount DECIMAL(10,2),
  Quantity INT,
  PRIMARY KEY (OrderID),
  FOREIGN KEY (MenuID) REFERENCES Menus(MenuID),
  FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);
"""


# In[8]:


# Create MenuItems table
cursor.execute(create_menuitems_table)

# Create Menu table
cursor.execute(create_menus_table)

# Create Bookings table
cursor.execute(create_employees_table)

# Create Orders table
cursor.execute(create_bookings_table)

# Create Employees table
cursor.execute(create_menuitems_menus_table)

cursor.execute(create_orders_table)


# In[9]:


# Insert sample data
insert_menuitems = """
INSERT INTO MenuItems (Name, Type, Price) VALUES
('Olives', 'Starters', 5.00),
('Flatbread', 'Starters', 5.00),
('Minestrone', 'Starters', 8.00),
('Tomato bread', 'Starters', 8.00),
('Falafel', 'Starters', 7.00),
('Hummus', 'Starters', 5.00),
('Greek salad', 'Main Courses', 15.00),
('Bean soup', 'Main Courses', 12.00),
('Pizza', 'Main Courses', 15.00),
('Greek yoghurt', 'Desserts', 7.00),
('Ice cream', 'Desserts', 6.00),
('Cheesecake', 'Desserts', 4.00),
('Athens White wine', 'Drinks', 25.00),
('Corfu Red Wine', 'Drinks', 30.00),
('Turkish Coffee', 'Drinks', 10.00),
('Kabasa', 'Main Courses', 17.00);
"""

insert_menus = """
INSERT INTO Menus (Cuisine) VALUES
('Greek'),
('Italian'),
('Turkish');
"""

# Note: Adjust MenuID and ItemID according to actual IDs after inserts
insert_menuitems_menus = """
INSERT INTO MenuItems_Menus (MenuItemID, MenuID) VALUES
(1, 1),
(7, 1),
(10, 1),
(13, 1),
(3, 2),
(9, 2),
(12, 2),
(15, 2),
(5, 3),
(16, 3),
(11, 3);
"""

insert_employees = """
INSERT INTO Employees (Name, Role, Address, Contact_Number, Email, Annual_Salary) VALUES
('Mario Gollini', 'Manager', '724 Parsley Lane, Old Town, Chicago, IL', '351258074', 'Mario.g@littlelemon.com', 70000.00),
('Adrian Gollini', 'Assistant Manager', '334 Dill Square, Lincoln Park, Chicago, IL', '351474048', 'Adrian.g@littlelemon.com', 65000.00),
('Giorgos Dioudis', 'Head Chef', '879 Sage Street, West Loop, Chicago, IL', '351970582', 'Giorgos.d@littlelemon.com', 50000.00),
('Fatma Kaya', 'Assistant Chef', '132 Bay Lane, Chicago, IL', '351963569', 'Fatma.k@littlelemon.com', 45000.00),
('Elena Salvai', 'Head Waiter', '989 Thyme Square, EdgeWater, Chicago, IL', '351074198', 'Elena.s@littlelemon.com', 40000.00),
('John Millar', 'Receptionist', '245 Dill Square, Lincoln Park, Chicago, IL', '351584508', 'John.m@littlelemon.com', 35000.00);
"""

insert_bookings = """
INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES
(12, 'Anna', 'Iversen', '19:00:00', 1),
(19, 'Vanessa', 'McCarthy', '15:00:00', 3),
(15, 'Marcos', 'Romero', '17:30:00', 4),
(5, 'Hiroki', 'Yamane', '18:30:00', 2),
(8, 'Diana', 'Pinto', '20:00:00', 5);
"""

insert_orders = """
INSERT INTO Orders (TableNo, MenuID, BookingID, Quantity, BillAmount) VALUES
(12, 1, 1, 2, 86.00),
(19, 2, 2, 1, 37.00),
(15, 2, 3, 1, 37.00),
(5, 3, 4, 1, 40.00),
(8, 1, 5, 1, 43.00);
"""

# Execute insert queries
insert_queries = [insert_menuitems, insert_menus, insert_menuitems_menus,
                  insert_employees, insert_bookings, insert_orders]

for query in insert_queries:
    cursor.execute(query)

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()

print("Database, tables, and sample data created successfully.")


# In[ ]:





# In[ ]:


#Below is the code for the procedures, I entered this into the MYSQL Command Line Interafce

DELIMITER $$

CREATE PROCEDURE GetMaxQuantity(IN itemID INT)
BEGIN
  SELECT MAX(Quantity) AS MaxQuantity
  FROM Orders
  WHERE ItemID = itemID;
END$$

DELIMITER ;


# In[ ]:


DELIMITER $$

CREATE PROCEDURE ManageBooking(IN bookingDate DATE, IN bookingSlot TIME, OUT availableTables INT)
BEGIN
  SELECT COUNT(TableNo) INTO availableTables
  FROM Bookings
  WHERE BookingSlot = bookingSlot
  AND BookingDate = bookingDate;
END$$

DELIMITER ;


# In[ ]:


DELIMITER $$

CREATE PROCEDURE UpdateBooking(IN bookingID INT, IN guestFirstName VARCHAR(100), IN guestLastName VARCHAR(100), IN bookingSlot TIME)
BEGIN
  UPDATE Bookings
  SET GuestFirstName = guestFirstName, GuestLastName = guestLastName, BookingSlot = bookingSlot
  WHERE BookingID = bookingID;
END$$

DELIMITER ;


# In[ ]:


DELIMITER $$

CREATE PROCEDURE AddBooking(IN tableNo INT, IN guestFirstName VARCHAR(100), IN guestLastName VARCHAR(100), IN bookingSlot TIME, IN employeeID INT)
BEGIN
  INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID)
  VALUES (tableNo, guestFirstName, guestLastName, bookingSlot, employeeID);
END$$

DELIMITER ;


# In[ ]:


DELIMITER $$

CREATE PROCEDURE CancelBooking(IN bookingID INT)
BEGIN
  DELETE FROM Bookings WHERE BookingID = bookingID;
END$$

DELIMITER ;


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




