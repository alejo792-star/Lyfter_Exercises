my_list = [9, 4, 7, 1, 5]
lower_number = my_list[0]

for numbers in my_list:
    if numbers < lower_number:
        lower_number = numbers 
        print(f"{numbers} is the new lowest number ✅")
    else:
        print(f"the number {numbers} isn't lowesr❌")
print(f"the lowest number is: {lower_number}🏆")