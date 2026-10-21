words_user_list = []
final_list = []
for i in range(0,5):
    words_user = input(" enter a word🤓: ")
    words_user_list.append(words_user)
    if len(words_user) > 4:
        final_list.append(words_user)
    else:
        continue
print(f"These words have more than 4 letters. 🫡 ")
print(final_list)
print("thank ✅")