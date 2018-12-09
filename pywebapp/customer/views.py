from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import customer
from .forms import CustomerForm
from .. import db
from ..globals import title_name
from ..models import Customer


@customer.route('/customers')
@login_required
def list_customers():
    """
    Display all known customers in a list
    """

    Title = "Kundenliste"

    customers = Customer.query.all()

    return render_template('secured/customers/customers.html', title=str(title_name + ' - ' + Title), customers=customers)


@customer.route('/customers/add', methods=['GET', 'POST'])
@login_required
def add_customer():
    """
    Add a new Customer Data to database
    """

    Title = "Neuen Kunden anlegen"
    add_customer = True

    form = CustomerForm()

    if form.validate_on_submit():
        _customer = Customer(
            id=form.id.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            full_name=str(form.first_name.data) + " " + str(form.last_name.data),
            address=form.address.data,
            phone_number=form.phone_number.data,
        )
        try:
            db.session.add(_customer)
            db.session.commit()

            flash('Der Kunde wurde erfolgreich angelegt. Das anlegen von Terminen und Rechnungen ist nun möglich.')
        except:
            flash('Error: Kunde bereits in der Datenbank vorhanden!')

        return redirect(url_for('customer.list_customers'))

    return render_template('secured/customers/customer.html', title=str(title_name + ' - ' + Title), action="Add",
                           add_customer=add_customer, form=form)


@customer.route('/customers/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_customer(id):
    """
    Edit a Customer
    """

    Title = "Kunde bearbeiten"
    add_customer = False

    _customer = Customer.query.get_or_404(id)
    form = CustomerForm(obj=_customer)
    if form.validate_on_submit():
        _customer.id = form.id.data,
        _customer.email = form.email.data,
        _customer.first_name = form.first_name.data,
        _customer.last_name = form.last_name.data,
        _customer.full_name = str(form.first_name.data) + " " + str(form.last_name.data),
        _customer.address = form.address.data,
        _customer.phone_number = form.phone_number.data,
        db.session.commit()
        flash('Kunde erfolgreich bearbeitet!')

        # redirect to the departments page
        return redirect(url_for('customer.list_customers'))

    form.id.data = _customer.id
    form.email.data = _customer.email
    form.first_name.data = _customer.first_name
    form.last_name.data = _customer.last_name
    form.address.data = _customer.address
    form.phone_number.data = _customer.phone_number
    return render_template('secured/customers/customer.html', title=str(title_name + ' - ' + Title), action="Edit",
                           add_customer=add_customer, form=form,
                           customer=_customer)


@customer.route('/customers/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_customer(id):
    """
    Delete a Customer from the database
    """
    Title = "Kunde löschen"

    _customer = Customer.query.get_or_404(id)
    db.session.delete(_customer)
    db.session.commit()
    flash('Kunde erfolgreich gelöscht.')

    # redirect to the departments page
    return redirect(url_for('customer.list_customers'))

    return render_template(title=str(title_name + ' - ' + Title))
