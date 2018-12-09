from flask import Blueprint

admin = Blueprint('employee', __name__)

from . import views
