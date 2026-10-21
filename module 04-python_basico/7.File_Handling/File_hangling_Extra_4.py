def get_text ():
    text = input("Give a text 📝:")
    return text

def create_to_new_file(path,text):
    with open(path,'a', encoding='utf-8') as file:
        file.write(text + "\n")

def main():
    text = get_text()
    create_to_new_file("new_file_append.txt",text)

if __name__ == "__main__":
    main()
