class Bank:

    def __init__(self):
        self.__balance = 1000

    def set_balance(self, amount):

        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")

    def get_balance(self):
        return self.__balance


b = Bank()

b.set_balance(-500)

print(b.get_balance())