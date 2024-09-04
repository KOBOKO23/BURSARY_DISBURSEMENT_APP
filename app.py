from flask import Flask, request, jsonify
from models import storage
from models.student import Student  # Adjust this path if necessary

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask app is running!"

@app.route('/students', methods=['GET'])
def get_students():
    """Fetch all students"""
    students = storage.all('Student')
    return jsonify([student.to_dict() for student in students.values()])

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Fetch a single student by ID"""
    student = storage.all().get(f'Student.{student_id}', None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.to_dict())

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student"""
    data = request.get_json()
    try:
        new_student = Student(**data)
        new_student.save()
        return jsonify(new_student.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    """Update an existing student"""
    student = storage.all().get(f'Student.{student_id}', None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(student, key, value)
    student.save()
    return jsonify(student.to_dict())

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student"""
    student_key = f'Student.{student_id}'
    if student_key not in storage.all():
        return jsonify({"error": "Student not found"}), 404
    del storage.all()[student_key]
    storage.save()
    return jsonify({"message": "Student deleted successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
