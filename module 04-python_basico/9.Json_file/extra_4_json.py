# 4. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON
# Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:
import json
def open_file(path_file):
    try:
        with open(path_file,"r",encoding="utf-8") as f:
            data= json.load(f)
            return data
    except FileNotFoundError:
        print(" File Not Found, make sure file path ")
    except json.JSONDecodeError:
        print("Sonting is wrong ⚠️")

def get_pokemontype(data):
    result = {}
    for pokemon in data:
        type_pokemon = pokemon["type"]
        if type_pokemon in result:
            result[type_pokemon].append(pokemon["level"])
        else:
            result[type_pokemon]=[pokemon["level"]]
    return result

def average_types(result):
    for type_pokemon, levels in result.items():
        average = sum(levels) / len(levels)
        print(f"{type_pokemon:<15} -> level averge {average:.2f}")      


def main ():
    path_file="pokemos.json"
    pokemon_data = open_file(path_file)
    list_type= get_pokemontype(pokemon_data)
    average_types(list_type)

if __name__ == "__main__":
    main()