# College Management System

The College Management System is a Python-based project that offers a comprehensive solution for efficiently managing various aspects of a college. It includes functionalities to manage student and teacher information using an SQLite database. This project is designed to assist college administrators and developers in creating an intuitive and effective system for college management.

## Features

- **SQLite Database:** The system utilizes SQLite for seamless storage, retrieval, and management of student and teacher records.

- **User Roles:** The project is divided into distinct modules for administrators, students, and teachers, each implemented in separate files (`admin.py`, `student.py`, `teacher.py`).

- **Student Module:** The `student.py` module allows addition, retrieval, modification, and deletion of student records. It also provides functionality to calculate student age based on the date of birth.

- **Teacher Module:** The `teacher.py` module facilitates management of teacher information, including employment details and contact information.

- **Admin Module:** The `admin.py` module is dedicated to administrator functionalities, such as adding and managing teacher records, and overall database management.

- **Main Module:** The `main.py` module serves as the entry point to the College Management System. It provides an interactive command-line interface for easy navigation through various functionalities.

## Getting Started

1. Clone this repository to your local machine.

   ```bash
   git clone <repository_url>
   ```
2. Navigate to the directory
    ```bash
    cd College-Management-System
    ```
3. Make sure you have Python installed
4. Install the required dependencies along eith sqlite3
5. Run the main.py script

