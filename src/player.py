# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room: Room):
        self.name = name
        self.current_room = current_room
