from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#CONTROLLER

@app.route('/')
def index():
    return render_template('sign_in.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    if not User.validate_user(request.form):
        return redirect('/sign_up')
    hash_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "username": request.form['username'],
        "email": request.form['email'],
        "password": hash_pass
    }
    id = User.add_user(data)
    session['user_id'] = id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['username'] = request.form['username']
    return redirect('/sightings')

@app.route('/login_user', methods=['POST'])
def login_user():
    data = {
        "email": request.form['email'],
    }
    this_user = User.get_user_by_email(data)
    if not this_user:
        flash("Invalid Email or Password")
        return redirect('/')
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect('/')
    session['user_id'] = this_user.id
    session['first_name'] = this_user.first_name
    session['last_name'] = this_user.last_name
    session['username'] = request.form['username']
    return redirect('/sightings')

@app.route('/sightings')
def success():
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    return render_template('sightings.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')