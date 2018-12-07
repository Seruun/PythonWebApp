# Eligor_CMS/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from Eligor_CMS import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    full_name = db.Column(db.String(121), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        """
        Reset password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'Employee: {}'.format(self.full_name)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return 'Role: {}'.format(self.name)


class Room(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return 'Raum: {}'.format(self.id)


class Customer(db.Model):
    """
    Create a DatesTable table
    """

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    full_name = db.Column(db.String(121), index=True)
    address = db.Column(db.String(60), index=True)
    phone_number = db.Column(db.String(15), index=True)

    def __repr__(self):
        return 'Kundennummer: {} \n Vorname: {} \n Nachname: {}'.format(self.id, self.first_name, self.last_name)


class DatesTable(db.Model):
    """
    Create a DatesTable table
    """

    __tablename__ = 'dates_table'

    id = db.Column(db.Integer, primary_key=True)

    start_time = db.Column(db.Integer, index=True)
    duration = db.Column(db.Integer, index=True)
    end_time = db.Column(db.Integer, index=True)

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    employee = db.Column(db.String(121), index=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.Column(db.String(121), index=True)
    room = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    date_id = db.Column(db.Integer, db.ForeignKey('calendar_table.id'))
    date = db.Column(db.String(10), db.ForeignKey('calendar_table.full_date'))

    def __repr__(self):
        return 'Kundennummer: {} \n Kunde: {} \n Tattowierer: {} \n Datum: {} \n Raum: {} \n Uhrzeit (Beginn): {} \n Dauer: {}'.format(
            self.customers_id, self.customers, self.employee, self.date, self.room, self.start_time, self.duration)


class CalendarTable(db.Model):
    """
    Create a CalendarTable table
    """

    __tablename__ = 'calendar_table'

    id = db.Column(db.Integer, primary_key=True)
    full_date = db.Column(db.String(10), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return 'Datum_ID {} -> Datum: {}'.format(self.id, self.full_date)


class TimeTable(db.Model):
    """
    Create a TimeTable table
    """

    __tablename__ = 'time_table'

    id = db.Column(db.Integer, primary_key=True)
    full_time = db.Column(db.String(5), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return 'Uhrzeit_ID {} -> Uhrzeit: {}'.format(self.id, self.full_time)
