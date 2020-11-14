print("    BMI CALCULATOR    ")

weight = float(input("ENTER YOUR WEIGHT(KG): "))
height = float(input("ENTER YOUR HEIGHT(M): "))

BMI = weight / (height * height)

print(f"Your Body Mass Index is: {BMI:.2f}")