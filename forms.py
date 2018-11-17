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


class SearchForm(FlaskForm):
    location = SelectField("", validators=[InputRequired()], choices=[('Bashundhara','Bashundhara'),('Uttara','Uttara')])
    service = SelectField("", validators=[InputRequired()], choices=[('MRI','MRI'),('X-Ray','X-Ray')])
    Submit = SubmitField("Search")


class ServiceForm(FlaskForm):
    ServiceName = StringField("", validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "Name"})
    Location = StringField("", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Location"})
    DetailsLocation = TextAreaField("", validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "details "})
    HospitalName = StringField("", validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "hospital"})
    Price = IntegerField("", render_kw={"placeholder": "price"})
    Phone = StringField("", validators=[InputRequired(), Length(min=2, max=200)], render_kw={"placeholder": "phone"})
    Submit = SubmitField("Create")
