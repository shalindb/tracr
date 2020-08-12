
class Tracr_User:
    def __init__(self, user_id: int, password: str):
        self.user_id = user_id
        self.password = password
        self.interactions = []
        self.name = 'User'

def interact(users: list, date: str):
    users[0].interactions.append(tuple([users[1].user_id, date]))
    users[1].interactions.append(tuple([users[0].user_id, date]))

def main():

# Run this file for DEBUGGING purposes only

    shalin = Tracr_User(123, 'Pop')
    shalin.name = 'Shalin Brahmbhatt'

    bob = Tracr_User(333, 'Lop')
    bob.name = 'Bob Bob'

    john = Tracr_User(645, 'Loasd')
    bob.name = 'John W'

    print(shalin.interactions)
    print(bob.interactions)

    interact([shalin, bob], 'August 10')

    interact([john, shalin], 'August 11')

if __name__ == '__main__':
    main()