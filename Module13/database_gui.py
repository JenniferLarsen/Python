"""
Jennifer Larsen
11/22/2023
This program adds a gui to database interactions.
"""


import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk

def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def create_table(conn, sql_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def create_tables(database):
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id INTEGER PRIMARY KEY,
                                        firstname TEXT NOT NULL,
                                        lastname TEXT NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id INTEGER PRIMARY KEY,
                                    major TEXT NOT NULL,
                                    begin_date TEXT NOT NULL,
                                    end_date TEXT,
                                    person_id INTEGER,
                                    FOREIGN KEY (person_id) REFERENCES person (id)
                                );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_person_table)
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_person(conn, person):
    sql = ''' INSERT INTO person(firstname, lastname)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, person)
    return cur.lastrowid


def create_student(conn, student):
    sql = ''' INSERT INTO student(major, begin_date, person_id)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    return cur.lastrowid


def select_all_persons(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")
    rows = cur.fetchall()
    return rows


def select_all_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    return rows

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database App")

        self.create_tables_button = ttk.Button(root, text="Create Database & Table", command=self.create_tables)
        self.create_tables_button.pack(pady=10)

        self.add_person_button = ttk.Button(root, text="Add Person", command=self.add_person)
        self.add_person_button.pack(pady=10)

        self.add_student_button = ttk.Button(root, text="Add Student", command=self.add_student)
        self.add_student_button.pack(pady=10)

        self.view_person_table_button = ttk.Button(root, text="View Person Table", command=self.view_person_table)
        self.view_person_table_button.pack(pady=10)

        self.view_student_table_button = ttk.Button(root, text="View Student Table", command=self.view_student_table)
        self.view_student_table_button.pack(pady=10)

        self.exit_button = ttk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=10)

    def create_tables(self):
        create_tables("pythonsqlite.db")
        print("Database and tables created successfully!")

    def add_person(self):
        person_first_name = input("Enter person's first name: ")
        person_last_name = input("Enter person's last name: ")

        conn = create_connection("pythonsqlite.db")
        with conn:
            person = (person_first_name, person_last_name)
            person_id = create_person(conn, person)
            print(f"Person added successfully with ID: {person_id}")

    def add_student(self):
        student_first_name = input("Enter student's first name: ")
        student_last_name = input("Enter student's last name: ")
        major = input("Enter student's major: ")
        start_date = input("Enter student's start date (YYYY-MM-DD): ")

        conn = create_connection("pythonsqlite.db")
        with conn:
            person_id = self.query_person_id(conn, student_first_name, student_last_name)
            if person_id is not None:
                student = (major, start_date, person_id)
                student_id = create_student(conn, student)
                print(f"Student added successfully with ID: {student_id}")
            else:
                print("Person not found.")

    def view_person_table(self):
        conn = create_connection("pythonsqlite.db")
        with conn:
            rows = select_all_persons(conn)
            for row in rows:
                print(row)

    def view_student_table(self):
        conn = create_connection("pythonsqlite.db")
        with conn:
            rows = select_all_students(conn)
            for row in rows:
                print(row)

    def query_person_id(self, conn, first_name, last_name):
        cur = conn.cursor()
        cur.execute("SELECT id FROM person WHERE firstname=? AND lastname=?", (first_name, last_name))
        result = cur.fetchone()
        return result[0] if result else None


if __name__ == '__main__':
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()


