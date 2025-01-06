First clone the repo locally.

git clone https://github.com/MarwaneMLE/generate-medical-report.git
Create a new virtual environment in the project directory.

python3 -m venv ./venv
Activate the virtual environment.

source venv/bin/activate
While in the virtual environment, install required dependencies from requirements.txt.

pip install -r ./requirements.txt
Now we can deploy the web application via

python app.py

and navigate to http://127.0.0.1:5000/ to see it live. to explore the web app
