my_list = [4, 2, 7, 2, 8, 2, 1]
counter = 0 
number_to_count = int(input(f"Enter a number to count in the list📋: {my_list}: "))
for numbers in my_list:
    if numbers == number_to_count:
        counter += 1
    else:
        continue
print(f"The number {number_to_count} appears {counter} times in the list.📝")
print("Thank you for using the program! 🙏")
