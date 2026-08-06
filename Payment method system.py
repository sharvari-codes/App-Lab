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
        print("\nPayment Successful!")
        print(f"Paid ₹{amount} using Credit Card.")
        print(f"Card Number: {self.card_number}")


# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print("\nPayment Successful!")
        print(f"Paid ₹{amount} using PayPal.")
        print(f"PayPal Account: {self.email}")


# Concrete Strategy 3
class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print("\nPayment Successful!")
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


# Main Program

processor = PaymentProcessor()

while True:

    print("\n===== Payment Processing System =====")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. UPI")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank You!")
        break

    amount = float(input("Enter Amount: ₹"))

    if choice == 1:
        card = input("Enter Credit Card Number: ")
        processor.set_payment_strategy(CreditCardPayment(card))

    elif choice == 2:
        email = input("Enter PayPal Email: ")
        processor.set_payment_strategy(PayPalPayment(email))

    elif choice == 3:
        upi = input("Enter UPI ID: ")
        processor.set_payment_strategy(UPIPayment(upi))

    else:
        print("Invalid Choice!")
        continue

    processor.process_payment(amount)


 
