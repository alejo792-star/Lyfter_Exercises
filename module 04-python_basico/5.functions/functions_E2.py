def filter_words_by_length(list_word, number):
    new_list =[]
    for word in list_word:
        if(len(word) > number):
            new_list.append(word)
    return new_list


def main():
    list_word = input("give words 📝: ").split()
    number =int(input("now give a number📝: "))
    new_list = filter_words_by_length(list_word,number)
    print(f"{new_list} ✅")

main()

