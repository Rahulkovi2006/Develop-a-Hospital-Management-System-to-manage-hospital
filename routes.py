from flask import request, jsonify
from . import app, db
from .models import Patient, Doctor, Appointment, MedicalRecord

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully!'}), 201

@app.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.get_json()
    new_doctor = Doctor(name=data['name'], specialization=data['specialization'])
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor added successfully!'}), 201

@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()
    new_appointment = Appointment(patient_id=data['patient_id'], doctor_id=data['doctor_id'], date=data['date'])
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment added successfully!'}), 201

@app.route('/medical_records', methods=['POST'])
def add_medical_record():
    data = request.get_json()
    new_record = MedicalRecord(patient_id=data['patient_id'], description=data['description'])
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'message': 'Medical record added successfully!'}), 201