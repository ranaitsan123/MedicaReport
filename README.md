## First clone the repo locally.
git clone https://github.com/MarwaneMLE/generate-medical-report.git

## Create a new virtual environment in the project directory.
python3 -m venv ./venv

## Activate the virtual environment.
source venv/bin/activate
While in the virtual environment, install required dependencies from requirements.txt.

## Install requirements
pip install -r ./requirements.txt  

## Run the app
python app.py

and navigate to http://127.0.0.1:5000/ to see it live. to explore the web app

# Project Structure

generate-medical-report 

generate-medical-report
├── model_dev
│   ├── data
│   │   └── data.json         # Sample data used for development
│   └── model_dev.ipynb       # Jupyter notebook for model development
├── templates
│   └── index.html            # Main HTML template for the web interface
│   └── reports.html          # Main HTML template for the web reports
│   └── login.html            # Main HTML template for the web login
│   └── dashboard.html        # Main HTML template for the web dashboard
│   └── signup.html           # Main HTML template for the web signup
├── assets
│   ├── css                   # CSS files for styling
│   ├── fonts                 # Font files used in the app
│   ├── img                   # Image assets for the app
│   ├── js                    # JavaScript files for frontend functionality
│   └── scss                  # SCSS files for custom styles
├── app.py                    # Main application file
├── api.py                    # API routes for interaction
├── auth.py                   # Authentication related functions
├── pdf_generator.py          # PDF report generation logic
├── report_generator.py       # Logic to generate medical reports
├── data.zip                  # Compressed data file used by the app
├── users.json                # User data in JSON format
├── requirements.txt          # Python dependencies for the project
└── README.md                 # Project documentation




├── model_dev
│   ├── data
│   │   └── data.json            # Sample data used for development
│   └── model_dev.ipynb          # Jupyter notebook for model development
├── templates
│   └── index.html               # Main HTML template for the web interface
│   └── reports.html             # Main HTML template for the web reports
│   └── login.html               # Main HTML template for the web login
│   └── dashborad.html           # Main HTML template for the web dashborad
│   └── signup.html              # Main HTML template for the web signup
├── assets
│   ├── css                      # CSS files for styling
│   ├── fonts                    # Font files used in the app
│   ├── img                      # Image assets for the app
│   ├── js                       # JavaScript files for frontend functionality
│   └── scss                     # SCSS files for custom styles
├── app.py                        # Main application file
├── api.py                        # API routes for interaction
├── auth.py                       # Authentication related functions
├── pdf_generator.py              # PDF report generation logic
├── report_generator.py           # Logic to generate medical reports
├── data.zip                      # Compressed data file used by the app
├── users.json                    # User data in JSON format
├── requirements.txt              # Python dependencies for the project
└── README.md                     # Project documentation
