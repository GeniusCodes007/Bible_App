"""
FEATURES:

Books Buttons:
AutoExclusive - True
checkable - True
checked - False, but for Genesis - True

Chapter Frames:
setHidden - True
show: when book_button is toggled

"""
from PySide6.QtWidgets import QPushButton
from BibleHousingAndDisplay.chapter_buttons import *




class BibleEdit(ChapterButtons):
    def __init__(self):
        super().__init__()





        #Traditional Old Testament
        self.genesis.toggled.connect(self.genesis_button_function)
        self.exodus.toggled.connect(self.exodus_button_function)
        self.leviticus.toggled.connect(self.leviticus_button_function)
        self.numbers.toggled.connect(self.numbers_button_function)
        self.deuteronomy.toggled.connect(self.deuteronomy_button_function)
        self.joshua.toggled.connect(self.joshua_button_function)
        self.judges.toggled.connect(self.judges_button_function)
        self.ruth.toggled.connect(self.ruth_button_function)
        self.sam_1.toggled.connect(self.sam_1_button_function)
        self.sam_2.toggled.connect(self.sam_2_button_function)
        self.kings_1.toggled.connect(self.kings_1_button_function)
        self.kings_2.toggled.connect(self.kings_2_button_function)
        self.chronicles_1.toggled.connect(self.chronicles_1_button_function)
        self.chronicles_2.toggled.connect(self.chronicles_2_button_function)
        self.ezra.toggled.connect(self.ezra_button_function)
        self.nehemiah.toggled.connect(self.nehemiah_button_function)
        self.esther.toggled.connect(self.esther_button_function)
        self.job.toggled.connect(self.job_button_function)
        self.psalms.toggled.connect(self.psalms_button_function)
        self.proverbs.toggled.connect(self.proverbs_button_function)
        self.ecclesiastes.toggled.connect(self.ecclesiastes_button_function)
        self.song_of_songs_solomon.toggled.connect(self.song_of_songs_solomon_button_function)
        self.isaiah.toggled.connect(self.isaiah_button_function)
        self.jeremiah.toggled.connect(self.jeremiah_button_function)
        self.lamentations.toggled.connect(self.lamentations_button_function)
        self.ezekiel.toggled.connect(self.ezekiel_button_function)
        self.daniel.toggled.connect(self.daniel_button_function)
        self.hosea.toggled.connect(self.hosea_button_function)
        self.joel.toggled.connect(self.joel_button_function)
        self.amos.toggled.connect(self.amos_button_function)
        self.obadiah.toggled.connect(self.obadiah_button_function)
        self.jonah.toggled.connect(self.jonah_button_function)
        self.micah.toggled.connect(self.micah_button_function)
        self.nahum.toggled.connect(self.nahum_button_function)
        self.habakkuk.toggled.connect(self.habakkuk_button_function)
        self.zephaniah.toggled.connect(self.zephaniah_button_function)
        self.haggai.toggled.connect(self.haggai_button_function)
        self.zechariah.toggled.connect(self.zechariah_button_function)
        self.malachi.toggled.connect(self.malachi_button_function)

        #Deuterocanonical Books

