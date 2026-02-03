class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self.balance


B, W = map(int, input().split())

acc = Account(B)
result = acc.withdraw(W)

print(result)