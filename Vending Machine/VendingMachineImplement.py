from VendingMachine import VendingMachine
# from coin_change import coin_change

class VendingMachineImpl(VendingMachine):
    def __init__(self, products, accepted_coins, balance):
        super().__init__(products, accepted_coins, balance)

    
    def insert_money(self, amnt):
        if amnt in self.accepted_coins:
            self.balance += amnt
            print(f"Inserted {amnt} into the vending machine. Balance is {self.balance}")
        else:
            print(f"Invalid coin insertion of {amnt} cents. Please insert a valid one")


    def select_product(self, product_name):
        if product_name in self.products:
            price = self.products[product_name]
            if self.balance >= price:
                self.balance -= price
                print(f"Here is your {product_name}. Remaining change is {self.balance}")
            else:
                return "Insufficient balance. Please insert more money"
        else:
            return "Invalid product selection."
    

    def cancel_request(self):
        refund = self.balance
        self.balance = 0
        print(f"Request cancelled. Here is your refund of {refund} cents")

    
    def reset(self):
        self.balance = 0
    
