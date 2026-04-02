def register_employee(emp_id, name, department):
    return {
        "employee_id": emp_id,
        "name": name,
        "department": department
    }

def capture_biometrics(fingerprint, heart_rate, bp, temperature):
    return {
        "fingerprint": fingerprint,
        "heart_rate": heart_rate,
        "blood_pressure": bp,
        "temperature": temperature
    }

def validate_medical_data(data):
    if 40 <= data["heart_rate"] <= 180:
        return True
    return False

employee = register_employee("ML101", "Employee Name", "IT")
biometric_data = capture_biometrics("FP_HASH", 72, "120/80", 36.5)

if validate_medical_data(biometric_data):
    print("Medical data validated and stored")
else:
    print("Invalid medical data. Please re-capture.")
