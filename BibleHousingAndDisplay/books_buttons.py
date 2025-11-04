from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton
from BibleHousingAndDisplay.re_assign_buttons import ReAssignButtons

#chaptersNumberGridLayout
class BooksButtons(ReAssignButtons):
    def __init__(self):
        super().__init__()

        self.font1 = QFont()
        self.font1.setPointSize(10)
        self.font1.setBold(True)

    def genesis_button_function(self):
        chapters = 50

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.genesis.objectName())

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

    def exodus_button_function(self):
        chapters = 40

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.exodus.objectName())

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

    def leviticus_button_function(self):
        chapters = 27

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.leviticus.objectName())

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

    def numbers_button_function(self):
        chapters = 36

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.numbers.objectName())

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

    def deuteronomy_button_function(self):
        chapters = 34

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.deuteronomy.objectName())

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

    def joshua_button_function(self):
        chapters = 24

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.joshua.objectName())

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

    def judges_button_function(self):
        chapters = 21

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.judges.objectName())

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

    def ruth_button_function(self):
        chapters = 4

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.ruth.objectName())

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

    def sam_1_button_function(self):
        chapters = 31

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.sam_1.objectName())

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

    def sam_2_button_function(self):
        chapters = 24

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.sam_2.objectName())

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

    def kings_1_button_function(self):
        chapters = 22

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.kings_1.objectName())

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

    def kings_2_button_function(self):
        chapters = 25

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.kings_2.objectName())

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

    def chronicles_1_button_function(self):
        chapters = 29

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.chronicles_1.objectName())

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

    def chronicles_2_button_function(self):
        chapters = 36

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.chronicles_2.objectName())

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

    def ezra_button_function(self):
        chapters = 10

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.ezra.objectName())

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

    def nehemiah_button_function(self):
        chapters = 13

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.nehemiah.objectName())

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

    def esther_button_function(self):
        chapters = 10

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.esther.objectName())

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

    def job_button_function(self):
        chapters = 42

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.job.objectName())

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

    def psalms_button_function(self):
        chapters = 150

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.psalms.objectName())

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

    def proverbs_button_function(self):
        chapters = 31

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.proverbs.objectName())

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

    def ecclesiastes_button_function(self):
        chapters = 12

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.ecclesiastes.objectName())

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

    def song_of_songs_solomon_button_function(self):
        chapters = 8

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.song_of_songs_solomon.objectName())

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

    def isaiah_button_function(self):
        chapters = 66

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.isaiah.objectName())

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

    def jeremiah_button_function(self):
        chapters = 52

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.jeremiah.objectName())

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

    def lamentations_button_function(self):
        chapters = 5

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.lamentations.objectName())

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

    def ezekiel_button_function(self):
        chapters = 48

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.ezekiel.objectName())

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

    def daniel_button_function(self):
        chapters = 12

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.daniel.objectName())

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

    def hosea_button_function(self):
        chapters = 14

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.hosea.objectName())

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

    def joel_button_function(self):
        chapters = 3

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.joel.objectName())

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

    def amos_button_function(self):
        chapters = 9

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.amos.objectName())

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

    def obadiah_button_function(self):
        chapters = 1

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.obadiah.objectName())

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

    def jonah_button_function(self):
        chapters = 4

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.jonah.objectName())

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

    def micah_button_function(self):
        chapters = 7

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.micah.objectName())

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

    def nahum_button_function(self):
        chapters = 3

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.nahum.objectName())

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

    def habakkuk_button_function(self):
        chapters = 3

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.habakkuk.objectName())

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

    def zephaniah_button_function(self):
        chapters = 3

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.zephaniah.objectName())

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

    def haggai_button_function(self):
        chapters = 2

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.haggai.objectName())

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

    def zechariah_button_function(self):
        chapters = 14

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.zechariah.objectName())

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

    def malachi_button_function(self):
        chapters = 4

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.malachi.objectName())

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

    def matthew_button_function(self):
        chapters = 28

        count = self.chaptersNumberGridLayout.count()

        self.book_name_label.setText(self.matthew.objectName())

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