class Logger:
    def __init__(self):
        print("logger class")

    def log(self, *args):
        if len(args) == 1:
            print("input message is error")
        elif len(args) == 2:
            print("it is warning")
        else:
            print("it is info")

obj = Logger()
obj.log("hi")              
obj.log("hi", 'hello')      
obj.log("hi", 'hello', 'yes')  
