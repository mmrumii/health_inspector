from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import InputRequired, Email, Length
from forms import *
from other_forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

##################################
#Connecting to the database and ORM as known sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import *

engine = create_engine('sqlite:///health.db')
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

# Integration with the flask login
# A flowless connection between
# User Model and Flask Login
@login_manager.user_loader
def load_user(user_id):
    user = session.query(Users).filter_by(UserIDNumber = int(user_id)).first()
    return user


# Log out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


# Password Reset
@app.route('/reset_password')
def reset_password():
    return 'password reset page'


# User Registration System
# Recieves all the datas from the
# sign up form and then store in the database
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


# User Login System
# Recieves datas from login form and
# If datas matche with database datas,
# It complete the login process
# and redirect to dashboard.
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

# First it checks the login user type,
# then redirect to specific dashboard page
# IF user_type = 'customer' then rediect to  "customer_dashboard" template
# IF user_type = 's_provider' then rediect to  "s_provider_dashboard" template
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.UserType == 'Customer':
        return render_template('customer_dashboard.html')
    elif current_user.UserType == 'S_provider':
        services = session.query(Service).filter_by(ServiceOwner=current_user.UserIDNumber).all()
        return render_template('s_provider_dashboard.html', services=services)
    else: return redirect(url_for('home'))


# HOMEPAGE
# This controller reponse user the index.html template file
@app.route('/')
def home():
    form = SearchForm(request.form)
    form.location.choices = [(srv.Location, srv.Location)for srv in session.query(Service).all()]
    form.service.choices = [(srv.ServiceName, srv.ServiceName) for srv in session.query(Service).all()]
    return render_template('index.html', form = form)


# Recieves data from home page search form
# Process the query and gather search result .
# sends those datas to search_result template
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST':
        results = session.query(Service).filter_by(ServiceName=form.service.data, Location=form.location.data).all()
        res_count = len(results)
        comment_form = CommentForm()
        return render_template('search_result.html',results=results, res_count = res_count, comment_form=comment_form)
    else: return redirect(url_for('home'))


# Response with about_us template which contains
# Development team information.
@app.route('/about')
def about():
    return render_template('about_us.html')

# Response with contact template which
# contains Contact form..
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Helper function which helps to
# identify the user type
def is_s_provider(current_user):
    if current_user.UserType == 'S_provider':
        return True
    else: return False


# Recieves the data from create new service from,
# checks if the service already exist or not and finally
# strore into database.
@app.route('/new_service', methods=['GET','POST'])
@login_required
def new_service():
    if is_s_provider(current_user):
        form = ServiceForm(request.form)
        if request.method == 'POST' and form.validate():
            serv = Service(ServiceName=form.ServiceName.data, Location=form.Location.data, DetailsLocation=form.DetailsLocation.data, HospitalName=form.HospitalName.data, Price=form.Price.data, Phone=form.Phone.data, ServiceOwner=current_user.UserIDNumber)
            session.add(serv)
            session.commit()
            flash('Service Successfully added!')
            return redirect(url_for('dashboard'))
        else:
            return render_template('new_service.html',form=form)
    else:
        return redirect(url_for('home'))

# Displays service details page
@app.route('/comments/<int:service_id>')
def comments(service_id):
    form = CommentForm()
    cmnts = session.query(Comment).filter_by(ServiceID=service_id).all()
    srv = session.query(Service).filter_by(ServiceID=service_id).first()
    cmnt_count = len(cmnts)
    return render_template('service_details.html', cmnts = cmnts, srv = srv, cmnt_count=cmnt_count,form=form)

# Recieves data from comment form
# then store into database only
# if it is not alreadt stored in databse.
@app.route('/create_comment', methods=['GET', 'POST'])
@login_required
def create_comment():
    form = CommentForm(request.form)
    if request.method == 'POST':
        check_comment = session.query(Comment).filter_by(UserIDNumber = current_user.UserIDNumber, ServiceID = request.form.get('service_id')).first()
        if check_comment:
            flash('You already have written a comment earlier.')
            return redirect(url_for('comments',service_id = request.form.get('service_id') ))
        else:
            new_comment = Comment(CommentText=form.comment_text.data, UserIDNumber=current_user.UserIDNumber, ServiceID = request.form.get('service_id'))
            session.add(new_comment)
            session.commit()
            flash("Successfully created")
            return redirect(url_for('comments',service_id = request.form.get('service_id') ))

    else: return render_template('add_comment.html', form = form)


# Displays the comment from
# after a button action.
@app.route('/add_comment/<int:service_id>')
@login_required
def show_comment_form(service_id):
    form = CommentForm(request.form)
    return render_template('add_comment.html', form = form, service_id = service_id)


#============================
# Main Function
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
