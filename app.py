from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Welcome to Flex Fit!'
    return render_template('index.html')

# Define a route for handling the form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    return f'Hello, {name}, Welcome to Flex Fit!'

if __name__ == "__main__":
   app.run(debug=True)