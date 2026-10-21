products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
total_by_catedory ={}
for product in products:
    if product["category"] in total_by_catedory:
        total_by_catedory[product["category"]]+= product["price"]
        print(f"added {product["name"]}, to {product['category']} 🤑🤑 {product['price']}")
    else:
        total_by_catedory[product["category"]] = product["price"]
        print(f"has been created a new category {product['category']} 🥳")
    print(total_by_catedory)