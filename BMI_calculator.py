# BMI Calculator
# Beginner Tier - Python Command Line Program

print("===== BMI CALCULATOR =====")

while True:
    try:
        # Take weight input
        weight = float(input("Enter your weight in kg: "))

        # Take height input
        height = float(input("Enter your height in meters: "))

        # Validate input
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive values.")
            print("Please try again.\n")
            continue

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Classify BMI
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        print("\n===== RESULT =====")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

        break

    except ValueError:
        print("Error: Please enter numbers only.")
        print("Example: Weight = 60, Height = 1.65\n")
