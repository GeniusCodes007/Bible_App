# Create and edit the buttons for displaying the books buttons

from PySide6.QtWidgets import QPushButton
from Bible_Content_Organisation_Window.Bible_Content_Organization.Bible_Books import newTestament, deuterocanonical_Testament

# Import Parent Class
from main_bible_app.bible_window_organisation.bible_organisation_and_display.chapter_buttons import ChapterButtons

class BibleBooksButtons(ChapterButtons):


    def __init__(self):
        super().__init__()


        self.spaced_books = ["1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles","Song of Songs",
                             "Esther (Greek)", "Wisdom of Solomon", "Letter of Jeremiah", "Song of the Three Young Men", "Bel and the Dragon", "1 Maccabees", "2 Maccabees",
                             "1 Corinthians", "2 Corinthians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "1 Peter", "2 Peter", "1 John", "2 John", "3 John"]

        self.oldTestament = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth",
                        "Samuel 1",
                        "Samuel 2", "Kings 1", "Kings 2", "Chronicles 1", "Chronicles 2", "Ezra", "Nehemiah", "Esther",
                        "Job",
                        "Psalms", "Proverbs", "Ecclesiastes", "Song of Songs", "Isaiah", "Jeremiah", "Lamentations",
                        "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
                        "Zephaniah", "Haggai", "Zechariah", "Malachi"]

        self.deuterocanonical_Testament = ["Tobit", "Judith", "Esther Greek", "Wisdom of Solomon", "Sirach", "Baruch",
                                      "Letter of Jeremiah",
                                      "Song of the Three Young Men", "Susana", "Bel and the Dragon", "Maccabees 1",
                                      "Maccabees 2"]

        self.newTestament = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "Corinthians 1", "Corinthians 2",
                        "Galatians", "Ephesians", "Philippians",
                        "Colossians", "Thessalonians 1", "Thessalonians 2", "Timothy 1", "Timothy 2", "Titus",
                        "Philemon", "Hebrews", "James",
                        "Peter 1", "Peter 2", "John 1", "John 2", "John 3", "Jude", "Revelation"]

        self.catholicBible = self.oldTestament + self.deuterocanonical_Testament + self.newTestament
        self.pentecostalBible = self.oldTestament + self.newTestament

        self.catholicBibleTranslations = ["The New Jerusalem", "Good News"]

        self.pentecostalBibleTranslations = ["King James", "Amplified"]

        self.bibleVersions = self.catholicBible + self.pentecostalBible


    # This is a base function, with which the books buttons can be able to display the number of chapters they have
    def button_function(self, book_name:str, book_chapters_number:int):

        count = self.chaptersNumberGridLayout.count()

        # Set the text of the book-name-label in the chapters-number-gridlayout to the name of the
        self.book_name_label.setText(book_name)

        self.gn_book_label.setText(book_name)
        self.amp_book_label.setText(book_name)
        self.kjv_book_label.setText(book_name)
        self.njb_book_label.setText(book_name)

        for x in range(count):
            chapter_pushbutton = self.chaptersNumberInnerFrame.findChild(QPushButton, f"chap_but_{x + 1}")
            if x < book_chapters_number:
                chapter_pushbutton.setEnabled(True)
                chapter_pushbutton.show()
            else:
                chapter_pushbutton.setEnabled(False)
                chapter_pushbutton.hide()
        self.chaptersNumberFrame.show()


    # Creating the button functions for each book, these functions work with their designated QPushButtons
    #  All Inherited and made use of by bible_books_button_actions function of the BibleEdit class, in the bibleEdit.py file
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
    def esther_greek_function(self): self.button_function("Esther (Greek)", 16)

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

    # Inherited
    # Alternates the color of the old_testament, deuterocanonical and new_testament books
    def change_books_button_colors(self):
        print(self.hide_show_bible_books_pushbutton.styleSheet())

        for x in range(len(self.oldTestament)):
            text = self.oldTestament[x].replace(" ", "_").lower()
            self.bibleBooksFrame.findChild(QPushButton, text).setStyleSheet("""background-color: rgb(121, 121, 90);""")

        # Change the color of the New Testament Books
        for x in range(27):
            try:
                self.bibleBooksFrame.findChild(QPushButton, newTestament[x].lower()).setStyleSheet(
                    u"background-color: rgb(97, 97, 72);")
            except AttributeError:
                self.bibleBooksFrame.findChild(QPushButton, newTestament[x].replace(" ", "_").lower()).setStyleSheet(
                    u"background-color: rgb(97, 97, 72);")

        # Change the color of the Deuterocanonical Books
        for x in range(12):
            try:
                self.bibleBooksFrame.findChild(QPushButton, self.deu_books_obj_names[x]).setStyleSheet(
                    u"background-color: rgb(13, 65, 87);")
            except AttributeError:
                self.bibleBooksFrame.findChild(QPushButton,
                                               deuterocanonical_Testament[x].replace(" ", "_").lower()).setStyleSheet(
                    u"background-color: rgb(13, 65, 87);")

    # Inherited
    # Function That Contains All Books-Button-Clicking Actions - Signals and Slots
    def bible_books_button_actions(self):
        # Old Testament Book-Buttons and Actions
        self.genesis.toggled.connect(self.genesis_function)
        self.exodus.toggled.connect(self.exodus_function)
        self.leviticus.toggled.connect(self.leviticus_function)
        self.numbers.toggled.connect(self.numbers_function)
        self.deuteronomy.toggled.connect(self.deuteronomy_function)
        self.joshua.toggled.connect(self.joshua_function)
        self.judges.toggled.connect(self.judges_function)
        self.ruth.toggled.connect(self.ruth_function)
        self.samuel_1.toggled.connect(self._1_sam_function)
        self.samuel_2.toggled.connect(self._2_sam_function)
        self.kings_1.toggled.connect(self._1_kings_function)
        self.kings_2.toggled.connect(self._2_kings_function)
        self.chronicles_1.toggled.connect(self._1_chronicles_function)
        self.chronicles_2.toggled.connect(self._2_chronicles_function)
        self.ezra.toggled.connect(self.ezra_function)
        self.nehemiah.toggled.connect(self.nehemiah_function)
        self.esther.toggled.connect(self.esther_function)
        self.job.toggled.connect(self.job_function)
        self.psalms.toggled.connect(self.psalms_function)
        self.proverbs.toggled.connect(self.proverbs_function)
        self.ecclesiastes.toggled.connect(self.ecclesiastes_function)
        self.song_of_songs.toggled.connect(self.song_of_songs_solomon_function)
        self.isaiah.toggled.connect(self.isaiah_function)
        self.jeremiah.toggled.connect(self.jeremiah_function)
        self.lamentations.toggled.connect(self.lamentations_function)
        self.ezekiel.toggled.connect(self.ezekiel_function)
        self.daniel.toggled.connect(self.daniel_function)
        self.hosea.toggled.connect(self.hosea_function)
        self.joel.toggled.connect(self.joel_function)
        self.amos.toggled.connect(self.amos_function)
        self.obadiah.toggled.connect(self.obadiah_function)
        self.jonah.toggled.connect(self.jonah_function)
        self.micah.toggled.connect(self.micah_function)
        self.nahum.toggled.connect(self.nahum_function)
        self.habakkuk.toggled.connect(self.habakkuk_function)
        self.zephaniah.toggled.connect(self.zephaniah_function)
        self.haggai.toggled.connect(self.haggai_function)
        self.zechariah.toggled.connect(self.zechariah_function)
        self.malachi.toggled.connect(self.malachi_function)

        # Deuterocanonical Book-Button and Actions
        self.tobit.toggled.connect(self.tobit_function)
        self.judith.toggled.connect(self.judith_function)
        self.esther_greek.toggled.connect(self.esther_greek_function)
        self.wisdom_of_solomon.toggled.connect(self.wisdom_of_solomon_function)
        self.sirach.toggled.connect(self.sirach_function)
        self.baruch.toggled.connect(self.baruch_function)
        self.letter_of_jeremiah.toggled.connect(self.letter_of_jeremiah_function)
        self.song_of_the_three_young_men.toggled.connect(self.song_of_the_three_young_men_function)
        self.susana.toggled.connect(self.susana_function)
        self.bel_and_the_dragon.toggled.connect(self.bel_and_dragon_function)
        self.maccabees_1.toggled.connect(self._1_maccabees_function)
        self.maccabees_2.toggled.connect(self._2_maccabees_function)

        # New Testament Book-Buttons and Actions
        self.matthew.toggled.connect(self.matthew_function)
        self.mark.toggled.connect(self.mark_function)
        self.luke.toggled.connect(self.luke_function)
        self.john.toggled.connect(self.john_function)
        self.acts.toggled.connect(self.acts_function)
        self.romans.toggled.connect(self.romans_function)
        self.corinthians_1.toggled.connect(self._1_corinthians_function)
        self.corinthians_2.toggled.connect(self._2_corinthians_function)
        self.galatians.toggled.connect(self.galatians_function)
        self.ephesians.toggled.connect(self.ephesians_function)
        self.philippians.toggled.connect(self.philippians_function)
        self.colossians.toggled.connect(self.colossians_function)
        self.thessalonians_1.toggled.connect(self._1_thessalonians_function)
        self.thessalonians_2.toggled.connect(self._2_thessalonians_function)
        self.timothy_1.toggled.connect(self._1_timothy_function)
        self.timothy_2.toggled.connect(self._2_timothy_function)
        self.titus.toggled.connect(self.titus_function)
        self.philemon.toggled.connect(self.philemon_function)
        self.hebrews.toggled.connect(self.hebrews_function)
        self.james.toggled.connect(self.james_function)
        self.peter_1.toggled.connect(self._1_peter_function)
        self.peter_2.toggled.connect(self._2_peter_function)
        self.john_1.toggled.connect(self._1_john_function)
        self.john_2.toggled.connect(self._2_john_function)
        self.john_3.toggled.connect(self._3_john_function)
        self.jude.toggled.connect(self.jude_function)
        self.revelation.toggled.connect(self.revelation_function)