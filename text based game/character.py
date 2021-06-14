class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.stealable_item = None

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def hug(self):
        print("You are not friends with " + self.name + ".")
    
    def steal(self):
        if self.stealable_item is not None:
            self.stolen_item = self.stealable_item
            self.stealable_item = None
            return self.stolen_item
        else:
            print("There is nothing to steal.")
            return None
        
    def set_steal(self, stealable_item):
        self.stealable_item = stealable_item

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.__weakness = None

    def fight(self, combat_item, item_name):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + item_name + ".")
            return True
        else:
            print(self.name + " crushes you, puny adventurer.")
            return False

    @property
    def weakness(self):
        return self.__weakness

    @weakness.setter
    def weakness(self, weakness):
        self.__weakness = weakness


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print("You and " + self.name + " have a long hug.")
