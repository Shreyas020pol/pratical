print("========== Monthly Expense Tracker ==========")

food = []
travel = []
other = []

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
        food.append(amount)
    elif choice == 2:
        travel.append(amount)
    elif choice == 3:
        other.append(amount)
    else:
        print("Invalid Choice!")

print("\n========== Monthly Expense Summary ==========")

# Food Expenses
print("\nFood Expenses:")
for i in range(len(food)):
    print("Expense", i + 1, ":", food[i])
print("Total Food Expense :", sum(food))

# Travel Expenses
print("\nTravel Expenses:")
for i in range(len(travel)):
    print("Expense", i + 1, ":", travel[i])
print("Total Travel Expense :", sum(travel))

# Other Expenses
print("\nOther Expenses:")
for i in range(len(other)):
    print("Expense", i + 1, ":", other[i])
print("Total Other Expense :", sum(other))

# Grand Total
grand_total = sum(food) + sum(travel) + sum(other)

print("\n--------------------------------------------")
print("Grand Total Expense :", grand_total)