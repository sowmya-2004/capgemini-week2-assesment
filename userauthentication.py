from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self,username):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username):
        return f"{username} logged in via Google"

    def logout(self,username):
        return f"{username} Logged out from Google"

class FacebookAuth(UserAuthentication):
    def login(self, username):
        return f"{username} logged in via Facebook"

    def logout(self,username):
        return f"{username} Logged out from Facebook"

google = GoogleAuth()
facebook = FacebookAuth()

print(google.login("A"))
print(google.logout("A"))

print(facebook.login("B"))
print(facebook.logout("B"))
