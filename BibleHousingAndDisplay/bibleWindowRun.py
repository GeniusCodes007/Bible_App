from PySide6.QtWidgets import QApplication
import sys
from display_content import *
#background-color: rgb(97, 97, 72);
class MainWindow(Display_Content):
    def __init__(self):
        super().__init__()

        # Set the tab for Genesis to show by default
        self.tabWidget.setCurrentIndex(3)

        self.chaptersNumberFrame.hide()

        self.bibleBooksFrame.hide()

        # Connect the menu button to the hide_menu function
        self.pushButton_menu.toggled.connect(self.toggle_menu)

        # Connect the content button to the toggle_books function
        self.pushButton_content.toggled.connect(self.toggle_books)

        #print(self.findChild(QPushButton, "Genesis").parentWidget().objectName())

        for x in range(27):
            if self.findChild(QPushButton, newTestament[x]).objectName() == newTestament[x]:
                self.findChild(QPushButton, newTestament[x]).setStyleSheet(u"background-color: rgb(97, 97, 72);")

        for x in range(12):
            if self.findChild(QPushButton, deuterocanonical_Testament[x]).objectName() == deuterocanonical_Testament[x]:
                self.findChild(QPushButton, deuterocanonical_Testament[x]).setStyleSheet(u"background-color: rgb(108, 108, 0);")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
