from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
  #email, password, sumit_button
  email = StringField('Email', validators= [DataRequired(), Email()])
  first_name = StringField('first name')
  last_name = StringField('last Name')
  password = PasswordField('passowrd', validators=[DataRequired()])
  submit_button = SubmitField()
