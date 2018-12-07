from datetime import time

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, DateField, QuerySelectField
from wtforms.validators import DataRequired
from wtforms_components import TimeField, DateRange

from ..models import Customer, DatesTable, TimeTable, CalendarTable, Employee


class NewDateForm(FlaskForm):
    """
    Form fo new Date creation
    """
    # Customer
    form_customer_id = QuerySelectField(query_factory=lambda: Customer.query.all(),
                                  get_label='Kundennummer')
    form_customer_first_name = StringField('Vorname', validators=[DataRequired()])
    form_customer_last_name = StringField('Nachname', validators=[DataRequired()])
    # Employee
    form_employee_id = QuerySelectField(query_factory=lambda: Employee.query.all(),
                                  get_label='Mitarbeiternummer')
    form_employee_first_name = StringField('Vorname', validators=[DataRequired()])
    form_employee_last_name = StringField('Nachname', validators=[DataRequired()])
    # Date Planning
    form_date = DateField('Datum', validators=[DataRequired()], format="%d.%m.%Y")
    start_time = TimeField('Beginn', validators=[DataRequired(), DateRange(
        min=time(8, 0, 0),
        max=time(18, 0, 0)
    )])
    room_id = StringField('Raum', validators=[DataRequired()])
    duration = StringField('Geplante Länge', validators=[DataRequired()])
    submit = SubmitField('Termin anlegen')
