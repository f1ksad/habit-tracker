def habit_tracker():
    habits = {
        
    }

    print("=== cool habit tracker ===")

    while True:
        print("\n--- MENU ---")
        print("1. Show my habits")
        print("2. Add a new habit")
        print("3. Mark a habit as completed")
        print("4. Reset all statuses (New day)")
        print("5. Exit")

        choice = input("\nChoose an action (1-5): ")

        if choice == "1":
            # 1. Show my habits
            if not habits:
                print("\nYou don't have any habits in the list yet.")
            else:
                print("\n=== YOUR HABITS ===")
                for index, (habit, done) in enumerate(habits.items(), 1):
                    # If completed — draw a checkmark [V], if not — empty brackets [ ]
                    status = "[V]" if done else "[ ]"
                    print(f"{index}. {status} {habit}")
                print("=====================")

        elif choice == "2":
            # 2. Add a new habit
            new_habit = input("\nEnter the name of the new habit: ").strip()
            if new_habit:
                if new_habit in habits:
                    print("That habit is already in the list!")
                else:
                    habits[new_habit] = False
                    print(f"Habit '{new_habit}' added successfully!")
            else:
                print("Habit name cannot be empty.")

        elif choice == "3":
            # 3. Mark a habit as completed
            if not habits:
                print("\nThe list is empty, nothing to mark.")

            else:
                print("\nWhich habit did you complete today?")
                # Convert dictionary keys to a list to access by index
                habit_list = list(habits.keys())
                
                for index, habit in enumerate(habit_list, 1):
                    status = "[V]" if habits[habit] else "[ ]"
                    print(f"{index}. {status} {habit}")
                
                try:
                    num = int(input("\nEnter the number of the completed habit: "))
                    if 1 <= num <= len(habit_list):
                        selected_habit = habit_list[num - 1]
                        habits[selected_habit] = True  # Меняем статус на выполненный
                        print(f"Habit '{selected_habit}' marked as completed!")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "4":
            # 4. Сброс статусов (имитация нового дня)
            if not habits:
                print("\nThe list is empty.")
            else:
                for habit in habits:
                    habits[habit] = False
                print("\nAll statuses reset! Good luck with your new day!")

        elif choice == "5":
            print("\nProgram completed. Good luck with your goals!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Запуск программы
habit_tracker()