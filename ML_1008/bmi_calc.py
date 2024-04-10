#
# BMI Calculator 
# Regina 
# 

while True:
    # 1. Input
    weight = float(input("Enter your weight in kilograms : "))
    height = float(input("Enter your height in meters    : "))

    #2. Process
    bmi = weight/(height**2)
    print(f"Your BMI is: {bmi}")

    #3. Output
    opt = input("Continue? (yes/no): ")
    if opt == "yes":
        continue
    elif opt == "no":
        break
    else:
        print("Wrong input, stopping the program")
        break
