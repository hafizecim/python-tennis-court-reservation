# 🎾 Python Tennis Court Reservation System

A console-based tennis court reservation system developed with Python.

The project allows users to create, list, search, and delete tennis court reservations through a simple console menu. Reservation data is stored persistently in a JSON file.

## 📸 Screenshot


<img width="366" height="154" alt="image" src="https://github.com/user-attachments/assets/d9bcb187-6f51-48f7-91d3-84d10c278b9b" />


### 1 - ➕ Add Reservation

<img width="226" height="121" alt="image" src="https://github.com/user-attachments/assets/6f13106d-8443-49f2-8ef3-86e534d3c0eb" />


### 2 - 📋 List Reservations

<img width="208" height="125" alt="image" src="https://github.com/user-attachments/assets/c8ee375a-ca08-4d09-a89c-37d7e4b15ee7" />


### 3 - 🔍 Search Reservation

<img width="235" height="64" alt="image" src="https://github.com/user-attachments/assets/298d83ca-5acb-4932-ae6d-da53647143d0" />


### 4 - 🗑️  Delete Reservation

<img width="276" height="74" alt="image" src="https://github.com/user-attachments/assets/b90cba90-ae5c-4db6-8fd3-d744f54638f3" />


### 5 - 📊 Reservation Report

<img width="232" height="159" alt="image" src="https://github.com/user-attachments/assets/aa4ffd69-1393-415d-ae85-064644e11793" />


### 0 - 🚪 Exit

<img width="157" height="34" alt="image" src="https://github.com/user-attachments/assets/3d2e91fb-8cd3-4aa0-9973-6f348f0da0c6" />


## ✨ Features

* ➕ Add a new reservation
* 📋 List all reservations
* 🔍 Search reservations by name or date
* 🗑️ Delete a reservation
* 📊 Display reservation reports
* 💾 Save reservation data to a JSON file
* 📂 Load reservation data when the application starts
* ⚠️ Validate user input
* 🛡️ Handle common input and file errors
* 🎨 Colored console output

## 🛠️ Technologies

* **Python 3**
* **JSON**
* **Colorama**

## 📚 Python Topics

This project demonstrates the following Python concepts:

* Variables
* Input and output
* Conditional statements (`if / elif / else`)
* `while` loops
* `for` loops
* Lists
* Dictionaries
* Functions
* Classes and objects
* Object-Oriented Programming (OOP)
* File operations
* JSON data storage
* Exception handling (`try / except`)
* Input validation
* Modular programming

## 📁 Project Structure

```text
python-tennis-court-reservation/
│
├── main.py
├── reservation.py
├── reservation_manager.py
├── .gitignore
├── README.md
└── reservations.json
```

### File Descriptions

| File                     | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| `main.py`                | Contains the console menu and controls the application flow          |
| `reservation.py`         | Defines the `Reservation` class                                      |
| `reservation_manager.py` | Manages reservations, search, deletion, reports, and JSON operations |
| `reservations.json`      | Stores reservation data locally at runtime                           |
| `.gitignore`             | Prevents reservation data from being uploaded to GitHub              |
| `README.md`              | Project documentation                                                |

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/hafizecim/python-tennis-court-reservation.git
```

### 2. Open the project folder

```bash
cd python-tennis-court-reservation
```

### 3. Install the required package

```bash
pip install colorama
```

### 4. Run the application

```bash
python main.py
```

## 🎾 Application Menu

```text
===== Tennis Court Reservation System =====

1 - Add Reservation
2 - List Reservations
3 - Search Reservation
4 - Delete Reservation
5 - Reservation Report
0 - Exit
```

## 💾 Data Storage

Reservation data is stored in a local JSON file:

```text
reservations.json
```

The application automatically:

* Loads existing reservations when it starts.
* Saves reservation changes to the JSON file.
* Creates the JSON file when reservation data is saved.

The `reservations.json` file is excluded from GitHub using `.gitignore`.

## 🔍 Search

Reservations can be searched using:

* Player name
* Reservation date

For example:

```text
Enter name or date: Ahmet
```

or:

```text
Enter name or date: 2026-09-12
```

## 📊 Reservation Report

The report section provides a summary of the reservation data.

It displays:

* Total number of reservations
* Total number of players
* Number of reservations according to player count

Example:

```text
===== Reservation Report =====

Total reservations: 2
Total players: 6

Players per reservation:
2 players: 1 reservations
4 players: 1 reservations
```

## 🛡️ Error Handling

The application handles common errors using `try / except`.

Examples include:

* Invalid numeric input
* Missing reservation file
* Empty reservation information
* Invalid player count

Example:

```text
Please enter a number.
```

## 🎨 Console Interface

The application uses **Colorama** to improve console readability with colored output.

Different colors are used for:

* Menu and section headings
* Successful operations
* Errors and warnings
* User input prompts
* Informational messages

## 🎯 Project Purpose

This project was developed as a Python course final project to demonstrate fundamental Python programming concepts in a practical application.

The main goal is to combine:

* Functions
* Lists and dictionaries
* Classes and objects
* File operations
* JSON data storage
* Exception handling
* Console-based user interaction

in a single application.

## 🔗 Repository

GitHub:

https://github.com/hafizecim/python-tennis-court-reservation

## 👩‍💻 Author

Developed as a Python course final project.
