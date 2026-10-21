
def counter_vowels (text):
    counter = 0
    for character in text:
        if character in ["a","e","i","o","u"]:
            counter = counter + 1
    return counter

def main():
    text = input("gime a word or small tex 🔎")
    text_clean = text.lower()
    result = counter_vowels(text_clean)
    print(f"the Vowel have been found {result}✅")


main()
