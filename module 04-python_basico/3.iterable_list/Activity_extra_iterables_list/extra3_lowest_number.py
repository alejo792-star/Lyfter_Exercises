my_list = [9, 4, 7, 1, 5]
min_number=my_list[0]

for number in my_list:
    if number < min_number:
        min_number = number
        print(f"the new lowest number is 😎: {min_number}")
    else:
        print(f"the number {number} is not the lowest ❌")

print(f"the lowest number  is {min_number} ✅")