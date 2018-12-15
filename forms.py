from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, SelectField, IntegerField, FloatField, SubmitField,TextAreaField
from wtforms.validators import InputRequired, Email, Length
from wtforms.fields.html5 import TelField, EmailField



class UserRegistrationForm(FlaskForm):
    FullName = StringField("",validators = [InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Full Name"})
    EmailAddress = EmailField("",validators =[InputRequired(), Email()], render_kw={"placeholder": "Email Address"})
    UserType = SelectField("", validators=[InputRequired()], choices=[('Customer','Customer'),('S_provider','Service Provider')])
    Username = StringField("",validators = [InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "@Username"})
    Password = PasswordField("", validators=[InputRequired(), Length(min=8,max=50)], render_kw={"placeholder": "Password"})
    Submit = SubmitField("Register")


class LoginForm(FlaskForm):
    Username = StringField("Username",validators = [InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "@Username"})
    Password = PasswordField("Password", validators=[InputRequired(), Length(min=8,max=50)], render_kw={"placeholder": "Password"})
    Remember = BooleanField('Remember me')
    Submit = SubmitField("Login")
