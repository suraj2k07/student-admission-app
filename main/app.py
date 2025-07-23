from flask import Flask, request, jsonify, render_template 
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app) 

DATA_FILE = 'students.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/submit', methods=['POST'])
def submit_student():
    try:
        data = request.json
        if not all(key in data for key in ['fullName', 'email', 'age', 'course', 'phoneNumber', 'address']):
            return jsonify({"error": "Missing required fields"}), 400

        with open(DATA_FILE, 'r+') as f:
            students = json.load(f)
            students.append(data)
            f.seek(0) 
            json.dump(students, f, indent=4)
        return jsonify({"message": "Student data submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/students', methods=['GET'])
def get_students():
    try:
        with open(DATA_FILE, 'r') as f:
            students = json.load(f)
        return jsonify(students), 200
    except FileNotFoundError:
        return jsonify([]), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/clear_all_submissions', methods=['DELETE'])
def clear_all_submissions():
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump([], f) 
        return jsonify({"message": "All student submissions cleared successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)