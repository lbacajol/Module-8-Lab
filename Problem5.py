# Leslie Bacajol
# 11/20/21
# This program checks whether your game character has picked up all the items
# needed to perform certain tasks and checks against any status debuffs. Confirm checks with print statements.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self. weaknesses

    def profile(self):
        return self.nickname + ' ' + self.weapons + ' ' + self. weaknesses

    def check_equipment(self, taskL, state):
        missing_item = []
        for item in range(len(taskL)):
            if taskL[item] not in self.weapons:
                missing_item.append(taskL[item])
                print('{} is not ready'.format(taskL[item]))
        if len(missing_item) == 0:
            print('Confirmed all items are prepared')

        if state == self.weaknesses[0]:
            print("Player's status is {}, which is not allowed condition".format(state))
        else:
            print("Player is good condition.")


player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)


print("There are three tasks you can choose.")
print("1. Task1 - Climb a mountain")
print("2. Task2 - Cooke a meal")
print("3. Task3 - Write a book")
option = input("Please enter one of the following options(1-3):")

if option == '1':
    task = ['rope', 'coat', 'first aid kit']
    not_allowed_state = 'slow'

# option 2
if option == '2':
    task = ['pan', 'groceries']
    not_allowed_state = 'small'
# option 3
if option == '3':
    task = ['pen', 'paper', 'idea']
    not_allowed_state = 'confusion'

# call check_equipment and weakness
player1.check_equipment(task, not_allowed_state)
