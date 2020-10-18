class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    def get_name(self):
        return self.name
    
    def set_name(self, char_name):
        self.name = char_name

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self,char_name,char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    def get_weakness(self):
        return self.weakness
    def set_weakness(self, weakness):
        self.weakness = ((str(weakness).lower()).capitalize())
    def fight(self, combat_item):
        if ((str(combat_item).lower()).capitalize()) == self.weakness:
            return True
        else:
            return False