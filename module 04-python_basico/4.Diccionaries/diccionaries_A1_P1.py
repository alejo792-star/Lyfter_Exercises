new_dictionaries = {
    "name": "Zahara Hotels",
    "star_calification": 5,
    "rooms": [
        {
            "number": 101,
            "level": 1,
            "night_price": 100
        },
        {
            "number": 201,
            "level": 2,
            "night_price": 150
        },
        {
            "number": 301,
            "level": 3,
            "night_price": 200
        }
    ]
}
"""
print(new_dictionaries["name"])
print(new_dictionaries.get("rooms"))
"""

for information,descripcion in new_dictionaries.items():
    print(f"{information}: {descripcion}")