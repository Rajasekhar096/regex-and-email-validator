from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for regex matching
@app.route('/regex', methods=['POST'])
def regex_match():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    
    matches = re.findall(regex_pattern, test_string)
    
    return render_template('index.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)

# Route for email validation
@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Check if email matches the regex pattern
    if re.match(email_regex, email):
        validation_result = "Valid email address"
    else:
        validation_result = "Not a valid email address"
    
    return render_template('index.html', validation_result=validation_result)

if __name__ == '__main__':
    app.run(debug=True)
