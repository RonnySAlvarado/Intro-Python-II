# Write a class to hold player information, e.g. what room they are in
# currently.

# player = Player('Ronny', room['outside'])  string and object
"""
class Room:
    def __init__(self, location, description):
        self.location_name = location_name
        self.description = description
        self.n_to = room['foyer']
        self.s_to = None 
        self.e_to = None 
        self.w_to = None

"""


class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def move_player(self, movement):
        if(getattr(self.currentRoom, f'{movement}_to') != None):
            self.currentRoom = getattr(self.currentRoom, f'{movement}_to')
        else:
            print('That move is not possible')

    def __str__(self):
        return f'{self.name} is in the {self.currentRoom}. \n {self.currentRoom.description}'
