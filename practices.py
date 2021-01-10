class Owners:

    def __init__(self, name, username, position, experience):
        self.name = name
        self.username = username
        self.position = position
        self.experience = experience

    def getUser(self):
        return self.name +  "@" + self.username

obj = Owners("Ahmet", "ahmet", "Jr Python Developer", "3")
print(obj.getUser())