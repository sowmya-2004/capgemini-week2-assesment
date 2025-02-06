from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connection with MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sowmya@123',
    database='api_db',
    use_pure=True
)
cursor = conn.cursor()

# Inserting student details
@app.route('/students', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']
    age = data['age']
    dept = data['dept']
    gender = data['gender']
    grade = data['grade']
    try:
        cursor.execute("INSERT INTO students (name, email, age, dept, gender, grade) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, age, dept, gender, grade))
        conn.commit()
        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Fetching all students' details
@app.route('/students', methods=['GET'])
def get_students():
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Get student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    try:
        cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
        student = cursor.fetchone()
        if student:
            return jsonify(student), 200
        return jsonify({"message": "Student not found"}), 404
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Get student by department
@app.route('/students/dept/<string:dept>', methods=['GET'])
def get_dept_students(dept):
    try:
        cursor.execute("SELECT * FROM students WHERE dept=%s", (dept,))
        students = cursor.fetchall()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Get students by gender
@app.route('/students/gender/<string:gender>', methods=['GET'])
def get_students_by_gender(gender):
    try:
        cursor.execute("SELECT * FROM students WHERE gender=%s", (gender,))
        students = cursor.fetchall()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Get students by grade
@app.route('/students/grade/<string:grade>', methods=['GET'])
def get_students_by_grade(grade):
    try:
        cursor.execute("SELECT * FROM students WHERE grade=%s", (grade,))
        students = cursor.fetchall()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Total number of students
@app.route('/students/total_students', methods=['GET'])
def total_students():
    try:
        cursor.execute("SELECT COUNT(id) FROM students")
        students = cursor.fetchone()
        total = students[0]
        return jsonify({"total_students": total}), 200
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Update student details by ID
@app.route("/students/update_details/<int:id>", methods=["PUT"])
def update_details(id):
    data = request.json
    name = data['name']
    email = data['email']
    age = data['age']
    dept = data['dept']
    gender = data['gender']
    grade = data['grade']
    try:
        cursor.execute("UPDATE students SET name=%s, email=%s, age=%s, dept=%s, gender=%s, grade=%s WHERE id=%s", (name, email, age, dept, gender, grade, id))
        conn.commit()
        return jsonify({"message": "Student updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

# Deleting student information
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        cursor.execute("DELETE FROM students WHERE id=%s", (id,))
        conn.commit()
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Database error"}), 500

if __name__ == '__main__':
    app.run(debug=True)