from PySide6.QtWidgets import QPushButton, QLabel, QFrame
from PySide6.QtWidgets import QMainWindow






# Inherited - to be copied

# Import Parent Class
from UI_Python_Content.ui_Bible_ui import Ui_Bible_MainWindow
# Settled
# This class contains the most basic features of the app
class Edit_Display(QMainWindow,Ui_Bible_MainWindow):
    def __init__(self):
        super().__init__()

        # Contains all the object_names of the deuterocanonical books buttons



    # Embedded
    # Function That Hides or Displays The Left-Scroll-Area Widget
    def toggle_menu(self):
        if self.pushButton_menu.isChecked():
            self.leftScrollArea.hide()
        else:
            self.leftScrollArea.show()
        self.chaptersNumberFrame.hide()


    # Embedded
    # Function That Hides or Displays The Bible-Books-Frame Widget
    def toggle_books_frame(self):
        if self.hide_show_bible_books_pushbutton.isChecked():
            self.bibleBooksFrame.show()
        else:
            self.bibleBooksFrame.hide()
        self.stackedWidget.setCurrentIndex(0)
        self.chaptersNumberFrame.hide()

    # Embedded
    # Function That Displays The Fun-Facts Page
    def show_fun_facts_page(self):
        self.stackedWidget.setCurrentIndex(1)

    # Embedded
    # Function That Displays The Study-Plan Page
    def show_study_plan(self):
        self.stackedWidget.setCurrentIndex(2)

    # Embedded
    # Function That Displays The Study-Topics Page
    def show_study_topics(self):
        self.stackedWidget.setCurrentIndex(3)

    # Embedded
    # Function That Displays The Study-Character Page
    def show_study_character(self):
        self.stackedWidget.setCurrentIndex(4)

    # Embedded
    # Function That Displays The Settings Page
    def show_settings(self):
        self.stackedWidget.setCurrentIndex(5)


    # Function that sets the text on the widgets concerned
    def setTexts(self):
        # Set the default text for the Hide-Show-Bible-Books Button
        self.hide_show_bible_books_pushbutton.setText("Bible Books")

        # Set the default text for the Menu Button
        self.pushButton_menu.setText("Menu")

        # Set the default text for the Book-Labels of the different Bible-Version Tabs
        self.njb_book_label.setText("NJB Books")
        self.kjv_book_label.setText("KJV Books")
        self.gn_book_label.setText("GN Books")
        self.amp_book_label.setText("AMP Books")

    # Function the sets the default windows
    def set_default_windows(self):

        # Set the page for the main Bible to show by default

        # Set the default stack widget index
        self.stackedWidget.setCurrentIndex(0)
        # Set the default tab widget index
        self.bibleContentTabWidget.setCurrentIndex(0)

        # Hide the frame displaying the chapters-button, by default
        self.chaptersNumberFrame.hide()

        # Hide the frame displaying the books-buttons, by default
        self.bibleBooksFrame.hide()

    # Inherited
    # Function that creates all 150-chapters button by default
    # 150 is the maximum number of chapters in a Book in the Bible
    def create_all_chapters_buttons(self):

        # Makes Available All The Chapter Buttons
        for x in range(150):
            but = QPushButton(self.chapters_scrollAreaWidgetContents)
            but.setObjectName(f"chap_but_{x + 1}")
            but.setText(f"Chapter {x + 1}")
            but.setCheckable(True)
            but.setAutoExclusive(True)
            self.chaptersNumberGridLayout.addWidget(but, x, 0)

    # Inherited
    # Function that creates all 176-verses button by default and adds them to the njb tab
    # 176 is the maximum number of verses in a chapter in the Bible
    def add_max_verses_to_njb_tab(self):
        column_count=0
        for x in range(176):
                verse_label = QLabel(self.njb_ScrollAreaContents)
                verse_label.setObjectName(f"njb_verse_number_label_{x + 1}")
                verse_label.setMaximumSize(30, 50)
                verse_label.setMinimumSize(30, 50)
                verse_label.setText(str(x + 1))

                verse_content_label = QLabel(self.njb_ScrollAreaContents)
                verse_content_label.setObjectName(f"njb_verse_content_label_{x + 1}")
                verse_content_label.setText(f"This number {x + 1}\n\n\n\nThis number {x+1}")
                verse_content_label.setFrameShape(QFrame.Shape.WinPanel)
                verse_content_label.setFrameShadow(QFrame.Shadow.Plain)

                self.njb_gridLayout.addWidget(verse_label, x,column_count)
                self.njb_gridLayout.addWidget(verse_content_label, x,column_count+1)


    # Inherited
    # Function that creates all 176-verses button by default and adds them to the amp tab
    # 176 is the maximum number of verses in a chapter in the Bible
    def add_max_verses_to_amp_tab(self):
        column_count = 0
        for x in range(176):
            verse_label = QLabel(self.amp_ScrollAreaContents)
            verse_label.setObjectName(f"amp_verse_number_label_{x + 1}")
            verse_label.setMaximumSize(30, 50)
            verse_label.setMinimumSize(30, 50)
            verse_label.setText(str(x + 1))

            verse_content_label = QLabel(self.amp_ScrollAreaContents)
            verse_content_label.setObjectName(f"amp_verse_content_label_{x + 1}")
            verse_content_label.setText(f"This number {x + 1}\n\n\n\nThis number {x + 1}")
            verse_content_label.setFrameShape(QFrame.Shape.WinPanel)
            verse_content_label.setFrameShadow(QFrame.Shadow.Plain)

            self.amp_gridLayout.addWidget(verse_label, x, column_count)
            self.amp_gridLayout.addWidget(verse_content_label, x, column_count + 1)

    # Inherited
    # Function that creates all 176-verses button by default and adds them to the kjv tab
    # 176 is the maximum number of verses in a chapter in the Bible
    def add_max_verses_to_kjv_tab(self):
        column_count=0
        for x in range(176):
                verse_label = QLabel(self.kjv_ScrollAreaContents)
                verse_label.setObjectName(f"kjv_verse_number_label_{x + 1}")
                verse_label.setMaximumSize(30, 50)
                verse_label.setMinimumSize(30, 50)
                verse_label.setText(str(x + 1))

                verse_content_label = QLabel(self.kjv_ScrollAreaContents)
                verse_content_label.setObjectName(f"kjv_verse_content_label_{x + 1}")
                verse_content_label.setText(f"This number {x + 1}\n\n\n\nThis number {x+1}")
                verse_content_label.setFrameShape(QFrame.Shape.WinPanel)
                verse_content_label.setFrameShadow(QFrame.Shadow.Plain)

                self.kjv_gridLayout.addWidget(verse_label, x,column_count)
                self.kjv_gridLayout.addWidget(verse_content_label, x,column_count+1)


    # Inherited
    # Function that creates all 176-verses button by default and adds them to the gn tab
    # 176 is the maximum number of verses in a chapter in the Bible
    def add_max_verses_to_gn_tab(self):
        column_count=0
        for x in range(176):
            verse_label = QLabel(self.gn_scrollAreaWidgetContents)
            verse_label.setObjectName(f"gn_verse_number_label_{x + 1}")
            verse_label.setMaximumSize(30, 50)
            verse_label.setMinimumSize(30, 50)
            verse_label.setText(str(x + 1))

            verse_content_label = QLabel(self.njb_ScrollAreaContents)
            verse_content_label.setObjectName(f"gn_verse_content_label_{x + 1}")
            verse_content_label.setText(f"This number {x + 1}\n\n\n\nThis number {x+1}")
            verse_content_label.setFrameShape(QFrame.Shape.WinPanel)
            verse_content_label.setFrameShadow(QFrame.Shadow.Plain)

            self.gn_gridLayout.addWidget(verse_label, x,column_count)
            self.gn_gridLayout.addWidget(verse_content_label, x,column_count+1)

