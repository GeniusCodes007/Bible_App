from PySide6.QtWidgets import QApplication, QPushButton
import sys
from bibleEdit import BibleEdit

class MainWindow(BibleEdit):
    def __init__(self):
        super().__init__()

        self.chaptersNumberFrame.hide()
        self.tabWidget.setCurrentIndex(0)
        self.gn_book_label.setText("Genesis")

        self.gn_version_label.setText("Good News Version")
        self.amp_version_label.setText("Amplified Bible Version")
        self.kjv_version_label.setText("King James Version")
        self.njb_version_label.setText("New Jerusalem Bible")

        self.gn_inner_frame.setMinimumHeight(1500)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())