import sqlite3

connection = sqlite3.connect('shipbite.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name text,
        email text,
        phone_no text,
        message text
        ); """
    )

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY,
        first_name text,
        last_name text,
        other_names text NULL,
        email text,
        address text,
        state text,
        city text,
        phone_no text,
        ssn text,
        position text,
        files blob NULL,
        reference text 
    ); """
)

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS newsletter (
        id INTEGER PRIMARY KEY,
        email text
    ); """
)

print("Tables created successfully")

connection.close()
