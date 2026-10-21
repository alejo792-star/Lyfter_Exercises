def read_complete_text(path):
    with open(path, 'r',encoding='utf-8') as file:
        content= file.readlines()
        return content

def create_to_new_file(path,text):
    with open(path,'w', encoding='utf-8') as file:
        file.write(text)

def cleaner_list_text(text):
    clean_text = []
    for line in text:
        line = line.strip()
        clean_text.append(line)
    clean_text = " ".join(clean_text)
    return clean_text


def main():
    path = "text_extra_1.txt"
    text = read_complete_text(path)
    clean_text = cleaner_list_text(text)
    create_to_new_file('new_file_tex.txt',clean_text)


if __name__ == "__main__":
    main()