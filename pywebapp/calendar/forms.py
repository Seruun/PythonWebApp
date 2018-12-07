from datetime import time

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, DateField, SelectField
from wtforms.validators import DataRequired
from wtforms_components import TimeField, DateRange

from ..models import Customer, DatesTable, TimeTable, CalendarTable, Employee


class NewDateForm(FlaskForm):
    """
    Form fo new Date creation
    """
    # Customer
    form_customer_id = SelectField(label='Kundennummer', coerce=int)
    form_customer_first_name = StringField('Vorname', validators=[DataRequired()])
    form_customer_last_name = StringField('Nachname', validators=[DataRequired()])
    # Employee
    form_employee_id = SelectField(label='Mitarbeiternummer')
    form_employee_first_name = StringField('Vorname', validators=[DataRequired()])
    form_employee_last_name = StringField('Nachname', validators=[DataRequired()])
    # Date Planning
    form_date = DateField('Datum', validators=[DataRequired()], format="%d.%m.%Y")
    start_time = TimeField('Beginn', validators=[DataRequired(), DateRange(
        min=time(8, 0, 0),
        max=time(20, 0, 0)
    )])
    room_id = StringField('Raum', validators=[DataRequired()])
    duration = StringField('Geplante Länge', validators=[DataRequired()])
    submit = SubmitField('Termin anlegen')

    def edit_employee(request, id):
        employee = Employee.query.get(id)
        form = NewDateForm(request.POST, obj=employee)
        form.form_employee_id.choices = [(e.first_name, e.last_name) for e in Employee.query.order_by('id')]

    def edit_user(request, id):
        customer = Customer.query.get(id)
        form = NewDateForm(request.POST, obj=customer)
        form.form_customer_id.choices = [(c.first_name, c.last_name) for c in Customer.query.order_by('id')]

    def validate_date_time(self, date_field, room_field):
        if not DatesTable.query.filder_by(date_id=date_field.data, room_id=room_field.data, ).all():
            raise ValidationError("Termin an diesem Tag nicht möglich! Bitte anderes Datum wählen.")
