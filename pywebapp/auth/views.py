from datetime import datetime

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm, PasswordUpdateForm
from .. import db
from ..globals import REV_NUM
from ..models import Employee

# if 0 -> no maintenance else maintenance
maintenance = 0


@auth.context_processor
def inject_now():
    """
    Footer Copyright Year Getter
    """
    return {'now': datetime.utcnow()}


@auth.context_processor
def revision():
    return {'rev_version': REV_NUM}


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an Employee through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(username=form.username.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            login_user(employee)
            return redirect(url_for('home.homepage'))

        else:
            flash('Email oder Passwort falsch!')

    return render_template('secured/login.html', title=str(title.name + ' - ' + page.name), form=form)


@auth.route('/password_reset', methods=['GET', 'POST'])
@login_required
def password_reset():
    """
    Handle requests to the /login route
    Log an Employee through the login form
    """
    form = PasswordUpdateForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(username=form.username.data).first()
        if employee is not None:
            employee.set_password(form.password.data)
            db.session.commit()
            return redirect(url_for('home.homepage'))

        else:
            flash('Password konnte nicht zurück gesetzt werden!')

    return render_template('secured/password_reset.html',
                           title=str(title.name + ' - ' + page.name), form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.homepage'))
