# run.py

import os

from pywebapp import create_app

config_name = os.getenv('FLASK_ENV', 'default')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()
