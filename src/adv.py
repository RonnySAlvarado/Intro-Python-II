from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! What is that I see?"""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Linking my newly created items into their correct rooms :)

room['outside'].items = [Item(
    'knife', 'A dull knife. Probably not very useful...')]
room['foyer'].items = [Item(
    'longsword', 'A longsword. It is a bit rusted, but it will do.')]
room['narrow'].items = [Item(
    'coin', 'A few coins, looks like someone has been here before...I wonder where this leads?')]
room['treasure'].items = [Item(
    'treasure', 'There must be a lot of gold in here!')]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newplayer = Player('Ronny', room['outside'])
completion = False


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while completion == False:
    print(f'\n\n{newplayer.name} is now in the {newplayer.currentRoom.location}. {newplayer.currentRoom.description}\n')
    if(len(newplayer.currentRoom.items) > 0):
        print(
            f'The following items are observed in this room: {[item.name for item in newplayer.currentRoom.items]}\n')
    else:
        print('There are no items left in this room.\n')
    movement = input(
        f"What would you like to do? \nN(n), E(e), S(s), W(w) to move \nType 'get' and the name of the item to add the item to player inventory.\nI(i) to view your inventory.\nType 'remove' and the name of the item to remove the item from the player inventory.\nPress Q(q) to exit.\n\n")
    result = movement.split(' ')
    if result[0] == 'get':
        for item in newplayer.currentRoom.items:
            if(item.name == result[1]):
                newplayer.get_item(item)
                newplayer.currentRoom.items.remove(item)
                for x in newplayer.items:
                    if(x.name == 'treasure'):
                        print('\n\n\nCongratulations! You got the treasure! You win!')
                        completion = True
            else:
                print('\n\n\nThat item is not in this room.')
    elif result[0] == 'drop':
        for item in newplayer.items:
            if(item.name == result[1]):
                newplayer.drop_item(item)
            else:
                print(f'You do not have a {result[1]} to drop in here.')
    elif movement.lower() == 'q':
        completion = True
        print('Thanks for playing.')
    elif movement.lower() == 'n' or movement.lower() == 'e' or movement.lower() == 's' or movement.lower() == 'w':
        newplayer.move_player(movement)
    elif movement.lower() == 'i':
        print(
            f'\nThe items in your inventory are as followed: {[item.name for item in newplayer.items]} \n')
    else:
        print('Please choose a valid movement or action.')
