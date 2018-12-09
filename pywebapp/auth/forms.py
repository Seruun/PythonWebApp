from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    """
    Form for user login
    """
    username = StringField('Nutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Login merken?')
    submit = SubmitField('Login')


class PasswordUpdateForm(FlaskForm):
    """
    Form for user login
    """
    username = StringField('Nutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Passwort bestätigen')
    submit = SubmitField('Passwort zurücksetzen')
