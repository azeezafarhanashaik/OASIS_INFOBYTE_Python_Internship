import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Define the character sets based on user preferences
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters  # Adds lowercase and uppercase letters
    if use_numbers:
        character_set += string.digits  # Adds digits 0-9
    if use_symbols:
        character_set += string.punctuation  # Adds special characters (!, @, #, etc.)

    # Ensure there's at least one type of character chosen
    if not character_set:
        print("You must select at least one character type (letters, numbers, or symbols).")
        return ""

    # Generate the password by randomly choosing from the character set
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def get_user_input():
    # Get password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                break
            else:
                print("Password length must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get character set preferences from the user
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    return length, use_letters, use_numbers, use_symbols

def main():
    print("Welcome to the Password Generator!")
    length, use_letters, use_numbers, use_symbols = get_user_input()
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
