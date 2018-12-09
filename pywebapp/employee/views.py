from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import employee
from .forms import EmployeeForm
from .. import db
from ..models import Employee
from ..globals import title_name


def check_admin_role():
    if not current_user.role_id >= 3:
        abort(403)


@employee.route('/employees')
@login_required
def list_employees():
    """
    Display all registered employees in a list
    """
    check_admin_role()

    Title = "Mitarbeiterliste"

    employees = Employee.query.all()

    return render_template('secured/employees/employees.html', title=str(title_name + ' - ' + Title), employee=employees)


@employee.route('/employees/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Add new Employee and the Account to Database
    """
    check_admin_role()

    Title = "Mitarbeiterkonto einrichten"

    form = EmployeeForm()

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

    return render_template('secured/employees/employee.html', title=str(title_name + ' - ' + Title), form=form)


@employee.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_employee(id):
    """
    Edit a Employee
    """

    Title = "Mitarbeiter bearbeiten"
    add_employee = False

    _employee = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=_employee)
    if form.validate_on_submit():
        _employee.email = form.email.data,
        _employee.username = form.username.data,
        _employee.first_name = form.first_name.data,
        _employee.last_name = form.last_name.data,
        _employee.full_name = str(form.first_name.data) + " " + str(form.last_name.data),
        _employee.phone_number = form.phone_number.data,
        db.session.commit()
        flash('Mitarbeiter erfolgreich bearbeitet!')

        # redirect to the departments page
        return redirect(url_for('employee.list_employees'))

    form.email.data = _employee.email
    form.first_name.data = _employee.first_name
    form.last_name.data = _employee.last_name
    form.full_name.data = _employee.full_name
    form.phone_number.data = _employee.phone_number
    return render_template('secured/employees/employee.html', title=str(title_name + ' - ' + Title), action="Edit",
                           add_employee=add_employee, form=form,
                           customer=_employee)