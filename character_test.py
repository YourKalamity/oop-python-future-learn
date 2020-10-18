from character import Character, Enemy

dave = Enemy("Dave","A zombman")
dave.set_conversation("Ima eat dat ass")

dave.describe()
dave.talk()

dave.set_weakness("cheese")

print("What will you fight "+dave.get_name()+" with?")

fight_with = (((str(input())).lower()).capitalize())

if dave.fight(fight_with):
    print("You fight Dave off with the "+fight_with)
else:
    print("Dave eats your ass")

