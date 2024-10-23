class MobileBanking:
    def __init__(self):
        self.accounts = {}

    def deposit(self):
        account_number = input("Enter your account number: ")
        amount = float(input("Enter the amount to deposit: "))
        if account_number not in self.accounts:
            pin = input("Set a 4-digit PIN for your account: ")
            self.accounts[account_number] = {'balance': 0, 'pin': pin}
        self.accounts[account_number]['balance'] += amount
        print(f"Deposited {amount} to {account_number}. New balance: {self.accounts[account_number]['balance']}")

    def withdraw(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        amount = float(input("Enter the amount to withdraw: "))
        if self.authenticate(account_number, pin):
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(
                    f"Withdrew {amount} from {account_number}. New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance!")
        else:
            print("Authentication failed!")

    def transfer(self):
        sender_account = input("Enter your account number: ")
        sender_pin = input("Enter your PIN: ")
        receiver_account = input("Enter the receiver's account number: ")
        amount = float(input("Enter the amount to transfer: "))
        if self.authenticate(sender_account, sender_pin):
            if receiver_account not in self.accounts:
                pin = input("Set a 4-digit PIN for the receiver account: ")
                self.accounts[receiver_account] = {'balance': 0, 'pin': pin}
            if self.accounts[sender_account]['balance'] >= amount:
                self.accounts[sender_account]['balance'] -= amount
                self.accounts[receiver_account]['balance'] += amount
                print(f"Transferred {amount} from {sender_account} to {receiver_account}")
            else:
                print("Insufficient balance!")
        else:
            print("Authentication failed!")

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        if self.authenticate(account_number, pin):
            print(f"Account {account_number} balance: {self.accounts[account_number]['balance']}")
        else:
            print("Authentication failed!")

    def pay_bill(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        bill_amount = float(input("Enter the bill amount: "))
        if self.authenticate(account_number, pin):
            if self.accounts[account_number]['balance'] >= bill_amount:
                self.accounts[account_number]['balance'] -= bill_amount
                print(f"Paid bill of {bill_amount}. New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance to pay bill!")
        else:
            print("Authentication failed!")

    def mobile_recharge(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        recharge_amount = float(input("Enter the recharge amount: "))
        mobile_number = input("Enter the mobile number to recharge: ")
        if self.authenticate(account_number, pin):
            if self.accounts[account_number]['balance'] >= recharge_amount:
                self.accounts[account_number]['balance'] -= recharge_amount
                print(
                    f"Recharged {mobile_number} with {recharge_amount}. New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance for mobile recharge!")
        else:
            print("Authentication failed!")

    def payment(self):
        sender_account = input("Enter your account number: ")
        sender_pin = input("Enter your PIN: ")
        merchant_account = input("Enter the merchant's account number: ")
        amount = float(input("Enter the payment amount: "))
        if self.authenticate(sender_account, sender_pin):
            if merchant_account not in self.accounts:
                pin = input("Set a 4-digit PIN for the merchant account: ")
                self.accounts[merchant_account] = {'balance': 0, 'pin': pin}
            if self.accounts[sender_account]['balance'] >= amount:
                self.accounts[sender_account]['balance'] -= amount
                self.accounts[merchant_account]['balance'] += amount
                print(
                    f"Paid {amount} to merchant {merchant_account}. New balance: {self.accounts[sender_account]['balance']}")
            else:
                print("Insufficient balance!")
        else:
            print("Authentication failed!")

    def change_pin(self):
        account_number = input("Enter your account number: ")
        old_pin = input("Enter your old PIN: ")
        new_pin = input("Enter your new PIN: ")
        if self.authenticate(account_number, old_pin):
            self.accounts[account_number]['pin'] = new_pin
            print(f"PIN changed successfully for {account_number}")
        else:
            print("Incorrect old PIN!")

    def authenticate(self, account_number, pin):
        return self.accounts.get(account_number, {}).get('pin') == pin


def main():
    banking = MobileBanking()

    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. Check Balance")
        print("5. Pay Bill")
        print("6. Mobile Recharge")
        print("7. Make Payment")
        print("8. Change PIN")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            banking.deposit()
        elif choice == '2':
            banking.withdraw()
        elif choice == '3':
            banking.transfer()
        elif choice == '4':
            banking.check_balance()
        elif choice == '5':
            banking.pay_bill()
        elif choice == '6':
            banking.mobile_recharge()
        elif choice == '7':
            banking.payment()
        elif choice == '8':
            banking.change_pin()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
