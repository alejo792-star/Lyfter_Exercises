import csv
from pathlib import Path
from student import Student
def export_students(student_list):
    if not student_list:
        print("No students registered yet.")
        return
    file_path = Path(__file__).resolve().parent / "students.csv"
    with open(file_path,"w",newline="",encoding="utf-8")as file:
        fieldnames = [
        "full_name",
        "section",
        "spanish",
        "english",
        "social_studies",
        "science" ]
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        writer.writeheader()
        for student in student_list:
            row = {
                "full_name": student.full_name,
                "section" : student.section,
                "spanish" :student.spanish,
                "english": student.english,
                "social_studies":student.social_studies,
                "science" : student.science

            }
            writer.writerow(row)
    print("Students exported successfully!")

def import_students(student_list):
    try:
        file_path = Path(__file__).resolve().parent / "students.csv"
        with open(file_path,"r", encoding= "utf-8", newline="") as file:
            reader = csv.DictReader(file)
            imported_students = []
            for row in reader:
                student = Student(
                    full_name=row["full_name"],
                    section=row["section"],
                    spanish= float(row["spanish"]),
                    english= float(row["english"]),
                    social_studies= float(row["social_studies"]),
                    science= float(row["science"]),
                )
                imported_students.append(student)
            student_list.clear()
            student_list.extend(imported_students)
        print("Students imported successfully!")
    except FileNotFoundError as f:
        print(f"File not found: {f}")
    except ValueError as f:
        print(f"value Error: Invalid grade found {f}")
    except KeyError as f:
        print(f"Invalid CSV: missing column {f}")
        
