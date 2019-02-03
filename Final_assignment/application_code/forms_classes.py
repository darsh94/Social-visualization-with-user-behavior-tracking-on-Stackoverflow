from wtforms import *
from flask_wtf import *
import wtforms.validators
from wtforms.validators import *
from data_table_model import user_login

class login_form(FlaskForm):
    uname=StringField('Username',validators=[wtforms.validators.DataRequired()])
    password=PasswordField('Password',validators=[wtforms.validators.DataRequired()])
    submit=SubmitField('Enter the Website')

class registeraton_form(FlaskForm):
    uname=TextField('User_name',validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=3,max=10,message='The username must be atleast 3 characters')])
    password=PasswordField('Password',validators=[wtforms.validators.DataRequired(),wtforms.validators.length(min=3,max=20,message='Password should atleast have 3 characters')])
    re_password=PasswordField('confirm_Password',validators=[wtforms.validators.DataRequired(), wtforms.validators.EqualTo('password',message='The passwords should match')])
    submit=SubmitField('Register!!!')

    def check_username(self):
        user=user_login.query.filter_by(user_name=form.uname.data).first()
        if user is not None:
            raise ValidationError('Please choose a different username')





