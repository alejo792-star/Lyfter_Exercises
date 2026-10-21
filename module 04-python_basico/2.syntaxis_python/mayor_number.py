print("Welcome to the mayor number comparator!")
num1 = float(input("Enter the first number 1️⃣: "))
num2 = float(input("Enter the second number 2️⃣: "))
num3 = float(input("Enter the third number 3️⃣: "))
mayor_number = num1
if num2 > mayor_number:
    mayor_number = num2
if num3 > mayor_number:
    mayor_number = num3
print(f"The mayor number is: {mayor_number} 🏆")
