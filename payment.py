class Payment:
    def __init__(self):
        print("payment class")
    def process_payment(self):
        print("payment class process payment")
class CreditCardPayment(Payment):
    def __init__(self):
        print("CreditCardPayment class")
    def process_payment(self):
        print("CreditCardPayment class process payment")
class PayPalPayment(Payment):           
    def __init__(self):
        print("PayPalPayment class")
    def process_payment(self):
        print("PayPalPayment class process payment")
class BitcoinPayment(Payment):
    def __init__(self):
        print("BitcoinPayment class")
    def process_payment(self):
        print("BitcoinPayment class process payment")

inp=input("enter the payment method")
if(inp=="bitcoin"):
    b=BitcoinPayment()
    b.process_payment()
if(inp=="creditacrd"):
    c=CreditCardPayment()
    c.process_payment()
if(inp=="paypal"):
    p=PayPalPayment()
    p.process_payment()
