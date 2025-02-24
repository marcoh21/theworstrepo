import sqlite3

# Creating the table
with sqlite3.connect("students.db") as con:
    c = 