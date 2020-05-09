from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance:\n",
                     """North of you, the cave mount beckons""", "\n\n"),

    'foyer':    Room("Foyer:", """Dim light filters in from the south. Dusty passages run north and east.""", "\n"),

    'overlook': Room("Grand Overlook:\n", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", "\n"),

    'narrow':   Room("Narrow Passage;\n", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", "\n"),

    'treasure': Room("Treasure Chamber\n", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "\n"),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
#  Prints the current room name
#  Prints the current description (the textwrap module might be useful here).
#  Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# This will allow mapping from player input into the linkage of rooms that has been established

direction_map = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to'
}


def main():
    # set the initial state of the player outside
    player_1 = Player("Richard", room["outside"])

    while True:
        print(f"You are currently in {player_1.current_room.name}")
        print(f"Description: {player_1.current_room.description}")
        print("""------------Choose Your Direction---------------
North: n | South: s | East:  e | West:  w | Quit: q
---------------------------------------------------
---------------------------------------------------
""".lower())
# logic to determine prompt that will occur when there are no items in the room or ther are items
        if len(player_1.current_room.items) <= 0:
            print("No items in room!")
        else:
            print("There may be an item here!")
            for items in player_1.current_room.items:
                print(items)
        user_input = input("Make your move: ")
        print("\n\n"*3)

        # Logic for user action and indicating where they are going
        if user_input in direction_map.keys():
            try:

                player_1.current_room = getattr(
                    player_1.current_room, direction_map[user_input])
            except AttributeError:
                print("-----------------------------------")
                print("There Is No Room In That Direction")
                print("-----------------------------------")
                print("\n\n")
        elif user_input == 'q':
            exit(0)


if __name__ == "__main__":
    main()
