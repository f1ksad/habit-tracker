import random
import string
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("=== 🔥 КРУТОЙ ГЕНЕРАТОР ПАРОЛЕЙ 🔥 ===\n")

# Выбор типов символов
include_upper = input("Включить заглавные буквы? (да/нет): ").lower() == "да"
include_lower = input("Включить строчные буквы? (да/нет): ").lower() == "да"
include_digits = input("Включить цифры? (да/нет): ").lower() == "да"
include_symbols = input("Включить специальные символы? (да/нет): ").lower() == "да"

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
    print("Ошибка! Нужно выбрать хотя бы один тип символов.")
    input("\nНажмите Enter для выхода...")
else:
    while True:
        clear_screen()
        print("=== 🔥 КРУТОЙ ГЕНЕРАТОР ПАРОЛЕЙ 🔥 ===\n")
        
        # Ввод длины
        while True:
            try:
                length = int(input("Введите длину пароля (от 4 до 70): "))
                if 4 <= length <= 70:
                    break
                else:
                    print("Длина пароля должна быть от 4 до 70 символов!")
            except ValueError:
                print("Пожалуйста, введите число!")

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
        print("✅ Сгенерированный пароль:")
        print(f"   {password}")
        print("=" * 55)

        strength = "Очень сильный 🔥" if length >= 16 and include_symbols and include_upper else \
                   "Сильный 👍" if length >= 12 else "Средний"
        print(f"Сила пароля: {strength}\n")

        again = input("Сгенерировать ещё один пароль? (да/нет): ").lower()
        if again != "да":
            print("\nДо свидания! 👋")
            break

# Это важно, чтобы окно не закрывалось сразу
print("\nПрограмма завершена.")
input("Нажмите Enter для выхода...")