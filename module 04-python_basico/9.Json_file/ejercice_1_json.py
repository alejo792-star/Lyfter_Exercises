import json

# Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
# Debe leer el archivo para importar los Pokémones existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

def open_file(file_path):
    try:    
        with open(file_path,"r",encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("something is wrong")


def skills_pokemos():
    skills_number= get_integer("How many skills have you new pokemon: ")
    skills = []
    if skills_number > 0:
        for i in range(skills_number):
            skill = input(f"Give me skill")
            skills.append(skill)
    else:
        print("no skills")
    return skills


def get_stats():
    stats = {}
    stats_names = [
    "hp",
    "attack",
    "defense",
    "sp_attack",
    "sp_defense",
    "speed"
]
    for stat in stats_names:
        stats[stat] = get_integer(f"Give me {stat}")
    return stats


def add_new_pokemon(data, new_pokemon):
    data.append(new_pokemon)
    return data



def create_pokemon():
    pokemon = {
        "name": input("Pokemon name: "),
        "type": input("Pokemon type: "),
        "level": get_integer("Pokemon level: "),
        "weight_kg": get_float("Pokemon weight: "),
        "is_shiny":get_bolean("Is shiny? (yes/no): "),
        "held_item":input("Held item (leave empty if none): ").strip(),
        "skills": skills_pokemos(),
        "stats" : get_stats() 
    }

    if pokemon["held_item"] == "":
        pokemon["held_item"] = None
    return pokemon

    
def save_file(file_path, data):
    with open(file_path,"w",encoding="utf-8")as f:
        json.dump(data,f,indent=4,ensure_ascii=False)


def get_integer(message):
    while True:
        try:
            integer = int(input(message))
            if integer >= 0:
                return integer
            else:
                print("no negative numbers")
            

        except ValueError:
            print("please give a integer number")

def get_float(message):
    while True:
        try:
            float_number = float(input(message))
            if float_number > 0:
                return float_number
            else:
                print("no negative numbers.")

        except ValueError:
            print("please give a float number ")

def get_bolean(messague):
    while True:
    
        answer = input(messague).strip().lower()
        if answer in ["si","yes"]:
            return True  
        elif answer in ["no", "not"]:
            return False
        else:
            print("please enter (yes/si) o (no/not)")
    

def main():
    file_path = "pokemos.json"
    data= open_file(file_path)
    if data is None:
        return
    new_pokemon = create_pokemon()
    add_new_pokemon(data,new_pokemon)
    save_file(file_path,data)

if __name__ == "__main__":
    main()
    