import random
import string
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("=== 🔥 COOL PASSWORD GENERATOR 🔥 ===\n")

# Выбор типов символов
include_upper = input("Include capital letters? (Not really): ").lower() == "да"
include_lower = input("Include lowercase letters? (Not really): ").lower() == "да"
include_digits = input("Include digits? (Not really): ").lower() == "да"
include_symbols = input("Include special symbols? (Not really): ").lower() == "да"

# Собираем символы
characters = ""
if include_lower:
    characters += string.ascii_lowercase
if include_upper:
    characters += string.ascii_uppercase
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

if not characters:
    print("Error! You must select at least one type of character.")
    input("\nPress Enter to exit...")
else:
    while True:
        clear_screen()
        print("=== 🔥 COOL PASSWORD GENERATOR 🔥 ===\n")
        
        # Ввод длины
        while True:
            try:
                length = int(input("Enter password length (from 4 to 70): "))
                if 4 <= length <= 70:
                    break
                else:
                    print("Password length must be between 4 and 70 characters!")
            except ValueError:
                print("Please enter a number!")

        # Генерация пароля
        password_list = []
        if include_upper:
            password_list.append(random.choice(string.ascii_uppercase))
        if include_lower:
            password_list.append(random.choice(string.ascii_lowercase))
        if include_digits:
            password_list.append(random.choice(string.digits))
        if include_symbols:
            password_list.append(random.choice(string.punctuation))

        remaining = length - len(password_list)
        for _ in range(remaining):
            password_list.append(random.choice(characters))

        random.shuffle(password_list)
        password = ''.join(password_list)

        print("\n" + "=" * 55)
        print("✅ Generated password:")
        print(f"   {password}")
        print("=" * 55)

        strength = "Very strong 🔥" if length >= 16 and include_symbols and include_upper else \
                   "Strong 👍" if length >= 12 else "Medium"
        print(f"Password strength: {strength}\n")

        again = input("Generate another password? (yes/no): ").lower()
        if again != "yes":
            print("\nGoodbye! 👋")
            break

# Это важно, чтобы окно не закрывалось сразу
print("\nProgram completed.")
input("Press Enter to exit...")