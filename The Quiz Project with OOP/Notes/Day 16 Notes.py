class User:
    # def __init__(self):
    #     print("New user being created.....")
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
user_1 = User("001", "angela") 
# user_1.id = "001"
# user_1.username = "angela"

# print(user_1.id)
# print(user_1.followers)


# user_2 = User("002")
# user_2.id = "002"
# user_2.username = "Mark"

# print(user_2.username)

user_1 = User("001", "angela")
user_2 = User("002", "Mark")

user_1.follow(user_2) #user 1 follows user 2
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)