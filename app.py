# app.py

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Connect to the database
def connect_db():
    conn = sqlite3.connect("hospital.db")
    return conn

# Refresh the table to show all records from the database
def load_data():
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

# Insert new patient information
def add_patient():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (name, reference_no, dose, num_tablets, lot, issue_date, exp_date, daily_dose, side_effect, blood_pressure, storage_advice, medication, nhs_number, dob, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name_var.get(), ref_var.get(), dose_var.get(), num_tablets_var.get(), lot_var.get(), issue_date_var.get(), exp_date_var.get(), daily_dose_var.get(), side_effect_var.get(), bp_var.get(), storage_var.get(), medication_var.get(), nhs_var.get(), dob_var.get(), address_var.get()))
    conn.commit()
    conn.close()
    load_data()
    messagebox.showinfo("Success", "Patient record added successfully.")

# GUI Setup
root = tk.Tk()
root.title("Hospital Management System")

# Title Label
title_label = tk.Label(root, text="HOSPITAL MANAGEMENT SYSTEM", font=("Arial", 20, "bold"), bg="red", fg="white")
title_label.pack(fill=tk.X)

# Patient Information Frame
info_frame = tk.Frame(root, bd=10, relief=tk.GROOVE)
info_frame.pack(side=tk.TOP, fill=tk.X)

# Patient Information Labels and Entry Fields
fields = [
    ("Name of Tablets", "reference_no"), ("Reference No", "ref"), ("Dose", "dose"), ("No of Tablets", "num_tablets"),
    ("Lot", "lot"), ("Issue Date", "issue_date"), ("Exp Date", "exp_date"), ("Daily Dose", "daily_dose"),
    ("Side Effect", "side_effect"), ("Blood Pressure", "bp"), ("Storage Advice", "storage"), ("Medication", "medication"),
    ("Patient ID", "nhs"), ("Date of Birth", "dob"), ("Patient Address", "address")
]

# Variables for Entries
name_var = tk.StringVar()
ref_var = tk.StringVar()
dose_var = tk.StringVar()
num_tablets_var = tk.StringVar()
lot_var = tk.StringVar()
issue_date_var = tk.StringVar()
exp_date_var = tk.StringVar()
daily_dose_var = tk.StringVar()
side_effect_var = tk.StringVar()
bp_var = tk.StringVar()
storage_var = tk.StringVar()
medication_var = tk.StringVar()
nhs_var = tk.StringVar()
dob_var = tk.StringVar()
address_var = tk.StringVar()

variables = [name_var, ref_var, dose_var, num_tablets_var, lot_var, issue_date_var, exp_date_var, daily_dose_var, side_effect_var, bp_var, storage_var, medication_var, nhs_var, dob_var, address_var]

for i, (label_text, var_name) in enumerate(fields):
    label = tk.Label(info_frame, text=label_text + ":", font=("Arial", 12))
    label.grid(row=i//2, column=(i % 2) * 2, padx=10, pady=5, sticky=tk.W)
    entry = tk.Entry(info_frame, textvariable=variables[i], font=("Arial", 12), width=30)
    entry.grid(row=i//2, column=(i % 2) * 2 + 1, padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root, bd=10, relief=tk.GROOVE)
btn_frame.pack(side=tk.TOP, fill=tk.X)

add_btn = tk.Button(btn_frame, text="Add Patient", command=add_patient, width=15)
add_btn.grid(row=0, column=0, padx=10, pady=10)

# Patient Table Frame
table_frame = tk.Frame(root, bd=10, relief=tk.GROOVE)
table_frame.pack(fill=tk.BOTH, expand=True)

# Scrollbar
scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)

# Treeview Table
columns = ("ID", "Name", "Reference No", "Dose", "No of Tablets", "Lot", "Issue Date", "Exp Date", "Daily Dose", "Side Effect", "Blood Pressure", "Storage Advice", "Medication", "NHS Number", "DOB", "Address")
tree = ttk.Treeview(table_frame, columns=columns, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)

# Treeview Heading and Column Configuration
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True)

# Initialize the table with data
load_data()

root.mainloop()
