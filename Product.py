class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def show_availability(self,quantity):
        if(quantity<=self.stock):
            print("available")
        else:
            print("not available")
p=Product("milk",20,50)
quantity=int(input("enter the required quantity"))
p.show_availability(quantity)