from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")
        print(f"Card Number: {self.card_number}")


# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")
        print(f"PayPal Account: {self.email}")


# Concrete Strategy 3
class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")
        print(f"UPI ID: {self.upi_id}")


# Context Class
class PaymentProcessor:

    def __init__(self):
        self.payment_strategy = None

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def process_payment(self, amount):
        if self.payment_strategy is None:
            print("No payment method selected!")
        else:
            self.payment_strategy.pay(amount)


# Driver Code
if __name__ == "__main__":

    processor = PaymentProcessor()

    # Credit Card Payment
    processor.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456"))
    processor.process_payment(2500)

    print()

    # PayPal Payment
    processor.set_payment_strategy(PayPalPayment("user@example.com"))
    processor.process_payment(1800)

    print()

    # UPI Payment
    processor.set_payment_strategy(UPIPayment("john@upi"))
    processor.process_payment(750)