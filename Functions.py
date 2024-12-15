import json
from tabulate import tabulate


class Student():
    def __init__(self):
        # Load existing data or initialize an empty dictionary
        try:
            with open("data.json", "r") as f:
                self.std_dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.std_dict = {}
            self.save_data()
            
    def save_data(self):
        #"""Helper method to save student data to the file."""
        with open("data.json", "w") as f:
            json.dump(self.std_dict, f, indent=4)
            
    # Add student function 
    def add_student(self):
        ID = input("Enter ID: ")
    # Check if ID already exists in the dictionary
        if ID in self.std_dict:
            print("ID already exists.")
        else:
            Name = input("Enter Name: ")
            Age = input("Enter Age: ")
            Address = input("Enter Address: ")
            Phone = input("Enter Phone: ")
            Email = input("Enter Email: ")
            # Store student information
            self.std_dict[ID] = {
                "Name": Name,
                "Age": Age,
                "Address": Address,
                "Phone": Phone,
                "Email": Email
            }
            self.save_data()
            Student.view_student(self,ID)
            print("Student added successfully!")
        
    # Update student function
    def update_student(self):
        """Update an existing student's information."""
        ID = input("Enter ID: ")
        if ID in self.std_dict:      
            print("Leave fields blank to keep the current value.")
            current_data = self.std_dict[ID]

            Name = input(f"Enter Name [{current_data['Name']}]: ") or current_data['Name']
            Age = input(f"Enter Age [{current_data['Age']}]: ") or current_data['Age']
            Address = input(f"Enter Address [{current_data['Address']}]: ") or current_data['Address']
            Phone = input(f"Enter Phone [{current_data['Phone']}]: ") or current_data['Phone']
            Email = input(f"Enter Email [{current_data['Email']}]: ") or current_data['Email']

            self.std_dict[ID] = {
                "Name": Name,
                "Age": Age,
                "Address": Address,
                "Phone": Phone,
                "Email": Email
            }
            self.save_data()
            #Show updated student.
            Student.view_student(self,ID)
            print("Student updated successfully!")
        else:
            print(f"ID {ID} does not exist.")
         
    def view_student(self, ID):
        dict = self.std_dict[ID]
        headers = ["ID", "Name", "Age", "Address", "Phone", "Email"]
        #headers = ["ID"] + list(next(iter(dict.values())).keys())
        rows = [[ID] + list(dict.values())]
        print(tabulate(rows, headers, tablefmt="fancy_grid"))
        
    #View student via ID
    def search_student(self):
        ID = input("Enter ID: ")
        if ID in self.std_dict:
            Student.view_student(self,ID)
        else: 
            print(f"ID {ID} does not exist.")
            
    #Display all students
    def display_student(self):
        dict = self.std_dict
        headers = ["Sr.No","ID", "Name", "Age", "Address", "Phone", "Email"]
        #headers = ["S.No","ID"] + list(next(iter(dict.values())).keys())
        rows = [[index +1, key] + list(values.values()) for index, (key, values) in enumerate(dict.items())]
        print(tabulate(rows, headers, tablefmt="fancy_grid"))
        
    #Delete student 
    def delete_student(self):
        ID = input("Enter ID: ")
        if ID in self.std_dict:
            choose = input("Are you sure you want to delete this student? (y/n): ")
            if choose == "y" or choose == "Y":
                del self.std_dict[ID]
                print(f"Student of ID:{ID} deleted successfully!")
                self.save_data()
            elif choose == "n" or choose == "N":
                print("Deletion cancelled.")
            else:
                print("Invalid choice. Deletion cancelled.")
        else:
            print(f"Student of ID:{ID} does not exist or has already been deleted.")