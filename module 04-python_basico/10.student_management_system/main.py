from menu import show_menu, get_option_menu
from actions import add_students, get_integer, show_all_students, show_top_three, show_overall_average
from data import export_students, import_students

def main():
    list_student = []
    while True:
        show_menu()
        user_option = get_option_menu()
        if user_option == 7:
            print("goodbye 👋")
            break
        elif user_option == 1:
            student_number = get_integer("How many students")
            for i in range(student_number):
                add_students(list_student)
        elif user_option == 2:
            show_all_students(list_student)
        elif user_option == 3:
            show_top_three(list_student)
        elif user_option == 4:
            show_overall_average(list_student)
        elif user_option == 5:
            export_students(list_student)
        elif user_option == 6:
            import_students(list_student)
        





            
if __name__ == "__main__":
    main()