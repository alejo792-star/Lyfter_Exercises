
def counter_character(text,character):
    counter = 0 
    for letter in text:
        if (character == letter):
            counter = counter + 1
    return counter


def main():
    text_analyze = input("give me a word📝: ")
    letter =input("give me a letter to find🔎: ")
    result = counter_character(text_analyze,letter)
    print("analyzing🧐")
    print(f"word: {text_analyze} --- character to find {letter}")
    print(f"has been found {result}")
main()
