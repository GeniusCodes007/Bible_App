from Bible_Content.theNewJerusalemBible import Genesis

class Concerning(Genesis):
    def __init__(self, topic):
        super().__init__()
        self.topic = topic

    concerningList= {1: "Wisdom",
                     2: "Enlightenment",
                     3: ""}

class BibleReferences:
    versesWisdomEnlightenmentUnderstanding = {1: f"Genesis 1 vs. 3 : {Genesis.chapterOne[3]}"}

    def __init__(self):
        super().__init__()

    def getWisdomEnlightenmentUnderstanding(self):
        for a in self.versesWisdomEnlightenmentUnderstanding.values():
            print(a)
        return ""


print(BibleReferences().getWisdomEnlightenmentUnderstanding())