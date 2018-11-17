from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import InputRequired, Email, Length
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

##################################
#Connecting to the database and ORM as known sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import *

engine = create_engine('sqlite:///classroom.db')
Base.metadata.bind = engine
#Creates the session


session = scoped_session(sessionmaker(bind=engine))


@app.teardown_request
def remove_session(ex=None):
    session.remove()


###############################

bootstrap = Bootstrap(app)

#################Login################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
######################################


@login_manager.user_loader
def load_user(user_id):
    userId = session.query(Users).filter_by(UserIDNumber = int(user_id)).first()
    return userId


# Log out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


# Password Reset
@app.route('/reset_password')
def reset_password():
    return 'password reset page'


# Registration System
@app.route('/register',  methods=['GET','POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    RegForm = UserRegistrationForm()
    if RegForm.validate_on_submit():
        hashed_password = generate_password_hash(RegForm.Password.data, method='sha256')
        newUser = Users(FullName=RegForm.FullName.data, Username=RegForm.Username.data, UserType = RegForm.UserType.data, EmailAddress=RegForm.EmailAddress.data, Password=hashed_password)
        session.add(newUser)
        session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', RegForm=RegForm)




# Login System
@app.route('/login', methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        tempUser = loginForm.Username.data
        user = session.query(Users).filter_by(Username=tempUser).first()
        if user:
            if check_password_hash(user.Password, loginForm.Password.data):
                login_user(user, remember=loginForm.Remember.data)
                return redirect(url_for('dashboard'))

    return render_template('login.html', LoginForm = loginForm)


# General User Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.UserType == 'Customer':
        return render_template('customer_dashboard.html')
    elif current_user.UserType == 'S_provider':
        return render_template('s_provider_dashboard.html')
    else: return redirect(url_for('home'))


# HOMEPAGE
@app.route('/')
def home():
    form = SearchForm()

    return render_template('index.html', form = form)

@app.route('/')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')



'''
Teacher's Functionalities
Classroom, Exam, Assignment management
'''


def is_s_provider(current_user):
    if current_user.UserType == 'S_provider':
        return True
    else: return False

'''
# Create New University
@app.route('/new_service', methods=['GET','POST'])
@login_required
def new_service():
    service_form = ServiceForm()
    if service_form.validate_on_submit():
        #university = University(UniName = university_form.Name.data, WikiLink=university_form.WikiLink.data, Location=university_form.Location.data, LocationLink=university_form.LocationLink.data, WebsiteLink=university_form.WebsiteLink.data, Establishment=university_form.Establishment.data, Type=university_form.Type.data, StudentQuantity=university_form.StudentQuantity.data, Ranking=university_form.Ranking.data, Climate=university_form.Climate.data, LivingCost=university_form.LivingCost.data, CurrencyName=university_form.CurrencyName.data, StudentFacultyRatio=university_form.StudentFacultyRatio.data, ApplicationMedium=university_form.ApplicationMedium.data, CountryName=university_form.CountryName.data)
        #session.add(university)
        #session.commit()
        #return redirect(url_for('universities'))
        return "validated"
    return render_template('new_service.html',form=service_form)
'''


#===============================
# Main Function
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
