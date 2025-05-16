# Gym Management System

**Description:**
This is a simple desktop application built with Python and tkinter for managing gym members. It allows you to add, view, edit, and delete member information, including their personal details, trainer, subscription package, and membership dates. The data is stored in a SQLite database.

**Features:**
*   User login with basic authentication.
*   Add new members with details such as Name, Age, Gender, Mobile Number, Address, Trainer Name, Subscription Package, Start Date, and End Date.
*   View all members in a table format, displaying all relevant information.
*   Edit existing member details.
*   Delete members from the system.
*   Basic input validation for member information.

**Technologies Used:**
*   Python: The core programming language.
*   tkinter: The standard GUI toolkit for Python, used for creating the application's graphical interface.
*   SQLite: A serverless, self-contained, high-reliability, embedded, full-featured, public-domain SQL database engine, used for storing member data.

**Setup/Installation:**
1.  **Prerequisites:**
    *   Ensure you have Python 3.x installed on your system. tkinter is usually included with Python installations.
2.  **Obtain the Project Files:**
    *   Download or clone the project files to your local machine. You should have at least `Gym_system.py` and `database.py`.
3.  **Run the Application:**
    *   Open a terminal or command prompt, navigate to the directory where the project files are located, and run the following command:
```
bash
        python Gym_system.py
        
```
**Usage:**
1.  When the application starts, a login window will appear. Use the following default credentials:
    *   **Username:** `admin`
    *   **Password:** `123`
2.  After successful login, you will be presented with the main menu.
3.  Select from the options to Add Member, View Members, or Edit/Delete Members.
4.  Follow the prompts and instructions on the respective pages to manage member information.

**File Structure:**
*   `Gym_system.py`: Contains the main application class, GUI layout using tkinter, and the logic for navigating between different pages (login, main menu, add member, view members, edit/delete members).
*   `database.py`: Contains functions for interacting with the SQLite database, including creating the database table, adding new members, retrieving member data, updating member information, and deleting members.
