# PythonWebApp

Small Web Application with implemented Calendar based on Python Flask and Jinja2.

Active Developed at the moment.
Will be turned into a full functional CMS System based on Python & Flask.
=> EligorCMS

### Requirements
- Python 3.7
- SQLite | MySQL | PostgreSQL (choose your preferred Database)

#### Tools used for Development
JetBrains: PyCharm Professional & WebStorm

####

How to use it:
- Clone from Github
- create on root a folder named "instance"
- in instance create file named "config.py"
- in this config file you need to define the "SECRET_KEY" for example SECRET_KEY = '7q659cwib7'
- you need also to define the database connection for example:
- MySQL -> SQLALCHEMY_DATABASE_URI = 'mysql://db_user:user_pass@localhost/db_name'
- SQLite -> SQLALCHEMY_DATABASE_URI = 'sqlite:////absolute/path/to/db_name.db'
- MongoDB -> SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:user_pass@localhost/db_name'
