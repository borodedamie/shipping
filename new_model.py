from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    __tablename__ = "contacts"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone_no = db.Column(db.String(14), nullable = False)
    message = db.Column(db.String(200), nullable = False)
         
    def save_contact_to_db(self, name, email, phone_no, message):
        contact = Contact(name=name, email=email, phone_no=phone_no, message=message)
        db.session.add(self)
        db.session.commit()

        
class Application(db.Model):
    __tablename__ = "applications"
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    other_names = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    state = db.Column(db.String, nullable = False)
    city = db.Column(db.String, nullable = False)
    phone_no = db.Column(db.String, nullable = False)
    ssn = db.Column(db.String, nullable = False)
    position = db.Column(db.String, nullable = False)
    files = db.Column(db.String, nullable = False)
    reference = db.Column(db.String, nullable = False)
        
    def save_application_to_db(self):
        db.session.add(self)
        db.session.commit()
                
       
class Newsletter(db.Model):
    __tablename__ = "newsletters"
     
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, nullable = False)
        
    def save_newsletters_to_db(self, email):
        newsletter = Newsletter(email=email)
        db.session.add(newsletter)
        db.session.commit()
