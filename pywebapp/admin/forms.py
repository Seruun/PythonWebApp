from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from ..models import Department, Role


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Adresse', validators=[DataRequired()])
    submit = SubmitField('Standort hinzufgen')


class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Rechte', validators=[DataRequired()])
    description = StringField('Beschreibung', validators=[DataRequired()])
    submit = SubmitField('Recht einrichten')


class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Zuweisen')
