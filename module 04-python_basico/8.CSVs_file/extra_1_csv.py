# 1. Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea

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


def main ():
    file_path = "games.csv"
    games = open_file(file_path)
    show_games(games)

if __name__ == "__main__":
        main()