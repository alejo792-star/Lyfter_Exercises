print("______-_ classifier Gaming____")
name = str(input("what's your name: "))
hours_played = float(input("How many hours have you played: "))
competed = input("have you comped (y/n): ").strip().lower()
category = ""
messaje = ""
if competed in ["yes", "y","si","s"]:
    competed = True
elif competed in ["no","n","not"]:
    competed = False
if hours_played < 10:
    category = "Novato"
    messaje = "Novato"
elif hours_played < 50:
    category = "casual"
    messaje = "casual"
elif hours_played < 200:
    category = "Nivel gamer "
    messaje = "Nivel gamer"
elif hours_played >=200 and competed ==True:
    category = "nivel pro."
    messaje = "Nivel pro."
else:
    category = False
    print("you don't have a category.")

print("______-_ classifier Gaming____")
print(f"Player name:{name}\nCategory: {category}\nend program" )