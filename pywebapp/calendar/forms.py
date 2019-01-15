from datetime import time

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from wtforms_components import TimeField, DateRange

from ..models import Customer, DatesTable, TimeTable, CalendarTable, Employee, Room


class NewDateForm(FlaskForm):
    """
    Form fo new Date creation
    """
    # Customer
    customer_id = QuerySelectField('Kunde', query_factory=lambda: Customer.query.all(),
                                  get_label='id')
    customer_first_name = StringField('Vorname', validators=[DataRequired()])
    customer_last_name = StringField('Nachname', validators=[DataRequired()])
    # Employee
    employee_id = QuerySelectField('Mitarbeiternummer', query_factory=lambda: Employee.query.all(),
                                  get_label='id')
    employee = QuerySelectField('Tätowierer/in', query_factory=lambda: Employee.query.all(),
                                   get_label='full_name')
    # Date Planning
    date = DateField('Datum', validators=[DataRequired()], format="%d.%m.%Y")
    start_time = QuerySelectField('Startzeit', query_factory=lambda: TimeTable.query.all(),
                                  get_label='full_time')
    room_id = QuerySelectField('Raum', query_factory=lambda: Room.query.all(),
                                  get_label='id')
    duration = StringField('Geplante Länge (in Minuten)', validators=[DataRequired()])
    submit = SubmitField('Termin anlegen')
