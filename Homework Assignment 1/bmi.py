weight_in_pound = "w"
height_in_feet = "f"
heighet_in_inches = "i"

w = int(input("Enter weight: "))
f = int(input("Enter height in feet: "))
i = int(input("Enter height in inches: "))

height = (f * 12 + i)

bmi = w * 0.45359237 / ((height * 0.0254) * (height * 0.0254))
print("BMI is:", bmi)

if bmi < 18.50:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overwight")
else:
    print("Obese")



