from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import model
# import urllib.request
import os

UPLOAD_FOLDER = '/mnt/c/Users/PC/Desktop/Shipping/static/images/upload'
ALLOWED_EXTENSIONS = {'doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "aswdqwe232343refeerheretti"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/submit', methods = ['GET', 'POST'])
def submit_application():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        other_names = request.form['other_names']
        email = request.form['email']
        address = request.form['address']
        state = request.form['state']
        city = request.form['city']
        phone_no = request.form['phone_no']
        ssn = request.form['ssn']
        position = request.form['position']
        reference = request.form['reference']
        
        if 'files[]' not in request.files:
            return 'no file found'
        
        images = request.files.getlist('files[]')
        for file in files:
            if file.filename == " ":
                print("file must have a name.")
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # model.save_application_to_db(first_name, last_name, other_names, email, address, state, city, phone_no, ssn, position, files, reference)
        
        return 'something happened at least.'

@app.route('/')
def load_homepage():
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
        name = request.form['name']
        email = request.form['email']
        phone_no = request.form['phone_no']
        message = request.form['message']
        
        model.save_contact_to_db(name, email, phone_no, message)
        
        return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8000, debug = True)
