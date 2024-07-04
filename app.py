from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f' {self.exercise}'

with app.app_context():
    db.create_all()

@app.route('/exercises')
def exercises():
    #exercises = db.exercise.query.all()
    exercises = ["Bicep Curl", "Jacknife Situps", "Swimming", "Jogging", "Hiking", "Table Tennis"]
    return render_template("exercises.html", exercises=exercises)


@app.route('/exercises/<exercise_name>')
def exercise_detail(site_name):
    # Replace spaces with underscores in site_name
    exercise_name_clean = site_name.replace(" ", "_")
    return render_template('exercise_details.html', exercise_name=exercise_name_clean)

@app.route('/workloads')
def workloads():
    return "Section still under construction :)"

@app.route('/')
def landscape():
    return render_template('index.html')


if __name__ == "__main__":
   app.run(debug=True)