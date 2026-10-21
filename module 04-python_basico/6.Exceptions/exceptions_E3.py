def convert_string_to_list():
    string_to_convert = input("give me a elements for the list📝: ")
    list_string = (string_to_convert).split()
    return list_string

def show_menu ():
    print("* ⭐️ WELCOME TO EXCEPTIONS MUNU ⭐️*")
    print("* ⭐️ ====MENU==== *")
    print("* 1️⃣. ACTIVITY LIST ['4', 'hola', '10', '5.2']")
    print("* 2️⃣. INPUT LIST ")

def execute_operation(list_string):
    for element in list_string:
        try:
            int_element = int(element)
            print(f"{int_element} comvet ✅")
        except ValueError:
            print(f"{element} can't to convert❌")
def get_menu_option():
    user_option = int(input("Choose an option.📝: "))
    if (user_option <= 0 or user_option > 2):
        raise InvalidUserOption("Invalid option❌")
    return user_option
    

class InvalidUserOption(Exception):
    pass
def main():
        try:
            show_menu()

            user_option = get_menu_option()
            if user_option == 1:
                list_string = ['4', 'hola', '10', '5.2']
                execute_operation(list_string)

            elif user_option == 2:
                list_string = convert_string_to_list()
                execute_operation(list_string)
        except InvalidUserOption as e:
                print(f"Error: {e}")
        except ValueError as e:
                print(f"error {e}")

main()    