from . import db
from flask_login import login_user, login_required, logout_user
from .forms import LoginForm, RegisterForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, flash, render_template, request, url_for, redirect

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if (login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        user = db.session.scalar(db.select(User).where(User.name == user_name))
        if user is None:
            error = 'Login credentials are incorrect'
        elif not check_password_hash(user.password_hash, password):
            error = 'Login credentials are incorrect'
        if error is None:
            login_user(user)
            flash("Login Successful")
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('auth/login.html', form=login_form, heading='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
        uname = register.user_name.data
        pwd = register.password.data
        email = register.email_id.data
        user = db.session.scalar(db.select(User).where(User.name == uname))
        if user: 
            flash('Username already exists, please try another')
            return redirect(url_for('auth.register'))
        pwd_hash = generate_password_hash(pwd)
        new_user = User(name=uname, password_hash=pwd_hash, emailid=email, address=register.address.data, contactNumber = register.contactNumber.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    else:
        return render_template('auth/register.html', form=register, heading='Register')
    
@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You are now logged out", 'success')
    return redirect(url_for('main.index'))