

# Import Parent Class
from main_bible_app.bible_window_organisation.bible_organisation_and_display.bible_books_buttons import BibleBooksButtons

#background-color: rgb(97, 97, 72);
class Bible_Window_Organisation(BibleBooksButtons):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        """From Edit Display"""

        # Controls when the deuterocanonical books-buttons are displayed
        self.bibleContentTabWidget.currentChanged.connect(self.show_hide_deuterocanonical_books)

        # Inherited from the edit_Display class, in edit_Display file
        self.setTexts()

        # Sets the windows that display by default
        # Inherited from the edit_Display class, in edit_Display file
        self.set_default_windows()

        # Automatically creates all buttons for the chapters
        # Inherited from the edit_Display class, in edit_Display file
        self.create_all_chapters_buttons()

        # Function that creates all 176-verses button by default and adds them to the njb tab
        # Inherited from the edit_Display class, in edit_Display file
        self.add_max_verses_to_njb_tab()

        # Function that creates all 176-verses button by default and adds them to the kjv tab
        # Inherited from the edit_Display class, in edit_Display file
        self.add_max_verses_to_kjv_tab()

        # Function that creates all 176-verses button by default and adds them to the amp tab
        # Inherited from the edit_Display class, in edit_Display file
        self.add_max_verses_to_amp_tab()

        # Function that creates all 176-verses button by default and adds them to the gn tab
        # Inherited from the edit_Display class, in edit_Display file
        self.add_max_verses_to_gn_tab()



        """Bible Books Buttons"""

        # Contains the actions performed by bible_books_buttons
        # Inherited from the BibleEdit class, in bibleEdit.py file
        self.bible_books_button_actions()

        # Alternates the color of the old_testament, deuterocanonical and new_testament books
        # Inherited from the BibleBooksButtons class, in bible_books_buttons.py file
        self.change_books_button_colors()


        """From Bible Edit"""

        # Closes the app
        # Inherited from the BibleEdit class, in bibleEdit.py file
        self.pushButton_quit_app.clicked.connect(self.quit_the_app)

        # Handles the switching between different windows
        # Inherited from the BibleEdit class, in bibleEdit.py file
        self.window_switching_button_actions()

        # Handles the setting of the StyleSheet features of our app
        # Inherited from the BibleEdit class, in bibleEdit.py file
        self.windowStyleSheet()

        self.window_icons()


        """Chapter Buttons"""

        # Calls all the actions that take place when a Chapter button is clicked
        # Inherited from the edit_Display class, in edit_Display file
        self.chapter_display_button_actions()


