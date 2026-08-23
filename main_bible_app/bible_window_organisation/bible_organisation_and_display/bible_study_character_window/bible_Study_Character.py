
class Bible_Study_Characters:
    def __init__(self):
        super().__init__()
        #self.topic = topic

    characters_list= { "David": [],
                     "a": [],
                     "": [],}

    def show_characters(self)->list[str]:
        characters = []
        for character in self.characters_list:
            print(character)
            characters.append(character)
        return characters

print(Bible_Study_Characters().characters_list)
print(Bible_Study_Characters().show_characters())