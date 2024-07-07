from flask import Flask, render_template, request, redirect, url_for, flash, session, get_flashed_messages
from user import User
import exercise
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'your_secret_key'  # Needed for session management and flash messages
# Dummy user data

user1 = User('user1', password='123456')
user2 = User('user2', password='123456')
users = [user1, user2]
@app.route('/')
def login_redirect():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        Firefly = User('firefly', password='I love you')
        if (Firefly.able_to_login(username, password)):
            session['username'] = username
            return redirect(url_for('firefly'))
        for user in users:
            if user.able_to_login(username, password):
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index', username=username, id = user.get_id()))
        else:
            flash('Invalid credentials', 'danger')
    get_flashed_messages()
    return render_template('login.html')


@app.route('/<username>/<id>/exercises')
def exercises(username, id):
    #exercises = db.exercise.query.all()
    exercises = exercise.exercises
    if 'username' in session:
        return render_template("exercises.html", exercises=exercises, user = users[int(id) - 1])
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route('/exercises/<exercise_name>')
def exercise_detail(exercise_name):
    # Replace spaces with underscores in site_name
    #exercise_name_clean = exercise_name.replace(" ", "_")
    return render_template('exercise_details.html', exercise_name=exercise_name)


@app.route('/<username>/<id>/index')
def index(username, id):
    id = int(id)
    return render_template('index.html', username=username, user = users[int(id) - 1])


@app.route('/<username>/<id>/workouts')
def workouts(username, id):
    id = int(id)
    return "This is " + users[int(id) - 1].get_username() + "'s workout page"


@app.route('/')
def landscape():
    return render_template('login.html')

@app.route('/firefly')
def firefly():
    return render_template('secret/firefly.html')

if __name__ == "__main__":
    app.run(debug=True)
