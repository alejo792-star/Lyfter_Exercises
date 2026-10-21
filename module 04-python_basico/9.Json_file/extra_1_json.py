# 1. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

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

def show_information(pokemons):
    for pokemon in pokemons:
        print("============")
        print(f"NAME: {pokemon["name"]}")
        print(f"TYPE: {pokemon["type"]}")
        print(f"LEVEL: {pokemon["level"]}")


def main ():
    file_path = "pokemos.json"
    pokemons = open_file(file_path)
    if pokemons is not None:
        show_information(pokemons)



if __name__ == "__main__":
    main()