employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
final_categories={

}
for employee in employees:
    if employee["department"] in final_categories:
        final_categories[employee["department"]].append(employee["name"])
        print(f"has been added {employee['name']} to the existing category {employee['department']}✅")
    else:
        final_categories[employee["department"]] = [employee["name"]]
        print(f"hass been added a new category {employee['department']}✅")
print(final_categories)

