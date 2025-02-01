class Electronics:
    def __init__(self):
        print("electronics class")
    def show(self):
        print("can have multiple types like tv,ipad,smartphone etc..,")
class MobileDevice(Electronics):
    def __init__(self,type):
        print("mobiledevice class")
        self.type=type
    def show(self):
        print(f"electronic type is {self.type}")
class SmartPhone(MobileDevice):
    def __init__(self,type,brand):
        super().__init__(type)
        self.brand=brand
    def show(self):
        super().show()
        print(f"mobiledevice type is {self.type}, brand is {self.brand}")

s=SmartPhone("smartphone","oppo")
s.show()