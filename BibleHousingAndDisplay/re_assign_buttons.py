# Re-assign button values to suit purpose

import PySide6
from PySide6.QtWidgets import QMainWindow

#from BibleHousingAndDisplay.ui_Bible_ui import Ui_MainWindow

from BibleHousingAndDisplay.ui_Bible_ui import *

#from BibleRunFiles.bibleCompilation import *


class ReAssignButtons(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.spaced_books = ["1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles","Song of Songs",
                             "Esther (Greek)", "Wisdom of Solomon", "Letter of Jeremiah", "Song of the Three Young Men", "Bel and the Dragon", "1 Maccabees", "2 Maccabees",
                             "1 Corinthians", "2 Corinthians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "1 Peter", "2 Peter", "1 John", "2 John", "3 John"]
        # I assign the push buttons new values, based on the values in the 'wholeBible' variable in bibleCompilation.py
