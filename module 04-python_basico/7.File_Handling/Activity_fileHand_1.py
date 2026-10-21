def read_complete_text(path):
    with open(path, 'r',encoding='utf-8') as file:
        content= file.readlines()
        return content

def create_to_new_file(path,text):
    with open(path,'w', encoding='utf-8') as file:
        file.write(text)

def main():
    path = "songs.txt"
    songs = read_complete_text(path)
    songs.sort()
    text ="".join(songs)
    create_to_new_file('new_file_songs.txt',text)




if __name__ == "__main__":
    main()
    