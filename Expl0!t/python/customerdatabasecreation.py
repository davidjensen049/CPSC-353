# @author Melinda Sherrill
# Creates a binary sqlite file

import sqlite3

# Connect to database and point to it
conn = sqlite3.connect("../dbs/cust.sqlite")
c = conn.cursor()


# Create Database Table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS customers'
              + '(customerid REAL, fname TEXT, lname TEXT, company TEXT)')


# Create Entries (noticed where the names are from?)
def data_entry():
    c.execute("DELETE FROM customers")
    c.execute("INSERT INTO customers VALUES(1, 'Rachel', "
              + " 'Green', 'Ralph Lauren')")
    c.execute("INSERT INTO customers VALUES(1982735, "
              + "'Michael', 'Fahy', 'Chapman')")
    c.execute("INSERT INTO customers VALUES(2, "
              + "'Monica', 'Geller', 'Chez Geller')")
    c.execute("INSERT INTO customers VALUES(3, 'Ross', "
              + " 'Geller', 'Professor')")
    c.execute("INSERT INTO customers VALUES(4, 'Chandler', "
              + " 'Bing', 'Data Analyist')")
    c.execute("INSERT INTO customers VALUES(5, 'Phoebe', "
              + " 'Buffay', 'Psychic')")

    # Commit entries and close database connection
    conn.commit()
    c.close()
    conn.close()

# Run functions
create_table()
data_entry()
