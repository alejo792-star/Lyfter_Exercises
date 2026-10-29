def show_menu():
    print("===== STUDENT MANAGEMENT SYSTEM =====\n"
        "1. Add students\n"
        "2. View all students\n"
        "3. View top 3 students\n"
        "4. View overall average\n"
        "5. Export students to CSV\n"
        "6. Import students from CSV\n"
        "7. Exit")

def get_option_menu():
    
        while True:
            try:
                option_menu = int(input("Select a option: "))
                if 1 <= option_menu <= 7:
                    return option_menu
                else:
                    print("please select option (1 to 7)")
                
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")



