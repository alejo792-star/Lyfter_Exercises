def execute_operation(list_string):
    result = 0
    for element in list_string:
        try:
            float_element = float(element)
            print(f"{float_element} added up correctly ✅")
            result = result + float_element
        except ValueError:
            print(f"{element} can't to added up correctly❌")
    return result

def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    total =execute_operation(my_list)
    print(f"Total: {total}")

if __name__ == "__main__":
    main()   
    