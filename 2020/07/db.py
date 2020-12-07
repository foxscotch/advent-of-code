import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Create tables
c.execute('CREATE TABLE bags (name TEXT PRIMARY KEY NOT NULL);')
