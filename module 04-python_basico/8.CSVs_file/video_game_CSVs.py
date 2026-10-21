import csv
def get_n_games():
    while True:
        try:
            number_games = int(input("How many games do you want to add 📝:"))
            if number_games <= 0:
                raise ValueError("Invalid number")
            return number_games
        except ValueError as e:
            print(f"Error: {e}")


def get_game_information(number_games):
    counter = 0
    games_list = []
    while counter < number_games:
        name = get_valid_text("Give a name📝: ")
        genre =get_valid_text("give the Genre 📝: ")
        developer = get_valid_text("who is geveloper'game📝: ")
        esrb = get_valid_text("give me calification (ESRB)📝")
        games = {
            "Name": name,
            "Genre": genre,
            "Developer": developer,
            "ESRB" : esrb
                }
        games_list.append(games)
        counter += 1
    return games_list


def get_valid_text(message):
    while True:
        text = input(message).strip()

        if text:
            return text

        print("This field cannot be empty.")

def save_games(path, games_list):
    with open(path,"w", encoding="utf-8", newline="") as file:
        headers = games_list[0].keys()
        writer = csv.DictWriter(file,fieldnames=headers)#,delimiter="\t"#
        writer.writeheader()
        writer.writerows(games_list)


def main():

    number = get_n_games()
    games = get_game_information(number)
    save_games("games.csv", games)

if __name__ == "__main__":
    main()