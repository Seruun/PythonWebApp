from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee


class AddEmployeeForm(FlaskForm):
    """
    Form for new user creation
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Nutzername', validators=[DataRequired()])
    first_name = StringField('Vorname', validators=[DataRequired()])
    last_name = StringField('Nachname', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Passwort bestätigen')
    role_id = StringField('Mitarbeiter Rolle [1: Mitarbeiter, 2: Teamleiter, 3: Admin]', validators=[DataRequired()])
    submit = SubmitField('Erstellen')

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email bereits in Benutzung!')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Nutzername beretis vergeben!')