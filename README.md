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
├── model_assets

│   ├── model.pkl

│   └── vectorizer.pkl

├── model_dev
│   ├── data
│   |   └── data.json
│   └── model_dev.ipynb
├── templates
│   └── index.html 
├── assets
│   ── css
│   ── fonts
│   ── img
│   ── js
│   ── scss
├── app.py
├── api.py
├── auth.py
├── pdf_generator.py
├── report_generator.py
├── data.zip
├── users.json
├── requirements.txt
└── README.md
