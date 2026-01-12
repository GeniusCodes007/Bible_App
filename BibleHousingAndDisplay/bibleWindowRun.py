from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

from BibleHousingAndDisplay.bibleEdit import BibleEdit
from BibleRunFiles.Bible_Books import newTestament, deuterocanonical_Testament
#from ui_Bible_ui import Ui_MainWindow

#from BibleRunFiles.Bible_Books import newTestament, deuterocanonical_Testament
from display_content import Display_Content
#background-color: rgb(97, 97, 72);
class RunWindow(Display_Content, QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setupUi(self)


        # Set the page for the main Bible to show by default
        self.stackedWidget.setCurrentIndex(0)

        self.chaptersNumberFrame.hide()

        self.bibleBooksFrame.hide()

        # Connect the menu button to the hide_menu function
        self.pushButton_menu.toggled.connect(self.toggle_menu)

        # Connect the content button to the toggle_books function
        self.pushButton_content.toggled.connect(self.toggle_content)

        self.pushButton_fun_facts.clicked.connect(self.show_fun_facts_page)
        self.pushButton_bible_study.clicked.connect(self.show_study_plan)
        self.pushButton_study_topic.clicked.connect(self.show_study_topics)
        self.pushButton_character.clicked.connect(self.show_study_character)
        self.pushButton_settings.clicked.connect(self.show_settings)
        self.pushButton_quit_app.clicked.connect(self.quit_the_app)

        for x in range(27):
            try:
                #if self.bibleBooksFrame.findChild(QPushButton, newTestament[x].lower()).objectName() == newTestament[x].lower():
                self.bibleBooksFrame.findChild(QPushButton, newTestament[x].lower()).setStyleSheet(u"background-color: rgb(97, 97, 72);")
            except AttributeError:
                print("Found - ", newTestament[x], " - in spaced books")
                pass

        for x in range(12):
            try:
                    if self.bibleBooksFrame.findChild(QPushButton, deuterocanonical_Testament[x].lower()).objectName() == deuterocanonical_Testament[x].lower():
                        self.bibleBooksFrame.findChild(QPushButton, deuterocanonical_Testament[x].lower()).setStyleSheet(u"background-color: rgb(13, 65, 87);")
            except AttributeError:
                pass

    def quit_the_app(self):
        self.close()

app = QApplication(sys.argv)
window = RunWindow()
window.show()
sys.exit(app.exec())
