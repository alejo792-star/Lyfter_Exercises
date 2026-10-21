my_string = "Hola mundo."

def iterate_strings_negative (my_string):
    my_new_string = ""

    for i in range(len(my_string)-1,-1,-1):
        my_new_string = my_new_string + my_string[i]
    return my_new_string

def main():

    new_string = iterate_strings_negative(my_string)
    print(new_string)
main()
