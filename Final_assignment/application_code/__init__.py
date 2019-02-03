from flask import *
from flask_cors import CORS
from config_file import config_var
import flask_migrate as fm
import flask_sqlalchemy as fs
import flask_login






application=Flask(__name__)
application.config.from_object(config_var)
CORS(application)
# For setting up the database everytime the system is run
database_var=fs.SQLAlchemy(application)
database_migration=fm.Migrate(application,database_var)

# For letting the user_login
login_var=flask_login.LoginManager(application)
login_var.login_view='login_page'


# print(application)

from application_code import routing,data_table_model