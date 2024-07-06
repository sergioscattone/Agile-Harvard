from flask import Flask, render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/exercises')
def exercises():
    #exercises = db.exercise.query.all()
    exercises = ["Bicep Curl", "Jacknife Situps", "Swimming", "Jogging", "Hiking", "Table Tennis"]
    return render_template("exercises.html", exercises=exercises)


@app.route('/exercises/<exercise_name>')
def exercise_detail(exercise_name):
    # Replace spaces with underscores in site_name
    exercise_name_clean = exercise_name.replace(" ", "_")
    return render_template('exercise_details.html', exercise_name=exercise_name_clean)

@app.route('/workloads')
def workloads():
    return "Section still under construction :)"

@app.route('/')
def landscape():
    return render_template('index.html')


if __name__ == "__main__":
   app.run(debug=True)