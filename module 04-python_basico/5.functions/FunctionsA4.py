
def use_isupper_islower (text):
    counter_isupper = 0
    counter_islower = 0
    for letter in text:
        if letter.isupper():
            counter_isupper += 1
        elif letter.islower():
            counter_islower += 1
        else:
            continue
    return f"There's {counter_isupper} upper cases and {counter_islower} lower cases"


def main():
    string_text = "I love Nación Sushi"
    result = use_isupper_islower(string_text)
    print(result)

main()
   