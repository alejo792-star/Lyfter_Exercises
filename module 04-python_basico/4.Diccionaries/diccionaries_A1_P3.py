list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key_delate in list_of_keys:
    delate_item = employee.pop(key_delate)
    print(f"delate item {key_delate} : {delate_item} ✅")

print(employee)