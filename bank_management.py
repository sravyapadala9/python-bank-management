# Bank Management System

balance = 5000

while True:
    print("\n===== Bank Management System =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print("Deposit Successful!")
        print("Updated Balance: ₹", balance)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")