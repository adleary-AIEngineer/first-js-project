# Data Access Layer
# Open a connection.
    # connection = sqlite3.connect("expenses.db")
# Create a cursor.
    # cursor = connection.cursor()
# Execute your CREATE TABLE IF NOT EXISTS.
    #cursor.execute(CREATE TABLE IF NOT EXISTS expenses ( 
        #id INTEGER PRIMARY KEY AUTOINCREMENT,
	    #date TEXT ISO NOT NULL DEFAULT NOW,
	    #))
# Commit.
    # connection.commit()
# Close the connection.
    # connection.close()

import sqlite3


def get_connection():
	connection=sqlite3.connect('expenses.db')
	cursor = connection.cursor()
	return connection, cursor

def initialize_database():
	connection, cursor = get_connection()
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS expenses ( 
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		date TEXT NOT NULL,
		created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
		updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
		description TEXT NOT NULL,
		amount REAL NOT NULL,
		payment_method TEXT NOT NULL,
		category TEXT,
		notes TEXT,
		tags TEXT
		)"""
	)
	connection.commit()
	cursor.close()
	connection.close()

# seed_data = {
# 	date='2024-06-05',
# 	created_at='2024-06-05',
# 	updated_at='2024-06-05',
# 	description='Groceries',
# 	amount='35.43',
# 	payment_method='Checking',
# 	category='work',
# 	notes='',
# 	tags=''}

# def seed_db():
# 	connection, cursor = get_connection()
# 	rows = cursor.execute("""SELECT * FROM expenses""")
# 	if rows == 0:
# 		cursor.execute("""INSERT INTO expenses {seed_data}""")
# ----------
# CREATE
# ----------

def add_expense(date, description, amount, payment_method, category='', notes='', tags=''):
	connection, cursor = get_connection()
	cursor.execute("""
		INSERT INTO expenses 
			(date, 
			description,
			amount, 
			payment_method,
			category, 
			notes, 
			tags)
			VALUES (?, ?, ?, ?, ?, ?, ?)""",
			(date, description, amount, payment_method, category, notes, tags))
	connection.commit()
	new_id=cursor.lastrowid
	cursor.close()
	connection.close()
	return new_id

# ----------
# READ
# ----------

def get_all_expenses():
	connection, cursor = get_connection()
	cursor.execute("""
		SELECT * FROM expenses;""")
	results = cursor.fetchall()
	connection.commit()
	cursor.close()
	connection.close()
	return results

def get_expense():
	None

# ----------
# UPDATE
# ----------

def update_expense():
	None
	
# ----------
# DELETE
# ----------

def delete_expense():
	None