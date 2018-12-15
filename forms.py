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
    location = SelectField("", validators=[InputRequired()], choices=[('Bashundhara','Bashundhara'),('Uttara','Uttara'),('Badda','Badda'),('Banani','Banani'),('Gulshan','Gulshan'),('Dhanmondi','Dhanmondi'),('Jatrabari','Jatrabari'),('Kalabagan','Kalabagan'),('Keraniganj','Keraniganj'),('Khilgaon','Khilgaon'),('Khilkhet','Khilkhet'),('Mirpur','Mirpur'),('Mohammadpur','Mohammadpur'),('Motijheel','Motijheel'),('Paltan','Paltan '),('Ramna','Ramna'),('Rampura','Rampura'),('Bashabo','Bashabo'),('Sabujbagh','Sabujbagh'),('Savar','Savar'),('Shahbagh ','Shahbagh'),('Shyampur','Shyampur'),('Sutrapur','Sutrapur'),('Tejgaon','Tejgaon')])
    service = SelectField("", validators=[InputRequired()], choices=[('MRI','MRI'),('X-Ray','X-Ray'),('CT scan','CT scan'),('Mammography','Mammography'),('Ultrasound','Ultrasound'),('Blood Sugar Test','Blood Sugar Test'),('Liver Function Test','Liver Function Test'),('Bilirubin Test','Bilirubin Test'),('T3/T4','T3/T4'),('Electrolytes (NA,K,CL,HCO3)','Electrolytes (NA,K,CL,HCO3)'),('Blood Gases (ABG)','Blood Gases (ABG)'),('PSA (Prostate Specific Antigen)','PSA (Prostate Specific Antigen)'),('Troponin I','Troponin I'),('Echocardiogram','Echocardiogram'),('Echo Color Doppler','Echo Color Doppler'),('Stress Test (TMT)','Stress Test (TMT)'),('Holter monitor','Holter monitor'),('Electrophysiology Study (EPS) & Ablation','Electrophysiology Study (EPS) & Ablation'),('Electrocardiogram (ECG)','Electrocardiogram (ECG)'),('Hearing screening test','Hearing screening test'),('Stool/Urine R/M/E (Routine)','Stool/Urine R/M/E (Routine)'),('Mantoux Test (MT)','Mantoux Test (MT)'),('Semen Analysis','Semen Analysis'),('Bone Marrow Biopsy Procedure & Opinion','Bone Marrow Biopsy Procedure & Opinion'),('Biopsy','Biopsy'),('Blood CS','Blood CS'),('Urine CS','Urine CS'),('HBV-DNA','HBV-DNA'),('Scaling and polishing Teeth','Scaling and polishing Teeth'),('Fillings, extractions and dentures teeth','Fillings, extractions and dentures teeth'),('Root canal therapy','Root canal therapy'),('Crown and bridgework','Crown and bridgework'),('Ovulation induction and cycle monitoring','Ovulation induction and cycle monitoring'),('Intra-Uterine Insemination (IUI)','Intra-Uterine Insemination (IUI)'),('In Vitro Fertilisation (IVF)','In Vitro Fertilisation (IVF)'),('Surgical sperm retrieval(MESA, TESA & PESA)','Surgical sperm retrieval(MESA, TESA & PESA)'),('Intra-Cytoplasmic Sperm Injection (ICSI)','Intra-Cytoplasmic Sperm Injection (ICSI)'),('Egg freezing','Egg freezing'),('Semen freezing','Semen freezing'),('Laser angioplasty','Laser angioplasty')])
    Submit = SubmitField("Search")


class ServiceForm(FlaskForm):
    ServiceName = StringField("", validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "Name"})
    Location = StringField("", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Location"})
    DetailsLocation = TextAreaField("", validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "details "})
    HospitalName = StringField("", validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "hospital"})
    Price = IntegerField("", render_kw={"placeholder": "price"})
    Phone = StringField("", validators=[InputRequired(), Length(min=2, max=200)], render_kw={"placeholder": "phone"})
    Submit = SubmitField("Create")
