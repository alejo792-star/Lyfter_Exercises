my_list = [3, 6, 0, -2, 4]
counter_negative = 0
for numbers in my_list:
    if numbers <= 0:
        counter_negative += 1
    else:
        continue
print(f"The list {my_list} contains {counter_negative} negative numbers.📝")
