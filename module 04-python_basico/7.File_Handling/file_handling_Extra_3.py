def read_complete_text(path):
    with open(path, 'r',encoding='utf-8') as file:
        content= file.readlines()
        return content


def convert_to_uppercase(text):
    text_upper = []
    for line in text:
        line = line.upper()
        text_upper.append(line)
    return text_upper

def create_to_new_file(path,text):
    with open(path,'w', encoding='utf-8') as file:
        for line in text:
            file.write(line)

def main():
    path = "file_handling_Extra_3.txt"
    text = read_complete_text(path)
    upper_text = convert_to_uppercase(text)
    create_to_new_file('new_file_upper.txt',upper_text)

if __name__ == "__main__":
    main()
