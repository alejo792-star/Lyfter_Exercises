print("---- welcome to the sever program ----")
name_customer = (input("what's your name: "))
mountly_saving = float(input("How much money do you want to save: "))
mountly_saving = int(input("How many months do you want to save: "))
total_saving = 0

for month in range(1, mountly_saving + 1):
    total_saving += mountly_saving
    print(f"Month {month}: Total saving: {total_saving}")   
print(f"{name_customer}, in {mountly_saving} months you will have saved: {total_saving}")

