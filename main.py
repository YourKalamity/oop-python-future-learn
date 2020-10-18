from room import Room
from item import Item
from character import Character, Enemy

kitchen = Room("Kitchen")
kitchen.set_description("The room most commonly used to cook food")
ballroom = Room("Ballroom")
ballroom.set_description("A room used for ball- dancing")
dining_hall = Room("Dining Hall")
dining_hall.set_description("The place someone would normally would eat")

kitchen.link_room(dining_hall,"South")
dining_hall.link_room(kitchen,"North")
dining_hall.link_room(ballroom,"West")
ballroom.link_room(dining_hall,"East")

dave = Enemy("Saqib", "A zombman")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("penis")
dining_hall.set_character(dave)


current_room = kitchen
current_input = None

while current_input != "End":
    print("The room you are currently in is : "+current_room.get_name())
    print("Rooms you can move to :")
    for direction in current_room.linked_rooms:
        print(str(current_room.linked_rooms[direction].get_name())+" : "+direction)
    inhabitant = current_room.get_character()
    if inhabitant != None:
        inhabitant.describe()

    print("Enter a command")
    current_input = ((input()).lower()).capitalize()
    if current_input in ["North","West","South","East"]:
        if current_room.move(current_input) != None:
            current_room = current_room.move(current_input)
        else:
            print("That's not a valid input sonny boy")
    elif current_input == "Talk":
        if inhabitant != None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to")
    elif current_input == "Fight":
        if inhabitant != None:
            print("What will you fight "+inhabitant.get_name()+" with?")
            fight_with = (((str(input())).lower()).capitalize())
            if inhabitant.fight(fight_with):
                print("You fight "+inhabitant.get_name()+"  off with the "+fight_with)
                inhabitant = None
                current_room.set_character(None)
            else:
                print(inhabitant.get_name()+" ate your ass")
                exit()

        else:
            print("There is no one here to fight")
    else:
        print("That's not a valid input sonny boy")



