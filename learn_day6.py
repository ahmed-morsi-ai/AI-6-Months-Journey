class BankAccount:
    def __init__(self, owner, balance):
        if balance > 0:
            self.owner = owner
            self.balance = balance
        else:
            print("should be >0.")
            self.owner = owner
            self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} took {amount} successful deposit: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("يجب أن يكون مبلغ السحب أكبر من صفر.")
        elif amount > self.balance:
            print("فشل السحب: الرصيد غير كافٍ.")
        else:
            self.balance -= amount
            print(f"تم سحب {amount} جنيه.")
            print(f"الرصيد الحالي: {self.balance} جنيه")
            print(f"{self.owner} took {amount} successful withdraw : {self.balance}")

account = BankAccount("Morsi", 1000)

account.deposit(1000)
account.withdraw(300)
