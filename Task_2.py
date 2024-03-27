# Your solution comes here
height = int(input("Enter your height (in metres): "))
mass = int(input("Enter your mass (in kg): "))

BMI = mass / height **2

if BMI < 18.5:
    print(f"Your body mass index is:{BMI}, that is underweight.")
elif BMI < 25:
    print(f"Your body mass index is:{BMI}, that is normal weight.")
else:
    print(f"Your body mass index is:{BMI}, that is overweight.")