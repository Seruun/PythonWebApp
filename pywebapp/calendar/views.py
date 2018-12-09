from datetime import datetime

from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import dates
from .forms import NewDateForm
from .. import db
from ..globals import title_name
from ..models import DatesTable, Employee, Customer


@dates.route('/calendar')
@login_required
def calendar():
    """
    Render the contact template on the /felicia route
    """
    Title = "Kalendar"

    return render_template('secured/calendar.html', title=str(title_name + ' - ' + Title))


@dates.route('/calendar/new_date', methods=['GET', 'POST'])
@login_required
def create_new_date():
    """
    Render the new_date template on the /new_date route
    Add an New Date to the database through the new_date form
    """

    Title = "Termin erstellen"

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

    return render_template('secured/new_date.html', title=str(title_name + ' - ' + Title), form=form)
