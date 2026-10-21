name_user = str(input("what's your name👌🏻: "))
last_name = input("what's your last name👌🏻: ")
age_user =int(input("How old are you👌🏻: "))
category = ""
if age_user <= 2:
    category = "baby 👶"   
elif age_user <= 11:
    category = "child 🧒"
elif age_user <= 14:
    category = "preteen🧑"
elif age_user <= 17:
    category = "teenager🧑‍🎓"
elif age_user <= 29:
    category = "young adult👨"
elif age_user <= 64:
    category = "adult👨"
else:
    category = "senior🦖"
print(f"Name: {name_user}\nLast Name: {last_name}\nCatefory: {category}")

