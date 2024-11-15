# db_connector.py

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Create the patients table
cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    reference_no TEXT,
    dose TEXT,
    num_tablets INTEGER,
    lot TEXT,
    issue_date TEXT,
    exp_date TEXT,
    daily_dose TEXT,
    side_effect TEXT,
    blood_pressure TEXT,
    storage_advice TEXT,
    medication TEXT,
    nhs_number TEXT,
    dob TEXT,
    address TEXT
)
''')

# Commit and close connection
conn.commit()
conn.close()
print("Database and table created successfully.")
