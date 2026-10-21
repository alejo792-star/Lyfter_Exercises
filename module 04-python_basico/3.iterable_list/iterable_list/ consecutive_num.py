num = int (input("enter a number: "))
sum_total = 0
if num > 0:
    for counter in range (1, num + 1):
        sum_total += counter
    print(f"the sum of consecutive numbers from 1 to {num} is: {sum_total}")
    