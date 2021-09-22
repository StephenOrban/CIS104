score = input("enter score: ")
score = float(score)
if score>0 and score<1:
    if score>.9:
        grade = "A"
    elif score>.8:
        grade = "B"
    elif score>.7:
        grade = "C"
    elif score>.6:
        grade = "D"
    else:
        grade = "F"
else:
    print("enter a number between 1 and 0")
    exit()
print(grade)
