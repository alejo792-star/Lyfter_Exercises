list_a = ["first_name", "last_name", "role"]
list_b = ["Alejandro", "Martinez", "DevOps"]
dicciorary = {}

for key in range(len(list_a)):
    dicciorary[list_a[key]] = list_b[key]
    print(f"has been added ✅ {list_a[key]} : {list_b[key]}")
print("new directory 📝")
print(dicciorary)
print("end program 🔚")

