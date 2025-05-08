print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print(bmi)
    if bmi < 18.5:
        bmi = -1
    elif bmi >= 18.5 and bmi <= 25.0:
        bmi = 0
    elif bmi > 25.0:
        bmi = 1
    return bmi
calculate_bmi(weight=80, height=1.76)