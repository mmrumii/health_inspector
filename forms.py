from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')



class SignUpForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired(), Length(min=3, max=50)])
    lastname = StringField('lastname', validators = [InputRequired(), Length(min=3, max=50)])
    phone = StringField('phone', validators=[InputRequired(), Length(min=8,max=50)])
    user_type = SelectField("", validators=[InputRequired()], choices=[('Customer','Customer'),('S_provider','Service Provider')])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField('submit')

