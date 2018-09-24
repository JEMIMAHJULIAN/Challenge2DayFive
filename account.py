class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = True

    def open(self):
        self.status = True

    def get_balance(self):

        if self.status == False:
            raise ValueError('account closed')

        return self.balance

    def deposit(self, amount):
        if self.status == False:
            raise ValueError('account closed')

        if amount < 0:
            raise ValueError('wrong value')

        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:
            raise ValueError('insufficient balance')

        if amount < 0:
            raise ValueError('wrong entry')

        self.balance -= amount

    def close(self):
        self.status = False