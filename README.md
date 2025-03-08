# [MedicaReport](https://medica-report.framer.website/)

![version](https://img.shields.io/badge/version-2.1.0-blue.svg)

![Image Preview](https://github.com/user-attachments/assets/41a9272f-e0bb-4b91-9e7d-b52c60dac72d)

MedicaReport is a web app designed for doctors to access patient medical reports generated from ambulance datasets. The reports are made available to the doctors before the ambulance arrives at the hospital, so they can prepare for patient care in advance. The app also provides authentication and a dashboard for doctors to review, download, and analyze medical data.

This tutorial will guide you through the process of installing and running MedicaReport on your local machine.

## Table of Contents

- [Demo](#demo)
- [Prerequisites](#Prerequisites)
- [Quick Start](#quick-start)
- [Running the Application](#Running-the-Application)
- [File Structure](#file-structure)
- [Features Overview](#Features-Overview)
- [Browser Support](#browser-support)
- [Customization](#Customization)
- [Contributing](#Contributing)
- [Resources](#resources)
- [Help Us Fix Bugs!](#Help-Us-Fix-Bugs!)
- [Technical Support or Questions](#technical-support-or-questions)
- [Useful Links](#Resources)
- [Licensing](#licensing)

## Demo

| Dashboard page                                                                                                                                                                                | Login page                                                                                                                                                                                 | Signup page                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Dashboard page](https://github.com/user-attachments/assets/eb19ad43-7c93-4896-8a70-ba2997198a17) | ![Login page](https://github.com/user-attachments/assets/87f8b22a-1ba3-43b8-bafc-3cef54b0bbcb) | ![Signup page](https://github.com/user-attachments/assets/759ca996-aa60-49c3-a35d-62ca895ae3ee) |

| Reports page                                                                                                                                                                         | About page                                                                                                                                                                                | Home page                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Reports page](https://github.com/user-attachments/assets/e1b710b4-ba85-4893-8e58-6bbb794a3e6b) | [![About page](https://github.com/user-attachments/assets/37ac89ec-d474-46f6-9cfe-6dab80e4450f)](https://github.com/user-attachments/assets/3a8ff9c0-170a-45c8-8bc1-c4786564dc22) | [![Home page](https://github.com/user-attachments/assets/f132341a-bd92-4c1d-ae93-27ea977d823f)](https://medica-report.framer.website/)|

## Prerequisites

Before you start, ensure that you have the following installed on your machine:

- Python 3.7+ (For running the app backend)
- pip (Python package installer)
- Git (To clone the repository)
- A Groq API key (For processing medical data and generating reports)
- A web browser (For accessing the web interface)

You will also need a local environment setup (virtual environment recommended) for running the Python-based web application.

## Download and Installation

**Step 1: Clone the Repository**

Start by cloning the MedicaReport repository to your local machine:

```bash
git clone https://github.com/ranaitsan123/MedicaReport.git
cd MedicaReport
```

**Step 2: Create a Virtual Environment**

To keep your dependencies isolated, it's recommended to create a virtual environment.

- For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

- For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 3: Install Dependencies**

Install the necessary Python dependencies using ```pip```:

```bash
pip install -r requirements.txt
```

**Step 4: Set Up Environment Variables**

Create a ```.env``` file in the root of the project directory and add the following environment variables:

```bash
GROQ_API_KEY=your_groq_api_key
```

Replace ```your_groq_api_key``` with the API key you get from [Groq API](https://console.groq.com/keys) and ```your_secret_key_for_flask_app``` with a random string used to secure your Flask application.

**Step 5: Set Up the Database (JSON Database)**

The project uses a JSON file as the database for authentication. Make sure to place the user data in users.json inside the project directory.

Example ```users.json``` structure:

```json
[
  {
    "username": "doctor1",
    "password": "password123",
    "email": "email@email.com"
  }
]
```
## Running the Application

**Step 1: Start the Flask Server**

Run the following command to start the Flask server:

```bash
python app.py
```

By default, the app will be accessible at http://localhost:5000.

**Step 2: Access the Web Interface**

Open a web browser and visit http://localhost:5000. You will be presented with a login page.

## File Structure

Within the download you'll find the following directories and files:

```
MedicaReport
  ├── assets
  │   ├── css
  │   ├── fonts
  │   ├── img
  │   ├── js
  │   │   ├── core
  │   │   ├── plugins
  │   │   └── argon-dashboard.js
  │   │   └── argon-dashboard.js.map
  │   │   └── argon-dashboard.min.js
  │   └── scss
  │       ├── argon-dashboard
  │       └── argon-dashboard.scss
  ├── templates
  │   ├── dashboard.html
  │   ├── login.html
  │   ├── signup.html
  │   ├── reports.html
  │   └── about.html
  ├── api.py
  ├── report_generator.py
  ├── auth.py
  ├── pdf_generator.py
  ├── human_vital_signs_dataset_2024.csv(data.zip extract)
  └── app.py
```

## Features Overview

**1. User Authentication**

The app provides a simple login system using a JSON-based database for storing doctor credentials. Doctors can log in to access the dashboard and medical reports.

**2. Dashboard & Reports pages**

Once authenticated, doctors are redirected to the dashboard, where they can choose Reports page and see:

- View a list of patients.
- Access individual patient reports.
- Download patient medical reports.

**3. Report Generation**

The app generates medical reports using vital signs data such as heart rate, respiratory rate, and body temperature. It also uses Groq's API for generating diagnoses and recommendations based on the data provided.

**4. Reports Page**

On the reports page, doctors can:

- Select a patient.
- View the patient’s medical report.
- Download the report in a structured format.

## Customization

MedicaReport is highly customizable, and you can enhance its functionality with the following features:

- **JWT Authentication:** Implement JSON Web Tokens (JWT) for stateless authentication, improving security and scalability by eliminating the need for server-side session storage.

- **Enhanced PDF Generation with ML:** Use machine learning algorithms like regression to predict patient health trends and generate more insightful, data-driven reports.

- **Report History Page:** Add a History Page to store and quickly access previously generated reports, reducing processing time and resource consumption.

- **DBMS for Authentication:** Switch to a Database Management System (DBMS) like Oracle or PostgreSQL for more secure and scalable user authentication, or integrate OAuth for third-party logins.

- **Cloud Deployment:** Deploy the app on cloud platforms like AWS, Google Cloud, or Heroku for global access, scalability, and better resource management.

These customizations can improve performance, security, and user experience.

## Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

## Technologies Used

MedicaReport is built using a variety of programming languages and libraries. Here's a quick overview of the main technologies used in the project, along with their official documentation:

**1. Python 🐍**

[Official Documentation](https://docs.python.org/3/)

Python is the main programming language used to build the backend of MedicaReport, handling everything from API logic to data processing.

**2. Flask 🖥️**

[Official Documentation](https://flask.palletsprojects.com/en/stable/)

Flask is used as the web framework for the MedicaReport backend, handling routing, templating, and HTTP request management.

**3. HTML 🌐**

[Official Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)

HTML is used to structure the front-end of the web application and display the reports and user interface.

**4. CSS 🎨**

[Official Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)

CSS is used to style and design the front-end of MedicaReport, ensuring the web app has a modern and responsive layout.

**5. JavaScript 💻**

[Official Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

JavaScript is used to implement interactive elements and client-side functionalities on the front-end.

**6. JSON 📄**

[Official Documentation](https://www.json.org/json-en.html)

JSON (JavaScript Object Notation) is used for storing and transferring patient data and other application-related information in MedicaReport.

<!-- Python -->
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="64" height="64"> [Python](https://docs.python.org/3/)

<!-- Flask -->
<img src="https://upload.wikimedia.org/wikipedia/commons/8/8d/Flask_logo.svg" width="64" height="64"> [Flask](https://flask.palletsprojects.com/)

<!-- HTML -->
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/640px-HTML5_logo_and_wordmark.svg.png" width="64" height="64"> [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

<!-- CSS -->
<img src="https://upload.wikimedia.org/wikipedia/commons/6/62/CSS3_logo.svg" width="64" height="64"> [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

<!-- JavaScript -->
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/640px-Unofficial_JavaScript_logo_2.svg.png" width="64" height="64"> [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<!-- JSON -->
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/JSON_vector_logo.svg/640px-JSON_vector_logo.svg.png" width="64" height="64"> [JSON](https://www.json.org/json-en.html)

## Contributing

We welcome contributions to improve MedicaReport. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. pen a pull request.

Please ensure that your code follows the existing style and includes tests if applicable.

## Resources

- Demo Video: <https://www.canva.com/design/DAGboI1PCgI/kYq-3SsJBE_ZfUFsOExFJA/edit?utm_content=DAGboI1PCgI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton>
- Documentation Boostrap Tempaltes: <https://www.creative-tim.com/learning-lab/bootstrap/overview/argon-dashboard>
- MedicaReport Home Page: <https://medica-report.framer.website/>
- Support: <https://www.linkedin.com/in/aicha-lahnite/>
- Issues: [Github Issues Page](https://github.com/MarwaneMLE/generate-medical-report/issues)

## Help Us Fix Bugs!

We’re actively working on improving MedicaReport, and we need your help! If you encounter any bugs or issues, we encourage you to contribute by fixing them. Here’s how you can get involved:

1. **Report the Bug:** If you find a bug, please report it in the [Issues](https://github.com/MarwaneMLE/generate-medical-report/issues) section with clear steps to reproduce the problem.

2. **Fix the Bug:** If you're familiar with the code, feel free to fix the issue. Fork the repository, create a branch, and submit a pull request with your changes.

3. **Contribute Improvements:** Even if you don't find a bug, any improvements, optimizations, or enhancements are always welcome!

Your contributions help make MedicaReport better for everyone — thank you for being part of the journey!

## Licensing

- Copyright &copy; 2025 [Aicha Lahnite](https://www.linkedin.com/in/aicha-lahnite/) & [Marwan Khadrouf](https://www.linkedin.com/in/marwane-khadrouf-785636141/)

## Social Media

Linkedin: [Aicha Lahnite](https://www.linkedin.com/in/aicha-lahnite/) | [Marwane Khadrouf](https://www.linkedin.com/in/marwane-khadrouf-785636141/)

Email: halaicha300@gmail.com | khmarwane10@gmail.com

Discord: aicha_a1000 <halaicha300@gmail.com>

Github: [Aicha Lahnite](https://github.com/ranaitsan123) | [Marwan Khadrouf](https://github.com/MarwaneMLE)
