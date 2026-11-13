from student import Student
def get_student_name():
    while True:
            student_name = (input("Give me  a Full student name:").strip())
            if not student_name.replace(" ", "").isalpha():
                print("The name can't contain numbers or special characters")  
            else:
                return student_name

def get_section():
    while True:
        section = input("enter Section: ").strip()
        if not section:
            print("The section can't be empty")
        else:
            return section

def add_students(student_list):
    name = get_student_name()
    section = get_section()
    for student in student_list:
        if (
            student.full_name.lower() == name.lower()
            and student.section.lower() == section.lower()
        ):
            print("Student already registered!")
            return

    student_info = Student(
        full_name = name,
        section = section,
        spanish= get_calification("Enter Spanish calification"),
        english = get_calification("Enter English calification"),
        social_studies = get_calification("Enter Social studies calification"),
        science = get_calification ("Enter science calification")
    )
    student_list.append(student_info)


def get_calification(message):
    while True:
            try:
                float_number = float(input(message))
                if float_number >= 0 and float_number <= 100:
                    return float_number
                else:
                    print("Grade must be between 0 and 100.")
    
            except ValueError:
                print("please give a float number ")


def get_integer(message):
    while True:
        try:
            integer = int(input(message))
            if integer >= 0:
                return integer
            else:
                print("no negative numbers")
        except ValueError:
            print("please give a integer number")


def show_all_students(data):
    if not data:
        print("❌No students at the moment❌")
    else:
        print("="*30)
        print(f"{"STUDENT DIRECTORY".center(30)}")
        print("="*30)
        for index, student in enumerate(data, start=1):
            print(f"{f'STUDENT #{index}':^40}")
            print(
                f"{'-' * 30}\n"
                f"{'Full Name:':<16} {student.full_name.title()}\n"
                f"{'Section:':<16} {student.section.upper()}\n"
                f"{'-' * 30}\n"
                f"{"Spanish:" :<16} {student.spanish}\n"
                f"{"English:" :<16} {student.english}\n"
                f"{"Social studies:" :<16} {student.social_studies}\n"
                f"{"science:" :<16} {student.science}"
            )
            print("="*30)

def calculate_average(student):
    grades =[student.spanish ,student.english,student.social_studies,student.science]
    average = sum(grades)/len(grades)
    return average

def show_top_three(student_list):
    if not student_list:
        print("No students registered yet.")
        return
    else:
        ordered = sorted(
        student_list,
        key=calculate_average,
        reverse= True
        )
        top_three = ordered[:3]
        print("="*30)
        print("🏆TOP 3 BEST AVERAGE STUDENTS🏆".center(30))
        print("="*30)
        for index,student in enumerate(top_three,start=1):
            print(
                f"{'-'*30}\n"
                f"{'Full Name:':<16} {student["full_name"].title()}\n"
                f"{"Average:":<16} {calculate_average(student):.2f}\n"
                f"{'Top #🏆:':<16} {index}⭐️\n"
                f"{'Congratulation 👌🏻'}\n"
            )

def show_overall_average(student_list):
    if not student_list:
            print("No students registered yet.")
            return
    else:
        students_average = []
        for student in student_list:
            average = calculate_average(student)
            students_average.append(average)
        overall_average = sum(students_average)/len(students_average)
        print("="*30)
        print("OVERALL AVERAGE".center(30))
        print("="*30)
        print(f"TOTAL STUDENTS: {len(students_average)}")
        print(F"OVERALL AVERAGE: {overall_average:.2f}")
        print("="*30)


    
