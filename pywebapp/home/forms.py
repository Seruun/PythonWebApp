from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email

from ..models import Customer


class NewCustomerForm(FlaskForm):
    """
    Form for new user creation
    """
    id = StringField('Kundennummer', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('Vorname', validators=[DataRequired()])
    last_name = StringField('Nachname', validators=[DataRequired()])
    address = StringField('Adresse', validators=[DataRequired()])
    phone_number = StringField('Telefonnummer', validators=[DataRequired()])
    submit = SubmitField('Erstellen')

    def validate_email(self, field):
        if Customer.query.filter_by(email=field.data).first():
            raise ValidationError('Email bereits in Benutzung!')

    def validate_customer_id(self, field):
        if Customer.query.filter_by(id=field.data).first():
            raise ValidationError('Kundennummer bereits vergeben!')
