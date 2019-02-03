from application_code import database_var,login_var
import datetime
# For keeping track of the users, hwo is logged in
from flask_login import UserMixin
# For hashing the password
from werkzeug.security import generate_password_hash, check_password_hash



# For tracking the user behviour
# @login_var.user_loader
# def get_user_from_db(id):
#     user=user_login.query.get(int(id))
#     return user
@login_var.user_loader
def getload_user(id):
    user=user_login.query.get(int(id))
    return user




# Class-to-table mappings

# Mapping for user_login tabe in the db
class user_login(UserMixin,database_var.Model):

    def set_hashed_password(self,password_given):
        hashed=self.hashed_password=generate_password_hash(password_given)
        return hashed

    def verify_password(self,password_given):
        result=check_password_hash(self.hashed_password,password_given)
        return result


    id=database_var.Column(database_var.Integer,primary_key=True)
    user_name=database_var.Column(database_var.String(20),index=True,unique=True)
    hashed_password=database_var.Column(database_var.String(50))
    user_logs=database_var.relationship('user_logging',backref='time',lazy='dynamic')
    user_activity=database_var.relationship('user_stackoverflow_activity',backref='time',lazy='dynamic')

# Mapping for user_logging table in the db
class user_logging(database_var.Model):
    id=database_var.Column(database_var.Integer,primary_key=True)
    user_id=database_var.Column(database_var.Integer,database_var.ForeignKey('user_login.id'))
    timestamp = database_var.Column(database_var.DateTime, index=True, default=datetime.datetime.utcnow)
    type=database_var.Column(database_var.String(10))


class user_stackoverflow_activity(database_var.Model):
    id=database_var.Column(database_var.Integer,primary_key=True)
    user_id=database_var.Column(database_var.Integer,database_var.ForeignKey('user_login.id'))
    event=database_var.Column(database_var.String(10))
    count=database_var.Column(database_var.Integer)
    timestamp=database_var.Column(database_var.DateTime, index=True, default=datetime.datetime.utcnow)


    #
    # def __repr__(self):
    #     return '<User {}>'.format(self.user_id)