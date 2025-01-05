
#================================================
'''# Authentification
@login_manager.user_loader
def loader_user(user_id):
    from models import Users
    return Users.query.get(user_id)

@app.route("/register", methods=["GET", "POST"])
def register():
    from models import Users
    if request.method == "POST":
        user = Users(username=request.form.get("username"), email=request.form.get("email"), password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login by username and password"""
    from models import Users
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("home"))
    return render_template("index.html")
 

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/")
def home():
    return render_template("home.html")
'''

"""from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import requests  # Use requests to make API calls
import traceback 
import json

app = Flask(__name__, static_folder='assets', static_url_path='/assets') 
 
app.secret_key = 'Reçport_ç_2025&app'  # Used for flashing messages

# Load users from a JSON file
def load_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

# Authenticate user
def authenticate(username, password):
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the credentials are correct
        if authenticate(username, password):
            return redirect(url_for('dashboard', user_name=username))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

# Route for dashboard page
@app.route('/dashboard')
def dashboard():
    # Retrieve user_name from the URL
    user_name = request.args.get('user_name')
    return render_template('dashboard.html', user_name=user_name)

# Route for dashboard page
@app.route('/dashboard')
def logout():
    # Retrieve user_name from the URL
    #user_name = request.args.get('user_name')
    return url_for('index')#, user_name=user_name)


# Register the API blueprint
from api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/report')
def index():
    try:
        page = int(request.args.get('page', 1))
        
        # Make a request to the API to fetch patient data
        response = requests.get(f'http://localhost:5000/api/patients?page={page}')
        
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            patients = data.get('patients', [])
            total_pages = data.get('total_pages', 0)
        else:
            # Handle error if API request fails
            patients = []
            total_pages = 0
        
        # Pass the data to the template
        return render_template(
            'index.html',
            show_patient_list=True,
            patients=patients,
            page=page,
            total_pages=total_pages
        )
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return "An error occurred", 500


@app.route('/patient/<int:patient_id>')
def patient_report(patient_id):
    try:
        # Fetch the patient report by calling the API endpoint
        response = requests.get(f'http://localhost:5000/api/patient_report/{patient_id}')
        
        if response.status_code == 200:
            # Parse the full report string returned by the API
            full_report = response.json().get('report', '')
            report_sections = full_report.split("\n\n")

            if len(report_sections) < 3:
                error = "Report is incomplete. Please check the data."
                return render_template('index.html', error=error)

            # Extract report, diagnosis, and recommendations
            report_data = eval(report_sections[0])  # Convert string to dictionary
            diagnosis = report_sections[1]
            recommendations = report_sections[2]

            # Pass parsed data to the template
            return render_template(
                'index.html',
                report_string=report_data,
                diagnosis=diagnosis,
                recommendations=recommendations,
                patient_id=patient_id
            )
        else:
            error = response.json().get('error', 'Unknown error occurred')
            return render_template('index.html', error=error)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return "An error occurred", 500


@app.route('/generate_pdf/<int:patient_id>')
def generate_pdf(patient_id):
    # Redirect to the API endpoint for PDF generation
    return redirect(f'/api/generate_pdf/{patient_id}')

if __name__ == '__main__':
    app.run(debug=True)"""
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import requests
import traceback
import json
import os

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

app.secret_key = 'Reçport_ç_2025&app'  # Used for flashing messages

# Load users from a JSON file
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            users = json.load(file)
    else:
        users = []
    return users

# Save users to a JSON file
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

# Authenticate user
def authenticate(username, password):
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

# Register user (Sign Up)
def register(username, password):
    users = load_users()
    # Check if the username already exists
    for user in users:
        if user['username'] == username:
            return False
    # If the username doesn't exist, create a new user
    users.append({'username': username, 'password': password})
    save_users(users)
    return True

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the credentials are correct
        if authenticate(username, password):
            session['user_name'] = username  # Store the username in the session
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

# Route for sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if register(username, password):
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('sign_up'))

    return render_template('sign_up.html')

# Route for dashboard page
@app.route('/dashboard')
def dashboard():
    if 'user_name' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    
    user_name = session['user_name']
    return render_template('dashboard.html', user_name=user_name)

# Route for logout
@app.route('/logout')
def logout():
    session.pop('user_name', None)  # Remove user from session
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Route for report (only accessible to logged-in users)
@app.route('/report')
def index():
    if 'user_name' not in session:
        flash('Please log in to access the report.', 'error')
        return redirect(url_for('login'))
    
    try:
        page = int(request.args.get('page', 1))

        # Make a request to the API to fetch patient data
        response = requests.get(f'http://localhost:5000/api/patients?page={page}')

        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            patients = data.get('patients', [])
            total_pages = data.get('total_pages', 0)
        else:
            # Handle error if API request fails
            patients = []
            total_pages = 0

        # Pass the data to the template
        redirect("index")
        return render_template(
            'index.html',
            show_patient_list=True,
            patients=patients,
            page=page,
            total_pages=total_pages
        )
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return "An error occurred", 500


@app.route('/patient/<int:patient_id>')
def patient_report(patient_id):
    if 'user_name' not in session:
        flash('Please log in to access the report.', 'error')
        return redirect(url_for('login'))

    try:
        # Fetch the patient report by calling the API endpoint
        response = requests.get(f'http://localhost:5000/api/patient_report/{patient_id}')

        if response.status_code == 200:
            # Parse the full report string returned by the API
            full_report = response.json().get('report', '')
            report_sections = full_report.split("\n\n")

            if len(report_sections) < 3:
                error = "Report is incomplete. Please check the data."
                return render_template('index.html', error=error)

            # Extract report, diagnosis, and recommendations
            report_data = eval(report_sections[0])  # Convert string to dictionary
            diagnosis = report_sections[1]
            recommendations = report_sections[2]

            # Pass parsed data to the template
            return render_template(
                'index.html',
                report_string=report_data,
                diagnosis=diagnosis,
                recommendations=recommendations,
                patient_id=patient_id
            )
        else:
            error = response.json().get('error', 'Unknown error occurred')
            redirect("/report")
            return render_template('index.html', error=error)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return "An error occurred", 500


@app.route('/generate_pdf/<int:patient_id>')
def generate_pdf(patient_id):
    return redirect(f'/api/generate_pdf/{patient_id}')



@app.route('/about')
def about():
    # Render the about.html page
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
