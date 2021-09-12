import sqlite3

def save_contact_to_db(name, email, phone_no, message):
    connection = sqlite3.connect("shipbite.db")
    cursor = connection.cursor()
    
    cursor.execute(" INSERT INTO contacts(name, email, phone_no, message)VALUES(?, ?, ?, ?)", ( name, email, phone_no, message ))
 
    connection.commit()
    cursor.close()
    connection.close()

def save_application_to_db(first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference):
    connection = sqlite3.connect("shipbite.db")
    cursor = connection.cursor()
        
    cursor.execute(" INSERT INTO applications(first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ", (first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference))
    
    connection.commit()
    cursor.close()
    connection.close()

def save_newsletters_to_db(email):
    connection = sqlite3.connect("shipbite.db")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO newsletters(email) VALUES(?)", (email,))
    connection.commit()
    cursor.close()
    connection.close()