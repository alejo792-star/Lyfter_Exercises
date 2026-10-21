# 3. Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada

import csv
def open_file(file_path):
    with open(file_path,"r",encoding="utf-8",newline="") as archivito:
        reader = csv.reader(archivito)
        headings = next(reader,None)
        games = []
        for game in reader:
            games.append(game)
        return games

def clasification_games(games):
    clasification ={}
    for game in games:
        category = game[1]
        if category in clasification:
            clasification[category]+=1
        else:
            clasification[category]=1
    return clasification

def show_category(clasification):
    print("Clasification")
    for category, amount in clasification.items():
        print(f"{category}:{amount}")


def main():
    file_path = "games.csv"
    games= open_file(file_path)
    clasification = clasification_games(games)
    show_category(clasification)

if __name__ == "__main__":
    main()

