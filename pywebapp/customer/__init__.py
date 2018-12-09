from flask import Blueprint

admin = Blueprint('customer', __name__)

from . import views
