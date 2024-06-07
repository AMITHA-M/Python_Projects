import datetime

class ATM:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transactions = []

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.datetime.now(), 'Withdrawal', amount))
            return True
        else:
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.datetime.now(), 'Deposit', amount))

    def transfer(self, amount, recipient_id):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.datetime.now(), f'Transfer to {recipient_id}', amount))
            return True
        else:
            return False

    def display_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(f"{transaction[0]} - {transaction[1]} - Amount: {transaction[2]}")

# Example usage
def main():
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")
    atm = ATM(user_id, pin)

    if not atm.check_pin(pin):
        print("Invalid PIN. Exiting.")
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Transactions History")
        print("6. Quit")
        choice = input("\nEnter choice: ")

        if choice == '1':
            print(f"Current Balance: {atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if atm.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Invalid amount or insufficient funds.")
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
            print("Deposit successful")
        elif choice == '4':
            amount = float(input("Enter amount to transfer: "))
            recipient_id = input("Enter recipient's user ID: ")
            if atm.transfer(amount, recipient_id):
                print("Transfer successful.")
            else:
                print("Invalid amount or insufficient funds.")
        elif choice == '5':
            atm.display_transactions()
        elif choice == '6':
            print("Exiting ATM.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
