class Notification:
    notifications=[]
    def send(self,notification):
        self.notifications.append(notification)
        print("recieved a notification")
class Email(Notification):
    emails=[]
    def send(self,email):
        self.emails.append(email)
        print("recieved an email")
class SMS(Notification):
    messages=[]
    def send(self,message):
        self.messages.append(message)
        print("recieved a message")

s=SMS()
s.send("hi")