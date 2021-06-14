class Room():
    number_of_rooms = 0
    def __init__(self, room_name):
        self.name = room_name
        self.__description = None
        self.linked_rooms = {}
        self.character = None
        Room.number_of_rooms += 1

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, room_description):
        self.__description = room_description

    def get_name(self):
        return self.name

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("----------------")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction + ".")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character
