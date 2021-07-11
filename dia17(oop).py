"""Dia 17."""

class User:
    def __init__(self, user_id, username):
        print("Creando nuevo usuario...")
        self.user_id = user_id
        self.username = username
        self.seguidores = 0
        self.siguiendo = 0
        

    def seguir(self, user):
        user.seguidores += 1
        self.siguiendo += 1

        


user_1 = User('001', 'Violeta')
user_2 = User('002', 'Ivana')
# user_1.id = "001"
# user_1.username = "Violeta"
atts = [x for x in dir(user_1) if not x.startswith('__')]

user_1.seguir(user_2)

print(user_1.siguiendo)
print(user_2.seguidores)

# for att in user_1:
#     print(att)
