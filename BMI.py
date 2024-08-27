def get_user_input():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight > 0 and height > 0:
                return weight, height
            else:
                print("Weight and height must be positive numbers. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator")
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
