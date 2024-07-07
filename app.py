from flask import Flask, render_template, request, redirect, url_for, flash, session, get_flashed_messages
from user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'your_secret_key'  # Needed for session management and flash messages
# Dummy user data

exercises = ["Bicep Curl", "Jacknife Situps", "Swimming", "Jogging", "Hiking", "Table Tennis"]
user1 = User('user1', password='password1')
user2 = User('user2', password='passward2')
users = [user1, user2]
@app.route('/')
def login_redirect():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user.able_to_login(username, password):
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index', username=username, id = user.get_id()))
        else:
            flash('Invalid credentials', 'danger')
    get_flashed_messages()
    return render_template('login.html')


@app.route('/exercises')
def exercises():
    #exercises = db.exercise.query.all()
    if 'username' in session:
        exercises = ["Bicep Curl", "Jacknife Situps", "Swimming", "Jogging", "Hiking", "Table Tennis"]
        return render_template("exercises.html", exercises=exercises)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route('/exercises/<exercise_name>')
def exercise_detail(exercise_name):
    # Replace spaces with underscores in site_name
    exercise_name_clean = exercise_name.replace(" ", "_")
    return render_template('exercise_details.html', exercise_name=exercise_name_clean)


@app.route('/index/<username>/<id>')
def index(username, id):
    return render_template('index.html', username=username, user = users[int(id)])


@app.route('/workouts')
def workouts():
    return "Section still under construction :)"


@app.route('/')
def landscape():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
