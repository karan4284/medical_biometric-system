CREATE TABLE employee (
    employee_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    joining_date DATE
);

CREATE TABLE biometric_medical (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(10),
    fingerprint_hash TEXT,
    heart_rate INT,
    blood_pressure VARCHAR(10),
    temperature FLOAT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);
