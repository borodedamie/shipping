import sqlite3

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

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
    
    for file in files:
        empPhoto = convertToBinaryData(file)
    
    cursor.execute("""INSERT INTO applications(first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference)VALUES('{first_name}', '{last_name}', '{other_names}', '{email}', '{address}', '{state}', '{city}', '{phone_no}', '{ssn}', '{position}', '{empPhoto}', '{reference}' );""".format(first_name = first_name, last_name = last_name, other_names = other_names, email = email, address = address, state = state, city = city, phone_no = phone_no, ssn = ssn, position = position, empPhoto = files, reference = reference ))
    
    connection.commit()
    cursor.close()
    connection.close()
    