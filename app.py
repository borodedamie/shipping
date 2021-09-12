from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import model
# from new_model import *
# import urllib.request
import os, webbrowser

UPLOAD_FOLDER = '/mnt/c/Users/PC/Desktop/Shipping/static/images/upload'
ALLOWED_EXTENSIONS = {'doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "aswdqwe232343refeerheretti"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shipbite.db'
# app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

# @app.before_first_request
# def create_tables():
#     db.create_all()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
def convertToBinary(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    return data
           
@app.route('/submit', methods = ['GET', 'POST'])
def submit_application():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        other_names = request.form.get('other_names')
        email = request.form.get('email')
        address = request.form.get('address')
        state = request.form.get('state')
        city = request.form.get('city')
        phone_no = request.form.get('phone_no')
        ssn = request.form.get('ssn')
        position = request.form.get('position')
        reference = request.form.get('reference')
        
        if 'files[]' not in request.files:
            return 'no file found'
        
        files = request.files.getlist('files[]')
        for file in files:
            if file.filename == " ":
                print("file must have a name.")
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        model.save_application_to_db(first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, filename, reference)
        
        return 'something happened'

@app.route('/mailto', methods = ['GET', 'POST'])
def launch_def_mailapp():    
    webbrowser.open('mailto:', new = 1)
    
    return redirect(request.referrer)

@app.route('/')
def load_homepage():
    if request.method == 'POST':
        max_weight = 150
        max_length = 108
        express = 62.50
        
        if request.form['weight'] >= max_weight and request.form['height'] >= max_length:
            shippingCost = express * 0.37
        elif request.form['weight'] <= max_weight and request.form['height'] <= max_length:
            shippingCost = 30.50 * 0.37
        elif request.form['weight'] < 15 and request.form['height'] < 10:
            shippingCost = 2.50 * 0.37
            
        return render_template("index.html", shippingCost = shippingCost)
    
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/logistics')
def logistics():
    return render_template("logistics.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/search', methods = ['GET', 'POST'])
def careerpage_search_button():
    
    services = ('services', 'supply chain', 'global freight forwarding', 'freight forwarding', 'internet fulfilment' )
    logistics = ('logistics', 'deliveries', )
    contactDetails = ('phone', 'office', 'contact', 'phone number', 'address', 'office address')
    careers = ('shipping clerk', 'job openings', 'job opportunities', 'career', 'empowerment')
    
    if request.method == 'POST':
        if request.form['query'] in services:
            return redirect(url_for('services'))
        elif request.form['query'] in logistics:
            return redirect(url_for('logistics'))
        elif request.form['query'] in contactDetails:
            return redirect(url_for('contact'))
        elif request.form['query'] in careers:
            return redirect(url_for('careers'))
        else:
            flash('Sorry, {} is not in our dictionary.'.format(request.form['query']))

@app.route('/careers')
def careers():
    return render_template("career/careers.html")

@app.route('/careers2')
def careers_contd():
    return render_template("career/careers2.html")

@app.route('/application')
def application():
    return render_template("career/application.html")

@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone_no = request.form.get('phone_no')
        message = request.form.get('message')
        
        model.save_contact_to_db(name, email, phone_no, message)
        
        return redirect(url_for('contact'))
    
@app.route('/trackShipment', methods = ['GET', 'POST'])
def trackShipment():
    if request.method == 'POST':
        if request.form['shippingNumber']:
             flash('{} shipment not found'.format(request.form['shippingNumber']))
        return redirect(url_for('load_homepage'))
    return redirect(url_for('load_homepage'))

@app.route('/subscription', methods = ['GET', 'POST'])
def newsletter_subscription():
    if request.method == 'POST':
        email = request.form.get('email')
        model.save_newsletters_to_db(email)
    return redirect(url_for('load_homepage'))

if __name__ == "__main__":
    # db.init_app(app)
    app.run(host = '0.0.0.0', port = 8000, debug = True)
