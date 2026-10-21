'''''
##access a variable defined inside a function from outside.
def calculete_tax(salary):
    tax = 0.10
    total = salary * tax
    return total


def main():
    print(tax)

main()
'''

 
bonus = 1000

def calculate_totalplusbonus (salary):
    global bonus
    bonus = bonus + salary
    return bonus

def main():
    salary = float(input(" give me you salary:🤑 "))
    print (calculate_totalplusbonus(salary))
    print (bonus)
main()
    

