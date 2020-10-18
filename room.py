

class Room():
    number_of_rooms = 0
    def __init__(self, room_name):
        number_of_rooms += 1
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
    def set_description(self, room_description):
        self.description = room_description
    def get_description(self):
        return self.description
    def get_name(self):
        return self.name
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    def get_details(self):
        rooms = [[],[]]
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            rooms[0].append(direction)
            rooms[1].append(room.get_name())
        return rooms
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            return None
    def get_character(self):
        return self.character
    def set_character(self,character):
        self.character = character
        



