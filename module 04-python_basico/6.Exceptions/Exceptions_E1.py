def calculate_addition(current_number, new_number):
    result = current_number + new_number
    return result


def calculate_subtraction(current_number,new_number):
    result = current_number - new_number
    return result


def calculate_multiplication(current_number,new_number):
    result = current_number * new_number
    return result


def calculate_division(current_number,new_number):
    result = current_number / new_number
    return result


def show_menu ():
    print("* ⭐️ WELCOME TO CALCULATOR ⭐️*")
    print("* ⭐️ ====MENU==== *")
    print("* 1️⃣. ADDITION ")
    print("* 2️⃣. SUBTRACTION ")
    print("* 3️⃣. MULTIPLICATION ")
    print("* 4️⃣. DIVISION ")
    print("* 5️⃣. DELETE ↻ ")
    print("====================") 


def get_number():
    new_number = float(input("Give me a new number:📝 "))
    return new_number


def get_menu_option():
    user_option = int(input("Choose an option.📝: "))
    if (user_option <= 0 or user_option > 5):
        raise Invalid_option("Invalid option❌")
    return user_option


def execute_operation (user_option, current_number):
    if user_option == 1:
        new_number =get_number()
        result = calculate_addition(current_number, new_number)
        print(f"{current_number} + {new_number} = {result} ✅")
        return result
    elif user_option == 2:
        new_number = get_number()
        result = calculate_subtraction(current_number,new_number)
        print(f"{current_number} - {new_number} = {result} ✅")
        return result
    elif user_option == 3:
        new_number =get_number() 
        result = calculate_multiplication(current_number,new_number)
        print(f"{current_number} * {new_number} = {result} ✅")
        return result
    elif user_option == 4:
        new_number =get_number() 
        if new_number == 0:
            raise ZeroDivisionError("can't calculate whit 0")
        result = calculate_division(current_number,new_number)
        print(f"{current_number} / {new_number} = {result} ✅")
        return result
    elif user_option == 5:
        current_number= 0
        print(f"Current number {current_number}")
        return current_number
    
    
class Invalid_option(Exception):
    pass

def main():
    current_number = 0
    while (True):
        print(f"*⭐️****CURRENT NUMBER: {current_number}***⭐️")
        show_menu()
        try:
            user_option = get_menu_option()
            current_number = execute_operation(user_option,current_number)
        except Invalid_option as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error [ValueError]: this is no a option: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        

main()