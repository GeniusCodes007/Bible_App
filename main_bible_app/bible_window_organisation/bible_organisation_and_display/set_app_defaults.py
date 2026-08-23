
# In this file, we set the default appearance of the app
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel
from needful_extra_functions import find_widget, books_obj_name, old_test_books_obj_names, deu_books_obj_names, \
    new_test_books_obj_names, my_font
from main_bible_app.Bible_UI_Files.Bible_ui_ui import Ui_Bible_MainWindow
from PySide6 import QtWidgets


class Set_App_Default_Texts(Ui_Bible_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set App/Window Title
        self.setWindowTitle("Student of the Gospel Bible")

        # Set default pages
        self.stackedWidget.setCurrentIndex(0)
        self.bibleContentTabWidget.setCurrentIndex(0)

        # Set the default app appearances of all container-type widgets
        self.set_central_widgets_default()
        self.set_pushbutton_menu_default()
        self.set_hide_show_books_pushbutton_default()
        self.set_default_text_color_of_bible_books()
        self.set_bible_study_plan_page_default()
        self.create_all_books_chapters_buttons()
        self.create_all_verses_labels_to_gn_tab()
        self.create_all_verses_labels_to_amp_tab()
        self.create_all_verses_labels_to_njb_tab()
        self.create_all_verses_labels_to_kjv_tab()
        self.upgrade_bible_books_buttons()


    # Set the default appearance of the central widget
    def set_central_widgets_default(self):

        self.centralwidget.setStyleSheet("""
                QWidget{
                background-color: rgb(223, 223, 166);
                }
                QFrame{
                background-color: rgb(121, 121, 90);
                border-radius: 10px;
                }
                """)#background-color: rgb(223, 223, 166);     #background-color: rgb(23, 223, 166);

    # Set the default appearance of the pushbutton_menu
    def set_pushbutton_menu_default(self):
        # background-color: rgb(121, 121, 90);  --- in case ....
        self.pushButton_menu.setStyleSheet("""
        QPushButton{
                color: rgb(213, 213, 159);
                border-radius: 10px;
                background-color: rgb(121, 121, 90);
                border-color: rgb(0, 0, 0);
                selection-background-color: rgb(170, 170, 127);
                selection-color: rgb(85, 170, 255);
                font: 10pt "Segoe Print";}
        """)
        # Set the text of pushbutton menu
        self.pushButton_menu.setText("Menu")

    # Set the default appearance of the hide_show_books_pushbutton
    def set_hide_show_books_pushbutton_default(self):
        self.hide_show_bible_books_pushbutton.setStyleSheet(
            """
            QPushButton{
                color: rgb(213, 213, 159);
                background-color: rgb(121, 121, 90);
                border-radius: 10px;
                }
            """
        )

        # Set the text of hide_show_books-pushbutton
        self.hide_show_bible_books_pushbutton.setText("Bible Books")

    # Set the text color of the bible books
    def set_default_text_color_of_bible_books(self):
        for book in books_obj_name:

            if book in old_test_books_obj_names:
                find_widget(self.bibleBooksFrame, QtWidgets.QPushButton, book).setStyleSheet("""QPushButton{
                            font: 10pt "Segoe Print";
                            color: rgb(5, 0, 255);
                            }""")

            if book in deu_books_obj_names:
                find_widget(self.bibleBooksFrame, QtWidgets.QPushButton, book).setStyleSheet("""QPushButton{
                            font: 10pt "Segoe Print";
                            color: rgb(255, 30, 0);
                            }""")

            if book in new_test_books_obj_names:
                find_widget(self.bibleBooksFrame, QtWidgets.QPushButton, book).setStyleSheet("""QPushButton{
                            font: 10pt "Segoe Print";
                            color: rgb(100, 25, 30);
                            }""")

    # Set the bible study plan page default appearance
    def set_bible_study_plan_page_default(self):
        self.bible_study_plan_scrollAreaWidgetContents.setStyleSheet("""
                        QTableWidget{
                        background-color: rgb(223, 223, 166);
                        }
                        """)

    # Create and Make Available All The Chapters Buttons
    def create_all_books_chapters_buttons(self):
        for num in range(150):
            book_chapters_button = QPushButton(self.chaptersNumberInnerFrame)
            book_chapters_button.setObjectName(f"chapter_{num + 1}")
            book_chapters_button.setText(f"Chapter {num + 1}")
            book_chapters_button.setStyleSheet("""QPushButton{
            background-color: rgb(223, 223, 166);
            border-radius: 10px;
            }""")
            book_chapters_button.setAutoExclusive(True)
            book_chapters_button.setFont(my_font)
            self.chaptersNumberGridLayout.addWidget(book_chapters_button, num, 0)
            book_chapters_button.hide()

    # Create and Make Available All the Verses Labels for GN Tab
    def create_all_verses_labels_to_gn_tab(self):
        for num in range(176):
            verse_number_label = QLabel(self.gn_scrollAreaContents)
            verse_number_label.setText(f"{num + 1}")
            verse_number_label.setObjectName(f"verse_{num + 1}")
            verse_number_label.setStyleSheet("""QLabel{
            background-color: rgb(223, 223, 166);
            }""")
            verse_number_label.setFont(my_font)
            verse_number_label.setMaximumSize(50, 50)

            verse_content_label = QLabel(self.gn_scrollAreaContents)
            verse_content_label.setText(f"Verse Content {num + 1}\n\n\n\n")
            verse_content_label.setObjectName(f"verse_content_{num + 1}")
            verse_content_label.setStyleSheet("""QLabel{
                        background-color: rgb(121, 121, 90);
                        border-radius: 10px;
                        }""")
            verse_content_label.setFont(my_font)

            self.gn_gridLayout.addWidget(verse_number_label, num, 0)
            self.gn_gridLayout.addWidget(verse_content_label, num, 1)

    # Create and Make Available All the Verses Labels for AMP Tab
    def create_all_verses_labels_to_amp_tab(self):
        for num in range(176):
            verse_number_label = QLabel(self.amp_ScrollAreaContents)
            verse_number_label.setText(f"Verse {num + 1}")
            verse_number_label.setObjectName(f"verse_{num + 1}")
            verse_number_label.setStyleSheet("""QLabel{
            background-color: rgb(223, 223, 166);
            }""")
            verse_number_label.setFont(my_font)
            verse_number_label.setMaximumSize(50, 50)

            verse_content_label = QLabel(self.amp_ScrollAreaContents)
            verse_content_label.setText(f"Verse Content {num + 1}")
            verse_content_label.setObjectName(f"verse_content_{num + 1}")
            verse_content_label.setStyleSheet("""QLabel{
                        background-color: rgb(121, 121, 90);
                        border-radius: 10px;
                        }""")
            verse_content_label.setFont(my_font)

            self.amp_gridLayout.addWidget(verse_number_label, num, 0)
            self.amp_gridLayout.addWidget(verse_content_label, num, 1)

    # Create and Make Available All the Verses Labels for NJB Tab
    def create_all_verses_labels_to_njb_tab(self):
        for num in range(176):
            verse_number_label = QLabel(self.njb_ScrollAreaContents)
            verse_number_label.setText(f"Verse {num + 1}")
            verse_number_label.setObjectName(f"verse_{num + 1}")
            verse_number_label.setStyleSheet("""QLabel{
            background-color: rgb(223, 223, 166);
            }""")
            verse_number_label.setFont(my_font)
            verse_number_label.setMaximumSize(50, 50)

            verse_content_label = QLabel(self.njb_ScrollAreaContents)
            verse_content_label.setText(f"Verse Content {num + 1}")
            verse_content_label.setObjectName(f"verse_content_{num + 1}")
            verse_content_label.setStyleSheet("""QLabel{
                        background-color: rgb(121, 121, 90);
                        border-radius: 10px;
                        }""")
            verse_content_label.setFont(my_font)

            self.njb_gridLayout.addWidget(verse_number_label, num, 0)
            self.njb_gridLayout.addWidget(verse_content_label, num, 1)

    # Create and Make Available All the Verses Labels for KJV Tab
    def create_all_verses_labels_to_kjv_tab(self):
        for num in range(176):
            verse_number_label = QLabel(self.kjv_ScrollAreaContents)
            verse_number_label.setText(f"Verse {num + 1}")
            verse_number_label.setObjectName(f"verse_{num + 1}")
            verse_number_label.setStyleSheet("""QLabel{
            background-color: rgb(223, 223, 166);
            }""")
            verse_number_label.setFont(my_font)
            verse_number_label.setMaximumSize(50, 50)

            verse_content_label = QLabel(self.kjv_ScrollAreaContents)
            verse_content_label.setText(f"Verse Content {num + 1}")
            verse_content_label.setObjectName(f"verse_content_{num + 1}")
            verse_content_label.setStyleSheet("""QLabel{
                        background-color: rgb(121, 121, 90);
                        border-radius: 10px;
                        }""")
            verse_content_label.setFont(my_font)

            self.kjv_gridLayout.addWidget(verse_number_label, num, 0)
            self.kjv_gridLayout.addWidget(verse_content_label, num, 1)

    # Upgrade the bible-books buttons a bit
    def upgrade_bible_books_buttons(self):
        for book_name in books_obj_name:
            find_widget(self.bibleBooksFrame, QtWidgets.QPushButton, book_name).setAutoExclusive(True)