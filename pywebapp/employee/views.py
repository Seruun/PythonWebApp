from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import employee
from .forms import AddEmployeeForm
from .. import db
from ..models import Employee
from ..globals import PageName


def check_admin_role():
    if not current_user.role_id >= 3:
        abort(403)


@employee.route('/add_employee', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Add new Employee and the Account to Database
    """
    check_admin_role()

    title_name = "Mitarbeiterkonto einrichten"

    form = AddEmployeeForm()

    if form.validate_on_submit():
        _employee = Employee(
            email=form.email.data,
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            full_name=str(form.first_name.data) + " " + str(form.last_name.data),
            password=form.password.data,
            role_id=form.role_id.data
        )

        db.session.add(_employee)
        db.session.commit()

        flash('Der Nutzer wurde erfolgreich angelegt. Das Login ist nun möglich.')

    return render_template('secured/register.html', title=str(title_name + ' - ' + PageName), form=form)


@employee.route('/list_employees')
@login_required
def show_customer():
    """
    Display all registered employees in a list
    """
    check_admin_role()

    title_name = "Mitarbeiterliste"

    employees = Employee.query.all()

    return render_template('secured/list_employees.html', title=str(title_name + ' - ' + PageName), employee=employees)
