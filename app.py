from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, get_flashed_messages
from flask_mail import Mail, Message
import os
import random
import string
import config
from user import User
import exercise

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure Flask-Mail
app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = config.MAIL_PORT
app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
app.config['MAIL_USERNAME'] = config.MAIL_ACCOUNT
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER

app.secret_key = 'your_secret_key'  # Needed for session management and flash messages

mail = Mail(app)

mail.init_app(app)
# Dummy user data
user1 = User(1, 'user1', password='123456')
user2 = User(2, 'user2', password='123456')
users = [user1, user2]

users[0].create_workout()
users[0].add_exercise(exercise.Jacknife_Situps)
users[0].add_exercise(exercise.Hiking)

@app.route('/')
def login_redirect():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        Firefly = User(0, 'firefly', password='I love you')
        if Firefly.able_to_login(username, password):
            session['username'] = username
            return redirect(url_for('firefly'))
        for user in users:
            if user.able_to_login(username, password):
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index', username=username, id=user.get_id()))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/<username>/<id>/exercises')
def exercises(username, id):
    exercises = exercise.exercises
    if 'username' in session:
        return render_template("exercises.html", exercises=exercises, user=users[int(id) - 1])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/exercises/<exercise_name>')
def exercise_detail(exercise_name):
    return render_template('exercise_details.html', exercise_name=exercise_name)

@app.route('/<username>/<id>/index')
def index(username, id):
    return render_template('index.html', username=username, user=users[int(id) - 1])

@app.route('/<username>/<id>/workouts')
def workouts(username, id):
    return render_template('MyWorkouts.html', username=username, user=users[int(id) - 1])

@app.route('/')
def landscape():
    return render_template('login.html')

@app.route('/firefly')
def firefly():
    return render_template('secret/firefly.html')

def generate_verification_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def send_verification_email(email, verification_code):
    msg = Message('Your Verification Code', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    #with app.open_resource("static/Secret/Firefly.jpg") as fp:
      #msg.attach('Firefly.jpg', 'Firefly/jpg', fp.read())
    mail.send(msg)

@app.route('/send_verification_code', methods=['POST'])
def send_verification_code():
    data = request.get_json()
    email = data.get('email')
    verification_code = generate_verification_code()

    # Store the verification code in the session
    session['verification_code'] = verification_code

    # Send the verification email
    send_verification_email(email, verification_code)

    return jsonify({'message': 'Verification code sent to your email.'})

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        verification_code = request.form['verificationCode']

        # Check if the verification code matches
        if verification_code == session.get('verification_code'):
            # Proceed with registration (e.g., save user to the database)
            flash('Registration successful!', 'success')
            users.append(User(len(users) + 1, email, password))
            return redirect(url_for('login'))
        else:
            flash('Invalid verification code. Please try again.', 'danger')

    return render_template('signup.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        verification_code = request.form['verificationCode']

        # Check if the code matches
        if verification_code == session.get('verification_code'):
            # Code is correct, proceed with registration
            flash('Email verified! You can now complete your registration.', 'success')
            return redirect(url_for('complete_registration'))
        else:
            flash('Invalid verification code. Please try again.', 'danger')

    return render_template('verify.html')

@app.route('/complete_registration', methods=['GET', 'POST'])
def complete_registration():
    # Logic to complete the registration process
    return 'Registration completed'

@app.route('/mail/text')
def mail_text():
    message = Message(subject='Agile', recipients=['xzhangha@connect.ust.hk'], body = "test")
    with app.open_resource("static/Secret/Firefly.jpg") as fp:
      message.attach('Firefly.jpg', 'Firefly/jpg', fp.read())
    mail.send(message)
    return 'mail sent'

@app.route('/check')
def user_info():
    return render_template('user_info.html', users = users)


if __name__ == "__main__":
    app.run(debug=True)
