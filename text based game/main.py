from room import Room
from item import Item
from character import Enemy, Character, Friend
from rpginfo import RPGInfo

inventory = []
result = True
game_won = False
directions = ["north", "east", "south", "west"]

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_room = Room("Dining room")

kitchen.description = "The room with an oven, knives and stuff."
ballroom.description = "That fancy ass room posh people have."
dining_room.description = "The room where people eat."

kitchen.link_room(dining_room, "south")
dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")
ballroom.link_room(dining_room, "east")

current_room = kitchen

cheese = Item("cheese")
cheese.description = "A slice of cheese with holes."

pencil = Item("pencil")
pencil.description = "A HB number 2 pencil."

sword = Item("sword")
sword.description = "A rusty sword."

cat = Friend("Spot", "Data's cat")
cat.set_conversation("Meow")
cat.set_steal(cheese)

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Rarrr...")
dave.weakness = cheese
dave.set_steal(pencil)

human = Character("Bob", "An ordinary human")
human.set_conversation("Psst.. did you know Dave is weak to: " + dave.weakness.get_item())
human.set_steal(sword)

dining_room.set_character(human)
ballroom.set_character(dave)
kitchen.set_character(cat)

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

while True:
    print("\n")
    current_room.get_details()
    room_name = current_room.get_name()
    description = current_room.description
    print(room_name+ ": " + description)
    inhabitant = current_room.get_character()
    
    if inhabitant is not None:
        inhabitant.describe()
        
    print("What will you do")
    user = input(">")
    user = user.lower()
    user = user.strip()
        
    if user == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here")
            
    elif user == "fight":
        if inhabitant is not None:
            print("What will you fight with.")
            weapon = input(">")
            weap_in_inven = False
            for item in inventory:
                if weapon == item.get_item():
                    result = inhabitant.fight(item, item.get_item())
                    weap_in_inven = True
                    if result == True:
                        game_won = True
            if weap_in_inven == False:
                print("You do not have a " + weapon)
        else:
            print("You punch the air.")
            
    elif user == "hug" and inhabitant is not None:
        inhabitant.hug()
        
    elif user in directions:
        current_room = current_room.move(user)
        
    elif user == "steal" and inhabitant is not None:
        stolen_item = inhabitant.steal()
        if stolen_item is not None:
            print("You steal " + stolen_item.get_item() + ".")
            inventory.append(stolen_item)

    elif user == "inventory":
        for i in range(len(inventory)):
            print(inventory[i].get_item())
            
    else:
        print("You can't do that.")

    if result == False:
        print("Game over :(")
        break
    elif game_won == True:
        print("You win!")
        break

RPGInfo.author = "Me"
RPGInfo.credits()
