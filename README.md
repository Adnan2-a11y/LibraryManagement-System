# AMUST Library Management System

## 📖 Introduction
The **AMUST Library Management System** is a simple Python-based application that allows students to interact with a digital library. The system provides functionalities for user authentication, viewing available books, borrowing books, and returning books.

## 🛠 Features
- **Student Login Verification**: Users must enter their name and ID for authentication.
- **View Available Books**: Displays a list of all books currently available.
- **Borrow Books**: Allows users to borrow books if they are available.
- **Return Books**: Users can return books to the library.
- **Exit System**: Users can exit the application when they are done.

## 🚀 How It Works
1. The program starts with a welcome message and prompts the user to log in.
2. The user selects one of the four options:
   - View available books
   - Borrow a book
   - Return a book
   - Exit the system
3. The system processes the user’s request accordingly and updates the book inventory.
4. If a user borrows a book, it is removed from the available books list.
5. If a user returns a book, it is added back to the available books list.
6. The system continues running in a loop until the user chooses to exit.

## 📌 Installation & Usage
### Prerequisites
- Python 3.x
- pandas module (`pip install pandas`)

### Running the Application
1. Clone or download the script.
2. Open a terminal and navigate to the script's directory.
3. Run the script using:
   ```sh
   python library_manager.py
   ```
4. Follow the on-screen instructions to interact with the library system.

## 📋 Code Overview
The program consists of the following key components:
- **Student Database**: A DataFrame containing student names and IDs.
- **LibraryManager Class**:
  - `StdLogin()`: Handles student verification.
  - `Available_books()`: Displays all available books.
  - `borrow_books(bookName)`: Allows students to borrow books.
  - `return_books(bookName)`: Returns books to the library.

## 📝 Example Usage
```
😎----Welcome to AMUST Library----😎
😕----Enter your name and login id for verification----😕
Enter your name: Fahim
Enter your id: 1
---verification successful---
===Welcome to AMUST Library===
1.---Available_books---.
2.---Borrow_books---.
3.---Returning_books---.
4.---Exit---.
Enter your choice: 1
```

## 🏆 Contributors
- Developed by **Md. Rafshan Jani**

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributions
Feel free to fork the repository and improve the system by adding new features or fixing bugs!

---
Happy Coding! 😊📚

