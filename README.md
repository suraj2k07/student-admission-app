# Student Admission Application

This is a web-based student admission application built with Python Flask for both the backend API and serving the static frontend (HTML, CSS, JavaScript).

## 📌 Objective

To provide a simple, full-stack web application that allows users to:
* Submit student details via a form.
* Store the submitted data (in a local JSON file for simplicity).
* View all stored student details in a tabular format on a separate page.
* Clear the admission form fields.
* Clear all submitted student records.

## 🛠 Tech Stack

* **Backend & Frontend Serving**: Python 3, Flask
* **Web Server Gateway Interface (WSGI)**: Gunicorn (for production deployment)
* **Frontend**: HTML5, CSS3, JavaScript
* **Data Storage**: JSON file (`students.json`)
* **Version Control**: Git
* **Hosting**: GitHub (for code repository), Render.com (for application deployment)

## 📋 Features

* **Admission Form**: Collects essential student details: Full Name, Email, Age, Course, Phone Number, and Address.
* **Form Submission**: Submits data to the Flask backend via a `POST` API request.
* **Data Storage**: Persists student entries in a `students.json` file.
* **View Submissions**: Fetches and displays all stored student entries dynamically using a `GET` API request.
* **Clear Form**: A dedicated button to reset all fields on the admission form.
* **Clear All Submissions**: A button on the view page to delete all stored student records via a `DELETE` API request (with confirmation).
* **CORS Enabled**: Flask backend includes Flask-CORS to handle cross-origin requests, though less critical when Flask serves the frontend.

## 📁 Project Structure
├── main/                   # Your main application directory (formerly 'backend')
│   ├── app.py              # Main Flask application file with routes and API endpoints
│   ├── students.json       # JSON file for storing student data
│   ├── requirements.txt    # Python dependencies for the project
│   ├── static/             # Static files (CSS, JS, images) served by Flask
│   │   └── style.css
│   └── templates/          # HTML template files served by Flask
│       ├── index.html      # Admission form page
│       └── view.html       # Student submissions viewing page
├── .gitignore              # Specifies files/directories to be ignored by Git
└── README.md               # This README file

## 🚀 How to Run Locally

Follow these steps to set up and run the application on your local machine:

1. Clone the Repository (if you haven't already)

If you're starting fresh or pulling to a new machine:

```bash
git clone [https://github.com/suraj2k07/student-admission-app.git]
cd student-admission-app\

2. Navigate to the Application Directory

The core application files are within the main/ directory.

3. Set Up a Python Virtual Environment (Recommended)

It's good practice to use a virtual environment to manage dependencies

4. Install Dependencies

Install the required Python packages listed in requirements.txt.

5. Run the Flask Application

Start the Flask development server.

You should see output indicating that the Flask app is running, typically on http://127.0.0.1:5000/.

6. Access the Application
Open your web browser and go to:

Admission Form: http://127.0.0.1:5000/

View Submissions: http://127.0.0.1:5000/view

🌐 Deployment to Render.com
This application is set up for deployment as a single web service on a platform like Render, where Flask serves all components (frontend and backend).

1. Prepare for Deployment
Ensure your requirements.txt file (located in main/) is up-to-date and contains Flask, Flask-Cors, and gunicorn.

Ensure all local changes are committed and pushed to your GitHub repository.

Bash

# (From project root: student-admission-app/)
git add .
git commit -m "Prepare for Render deployment: update requirements.txt"
git push -u origin main
2. Deploy on Render.com
Sign up/Login to Render: Go to https://render.com/ and log in (GitHub login is an option).

New Web Service: Click "New" > "Web Service".

Connect GitHub: Connect your GitHub account and select the suraj2k07/student-admission-app repository.

Configure Service:

Service Name: Choose a unique name (e.g., suraj-admission-app-live).

Root Directory: Set this to main/ (important, as your app.py is inside main/).

Runtime: Select Python 3.

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app (This tells Render to run your app Flask instance from app.py using Gunicorn).

Plan: Select Free (for testing, be aware of ephemeral storage for students.json).

Region: Choose your preferred region.

Create Web Service: Click the button to initiate deployment.

Render will now clone your repository, install dependencies, and start your Flask application. You can monitor the build logs directly on the Render dashboard.

3. Access the Deployed Application
Once the deployment is successful, Render will provide a public URL (e.g., https://your-service-name.onrender.com). Open this URL in your browser to access your live application.

⚠️ Important Notes on Deployment
Data Persistence: On Render's free tier, the students.json file where data is stored is ephemeral. This means any data you submit will be lost if the server restarts or goes to sleep due to inactivity. For a production application requiring persistent data, you would integrate a robust database like PostgreSQL (Render offers a free tier for PostgreSQL databases).

Local vs. Deployed URLs: Your frontend JavaScript now uses relative paths (e.g., /submit, /students) because Flask serves both frontend and backend. This means the same code works seamlessly whether run locally via http://127.0.0.1:5000 or deployed to Render's public URL.
