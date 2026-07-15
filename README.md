# Hospital Management System (HMS)

A Python-based suite of desktop applications for managing hospital records, patient information, prescriptions, and medical stores. This project utilizes Python's **Tkinter** library to provide a clean, user-friendly graphical user interface (GUI) for medical professionals, clinic administrators, and pharmacy staff.

The repository contains three different variants of the application tailored for different setups, ranging from standalone in-memory systems to database-connected solutions.

---

## Table of Contents
- [Applications Overview](#applications-overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Database Setup (For MySQL Version)](#database-setup-for-mysql-version)
- [How to Run](#how-to-run)
- [GUI Overview & Usage](#gui-overview--usage)

---

## Applications Overview

The workspace contains three Python scripts, each serving a slightly different variation of the system:

1. **Hospital Management System (`Hospital Management System.py`)**
   - The database-enabled version of the system.
   - Connects to a local MySQL server (`localhost`) to query and store prescription records persistently.
   - Best suited for multi-user setups or production-like environments where data must be retained across app sessions.

2. **Medical Store Management System (`Medical Store Management System.py`)**
   - A standalone, in-memory variant of the hospital management system.
   - Does not require a database connection, storing data directly in the graphical Treeview interface.
   - Ideal for quick demonstrations, testing, or environments without a dedicated database server.

3. **Patient Management System (`Patient Management System.py`)**
   - A standalone, clinic-oriented variant similar to the Medical Store version.
   - Operates in-memory and features UI title configurations tailored for clinic setups.

---

## Key Features

- **Patient Information Intake:** Fields for recording basic details such as Patient Name, ID, Date of Birth, NHS Number, and Patient Address.
- **Comprehensive Drug Details:** Options to record tablet names (via a dropdown combobox), reference numbers, doses, daily counts, lot numbers, issue dates, expiry dates, and storage advice.
- **Dynamic Prescription Generation:** Generates a clean, readable text prescription summary instantly in the prescription window which can be copied or printed.
- **Tabular View (Treeview):** Displays all records in a responsive grid. Click on any record in the table to load its values back into the form fields.
- **Data Operations (CRUD):**
  - **Prescription:** Creates a text format prescription from the current form data.
  - **Prescription Data (Add):** Inserts a new record into the table (or database).
  - **Update:** Edits the currently selected record in the table.
  - **Delete:** Removes the selected record.
  - **Clear:** Wipes the entry fields and the prescription text frame.

---

## Project Structure

```
HMS System/
│
├── Hospital Management System.py          # MySQL database-driven HMS variant
├── Medical Store Management System.py     # Standalone in-memory HMS variant
├── Patient Management System.py           # Standalone in-memory Clinic/Patient variant
└── README.md                              # Project documentation (this file)
```

---

## Prerequisites

To run these applications, you need:

1. **Python 3.x** installed on your system.
2. **Tkinter** library (usually bundled with standard Python installers).
3. **MySQL Server** (only required to run `Hospital Management System.py`).
4. **Python MySQL Connector** (only required for the MySQL version):
   ```bash
   pip install mysql-connector-python
   ```

---

## Database Setup (For MySQL Version)

If you plan to run the database-driven `Hospital Management System.py`, configure your MySQL server as follows:

1. Open your MySQL command-line client or GUI interface (such as phpMyAdmin or MySQL Workbench).
2. Create a database named `Mydata`:
   ```sql
   CREATE DATABASE Mydata;
   ```
3. Update the database credentials in [Hospital Management System.py](Hospital%20Management%20System.py) (specifically the connection parameters at the bottom of the script):
   ```python
   conn = mysql.connector.connect(
       host="localhost",
       username="root",
       password="your_mysql_password",
       database="Mydata"
   )
   ```

---

## How to Run

Navigate to the project root folder and execute the desired script via terminal or command prompt:

### Running the Standalone Versions (No Setup Required)

For the Medical Store system:
```bash
python "Medical Store Management System.py"
```

For the Patient/Clinic system:
```bash
python "Patient Management System.py"
```

### Running the Database Version

First, verify that your MySQL service is running and configured correctly. Then run:
```bash
python "Hospital Management System.py"
```

---

## GUI Overview & Usage

- **Patient Information Form:** Fill out all fields on the left pane. You can select common tablets from the dropdown combobox.
- **Generate Prescription:** Clicking **Prescription** will generate a text summary on the right-side box.
- **Save Record:** Clicking **Prescription Data** inserts the record into the database table or grid below.
- **Recall/Edit Record:** Select any row in the bottom table. The details will automatically populate the form fields. You can modify them and click **Update**, or click **Delete** to remove the record.
