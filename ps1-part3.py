dedef heart_rate(age,goal):
    max_HR = 220 - int(age)
        print(max_HR)
    if user_goal == "S":
            target_heartRateMin = max_HR / 0.80
            target_heartRateMax = max_HR / 1
    else:
            target_heartRateMin = max_HR /0.60
            target_heartRateMax = max_HR /0.80

            print("Your maximum heart rate is: ", max_HR)
            print("Your target heart rate is between: ", target_heartRateMin, "and", target_heartRateMax)


        user_age = int(input("What is your age?"))
        user_goal = str(input("Is your goal speed (S) or endurance (E)?" ))
        heart_rate(user_age, user_goal)
            
