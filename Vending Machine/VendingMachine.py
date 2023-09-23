from abc import ABC, abstractmethod

class VendingMachine(ABC):
    def __init__(self, products: dict, accepted_coins: list, balance: int):
        self.products = products
        self.accepted_coins = accepted_coins
        self.balance = balance

    @abstractmethod
    def insert_money(self, amount):
        pass

    @abstractmethod
    def select_product(self, product_name):
        pass

    @abstractmethod
    def cancel_request(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass
