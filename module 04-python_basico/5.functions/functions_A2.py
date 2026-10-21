
def sum_numbers(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

def main():
    numbers =[4, 6, 2, 29]
    total = sum_numbers(numbers)
    print(total)
main()