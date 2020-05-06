from flask import Flask, render_template, url_for, request, jsonify
import sqlite3
import os, csv
from datetime import datetime

app = Flask(__name__)

# Web Information
js_static = './static/script.js'
css_static = './static/style.css'
profile_image = './static/assets/images/profile_img.jpg'


# Home Page
@app.route('/')
def home_page():
    print("")
    print(f"[*] Homepage - Connection from {request.remote_addr}")
    return render_template('index.html', js_static=js_static, css_static=css_static)

@app.route('/<string:page_name>')
def page(page_name):
    if page_name == 'about_me':
        return render_template(f'{page_name}.html', js_static=js_static, css_static=css_static, profile_image=profile_image)
    elif page_name == 'projects' or page_name == 'contact':
        return render_template(f'{page_name}.html', js_static=js_static, css_static=css_static)
    elif page_name == 'admin':
        print("")
        print(f"[*] Admin - Connection from {request.remote_addr}")
        return render_template('admin_login.html')
    else:
        return render_template('error.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:

        # -- Information to grab --
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        email = data['email']
        subject = data['subject']
        content = data['content']
         # -- Information to grab --

        file = database.write(f'\n{email},{subject},{content},{current_time}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:

        # -- Information to grab --
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        email = data['email']
        subject = data['subject']
        content = data['content']
         # -- Information to grab --

        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,content,current_time])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print("-- Form Submitted --")
            print('Email: {}\nSubject: {}\nMessage: {}'.format(data['email'],data['subject'],data['content']))
            return render_template('form_submitted.html', js_static=js_static, css_static=css_static)
        except:
            print("")
            print("[x] An Error Occured - Could not save to database")
            return render_template('error.html')

# -- Admin Panel --
# To view information that has been sent through contact 




# -- Admin Panel --