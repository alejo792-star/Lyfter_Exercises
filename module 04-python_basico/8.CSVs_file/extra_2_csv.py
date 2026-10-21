# 2. Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación
import csv
def open_file(file_path):
    with open(file_path,"r",encoding="utf-8",newline="") as archivito:
        reader = csv.reader(archivito)
        headings = next(reader,None)
        games = []
        for game in reader:
            games.append(game)
        return games

    
def show_games(games):
    for game in games:
        print(f"Name: {game[0]}\nGenre: {game[1]}\nDeveloper: {game[2]}\nESRB: {game[3]}\n------------")


def give_me_category(games):
        classification = input("give me a category for filter")
        result=[]
        counter = 0
        for game in games:
            if classification.strip().lower() == game[3].strip().lower():
                result.append(game)
                counter += 1
        print(f"📝we have filtered {counter}")
        return result



def main ():
    file_path = "games.csv"
    try:
        games = open_file(file_path)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {file_path}")
        return
    filter_games = give_me_category(games)
    show_games(filter_games)


if __name__ == "__main__":
        main()