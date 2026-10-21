user_time = int(input("enter the time in seconds:⌚️"))
max_time = 600 
if user_time < max_time:
    rest_time = max_time - user_time
    print(f"you have {rest_time} seconds left.⏲️")
else:
    if user_time == max_time:
        print("the same")
    else:
        print("you have exceeded the time limit😱.")

print("Thank you for using the time calculator!😊")
