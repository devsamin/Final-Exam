
class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.accounts = []
    
    def create_account(self, name, email, address, account_type):
        new_account = BankAccount( name, email, address, account_type)
        self.accounts.append(new_account)
        print(f"AC _num {new_account.account_number} Account create successfully !")
    
    def find_account(self, account_number):
        for ac in self.accounts:
            if ac.account_number == account_number:
                return ac
        return None
    
    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"{account_number} is not fouund")
    
    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"{account_number} is not fouund")

    def check_transction_history(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.ac_transaction_history()
        else:
            print(f"{account_number} is not fouund")
    
    def check_avilable_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.check_balance()
        else:
            print(f"{account_number} is not fouund")
    
    def take_loan(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.take_a_loan(amount)
        else:
            print(f"{account_number} is not fouund")
    
    def transfer_money(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"{amount}tk transfered from {from_account_number} to {to_account_number}")
            else:
                print("The bank is bankrupt. you cannot transfer money")
        else:
            print("one or both account found.")


class Admin(User):
    def __init__(self, user_name):
        super().__init__(user_name)
        self.users = []
        self.is_loan_enable = True
    
    def add_user(self, user):
        self.users.append((user))
        print(f"user name {user.user_name} user added successfully")

    def see_al_user_list(self):
        for user in self.users:
            for account in user.accounts:
                print(f"User name {user.user_name} her name {account.name} account number {account.account_number}")

    def find_account(self, account_number):
        for user in self.users:
            for ac in user.accounts:
                if ac.account_number == account_number:
                    return ac
        return None
    
    def remove_account(self, account_number):
        for user in self.users:
            account = user.find_account(account_number)
            if account:
                user.accounts.remove(account)
                print(f"Account {account_number} removed successfully")
                return
        print("Account is not found")

    def check_total_balance(self):
        total_balance = sum(account.balance for user in self.users for account in user.accounts)
        print(f"total avilable balance in the bank {total_balance}")
    
    def check_total_loan(self):
        total_loan_amount = sum(account.total_loan for user in self.users for account in user.accounts)
        print(f"total avilable balance in the bank {total_loan_amount}")
    
    def is_loan_feature_enable(self):
        self.is_loan_enable = True
        print("Loan feature has been enable")
    
    def is_loan_feature_disable(self):
        self.is_loan_enable = False
        print("Loan feature has been disable")
    
    def is_loan_feature_enabled(self):
        return self.is_loan_enable
    

class BankAccount:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generated_account_number()
        self.transaction_history = []
        self.loan_count = 0
        self.loan_limit = 2
        self.total_loan = 0

    def generated_account_number(self):
        import random
        return str(random.randint(10000,99999))
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit amount : {amount}")
            print(f"Deposited amount : {amount} and new balance {self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Withdraw amount execeeded")
        elif amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw amount : {amount}")
            print(f"withdraw amount : {amount} and new balance {self.balance}")
        else:
            print("withdraw amount must be positive")
    
    def ac_transaction_history(self):
        for transction in self.transaction_history:
            print(transction)

    def check_balance(self):
        print(f"Availavle balanc : {self.balance}")

    def take_a_loan(self, amount):
        if admin.is_loan_feature_enabled():
            if self.loan_count < self.loan_limit:
                self.balance += amount
                self.total_loan += amount
                self.loan_count +=1
                self.transaction_history.append(f"Take loan : {amount}")
                print(f"Loan {amount} new balance {self.balance}")
            else:
                print("Loan limit exceeded. You cannot take more loans")
        else:
            print("Loan feature is currently disable")

    

admin = Admin("Admin1")

user1 = User("user1")
user2 = User("user2")

admin.add_user(user1)
admin.add_user(user2)

def user_menu(user):
    while True:
        print("\tUser Menu\n")
        print("1. Create Accouunt")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Transaction History")
        print("5. Check Avilable Balance")
        print("6. Take Loan")
        print("7. Transfer Money")
        print("8. Exit")

        option = int(input("Enter Option : "))
        if option == 1:
            name = input("Enter name : ")
            email = input("Enter email : ")
            address = input("Enter address : ")
            account_type = input("Enter account type (Savings/Cuurent) : ")
            user.create_account(name, email, address, account_type)
        elif option == 2:
            account_number = input("Enter account number : ")
            amount = int(input("Enter amount : "))
            user.deposit(account_number, amount)
        elif option == 3:
            account_number = input("Enter account number : ")
            amount = int(input("Enter amount : "))
            user.withdraw(account_number, amount)
        elif option == 4:
            account_number = input("Enter account number : ")
            user.check_transction_history(account_number)
        elif option == 5:
            account_number = input("Enter account number : ")
            user.check_avilable_balance(account_number)
        elif option == 6:
            account_number = input("Enter account number : ")
            amount = int(input("Enter amount : "))
            user.take_loan(account_number, amount)
        elif option == 7:
            from_account_number = input("Enter from account num : ")
            to_account_number = input("Enter to account num : ")
            amount = int(input("Enter amount : "))
            user.transfer_money(from_account_number, to_account_number,amount)
        elif option == 8:
            break
        else:
            print("Invalid choice. please try agin.")

def admin_menu(admin):
    while True:
        print("\tAdmin Menu\n")
        print("1. Add users")
        print("2. See all user account")
        print("3. Delete any user account")
        print("4. Check total balance of the bank")
        print("5. Check total loan of the bank")
        print("6. Enable loan Feature")
        print("7. Disable loan Feature")
        print("8. Exit")

        option = int(input("Enter option : "))
        if option == 1:
            user_name = input("Enter name : ")
            new_user = User(user_name)
            admin.add_user(new_user)
        elif option == 2:
            admin.see_al_user_list()
        elif option == 3:
            account_number = input("Enter account num : ")
            admin.remove_account(account_number)
        elif option == 4:
            admin.check_total_balance()
        elif option == 5:
            admin.check_total_loan()
        elif option == 6:
            admin.is_loan_feature_enable()
        elif option == 7:
            admin.is_loan_feature_disable()
        elif option == 8:
            break
        else:
            print("Invalid option. please try agin.")


while True:
    print("\tMain Menu\n")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    Choice = int(input("Enter choice : "))
    if Choice == 1:
        admin_menu(admin)
    elif Choice == 2:
        user_name = input("Enter name : ")
        if user_name == "user1":
            user_menu(user1)
        elif user_name == "user2":
            user_menu(user2)
        else:
            print("User not found")
    elif Choice == 3:
        break
    else:
        print("Invalid choice. please try agin.")


