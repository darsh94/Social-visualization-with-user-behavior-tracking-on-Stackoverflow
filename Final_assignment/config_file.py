import os
base_directory=os.path.abspath(os.path.dirname(__file__))

class config_var(object):
    SECRET_KEY='hello'
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(base_directory,'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False