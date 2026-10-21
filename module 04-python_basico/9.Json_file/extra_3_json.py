# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

import json

def open_file(file_path):
    try:    
        with open(file_path,"r",encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("something is wrong")

def show_information(pokemos):
    print("-" * 30)
    print("⭐ POKEMON INFORMATION ⭐")
    print("-" * 30)

    for pokemon in pokemos:
        print("-" * 30)
        print(f" ⭐️ NAME: {pokemon["name"]} ⭐️ ")
        print("-" * 30)
        for key , value in pokemon["stats"].items():
            print(f"{key.replace('_',' ').title():<15}:{value:>3}")


def main():
    file_path = "pokemos.json"
    pokemons = open_file(file_path)
    if pokemons is not None:
        show_information(pokemons)

if __name__ == "__main__":
    main() 