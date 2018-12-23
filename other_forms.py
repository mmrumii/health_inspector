from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, PasswordField, BooleanField, DateField, SelectField, IntegerField, FloatField, SubmitField,TextAreaField


class ServiceForm(Form):
    ServiceName = StringField("service name", [validators.DataRequired()], render_kw={"placeholder": "Name"})
    Location = StringField("location", [validators.DataRequired(),validators.Length(min=2, max=20)], render_kw={"placeholder": "Location"})
    DetailsLocation = StringField("details Location", [validators.DataRequired()], render_kw={"placeholder": "details "})
    HospitalName = StringField("hospital Name", [validators.DataRequired()], render_kw={"placeholder": "hospital"})
    Price = IntegerField("price", render_kw={"placeholder": "price"})
    Phone = StringField("phone", render_kw={"placeholder": "phone"})
    Submit = SubmitField("Create")


class SearchForm(Form):
    location = SelectField("", [validators.DataRequired()], choices=[])
    service = SelectField("", [validators.DataRequired()], choices=[])
    Submit = SubmitField("Search")


class CommentForm(Form):
    comment_text = TextAreaField("Comment", [validators.DataRequired()], render_kw={"placeholder": "Type your comment here"} )
    Submit = SubmitField("Done")
