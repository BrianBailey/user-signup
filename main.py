from flask import Flask, request, redirect, render_template
import re


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('master.html')

@app.route("/", methods=['POST'])



#def valid_username(username):
    #return username_regex.match(username)
#def valid_password(password):
    #return password_regex.match(password)

#def valid_email(email):
    #return email_regex.match(email)



#PASS_RE = re.compile(r"^.{3,20}$")
#EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def master_form():

    #username_regex = re.compile(r"^.\s+{3,20}$")
    #password_regex = re.compile(r"[^\s]{3,20}$")
    #verify_password_regex = re.compile(r"[^\s]{3,20}$")
    #email_regex = re.compile(r"[^\s]+\@[\S]+\.[^\s]+{3,20}$")

    

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    #if username_regex.match(username) == None:
        #username_error = "That's not a valid username"

    

    # username
    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username (*must be between 3-20 characters long)"

    if username == '':
        username_error = "That's not a valid username (*can't be left blank)"

    if ' ' in username:
        username_error = "That's not a valid username (*no spaces allowed)"

    # password

    if len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password (*must be between 3-20 characters long)"
    
    if password == '':
        password_error = "That's not a valid password (*can't be left blank)"

    if ' ' in password:
        password_error = "That's not a valid password (*no spaces allowed)"
    
    if verify_password == '':
        verify_password_error = "Passwords don't match (*can't be left blank)"
    
    if ' ' in verify_password:
        verify_password_error = "Passwords don't match (*no spaces allowed)"
    
    if password != verify_password:
        verify_password_error = "Passwords don't match (*try again)"        

    # Email
    if email:
        if len(email) < 3 or len(email) > 20:
            email_error = "That's not a valid email (*must be between 3-20 characters long)"

        if ' ' in email or '@' not in email or '.' not in email:
            email_error = "That's not a valid email (*must have no spaces, must include '@' and must include '.' )"
    
    if not username_error and not password_error and not verify_password_error and not email_error:
        # redirect
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('master.html',
        username=username, username_error=username_error,
        password_error=password_error,
        verify_password_error=verify_password_error,
        email=email, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html", username=username)

app.run()
