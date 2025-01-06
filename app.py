from flask import Flask, render_template, request, jsonify, redirect, session, url_for, flash
import requests  # Use requests to make API calls
import traceback
from auth import authenticate, register  # Import authentication functions from auth.py

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

# Register the API blueprint
from api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

app.secret_key = 'Reçport_ç_2025&app'  # Used for flashing messages

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # This should match the input name attribute
        password = request.form['password']

        # Check if the credentials are correct
        if authenticate(email, password):  # Use email for authentication
            session['user_email'] = email  # Store the email in the session, not username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')  # Error message for email or password mismatch
            return redirect(url_for('login'))  # Redirect back to login page with error message

    return render_template('login.html')  # Render the login page on GET request

# Route for sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['uname']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']

        # Validate the form
        if not username or not email or not password or not re_password:
            flash('All fields are required.', 'error')
            return render_template('signup.html', error='Please fill in all fields.')

        if password != re_password:
            flash('Passwords do not match.', 'error')
            return render_template('signup.html', error='Passwords do not match.')

        # Register the user with username, password, and email
        if register(username, password, email):
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose a different one.', 'error')
            return render_template('signup.html', error='Username already exists.')

    return render_template('signup.html')

# Route for dashboard page
@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    
    user_email = session['user_email']
    return render_template('dashboard.html', user_email=user_email)

# Route for logout
@app.route('/logout')
def logout():
    session.pop('user_email', None)  # Remove user from session
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Route for reports page
@app.route('/')
def reports():
    if 'user_email' not in session:
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
        return render_template(
            'reports.html',  # Ensure this is the correct template
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
                return render_template('reports.html', error=error)

            # Extract report, diagnosis, and recommendations
            report_data = eval(report_sections[0])  # Convert string to dictionary
            diagnosis = report_sections[1]
            recommendations = report_sections[2]

            # Pass parsed data to the template
            return render_template(
                'reports.html',
                report_string=report_data,
                diagnosis=diagnosis,
                recommendations=recommendations,
                patient_id=patient_id
            )
        else:
            error = response.json().get('error', 'Unknown error occurred')
            return render_template('reports.html', error=error)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()
        return "An error occurred", 500
   
# @app.route('/patient/<int:patient_id>')
# def patient_report(patient_id):
#     if 'user_email' not in session:
#         flash('Please log in to access the report.', 'error')
#         return redirect(url_for('login'))
    
#     try:
#         # Fetch the patient report by calling the API endpoint
#         response = requests.get(f'http://localhost:5000/api/patient_report/{patient_id}')
        
#         if response.status_code == 200:
#             # Parse the full report string returned by the API
#             full_report = response.json().get('report', '')
#             report_sections = full_report.split("\n\n")

#             if len(report_sections) < 3:
#                 error = "Report is incomplete. Please check the data."
#                 return render_template('reports.html', error=error)

#             # Try parsing the JSON data safely
#             try:
#                 # Use Python's standard JSON module for parsing
#                 report_data = json.loads(report_sections[0])  # Use json.loads instead of eval
#             except json.JSONDecodeError as e:  # Catch JSONDecodeError from the standard json module
#                 print(f"JSON Decode Error: {e}")
#                 print(f"Malformed JSON: {report_sections[0]}")
#                 return render_template('reports.html', error="There was an issue parsing the report.")

#             diagnosis = report_sections[1]
#             recommendations = report_sections[2]

#             # Pass parsed data to the template
#             return render_template(
#                 'reports.html',
#                 report_string=report_data,
#                 diagnosis=diagnosis,
#                 recommendations=recommendations,
#                 patient_id=patient_id
#             )
#         else:
#             error = response.json().get('error', 'Unknown error occurred')
#             return render_template('reports.html', error=error)
#     except Exception as e:
#         print("Error:", e)
#         traceback.print_exc()
#         return "An error occurred", 500

@app.route('/generate_pdf/<int:patient_id>')
def generate_pdf(patient_id):
    if 'user_email' not in session:
        flash('Please log in to access the report.', 'error')
        return redirect(url_for('login'))
        
    # Redirect to the API endpoint for PDF generation
    return redirect(f'/api/generate_pdf/{patient_id}')

if __name__ == '__main__':
    app.run(debug=True)
