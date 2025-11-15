# Create and edit the buttons for displaying the books buttons
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton
from re_assign_buttons import *

#chaptersNumberGridLayout
class BooksButtons(ReAssignButtons):

    # This is a base function, with which the books buttons can be able to display the number of chapters they have
    def button_function(self, book_name:str, book_chapters_number:int):
        chapters = book_chapters_number

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.findChild(QPushButton, book_name).objectName())

        book = self.book_name_label.text()

        self.gn_book_label.setText(book)
        self.amp_book_label.setText(book)
        self.kjv_book_label.setText(book)
        self.njb_book_label.setText(book)

        for x in range(count):
            b = self.chapterNumberScrollArea.findChild(QPushButton, f"chap_but_{x + 1}")
            b.setFont(self.font1)
            if x < chapters:
                b.setEnabled(True)
                b.show()
            else:
                b.setEnabled(False)
                b.hide()
        self.chaptersNumberFrame.show()

    def __init__(self):
        super().__init__()

        self.font1 = QFont()
        self.font1.setPointSize(10)
        self.font1.setBold(True)


    # Creating the button functions for each book

    # Old Testament Books
    def genesis_function(self): self.button_function("Genesis", 50)

    def exodus_function(self): self.button_function("Exodus", 40)

    def leviticus_function(self): self.button_function("Leviticus", 27)

    def numbers_function(self):  self.button_function("Numbers", 36)

    def deuteronomy_function(self):  self.button_function("Deuteronomy", 34)

    def joshua_function(self):  self.button_function("Joshua", 24)

    def judges_function(self):  self.button_function("Judges", 21)

    def ruth_function(self):  self.button_function("Ruth", 4)

    def _1_sam_function(self):  self.button_function("1 Samuel", 31)

    def _2_sam_function(self):  self.button_function("2 Samuel", 24)

    def _1_kings_function(self):  self.button_function("1 Kings", 22)

    def _2_kings_function(self):  self.button_function("2 Kings", 25)

    def _1_chronicles_function(self):  self.button_function("1 Chronicles", 29)

    def _2_chronicles_function(self):  self.button_function("2 Chronicles", 36)

    def ezra_function(self):  self.button_function("Ezra", 10)

    def nehemiah_function(self):  self.button_function("Nehemiah", 13)

    def esther_function(self):  self.button_function("Esther", 10)

    def job_function(self):  self.button_function("Job", 42)

    def psalms_function(self):  self.button_function("Psalms", 150)

    def proverbs_function(self):  self.button_function("Proverbs", 31)

    def ecclesiastes_function(self):  self.button_function("Ecclesiastes", 12)

    def song_of_songs_solomon_function(self): self.button_function("Song of Songs", 8)

    def isaiah_function(self): self.button_function("Isaiah", 66)

    def jeremiah_function(self): self.button_function("Jeremiah", 52)

    def lamentations_function(self): self.button_function("Lamentations", 5)

    def ezekiel_function(self): self.button_function("Ezekiel", 48)

    def daniel_function(self): self.button_function("Daniel", 12)

    def hosea_function(self): self.button_function("Hosea", 14)

    def joel_function(self): self.button_function("Joel", 3)

    def amos_function(self): self.button_function("Amos", 9)

    def obadiah_function(self): self.button_function("Obadiah", 1)

    def jonah_function(self): self.button_function("Jonah", 4)

    def micah_function(self): self.button_function("Micah", 7)

    def nahum_function(self): self.button_function("Nahum", 3)

    def habakkuk_function(self): self.button_function("Habakkuk", 3)

    def zephaniah_function(self): self.button_function("Zephaniah", 3)

    def haggai_function(self): self.button_function("Haggai", 2)

    def zechariah_function(self): self.button_function("Zechariah", 14)

    def malachi_function(self): self.button_function("Malachi", 4)

    # Deuterocanonical Books
    #1
    def tobit_function(self): self.button_function("Tobit", 14)

    #2
    def judith_function(self): self.button_function("Judith", 16)

    #3
    def esther_greek_function(self): self.button_function("Esther(Greek)", 16)

    #4
    def wisdom_of_solomon_function(self): self.button_function("Wisdom of Solomon", 19)

    #5
    def sirach_function(self): self.button_function("Sirach", 51)

    #6
    def baruch_function(self): self.button_function("Baruch", 6)

    #7
    def letter_of_jeremiah_function(self): self.button_function("Letter of Jeremiah", 1)

    #8
    def song_of_the_three_young_men_function(self): self.button_function("Song of the Three Young Men", 1)

    #9
    def susana_function(self): self.button_function("Susana", 1)

    #10
    def bel_and_dragon_function(self): self.button_function("Bel and the Dragon", 1)

    #11
    def _1_maccabees_function(self): self.button_function("1 Maccabees", 16)

    #12
    def _2_maccabees_function(self): self.button_function("2 Maccabees", 15)

    # New Testament Books
    def matthew_function(self): self.button_function("Matthew",28)

    def mark_function(self): self.button_function("Mark", 16)

    def luke_function(self): self.button_function("Luke", 24)

    def john_function(self): self.button_function("John", 21)

    def acts_function(self): self.button_function("Acts", 28)

    def romans_function(self): self.button_function("Roman", 16)

    def _1_corinthians_function(self): self.button_function("1 Corinthians", 16)

    def _2_corinthians_function(self): self.button_function("2 Corinthians", 13)

    def galatians_function(self): self.button_function("Galatians", 6)

    def ephesians_function(self): self.button_function("Ephesians", 6)

    def philippians_function(self): self.button_function("Philippians", 4)

    def colossians_function(self): self.button_function("Colossians", 4)

    def _1_thessalonians_function(self): self.button_function("1 Thessalonians", 5)

    def _2_thessalonians_function(self): self.button_function("2 Thessalonians", 3)

    def _1_timothy_function(self): self.button_function("1 Timothy", 6)

    def _2_timothy_function(self): self.button_function("2 Timothy", 4)

    def titus_function(self): self.button_function("Titus", 3)

    def philemon_function(self): self.button_function("Philemon", 1)

    def hebrews_function(self): self.button_function("Hebrews", 13)

    def james_function(self): self.button_function("James", 5)

    def _1_peter_function(self): self.button_function("1 Peter", 5)

    def _2_peter_function(self): self.button_function("2 Peter", 3)

    def _1_john_function(self): self.button_function("1 John", 5)

    def _2_john_function(self): self.button_function("2 John", 1)

    def _3_john_function(self): self.button_function("3 John", 1)

    def jude_function(self): self.button_function("Jude", 1)

    def revelation_function(self): self.button_function("Revelation", 22)