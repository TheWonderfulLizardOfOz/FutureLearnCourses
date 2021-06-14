class Item():
    def __init__(self, item):
        self.item = item
        self.__description = None

    def get_item(self):
        return self.item

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    def describe(self):
        print(self.__description)
