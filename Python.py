print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print(bmi)
calculate_bmi(weight=80, height=1.76)