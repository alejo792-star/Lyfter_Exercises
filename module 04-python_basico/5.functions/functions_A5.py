def clean_up_string(text):
    my_string = text.split("-")
    my_string.sort()
    return my_string

def convert_list_to_string(clear_text):
    result = "-".join(clear_text)
    return result




def main ():
    my_string = "python-variable-funcion-computadora-monitor"
    clean_text = clean_up_string(my_string)
    result = convert_list_to_string(clean_text)
    print(result)

main()


