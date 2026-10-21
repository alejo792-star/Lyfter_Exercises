
        
def convert_prime_numbers(list_user):
    prime_numbers = []
    for number in list_user:
        if number < 2:
            continue
        is_prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)

    return prime_numbers


def main():
    list_user = [1, 4, 6, 7, 13, 9, 67]
    result = convert_prime_numbers(list_user)
    print(result)

main()

