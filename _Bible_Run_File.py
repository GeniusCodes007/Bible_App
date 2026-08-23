
from PySide6.QtWidgets import QApplication
import sys
from main_bible_app.bible_window_organisation.bible_organisation_and_display.set_app_functionalities import Set_App_Functionalities

"""Windows involved

-> Bible Content Display
-> Bible Fun Facts
-> Bible Study Plan
-> Bible Study Topics
-> Bible Study Character 
-> Bible Settings

How to organize app

-> Get the app gui design from ui_bible_ui.py, let the most basic class inherit it from the Ui_Bible_MainWindow class
-> 
"""

app = QApplication(sys.argv)
window = Set_App_Functionalities()
window.show()
sys.exit(app.exec())

