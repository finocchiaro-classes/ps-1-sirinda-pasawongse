arrestnum = int(input("Prior arrests: "))
priorhist = input("Prior arrests for local ordinance (Y/N): ")

age = int(input("Age at release: "))
score = 0

if arrestnum>=5:
    score+=1
elif arrestnum>=2:
                score+=1

if priorhist == "Y":
    score+=1

if 18 <= age <=24:
    score+=1
elif age>=40:
    score=-1

print("The recidivism risk score is", score)
