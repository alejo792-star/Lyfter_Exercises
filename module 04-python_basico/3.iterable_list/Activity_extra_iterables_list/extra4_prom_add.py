my_list = [10, 20, 30, 40, 50]
average =sum(my_list) / len(my_list)
new_list = []

for number in my_list:
    if number > average:
        new_list.append(number)
        print(f"Added number ✅: {number} ")
    else:
        continue
print(f"the avrrage: {average} 🏆")
print(f"the new list 📝: {new_list}🏆")
print("thank so much for using this program 🙏🏻")