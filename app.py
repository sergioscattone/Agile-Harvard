from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, get_flashed_messages
from flask_mail import Mail, Message
import os
import random
import string
import config
from user import User
from exercise import Jacknife_Situps, Hiking, exercises, Swimming

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
users[0].add_exercise(Jacknife_Situps)
users[0].add_exercise(Hiking)
users[0].create_workout()
users[0].add_exercise(Swimming)
users[0].add_exercise(Swimming)
users[0].create_workout()


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
        flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/<username>/<id>/exercises')
def exercises_page(username, id):
    if username == session['username']:
        return render_template("exercises.html", exercises=exercises, user=users[int(id) - 1])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/<username>/<id>/<exercise_id>/exercise_detail')
def exercise_detail(username, id, exercise_id):
    check_username(username)
    return render_template('exercise_details.html', exercise_name=exercises[int(exercise_id) - 1].get_name(), exercise = exercises[int(exercise_id) - 1],user = users[int(id) - 1],id = id, exercise_id = exercise_id)


# @app.route('/<username>/<id>/<exercise_id>/<workout_id>/register_exercise', methods=['POST'])
# def register_exercise(username, id, exercise_id, workout_id):
#     data = request.get_json()
#
#
#     exercise = exercises[int(exercise_id) - 1]
#     user = users[int(id) - 1]
#     user.add_exercise(exercise, workout_id)
#
#     return jsonify({'message': 'Register successful!'}), 200

@app.route('/register_exercise', methods=['POST'])
def register_exercise():
    data = request.get_json()
    exercise_id = int(data.get('exercise_id'))
    workout_index = int(data.get('workout_index'))
    user_id = int(data.get('user_id'))

    exercise = exercises[exercise_id - 1]
    user = users[user_id - 1]

    user.add_exercise(exercise, workout_index)

    return jsonify({'message': exercise.get_name() + ' register successful! ' }), 200


@app.route('/delete_exercise', methods=['POST'])
def delete_exercise():
    data = request.get_json()
    exercise_index = int(data.get('exercise_id'))
    workout_index = int(data.get('workout_index'))
    user_id = int(data.get('user_id'))

    user = users[user_id - 1]

    name = user.get_workout()[workout_index].get_exercises()[exercise_index].get_name()

    user.get_workout()[workout_index].remove_by_index(exercise_index)

    return jsonify({'message': name + ' deleted successful! ' }), 200

@app.route('/delete_workout', methods=['POST'])
def delete_workout():
    data = request.get_json()
    workout_index = int(data.get('workout_index'))
    user_id = int(data.get('user_id'))
    user = users[user_id - 1]
    name = user.get_workout()[workout_index].get_name()
    user.delete_workout_by_id(workout_index)
    return jsonify({'message': name + ' deleted successful! '}), 200


@app.route('/<username>/<id>/index')
def index(username, id):
    if username == session['username']:
        return render_template('index.html', username=username, user=users[int(id) - 1])
    return redirect(url_for('login'))

@app.route('/<username>/<id>/workouts')
def workouts(username, id):
    check_username(username)
    return render_template('MyWorkouts.html', username=username, user=users[int(id) - 1])
    user = users[int(id) - 1]
    # Create example workout if user does not have any
    if user.get_num_workouts() < 2:
        create_sample_workouts(user)
    return render_template('MyWorkouts.html', username=username, user=user)


@app.route('/<username>/<id>/workouts/<workout_name>/<workout_index>')
def workout_detail(username, id, workout_name, workout_index):
    user = users[int(id) - 1]
    return render_template('workout_details.html', username=username, uid=id, user=user, workout_name=workout_name, workout_index=workout_index,exercises = exercises)

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
    with app.open_resource("static/Secret/Firefly.jpg") as fp:
      msg.attach('Firefly.jpg', 'Firefly/jpg', fp.read())
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


@app.route('/<username>/<id>/workouts/create_workouts')
def create_page(username, id):
    if username == session['username']:
        return render_template("create_workouts.html", exercises=exercises, user=users[int(id) - 1])
    return redirect(url_for('login'))

def check_username(username):
    if username != session['username']:
        return redirect(url_for('login'))


@app.route('/<username>/<id>/workouts/create_workouts', methods=['GET', 'POST'])
def create_new_workout(username, id):
    if request.method == 'POST':
        name = request.form['workout']
        description = request.form['description']
        if 'username' in session and username == session['username']:
            user = users[int(id) - 1]
            user.get_workout().append(user.create_workout(name, description))
            if user.get_workout()[-1] is None:
                user.get_workout().pop()
        return redirect(url_for('workouts', username=username, id=id))
    return render_template('create_workouts.html', username=username, user=users[int(id) - 1])

if __name__ == "__main__":
    app.run(debug=True)
