from PySide6.QtWidgets import QApplication
import sys
from bibleEdit import *

class MainWindow(BibleEdit):
    def __init__(self):
        super().__init__()

        self.font2 = QFont()
        self.font2.setFamilies([u"Segoe UI"])
        self.font2.setPointSize(10)
        self.font2.setBold(True)
        self.font2.setItalic(False)

        #Hide The Bible Book Frame
        self.bibleBooksFrame.hide()

        #Hide The Chapters Frame
        self.chaptersNumberFrame.hide()

        #Tab Widget with Index '0', -> Genesis
        #So, I set the Genesis Tab to display on app start up
        self.tabWidget.setCurrentIndex(0)

        #Set the Genesis Book Label to 'Genesis'
        self.gn_book_label.setText("Genesis")

        # I set the text of The Version Labels to their Respective Translations
        self.gn_version_label.setText("Good News Version")
        self.amp_version_label.setText("Amplified Bible Version")
        self.kjv_version_label.setText("King James Version")
        self.njb_version_label.setText("New Jerusalem Bible")

        #Set the Minimum Height of the inner frames of the translations to '1500'
        #self.gn_inner_frame.setMinimumHeight(1500)
        #self.amp_inner_frame.setMinimumHeight(1500)
        #self.kjv_inner_frame.setMinimumHeight(1500)
        #self.njb_inner_frame.setMinimumHeight(1500)

        #Search a button with an objectName 'chap_but_1', and give it a clicking action
        self.chapterNumberScrollArea.findChild(QPushButton, f"chap_but_1").clicked.connect(self.display_content)

        #Connect the content button to the 'toggle_content' function or method
        self.pushButton_content.toggled.connect(self.toggle_content)

    def display_content(self):
        print("You Left Me Without Functionality")
        if self.findChild(QPushButton, wholeBible[0]).isChecked():
            print("Yes")
            #print(new_jerusalem['Genesis']['Chapter 1'])

            for x in new_jerusalem['Genesis']['Chapter 1']:

                verse_label = QLabel(self.gn_scrollArea)
                verse_label.setText(f"{x}")
                verse_label.setFont(self.font2)
                verse_label.setMaximumSize(35, 50)

                verse_content = QLabel(self.centralwidget)
                verse_content.setText(f"{new_jerusalem['Genesis']['Chapter 1'][x]}")
                verse_content.setFont(self.font2)

                self.gn_gridLayout.addWidget(verse_label, x-1, 0)
                self.gn_gridLayout.addWidget(verse_content, x-1,1)

                #self.njb_gridLayout.addWidget(verse_label, x - 1, 0)
                #self.njb_gridLayout.addWidget(verse_content, x - 1, 1)

                #print(x, new_jerusalem['Genesis']['Chapter 1'][x])

    def toggle_content(self):
        if self.pushButton_content.isChecked():
            self.bibleBooksFrame.show()
        else:
            self.bibleBooksFrame.hide()
            self.chaptersNumberFrame.hide()




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())