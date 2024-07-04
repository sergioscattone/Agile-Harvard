from flask import Flask, render_template, request
app = Flask(__name__)


# Define a route for handling the form submission
@app.route('/exercise', methods=['POST'])
def exercise_form():
    # name = request.form['name']
    sites = ["Bicep Curl", "Jacknife Situps"]
    return render_template("exercises.html", sites=sites)


@app.route('/site/<site_name>')
def site_detail(site_name):
    # Replace spaces with underscores in site_name
    site_name_clean = site_name.replace(" ", "_")
    return render_template('exercise_details.html', site_name=site_name_clean)


@app.route('/')
def hello_world():
    # return 'Welcome to Flex Fit!'
    return render_template('index.html')


if __name__ == "__main__":
   app.run(debug=True)