class BankAccount:

    def __init__(self, client_id, client_first_name,
                 client_last_name):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = 0.0

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account_1 = BankAccount(1, 'John', 'Brown')
account_2 = BankAccount(2, 'Jim', 'White')

account_1.add(1000)
print(account_1.balance)
account_1.withdraw(500)
print(account_1.balance)
print(account_2.balance)
