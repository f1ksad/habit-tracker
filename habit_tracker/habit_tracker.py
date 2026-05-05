def habit_tracker():
    habits = {
        
    }

    print("=== Твой Трекер Привычек ===")

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показать мои привычки")
        print("2. Добавить новую привычку")
        print("3. Отметить привычку как выполненную")
        print("4. Сбросить все статусы (Новый день)")
        print("5. Выйти")

        choice = input("\nВыбери действие (1-5): ")

        if choice == "1":
            # 1. Показываем привычки
            if not habits:
                print("\nУ тебя пока нет привычек в списке.")
            else:
                print("\n=== ТВОИ ПРИВЫЧКИ ===")
                for index, (habit, done) in enumerate(habits.items(), 1):
                    # Если выполнено — рисуем галочку [V], если нет — пустые скобки [ ]
                    status = "[V]" if done else "[ ]"
                    print(f"{index}. {status} {habit}")
                print("=====================")

        elif choice == "2":
            # 2. Добавляем новую привычку
            new_habit = input("\nВведи название новой привычки: ").strip()
            if new_habit:
                if new_habit in habits:
                    print("Такая привычка уже есть в списке!")
                else:
                    habits[new_habit] = False
                    print(f"Привычка '{new_habit}' успешно добавлена!")
            else:
                print("Название не может быть пустым.")

        elif choice == "3":
            # 3. Отмечаем выполнение
            if not habits:
                print("\nСписок пуст, отмечать нечего.")
            else:
                print("\nКакую привычку ты выполнил сегодня?")
                # Превращаем ключи словаря в список, чтобы обращаться по номерам
                habit_list = list(habits.keys())
                
                for index, habit in enumerate(habit_list, 1):
                    status = "[V]" if habits[habit] else "[ ]"
                    print(f"{index}. {status} {habit}")
                
                try:
                    num = int(input("\nВведи номер выполненной привычки: "))
                    if 1 <= num <= len(habit_list):
                        selected_habit = habit_list[num - 1]
                        habits[selected_habit] = True  # Меняем статус на выполненный
                        print(f"Супер! Привычка '{selected_habit}' отмечена как выполненная!")
                    else:
                        print("Неверный номер.")
                except ValueError:
                    print("Пожалуйста, введи корректное число!")

        elif choice == "4":
            # 4. Сброс статусов (имитация нового дня)
            if not habits:
                print("\nСписок пуст.")
            else:
                for habit in habits:
                    habits[habit] = False
                print("\nВсе статусы сброшены! Удачи в новом дне!")

        elif choice == "5":
            print("\nПрограмма завершена. Удачи в достижении целей!")
            break
        else:
            print("Неверный выбор. Введи число от 1 до 5.")

# Запуск программы
habit_tracker()
     
