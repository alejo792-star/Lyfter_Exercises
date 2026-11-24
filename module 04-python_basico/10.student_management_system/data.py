import csv
from pathlib import Path

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
        writer.writerows(student_list)
    print("Students exported successfully!")

def import_students(student_list):
    try:
        file_path = Path(__file__).resolve().parent / "students.csv"
        with open(file_path,"r", encoding= "utf-8", newline="") as file:
            reader = csv.DictReader(file)
            imported_students = []
            for student in reader:
                student["spanish"]= float(student["spanish"])
                student["english"]= float(student["english"])
                student["social_studies"]= float(student["social_studies"])
                student["science"]= float(student["science"])
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
        
