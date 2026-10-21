# 2. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
# Lea el archivo JSON de Pokémon
# Pida al usuario un tipo de Pokémon
# Muestre todos los Pokémon que sean de ese tipo

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
def get_type_pokemon():
    while True:
        type_pokemon = input("what type pokemon are you looking for: ").strip().lower()
        if type_pokemon.isalpha():
            return type_pokemon
        else:
            print("the types doesn't have numbers")
def get_type_pokemon_information(pokemons,type_pokemon):
    filter_result=[]
    for pokemon in pokemons:
        
        if pokemon["type"].strip().lower() == type_pokemon:
            filter_result. append(pokemon)
    return filter_result
def show_information(filter_result,pokemon_type):
    if filter_result == []:
        print("No Pokémon of this type have been found.")
    else:
        print(f"we found this pokemons with {pokemon_type} type: ")
        for pokemon in filter_result:
            print(f"Pokemon Name: {pokemon["name"]}")
def main():
    file_path = "pokemos.json"
    pokemons= open_file(file_path)
    pokemon_type = get_type_pokemon()
    if pokemons is not None:
        filter_result= get_type_pokemon_information(pokemons, pokemon_type)
        show_information(filter_result, pokemon_type)

if __name__ == "__main__":
    main()


    