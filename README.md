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

## 🚀 How to Access the Deployed Application

This application is deployed on Render.com and can be accessed via the following public URL.

### 1. Application URL

Access the main application page using this link:

**[https://student-admission-app.onrender.com/](https://student-admission-app.onrender.com/)**

*(Replace `https://student-admission-app.onrender.com/` with your actual deployed URL if it's different).*

### 2. Usage Instructions

* **Admission Form**: Fill out the fields and click "Submit Admission".
* **Clear Form**: Click "Clear Form" to reset the current form's fields.
* **View All Submissions**: Click the "View All Submissions" link (or go directly to `https://student-admission-app.onrender.com/view`) to see all stored student entries.
* **Clear All Submissions**: On the "View All Submissions" page, click "Clear All Submissions" to remove all records (requires confirmation).

## 🌐 Deployment to Render.com

This application is set up for deployment as a single web service on a platform like Render, where Flask serves all components (frontend and backend).

### 1. Prepare for Deployment

* Ensure your `requirements.txt` file (located in `main/`) is up-to-date and contains `Flask`, `Flask-Cors`, and `gunicorn`.
* Ensure all local changes are committed and pushed to your GitHub repository.

    ```bash
    # (From project root: student-admission-app/)
    git add .
    git commit -m "Prepare for Render deployment: update requirements.txt"
    git push -u origin main
    ```

### 2. Deploy on Render.com

1.  **Sign up/Login to Render**: Go to [https://render.com/](https://render.com/) and log in (GitHub login is an option).
2.  **New Web Service**: Click **"New"** > **"Web Service"**.
3.  **Connect GitHub**: Connect your GitHub account and select the `suraj2k07/student-admission-app` repository.
4.  **Configure Service**:
    * **Service Name**: Choose a unique name (e.g., `suraj-admission-app-live`).
    * **Root Directory**: Set this to `main/` (important, as your `app.py` is inside `main/`).
    * **Runtime**: Select `Python 3`.
    * **Build Command**: `pip install -r requirements.txt`
    * **Start Command**: `gunicorn app:app` (This tells Render to run your `app` Flask instance from `app.py` using Gunicorn).
    * **Plan**: Select `Free` (for testing, be aware of ephemeral storage for `students.json`).
    * **Region**: Choose your preferred region.
5.  **Create Web Service**: Click the button to initiate deployment.

Render will now clone your repository, install dependencies, and start your Flask application. You can monitor the build logs directly on the Render dashboard.

### 3. Access the Deployed Application

Once the deployment is successful, Render will provide a public URL (e.g., `https://your-service-name.onrender.com`). Open this URL in your browser to access your live application.

NOTE: If you want to run locally, change the backend url in html documents under script to your local url.
