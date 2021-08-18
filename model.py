import sqlite3

# def convertToBinaryData(filename):
#     with open(filename, 'rb') as file:
#         blobData = file.read()
#     return blobData

def save_contact_to_db(name, email, phone_no, message):
    connection = sqlite3.connect("shipbite.db")
    cursor = connection.cursor()
    
    cursor.execute("""INSERT INTO contacts(name, email, phone_no, message)VALUES('{name}', '{email}', '{phone_no}', '{message}');""".format(name = name, email = email, phone_no = phone_no, message = message))
 
    connection.commit()
    cursor.close()
    connection.close()

def save_application_to_db(first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference):
    connection = sqlite3.connect("shipbite.db")
    cursor = connection.cursor()
    
    query = """ INSERT INTO applications(first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    
    data_tuple = (first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference)
    cursor.execute(query, data_tuple)
    
    connection.commit()
    cursor.close()
    connection.close()
    