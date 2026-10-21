def read_complete_text(path):
    with open(path, 'r',encoding='utf-8') as file:
        content = file.readlines()
        return content

def count_words(text):
    clean_text = []
    for line in text:
        line = line.strip().split()
        clean_text.extend(line)
    word_count = len(clean_text)
    return word_count

def main():
    path = "songs.txt"
    text = read_complete_text(path)
    word_count = count_words(text)
    print(f"this file have {word_count} words ⭐️😎")

if __name__ == "__main__":
    main()