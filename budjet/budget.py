import json
import os

DATA_FILE = "budget_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"transactions": [], "balance": 0.0}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_transaction(data, amount, description):
    data["transactions"].append({"amount": amount, "description": description})
    data["balance"] += amount
    save_data(data)

def show_summary(data):
    print("\n--- Budget Summary ---")
    print(f"Current Balance: ${data['balance']:.2f}")
    print("Transactions:")
    for t in data["transactions"]:
        sign = "+" if t["amount"] >= 0 else "-"
        print(f"  {sign}${abs(t['amount']):.2f} - {t['description']}")
    print("----------------------\n")

def reset_data():
    return {"transactions": [], "balance": 0.0}

def main():
    data = load_data()
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Reset Data")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            desc = input("Enter description: ")
            add_transaction(data, amount, desc)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            desc = input("Enter description: ")
            add_transaction(data, -amount, desc)
        elif choice == "3":
            show_summary(data)
        elif choice == "4":
            confirm = input("Are you sure you want to reset all data? (yes/no): ")
            if confirm.lower() == "yes":
                data = reset_data()
                save_data(data)
                print(" Data has been reset.")
            else:
                print(" Reset cancelled.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
