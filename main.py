from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup")
def index():
   
    return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '':
        username_error = 'That is not a valid username.'

    elif " " in username:
        username_error = 'The username must have no spaces.'
        username = ""

    elif len('username') < 3 or len('username') > 20:
        username_error = 'The username must be between 3-20 characters in length'
        username = ""

    if password == '':
        password_error = 'That is not a valid password.'

    elif " " in password:
        password_error = 'The password must have no spaces.'
        password = ""

    elif len('password') < 3 or len('password') > 20:
        password_error = 'The password must be between 3-20 characters in length'
        password = ""

    if verify == ' ' or verify != password:
        verify_error = 'Passwords do not match.'
        verify = ''

    if ' ' in email:
        email_error = 'Email must have no spaces'

    elif re.match('(^$|pattern[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+/.[a-zA-Z0-9-]+$)', email):
        email = ''
        
    else:
        if not re.fullmatch("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            email_error = 'Email must contain a . and an @ .' 

    


    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    
    else:
        return render_template('index.html', username = username,
        username_error = username_error,
        password_error = password_error, 
        verify_error = verify_error,
        email = email,
        email_error = email_error)


app.run()