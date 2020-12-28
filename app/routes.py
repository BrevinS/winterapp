from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_sqlalchemy import sqlalchemy
from app.forms import BaseForm
from app.models import Person, Administrator, User
from flask_login import current_user, login_user, logout_user, login_required

@app.before_first_request
def initDB(*args, **kwargs):
    db.create_all()

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = BaseForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, firstname=form.firstname.data,
                    lastname=form.lastname.data, email=form.email.data)
        user.get_password(form.password2.data)
        db.session.add(user)
        db.session.commit()
        flash('User Successfully Created')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)