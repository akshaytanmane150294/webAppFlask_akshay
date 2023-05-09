"""Route and Path, and URLS"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required , logout_user, current_user


auth  = Blueprint('auth', __name__)

@auth.route('/login', methods =['GET','POST'])
def login():
    """this is form data where we get data form user"""
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password try again", category='error')
        else:
            flash('Email  does not exist',category='error')
    
    return render_template("login.html", user = current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password = request.form.get('password1')
        confirmPassword = request.form.get('password2')
        print(email,firstname,password,confirmPassword)
        
        user = User.query.filter_by(email = email).first()
        if user:
            flash('This user already Exist', category='error')
        elif len(email) < 4:
            flash(" Email must be greater than 4 character.",category = 'error')
        elif len(firstname) < 3:
            flash(" FirstName must be greater than 3 character.",category = 'error')
        elif password != confirmPassword:
            flash(" Password does not match", category= 'error')
        elif len(password) < 5:
            flash("Password must be greater than 5 character.", category= 'error')
        else:
            new_user = User(email = email, firstname = firstname, password = generate_password_hash(password, method='sha256') )
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created successfully!", category='success')
            return redirect(url_for('views.home'))
    return render_template("signup.html", user = current_user)