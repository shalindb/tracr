
import random
class Tracr_User:

    login_info = {}
    def __init__(self, user_id: int, password: str, covid=False):
        self.user_id = user_id
        self.password = password
        self.interactions = []
        self.name = 'User'
        self.covid = covid
        Tracr_User.login_info[self.user_id] = self.password

def interact(users: list, date: str):
    # appends: user_id, date, # seconds, # feet, covid STATUS

    users[0].interactions.append(tuple([users[1].user_id, date, round(random.uniform(2, 100), 2), round(random.uniform(0, 6), 2), users[1].covid]))
    users[1].interactions.append(tuple([users[0].user_id, date, round(random.uniform(2, 100), 2), round(random.uniform(0, 6), 2), users[0].covid]))

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

    print(shalin.login_info[123])
    print(round(random.uniform(0, 30), 2))


if __name__ == '__main__':
    main()