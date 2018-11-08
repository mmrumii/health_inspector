from flask import Flask, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#Connecting to the database and ORM as known sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, User

engine = create_engine('sqlite:///health.db')
Base.metadata.bind = engine
#Creates the session
DBSession = sessionmaker(bind = engine)
session = DBSession()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret_key'


#################Login################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
######################################

@login_manager.user_loader
def load_user(user_id):
    userId = session.query(User).filter_by(id = int(user_id)).first()
    return userId


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        tempUser = form.username.data
        user = session.query(User).filter_by(username=tempUser).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form = form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        newUser = User(firstname=form.firstname.data, lastname=form.lastname.data, phone=form.phone.data, email=form.email.data, username=form.username.data, password=hashed_password)
        session.add(newUser)
        session.commit()
        return '<h1>Done</h1>'
    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():

    return render_template('dashboard.html', firstname = current_user.firstname, lastname = current_user.lastname, username = current_user.username, phone=current_user.phone, email=current_user.email, )



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
