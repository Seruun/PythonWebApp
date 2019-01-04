from datetime import datetime

from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import calendar
from .forms import NewDateForm
from .. import db
from ..globals import title_name
from ..models import DatesTable, Employee, Customer


@calendar.route('/dates')
@login_required
def dates():
    """
    Render the contact template on the /felicia route
    """
    Title = "Kalendar"

    return render_template('secured/calendar/date.html', title=str(title_name + ' - ' + Title))


@calendar.route('/dates/add', methods=['GET', 'POST'])
@login_required
def add_date():
    """
    Add a new date into the database.
    """

    Title = "Termin erstellen"
    add_date = True

    form = NewDateForm()
    if form.validate_on_submit():
        new_date_plan = DatesTable(
            date=form.form_date.data,
            customer_id=form.form_customer_id.data,
            customer=str(form.form_customer_first_name.data) + " " + str(form.form_customer_last_name.data),
            employee_id=form.form_employee_id.data,
            employee=str(form.form_employee_first_name.data) + " " + str(form.form_employee_last_name.data),
            room=form.room_id.data,
            start_time=form.start_time.data,
            duration=form.duration.data,
            end_time=form.start_time.data + form.duration.data

        )

        db.session.add(new_date_plan)
        db.session.commit()

        return redirect(url_for('dates.calendar'))
    else:

        flash('Termin ungültig! Bitte wähle ein aderes Datum oder einen anderen Zeitrahmen!')

    return render_template('secured/calendar/dates.html', title=str(title_name + ' - ' + Title), action="Edit",
                           add_date=add_date, form=form)


@calendar.route('/dates/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_date(id):
    """
    Edit date informations within the database
    """

    Title = "Termin erstellen"
    add_date = False

    _date = DatesTable.query.get_or_404(id)

    form = NewDateForm(obj=_date)
    if form.validate_on_submit():
            _date.id = form.date_id.data,
            _date.customer_id = form.customer_id.data,
            _date.customer = str(form.customer_first_name.data) + " " + str(form.customer_last_name.data),
            _date.employee_id = form.employee_id.data,
            _date.employee = str(form.employee_first_name.data) + " " + str(form.employee_last_name.data),
            _date.room = form.room_id.data,
            _date.start_time = form.start_time.data,
            _date.duration = form.duration.data,
            _date.end_time = form.start_time.data + form.duration.data
            db.session.commit()

            flash("Termin erfolgreich bearbeitet!")

            return redirect(url_for('dates.dates'))

    form.date_id.data = _date.id
    form.customer_id.data = _date.customer_id
    form.customer.data = _date.customer
    form.employee_id.data = _date.employee_id
    form.employee.data = _date.employee
    form.room_id.data = _date.room
    form.start_time.data = _date.start_time
    form.duration.data = _date.duration
    form.end_time = _date.end_time

    return render_template('secured/calendar/dates.html', title=str(title_name + ' - ' + Title), action="Edit",
                           add_date=add_date, form=form,
                           date=_date)
