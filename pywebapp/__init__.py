import os

# third-party imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config
from datetime import datetime
from .globals import REV_NUM, title_name

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    elif os.getenv('FLASK_CONFIG') == "testing":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config['development'])
        app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "Du must eingeloggt sein um diese Seite zu sehen!"
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    from pywebapp import models

    from .employee import employee as employee_blueprint
    app.register_blueprint(employee_blueprint)

    from .customer import customer as customer_blueprint
    app.register_blueprint(customer_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .calendar import dates as dates_blueprint
    app.register_blueprint(dates_blueprint)

    @app.context_processor
    def inject_now():
        """
        Footer Copyright Year Getter
        """
        return {'now': datetime.utcnow()}

    @app.context_processor
    def revision():
        return {'rev_version': REV_NUM}

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('error_pages/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error_pages/404.html', title='Page Not Found'), 404

    @app.errorhandler(405)
    def not_allowed_error(error):
        return render_template('error_pages/405.html', title='Permission Denied'), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('error_pages/500.html', title='Server Error'), 500

    return app
