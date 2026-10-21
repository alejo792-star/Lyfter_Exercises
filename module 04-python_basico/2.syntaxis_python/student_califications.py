print("Welcome to the student califications program!")
name = input("Enter the student's name: ")
counter = int(input("Enter the total number of califications: "))
all_grades = []
passing_grade = []
failed_grades =[]

for grade in range(1, counter +1):
    calification = float(input(f"Enter the calification📝 {grade}: "))
    while calification < 1 or calification > 100:
        print("The calification is invalid❌. Please enter a value between 1 and 10.")
        calification = float(input(f"Enter the calification {grade}: "))
    

    all_grades.append(calification)

    if calification >= 70 and calification <= 100:
        passing_grade.append(calification)
    else:
        failed_grades.append(calification)
if passing_grade  ==[]:
    print(f"cant to calculete cuz the list passing is empty")
else:
    print(f"The average of passing califications is: {prom_passing:.2f}")
    if failed_grades == []:
        print("cant to calculete cuz the list fail is empty")
    else:

        prom_grade = sum(all_grades) / len(all_grades)
        prom_passing = sum(passing_grade) / len(passing_grade) 
        prom_failed = sum(failed_grades) / len(failed_grades)
        print(f"The average of all califications is: {prom_grade:.2f}")
        print(f"The average of passing califications is: {prom_passing:.2f}")
        print(f"The average of failed califications is: {prom_failed:.2f}") 
       