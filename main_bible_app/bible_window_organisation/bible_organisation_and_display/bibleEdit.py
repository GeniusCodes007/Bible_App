from PySide6.QtGui import QIcon

# Import Parent Class
from main_bible_app.bible_window_organisation.bible_organisation_and_display.edit_Display import Edit_Display

class BibleEdit(Edit_Display):
    def __init__(self):
        super().__init__()

    # Inherited
    # Function for Quitting the App
    def quit_the_app(self):
        self.close()


    # Embeds all signals and slots that switch window display
    # Inherited
    def window_switching_button_actions(self):
        # Connect the menu button to the hide_menu function
        self.pushButton_menu.toggled.connect(self.toggle_menu)

        # Connect the content button to the toggle_books function
        self.hide_show_bible_books_pushbutton.toggled.connect(self.toggle_books_frame)

        #
        self.pushButton_fun_facts.clicked.connect(self.show_fun_facts_page)

        #
        self.pushButton_bible_study_plan.clicked.connect(self.show_study_plan)

        #
        self.pushButton_study_topic.clicked.connect(self.show_study_topics)

        #
        self.pushButton_character.clicked.connect(self.show_study_character)

        #
        self.pushButton_settings.clicked.connect(self.show_settings)

    def windowStyleSheet(self):
        self.setStyleSheet("""
        background-color: rgb(223, 223, 166);
        QPushButton{
        color: rgb(213, 213, 159);
        border-radius: 10px;
        background-color: rgb(121, 121, 90);
        border-color: rgb(0, 0, 0);
        selection-background-color: rgb(170, 170, 127);
        selection-color: rgb(85, 170, 255);
        font: 10pt "Segoe Print";}
        
        QFrame{
        background-color: rgb(223, 223, 166);}
        """)
#C:/Users/GENIUS DEXTER/Bible_App/
    def window_icons(self):
        self.setWindowIcon(QIcon("Bible_Organisation_And_Display/bible_icons/bible_icon.jpeg"))
        