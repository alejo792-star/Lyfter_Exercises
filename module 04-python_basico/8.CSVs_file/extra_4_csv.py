# 4. Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
import csv
def open_file(file_path):
    try:
        with open(file_path,"r",encoding="utf-8",newline="") as archivito:
            reader = csv.reader(archivito)
            headings = next(reader,None)
            games = []
            for game in reader:
                games.append(game)
            return games
    except FileNotFoundError:
        print("file  not found ")
        return[]

def find_games_by_developer(games):
        dev_gamer = input("give me a Developer games'name for filter")
        result=[]
        for game in games:
            if dev_gamer.strip().lower() == game[2].strip().lower():
                result.append(game)
        return result


def show_games(games):
    if not games:
        print("We didn't find the DEV")
        return
    for game in games:
        print(f" -{game[0]}(ESRB:{game[3]},gnero:{game[1]})")

        
def main():
    file_path = "games.csv"
    games = open_file(file_path)
    result=find_games_by_developer(games)
    show_games(result)
if __name__ == "__main__":
    main()