from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
students_data = []

@app.route('/students', methods=['POST'])
def add_student():
    student = request.get_json()
    students_data.append(student)
    return jsonify({"message": "Student added successfully"}), 201

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
