def get_name():
    name = input("What' your name: ")
    if name.isdigit():
            raise InvalidNameError("The name can't be or contain a number ❌")
    return name

def get_age():
    age = int(input("What's you age: "))
    if age <= 0 or age >100:
        raise InvalidAgeError("use a real age")
    return age

class InvalidAgeError (Exception):
    pass
class InvalidNameError (Exception):
    pass
def main ():
    try:
        name = get_name()
        age = get_age()
        print(f"hi {name} yout age is: {age} 😎")
    except InvalidNameError as e:
        print(f"Error [ValueError]:The name is not a number: {e}")
    except InvalidAgeError as e:
        print(f"Error [InvalidAgeError]: this is no a age: {e}")
    except ValueError as e:
        print(f"Error [ValueError]: this is no a age: {e}")

main()
