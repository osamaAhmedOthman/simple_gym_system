import sqlite3

def create_database():
    conn = sqlite3.connect('gym.db')
    c = conn.cursor()
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS members
                 (member_id INTEGER PRIMARY KEY,
                  name TEXT,
                  age INTEGER,
                  gender TEXT CHECK (gender IN ('male', 'female')),
                  mobile_number TEXT,
                  address TEXT,
                  trainer_name TEXT,
                  subscription_package TEXT)''')
    
    # Check if columns exist before adding to avoid errors on subsequent runs
    c.execute("PRAGMA table_info(members)")
    columns = [col[1] for col in c.fetchall()]
    if 'start_date' not in columns:
        c.execute('ALTER TABLE members ADD COLUMN start_date TEXT')
    
    # Also check for 'end_date'
    if 'end_date' not in columns:
        c.execute('ALTER TABLE members ADD COLUMN end_date TEXT')

    conn.commit()
    conn.close() 

# Corrected add_member function definition to include start_date and end_date
def add_member(name, age, gender, mobile_number, address, trainer_name, subscription_package, start_date, end_date):
 """Adds a new member to the database with start and end dates."""
    conn = sqlite3.connect('gym.db')
    c = conn.cursor()
    c.execute('''INSERT INTO members (name, age, gender, mobile_number, address, trainer_name, subscription_package, start_date, end_date)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (name, age, gender, mobile_number, address, trainer_name, subscription_package, start_date, end_date))
    conn.commit()
    conn.close()

def get_members():
    """Retrieves all members from the database including dates."""
    conn = sqlite3.connect('gym.db')
    c = conn.cursor()
    # Select all columns including dates
    c.execute("SELECT member_id, name, age, gender, mobile_number, address, trainer_name, subscription_package, start_date, end_date FROM members")
    members = c.fetchall()
    conn.close()
    return members

def delete_member(member_id):
    """Deletes a member from the database based on member_id."""
    conn = sqlite3.connect('gym.db')
    c = conn.cursor()
    c.execute("DELETE FROM members WHERE member_id = ?", (member_id,))
    conn.commit()
    conn.close()


def update_member(member_id, name, age, gender, mobile_number, address, trainer_name, subscription_package, start_date, end_date):
    """Updates an existing member's information in the database."""
    conn = sqlite3.connect('gym.db')
    c = conn.cursor()
    c.execute('''UPDATE members SET name = ?, age = ?, gender = ?, mobile_number = ?, address = ?, trainer_name = ?, subscription_package = ?, start_date = ?, end_date = ?
                 WHERE member_id = ?''',
              (name, age, gender, mobile_number, address, trainer_name, subscription_package, start_date, end_date, member_id))
    conn.commit()
    conn.close()