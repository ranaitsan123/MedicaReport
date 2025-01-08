# [MedicaReport](https://medica-report.framer.website/)

![version](https://img.shields.io/badge/version-2.1.0-blue.svg)

![Image](https://raw.githubusercontent.com/creativetimofficial/public-assets/master/argon-dashboard/argon-dashboard-2.jpg)

MedicaReport is a web app designed for doctors to access patient medical reports generated from ambulance datasets. The reports are made available to the doctors before the ambulance arrives at the hospital, so they can prepare for patient care in advance. The app also provides authentication and a dashboard for doctors to review, download, and analyze medical data.

This tutorial will guide you through the process of installing and running MedicaReport on your local machine.

## Table of Contents

- [Demo](#demo)
- [Prerequisites](#Prerequisites)
- [Quick Start](#quick-start)
- [File Structure](#file-structure)
- [Browser Support](#browser-support)
- [Resources](#resources)
- [Reporting Issues](#reporting-issues)
- [Technical Support or Questions](#technical-support-or-questions)
- [Licensing](#licensing)
- [Useful Links](#useful-links)

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
git clone https://github.com/MarwaneMLE/generate-medical-report.git
cd generate-medical-report
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
SECRET_KEY=your_secret_key_for_flask_app
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
    "role": "doctor"
  }
]
```

- [Download from Creative Tim](https://www.creative-tim.com/product/argon-dashboard)

- Install with Npm: `npm i @creative-tim-official/argon-dashboard-free`

- Install with Yarn: `yarn add @creative-tim-official/argon-dashboard-free`

- Install with Composer: `composer create-project creativetimofficial/argon-dashboard-free`

- Clone from Github: `git clone https://github.com/creativetimofficial/argon-dashboard.git`

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

## Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

## Resources

- Demo: <https://demos.creative-tim.com/argon-dashboard>
- Documentation: <https://www.creative-tim.com/learning-lab/bootstrap/overview/argon-dashboard>
- License Agreement: <https://www.creative-tim.com/license>
- Support: <https://www.creative-tim.com/contact-us>
- Issues: [Github Issues Page](https://github.com/creativetimofficial/argon-dashboard/issues)

## Reporting Issues

We use GitHub Issues as the official bug tracker for the Argon Dashboard. Here are some advices for our users that want to report an issue:

1. Make sure that you are using the latest version of the Argon Dashboard. Check the CHANGELOG from your copy on our [website](https://www.creative-tim.com).
2. Providing us reproducible steps for the issue will shorten the time it takes for it to be fixed.
3. Some issues may be browser specific, so specifying in what browser you encountered the issue might help.

## Licensing

- Copyright &copy; 2025 Aicha Lahnite [Aicha Lahnite](https://www.linkedin.com/in/aicha-lahnite/)

## Useful Links

- [Tutorials](https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w)
- [Affiliate Program](https://www.creative-tim.com/affiliates/new?ref=mk-github-readme) (earn money)
- [Blog Creative Tim](http://blog.creative-tim.com/)
- [Free Products](https://www.creative-tim.com/bootstrap-themes/free?ref=mk-github-readme) from Creative Tim
- [Premium Products](https://www.creative-tim.com/bootstrap-themes/premium?ref=mk-github-readme) from Creative Tim
- [React Products](https://www.creative-tim.com/bootstrap-themes/react-themes?ref=mk-github-readme) from Creative Tim
- [Angular Products](https://www.creative-tim.com/bootstrap-themes/angular-themes?ref=mk-github-readme) from Creative Tim
- [VueJS Products](https://www.creative-tim.com/bootstrap-themes/vuejs-themes?ref=mk-github-readme) from Creative Tim
- [More products](https://www.creative-tim.com/bootstrap-themes?ref=mk-github-readme) from Creative Tim
- [Argon Design](https://www.creative-tim.com/design-system/argon)
- Check our Bundles [here](https://www.creative-tim.com/bundles?ref=mk-github-readme)
- [Get Discount](https://www.creative-tim.com/coupon)

## Social Media

Twitter: <https://twitter.com/CreativeTim>

Facebook: <https://www.facebook.com/CreativeTim>

Dribbble: <https://dribbble.com/creativetim>

TikTok: <https://tiktok.com/@creative.tim>

Instagram: <https://instagram.com/creativetimofficial>
