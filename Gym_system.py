import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database import create_database, get_members, delete_member  # Import necessary database functions
from database import add_member, update_member  # Import add_member and update_member functions
from datetime import datetime  # Import datetime for date validation
import re


class GymApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a modern theme
        self.style.configure('TButton', font=('Arial', 10), padding=10)  # Configure button style
        self.style.configure('TLabel', font=('Arial', 10), padding=5)  # Configure label style
        self.style.configure('TEntry', padding=5)  # Configure entry style
        self.setup_login_page()

    # --- Setup Methods ---

    def setup_login_page(self):
        # Setup the login page
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Login")
        self.login_window.geometry("300x200")
        self.login_window.resizable(False, False)
        self.login_window.protocol("WM_DELETE_WINDOW", self.root.quit)  # Exit application if login window is closed

        self.username_label = ttk.Label(self.login_window, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(self.login_window)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(self.login_window, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self.login_window, show="*")
        self.password_entry.pack(pady=5)
        self.login_button = ttk.Button(self.login_window, text="Submit", command=self.login)
        self.login_button.pack(pady=3)

    # Helper method to clear the main window
    def clear_main_window(self, width=800, height=600):
        # Clear previous widgets in the main window
        for widget in self.root.winfo_children():
            widget.destroy()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')  # Set geometry with variable size and calculated position

    # --- Main Menu Methods ---

    def main_menu(self):
        # Clear previous widgets in the main window
        self.clear_main_window()

        title_label = ttk.Label(self.root, text="Gym Management System - Main Menu", font=('Arial', 20, 'bold'))
        title_label.pack(pady=30)

        self.add_member_button = ttk.Button(self.root, text="Add Member", command=self.add_member)
        self.add_member_button.pack(pady=20, ipadx=50, ipady=20)  # Increased padding
        self.view_members_button = ttk.Button(self.root, text="View Members", command=self.view_members)
        self.view_members_button.pack(pady=20, ipadx=50, ipady=20)  # Increased padding
        self.edit_member_button = ttk.Button(self.root, text="Edit Member", command=self.edit_member)
        self.edit_member_button.pack(pady=20, ipadx=50, ipady=20)  # Increased padding

    # --- Add Member Methods ---

    def add_member(self):  # This method now directly calls the add member page setup
        self.add_member_page()  # Method name corrected

    def add_member_page(self):
        # Clear previous widgets in the main window
        self.clear_main_window()  # Use helper method to clear frame

        # Setup the add member form page

        # Use a frame to contain the add member form
        form_frame = ttk.Frame(self.root, padding="20")
        form_frame.pack(expand=True, fill="both")  # Center the form frame

        add_member_label = ttk.Label(form_frame, text="Add New Member", font=('Arial', 16, 'bold'))
        add_member_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Labels and Entry fields for member details
        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.name_entry = ttk.Entry(form_frame, width=40)  # Increase width
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')  # Make entry expand horizontally

        ttk.Label(form_frame, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.age_entry = ttk.Entry(form_frame, width=40)  # Increase width
        self.age_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')  # Make entry expand horizontally

        ttk.Label(form_frame, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.gender_combobox = ttk.Combobox(form_frame, values=["male", "female"], width=38, state="readonly")  # Adjust width
        self.gender_combobox.grid(row=3, column=1, padx=10, pady=5, sticky='ew')  # Make combobox expand horizontally
        self.gender_combobox.set("male")  # Set a default value

        ttk.Label(form_frame, text="Mobile Number:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.mobile_entry = ttk.Entry(form_frame, width=40)  # Increase width
        self.mobile_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')  # Make entry expand horizontally

        ttk.Label(form_frame, text="Address:").grid(row=5, column=0, padx=10, pady=5, sticky='w')
        self.address_entry = ttk.Entry(form_frame, width=40)  # Increase width
        self.address_entry.grid(row=5, column=1, padx=10, pady=5, sticky='ew')  # Make entry expand horizontally

        ttk.Label(form_frame, text="Trainer Name:").grid(row=6, column=0, padx=10, pady=5, sticky='w')
        self.trainer_entry = ttk.Entry(form_frame, width=40)  # Increase width
        self.trainer_entry.grid(row=6, column=1, padx=10, pady=5, sticky='ew')  # Make entry expand horizontally

        ttk.Label(form_frame, text="Subscription Package:").grid(row=7, column=0, padx=10, pady=5, sticky='w')
        self.package_combobox = ttk.Combobox(form_frame, values=["Silver", "Gold", "Platinum"], width=38, state="readonly")  # Adjust width
        self.package_combobox.grid(row=7, column=1, padx=10, pady=5, sticky='ew')  # Make combobox expand horizontally
        self.package_combobox.set("Silver")  # Set a default value

        # Add Start Date and End Date fields
        ttk.Label(form_frame, text="Start Date (YYYY-MM-DD):").grid(row=8, column=0, padx=10, pady=5, sticky='w')
        self.start_date_entry = ttk.Entry(form_frame, width=40)
        self.start_date_entry.grid(row=8, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(form_frame, text="End Date (YYYY-MM-DD):").grid(row=9, column=0, padx=10, pady=5, sticky='w')
        self.end_date_entry = ttk.Entry(form_frame, width=40)
        self.end_date_entry.grid(row=9, column=1, padx=10, pady=5, sticky='ew')

        # Configure column weights so the second column expands
        form_frame.columnconfigure(1, weight=1)

        # Button frame for Save and Back buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=10, column=0, columnspan=2, pady=30)  # Adjust row and padding

        # Save button
        save_button = ttk.Button(button_frame, text="Save Member", command=self.save_new_member_to_db)
        save_button.pack(side="left", padx=10)  # Add padding between buttons

        # Add a back button to return to the main menu
        back_button = ttk.Button(button_frame, text="Back to Menu", command=self.main_menu)
        back_button.pack(side="left", padx=10)  # Add padding between buttons

    # Saves the new member data to the database
    def save_new_member_to_db(self):
        start_date = self.start_date_entry.get().strip()  # Get start date
        end_date = self.end_date_entry.get().strip()  # Get end date
        age = self.age_entry.get()
        gender = self.gender_combobox.get()

        # Data retrieval from entry fields
        mobile_number = self.mobile_entry.get().strip()
        address = self.address_entry.get().strip()
        trainer_name = self.trainer_entry.get().strip()
        subscription_package = self.package_combobox.get()

        # Date validation and comparison
        if not self.validate_date(start_date) or not self.validate_date(end_date):
            messagebox.showwarning("Invalid Input", "Please enter valid dates in YYYY-MM-DD format.")
            return
        if datetime.strptime(start_date, '%Y-%m-%d') > datetime.strptime(end_date, '%Y-%m-%d'):
            messagebox.showwarning("Invalid Input", "End Date cannot be before Start Date.")
            return  # Return if date comparison fails

        name = self.name_entry.get().strip()
        # Input validation for name (only alphabetical characters and spaces)
        if not re.fullmatch(r"[a-zA-Z\s]+", name) or not name.strip():
            messagebox.showwarning("Invalid Input", "Please enter a valid name.")
            # Return early if validation fails
            return
        # Input validation for age
        if not age.isdigit():
            messagebox.showwarning("Invalid Input", "Age must be an integer.")
            return
        age_int = int(age)
        if age_int <= 5 or len(age) > 2:
            messagebox.showwarning("Invalid Input", "Age must be a number greater than 5 and a maximum of 2 digits.")
            return

        # Input validation for mobile number (11 digits starting with '01')
        if not mobile_number.isdigit() or len(mobile_number) != 11 or not mobile_number.startswith('01'):
            messagebox.showwarning("Invalid Input", "Mobile number must be an 11-digit number starting with '01'.")
            return
        # Call the add_member function from database.py
        if not re.fullmatch(r"[a-zA-Z\s]+", trainer_name) or not trainer_name.strip():
            messagebox.showwarning("Invalid Input", "Please enter a valid trainer name.")
            return
        add_member(name, age, gender, mobile_number, address, trainer_name, subscription_package, start_date, end_date)

        messagebox.showinfo("Success", "Member added successfully!")

        # Clear entry fields after successful save (Optional)
        # self.clear_add_member_fields()

        # Optionally clear fields or go back to main menu
        self.main_menu()  # Go back to the main menu after saving

    # --- View Member Methods ---

    def view_members(self):  # directly calls the view members page setup
        self.view_members_page()

    # Method to display all members
    def view_members_page(self):
        self.clear_main_window(width=1200) # Use the larger width

        # Use a main frame to contain the widgets and use grid layout
        main_frame = ttk.Frame(self.root, padding="10") # Added padding for better spacing 
        main_frame.grid(row=0, column=0, sticky="nsew")

        view_members_label = ttk.Label(main_frame, text="View All Members", font=('Arial', 16, 'bold'))
        view_members_label.grid(row=0, column=0, pady=20, columnspan=2)
        tree_frame = ttk.Frame(self.root)
        tree_frame.grid(row=1, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)
        # Create a Scrollbar
        tree_scrollbar = ttk.Scrollbar(tree_frame)
        tree_scrollbar.pack(side="right", fill="y")

        # Create a Treeview widget
        self.members_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrollbar.set, selectmode="browse", show='tree headings borders') # Added show option 
        self.members_tree.pack(fill="both", expand=True)

        # Configure the scrollbar
        tree_scrollbar.config(command=self.members_tree.yview)

        # Define columns
        self.members_tree['columns'] = ("ID", "Name", "Age", "Gender", "Mobile Number", "Address", "Trainer Name",
                                        "Subscription Package", "Start Date", "End Date")  # Added Start and End Dates

        # Format columns with specific widths
        self.members_tree.column("#0", width=0, stretch=tk.NO)  # Hidden first column
        self.members_tree.column("ID", anchor=tk.W, width=50)  # Adjust width for ID
        self.members_tree.column("Name", anchor=tk.W, width=120)  # Adjust width for Name
        self.members_tree.column("Age", anchor=tk.W, width=50)  # Adjust width for Age
        self.members_tree.column("Gender", anchor=tk.W, width=80)  # Adjust width for Gender
        self.members_tree.column("Mobile Number", anchor=tk.W, width=100)  # Adjust width for Mobile Number
        self.members_tree.column("Address", anchor=tk.W, width=150)  # Adjust width for Address
        self.members_tree.column("Trainer Name", anchor=tk.W, width=100)  # Adjust width for Trainer Name
        self.members_tree.column("Subscription Package", anchor=tk.W, width=120)  # Adjust width for Subscription Package
        self.members_tree.column("Start Date", anchor=tk.W, width=100)  # Ensure sufficient width for Start Date
        self.members_tree.column("End Date", anchor=tk.W, width=100)  # Ensure sufficient width for End Date

        # Create headings
        self.members_tree.heading("#0", text="", anchor=tk.W)
        for col in self.members_tree['columns']:
            self.members_tree.heading(col, text=col, anchor=tk.W)

        # Fetch and display data
        self.populate_members_tree()

        back_button = ttk.Button(main_frame, text="Back to Menu", command=self.main_menu)
        back_button.grid(row=2, column=0, pady=10) # Adjusted grid placement 

        # Configure grid weights to make the tree_frame expand
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1) # Ensure root column expands

    def edit_member_page(self):
        # Method to display members for editing/deletion
        self.clear_main_window(width=1200) # Use the larger width
        # Use a main frame to contain the widgets and use grid layout
        main_frame = ttk.Frame(self.root, padding="10") # Added padding for better spacing 
        main_frame.grid(row=0, column=0, sticky="nsew")
        edit_member_label = ttk.Label(main_frame, text="Edit/Delete Members", font=('Arial', 16, 'bold'))
        edit_member_label.grid(row=0, column=0, pady=20, columnspan=2)

        tree_frame = ttk.Frame(main_frame)

        # Create a Scrollbar
        tree_scrollbar = ttk.Scrollbar(tree_frame)
        tree_scrollbar.pack(side="right", fill="y")

        # Create a Treeview widget
        self.edit_members_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrollbar.set, selectmode="browse", show='tree headings borders') # Added show option 
        self.edit_members_tree.pack(fill="both", expand=True)

        # Configure the scrollbar
        tree_scrollbar.config(command=self.edit_members_tree.yview)

        # Define columns
        self.edit_members_tree['columns'] = ("ID", "Name", "Age", "Gender", "Mobile Number", "Address", "Trainer Name",
                                             "Subscription Package", "Start Date", "End Date")  # Added Start and End Dates

        # Format columns with specific widths
        self.edit_members_tree.column("#0", width=0, stretch=tk.NO)  # Hidden first column
        self.edit_members_tree.column("ID", anchor=tk.W, width=50)  # Adjust width for ID
        self.edit_members_tree.column("Name", anchor=tk.W, width=120)  # Adjust width for Name
        self.edit_members_tree.column("Age", anchor=tk.W, width=50)  # Adjust width for Age
        self.edit_members_tree.column("Gender", anchor=tk.W, width=80)  # Adjust width for Gender
        self.edit_members_tree.column("Mobile Number", anchor=tk.W, width=100)  # Adjust width for Mobile Number
        self.edit_members_tree.column("Address", anchor=tk.W, width=150)  # Adjust width for Address
        self.edit_members_tree.column("Trainer Name", anchor=tk.W, width=100)  # Adjust width for Trainer Name
        self.edit_members_tree.column("Subscription Package", anchor=tk.W, width=120)  # Adjust width for Subscription Package
        self.edit_members_tree.column("Start Date", anchor=tk.W, width=100)  # Ensure sufficient width for Start Date
        self.edit_members_tree.column("End Date", anchor=tk.W, width=100)  # Ensure sufficient width for End Date

        # Create headings
        self.edit_members_tree.heading("#0", text="", anchor=tk.W)
        for col in self.edit_members_tree['columns']:
            self.edit_members_tree.heading(col, text=col, anchor=tk.W)

        # Populate the treeview with members
        self.populate_members_tree_edit()

        # Bind the treeview selection event to enable/disable buttons
        self.edit_members_tree.bind('<<TreeviewSelect>>', self.enable_edit_delete_buttons)

        # Buttons for Edit and Delete
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10, columnspan=2)
        # Placed buttons using grid within button_frame
        self.edit_button = ttk.Button(button_frame, text="Edit", command=self.open_edit_member_window,
                                      state=tk.DISABLED)
        self.edit_button.grid(row=0, column=0, padx=10, sticky="ew") # Added sticky for better alignment
 
        self.delete_button = ttk.Button(button_frame, text="Delete", command=self.delete_selected_member,
                                        state=tk.DISABLED)
        self.delete_button.grid(row=0, column=1, padx=10)

        # Configure grid weights to make the tree_frame expand
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Add a back button to return to the main menu
        back_button = ttk.Button(self.root, text="Back to Menu", command=self.main_menu)
        back_button.pack(pady=10)

    # --- Edit/Delete Member Methods ---

    def edit_member(self):  # directly calls the edit member page setup
        self.edit_member_page()

    def enable_edit_delete_buttons(self, event):
        selected_item = self.edit_members_tree.focus()
        if selected_item:
            self.edit_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.edit_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

    def open_edit_member_window(self):  # Method to open the edit details window
        self.selected_item = self.edit_members_tree.focus()
        if not self.selected_item:
            messagebox.showwarning("No Selection", "Please select a member to edit.")
            return

        self.member_details = self.edit_members_tree.item(self.selected_item, 'values')
        # Store member_id_to_edit as an instance variable
        self.member_id_to_edit = self.member_details[0]

        self.edit_member_details_window = tk.Toplevel(self.root)
        self.edit_member_details_window.title(f"Edit Member: {self.member_details[1]}")

        # Labels and Entry fields for member details
        ttk.Label(self.edit_member_details_window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.edit_name_entry = ttk.Entry(self.edit_member_details_window, width=30)
        self.edit_name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.edit_name_entry.insert(0, self.member_details[1])

        ttk.Label(self.edit_member_details_window, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.edit_age_entry = ttk.Entry(self.edit_member_details_window, width=30)
        self.edit_age_entry.grid(row=1, column=1, padx=10, pady=5)
        self.edit_age_entry.insert(0, self.member_details[2])

        ttk.Label(self.edit_member_details_window, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.edit_gender_combobox = ttk.Combobox(self.edit_member_details_window, values=["male", "female"], width=28,
                                                 state="readonly")
        self.edit_gender_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.edit_gender_combobox.set(self.member_details[3])  # Set current gender

        ttk.Label(self.edit_member_details_window, text="Mobile Number:").grid(row=3, column=0, padx=10, pady=5,
                                                                               sticky='w')
        self.edit_mobile_entry = ttk.Entry(self.edit_member_details_window, width=30)
        self.edit_mobile_entry.grid(row=3, column=1, padx=10, pady=5)
        self.edit_mobile_entry.insert(0, self.member_details[4])

        ttk.Label(self.edit_member_details_window, text="Address:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.edit_address_entry = ttk.Entry(self.edit_member_details_window, width=30)
        self.edit_address_entry.grid(row=4, column=1, padx=10, pady=5)
        self.edit_address_entry.insert(0, self.member_details[5])

        ttk.Label(self.edit_member_details_window, text="Trainer Name:").grid(row=5, column=0, padx=10, pady=5,
                                                                              sticky='w')
        self.edit_trainer_entry = ttk.Entry(self.edit_member_details_window, width=30)
        self.edit_trainer_entry.grid(row=5, column=1, padx=10, pady=5)
        self.edit_trainer_entry.insert(0, self.member_details[6])

        ttk.Label(self.edit_member_details_window, text="Subscription Package:").grid(row=6, column=0, padx=10, pady=5,
                                                                                      sticky='w')
        self.edit_package_combobox = ttk.Combobox(self.edit_member_details_window,
                                                  values=["Silver", "Gold", "Platinum"], width=28,
                                                  state="readonly")  # Corrected values to match standard packages
        self.edit_package_combobox.grid(row=6, column=1, padx=10, pady=5)
        self.edit_package_combobox.set(self.member_details[7])  # Set current package

        # Add Start Date and End Date fields to edit window
        ttk.Label(self.edit_member_details_window, text="Start Date (YYYY-MM-DD):").grid(row=7, column=0, padx=10,
                                                                                          pady=5, sticky='w')
        self.edit_start_date_entry = ttk.Entry(self.edit_member_details_window, width=30)
        self.edit_start_date_entry.grid(row=7, column=1, padx=10, pady=5)
        self.edit_start_date_entry.insert(0, self.member_details[8])  # Populate with existing start date

        ttk.Label(self.edit_member_details_window, text="End Date (YYYY-MM-DD):").grid(row=8, column=0, padx=10, pady=5,
                                                                                        sticky='w')
        self.edit_end_date_entry = ttk.Entry(self.edit_member_details_window, width=30)
        self.edit_end_date_entry.grid(row=8, column=1, padx=10, pady=5)
        self.edit_end_date_entry.insert(0, self.member_details[9])  # Populate with existing end date

        # Update button
        update_button = ttk.Button(self.edit_member_details_window, text="Update Member", command=self.update_member_in_db)

        update_button.grid(row=9, column=0, columnspan=2, pady=20)  # Adjust row

    def update_member_in_db(self):
        name = self.edit_name_entry.get().strip()
        age = self.edit_age_entry.get()
        gender = self.edit_gender_combobox.get()
        mobile_number = self.edit_mobile_entry.get().strip()
        address = self.edit_address_entry.get().strip()
        trainer_name = self.edit_trainer_entry.get().strip()
        subscription_package = self.edit_package_combobox.get()
        start_date = self.edit_start_date_entry.get().strip()
        end_date = self.edit_end_date_entry.get().strip()  # Get updated end date

        # Input validation
        if not re.fullmatch(r"[a-zA-Z\s]+", name) or not name.strip():
            messagebox.showwarning("Invalid Input", "Please enter a valid name.")
            return

        if not age.isdigit():
            messagebox.showwarning("Invalid Input", "Age must be an integer.")
            return
        age_int = int(age)
        if age_int <= 5 or len(age) > 2:
            messagebox.showwarning("Invalid Input", "Age must be a number greater than 5 and a maximum of 2 digits.")
            return

        if not mobile_number.isdigit() or len(mobile_number) != 11 or not mobile_number.startswith('01'):
            messagebox.showwarning("Invalid Input", "Mobile number must be an 11-digit number starting with '01'.")
            return

        if not re.fullmatch(r"[a-zA-Z\s]+", trainer_name) or not trainer_name.strip():
            messagebox.showwarning("Invalid Input", "Please enter a valid trainer name.")
            return

        # Date validation and comparison
        if not self.validate_date(start_date) or not self.validate_date(end_date):
            messagebox.showwarning("Invalid Input", "Please enter valid dates in YYYY-MM-DD format.")
            return

        # Check if end date is after start date
        if datetime.strptime(start_date, '%Y-%m-%d') > datetime.strptime(end_date, '%Y-%m-%d'):
            messagebox.showwarning("Invalid Input", "End Date cannot be before Start Date.")
            return

        try:
            age = int(age)  # Convert age to integer after validation
            update_member(self.member_id_to_edit, name, age, gender, mobile_number, address, trainer_name,
                          subscription_package, start_date, end_date)
            messagebox.showinfo("Success", "Member updated successfully!")
            self.edit_member_details_window.destroy()
            # Close the edit window and refresh the treeview on success
            self.populate_members_tree_edit()  # Refresh the Treeview
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update member: {e}")

    # --- Helper Methods ---
    def validate_date(self, date_string):
        """Validates if a string is a valid date in YYYY-MM-DD format."""
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def delete_selected_member(self):
        selected_item = self.edit_members_tree.focus()
        if selected_item:
            member_id = self.edit_members_tree.item(selected_item, 'values')[0]
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete member with ID: {member_id}?")
            if confirm:
                try:
                    delete_member(member_id)
                    self.edit_members_tree.delete(selected_item)
                    messagebox.showinfo("Success", "Member deleted successfully!")
                    self.enable_edit_delete_buttons(None)  # Disable buttons after deletion
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete member: {e}")
        else:
            # Show a warning if no member is selected
            messagebox.showwarning("No Selection", "Please select a member to delete.")

    def login(self):  # Corrected login logic
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "123":
            self.login_window.destroy()
            self.root.deiconify()  # Show the main window
            self.main_menu()  # Transition to main menu
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def populate_members_tree(self):
        # Clear existing data in the treeview
        for record in self.members_tree.get_children():
            self.members_tree.delete(record)

        # Fetch members from the database and insert into the view members treeview
        members_data = get_members()
        for member in members_data:
            self.members_tree.insert(parent='', index='end', iid=member[0], text='', values=member)

    # Populates the treeview in the edit/delete members page
    def populate_members_tree_edit(self):
        # Clear existing data in the treeview
        for record in self.edit_members_tree.get_children():
            self.edit_members_tree.delete(record)

        # Fetch members from the database and insert into the Treeview
        members_data = get_members()
        for member in members_data:
            self.edit_members_tree.insert(parent='', index='end', iid=member[0], text='', values=member)


# Main execution block
if __name__ == "__main__":
    create_database()
    root = tk.Tk()
    app = GymApp(root)
    root.mainloop()
