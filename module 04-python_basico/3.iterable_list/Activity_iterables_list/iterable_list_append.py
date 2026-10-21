numbers_list = []
max_number = -3
for number in range (1,11):
    user_number = int(input("Enter a number: "))
    numbers_list.append(user_number)
    if user_number > max_number:
        max_number = user_number
print(numbers_list,"The maximum number is:", max_number)




