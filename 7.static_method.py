"""
    We know classmethod can modify class state since it can access class attribute.
    While instance method can modify both state.

    There is also static method which cannot access any attribute, they are merely a function just that they are under class.

    We use them like to define utility functions or group functions that have some logical relationship in a class.

    Suppose you have class say smartphone, and it has all the attrbiute, but if you want the price in various format or conversion. Then here we can use static methods, since currency conversion or format is independent of your class.
"""

class Smarthpone:
    def __init__(self, brand, model, price_usd):
        self.brand=brand
        self.model=model
        self.price_usd=price_usd

    def display(self):
        print(f"{self.brand} {self.model}: ${self.price_usd} USD")

    @staticmethod
    def convert_currrency(amount_usd, rate):
        return amount_usd*rate
    
phone = Smarthpone("Samsung", "S25", 1199)
phone.display()

price_in_inr= Smarthpone.convert_currrency(phone.price_usd, 83)
print(price_in_inr)