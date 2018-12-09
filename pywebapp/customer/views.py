from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import customer
from .forms import
from .. import db
from ..models import Customer
from ..globals import PageName


def check_admin_role():
    if not current_user.role_id >= 3:
        abort(403)


@customer.route('/add_customer', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Add new Employee and the Account to Database
    """
    check_admin_role()

    title_name = "Neuen Kunden anlegen"

    form = AddCustomerForm()

    if form.validate_on_submit():
        _customer = Customer(
            id=form.customer_id.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            full_name=str(form.first_name.data) + " " + str(form.last_name.data),
            address=form.address.data,
            phone_number=form.phone_number.data,
        )

        db.session.add(_customer)
        db.session.commit()

        flash('Der Kunde wurde erfolgreich angelegt. Das anlegen von Terminen und Rechnungen ist nun möglich.')

    return render_template('secured/add_customer.html', title=str(title_name + ' - ' + PageName), form=form)


@customer.route('/list_customers')
@login_required
def show_customer():
    """
    Display all known customers in a list
    """
    check_admin_role()

    title_name = "Kundenliste"

    customers = Customer.query.all()

    return render_template('secured/list_customer.html', title=str(title_name + ' - ' + PageName), customer=customers)
