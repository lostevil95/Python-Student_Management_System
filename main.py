from Functions import Student


def main():
    sms = Student()
    
    while True:
        print("<===Student Management System of Library===>")
        print("List of choices:")
        print("1. Add Student.")
        print("2. Update Student Data.")
        print("3. Search and view Student via ID.")
        print("4. Display all students in list.")
        print("5. Delete student via ID.")
        print("0. Exit.")
        
        i = int(input("Enter your choice: "))
        
        if i == 1:
            sms.add_student()
        elif i == 2:
            sms.update_student()
        elif i == 3:
            sms.search_student()
        elif i == 4:
            sms.display_student()
        elif i == 5:
            sms.delete_student()
        elif i == 0:
            break
        else:
            print("Invalid choice. Please enter again.")            
            
if __name__ == "__main__":
    main()