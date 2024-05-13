class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
user_1 = User("001", "Caio")
user_2 = User("002", "João")

print(user_1.username) # Caio
print(user_2.username) # João