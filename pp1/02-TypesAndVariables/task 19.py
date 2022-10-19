height = int(input("Enter your height in cm: "))
weight = int(input("Enter your heigt in kg: "))
bmi = weight / height / height * 10000
round(bmi,2)
print(f"Your BMI:",round(bmi,2))