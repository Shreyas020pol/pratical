print("========== Monthly Expense Tracker ==========")

food = 0.0
travel = 0.0
other = 0.0

while True:
    print("\nExpense Categories:")
    print("1. Food")
    print("2. Traveling")
    print("3. Other")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 4:
        break

    amount = float(input("Enter Expense Amount: "))

    if choice == 1:
        food = food + amount
    elif choice == 2:
        travel = travel + amount
    elif choice == 3:
        other = other + amount
    else:
        print("Invalid Choice!")

print("\n========== Monthly Expense Summary ==========")
print("Food Expenses      :", food)
print("Travel Expenses    :", travel)
print("Other Expenses     :", other)
print("--------------------------------------------")
print("Total Expenses     :", food + travel + other)