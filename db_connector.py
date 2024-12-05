import sqlite3

def initialize_database():
    """
    Connect to the SQLite database and create the `patients` table if it doesn't exist.
    """
    try:
        # Connect to SQLite database (creates `hospital.db` if it doesn't exist)
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()

        # Create the `patients` table if it doesn't exist
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
        conn.commit()  # Save changes
        print("Database initialized and `patients` table ensured.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        # Close the database connection
        conn.close()

if __name__ == "__main__":
    # Initialize the database when the script is run directly
    initialize_database()
