from PySide6.QtWidgets import QPushButton
from PySide6 import QtWidgets
from main_bible_app.bible_window_organisation.bible_organisation_and_display.set_app_defaults import Set_App_Default_Texts, deu_books_obj_names
from needful_extra_functions import books_obj_name, find_widget, compile_chapter_numbers



class Set_App_Functionalities(Set_App_Default_Texts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_menu.clicked.connect(self.pushbutton_menu_clicked)
        self.hide_show_bible_books_pushbutton.clicked.connect(self.hide_show_books_clicked)
        self.bibleContentTabWidget.currentChanged.connect(self.bible_books_display_functionality)
        self.pushButton_bible_fun_facts.clicked.connect(self.bible_fun_facts_clicked)
        self.pushButton_bible_study_plan.clicked.connect(self.bible_study_plan_clicked)
        self.pushButton_study_topic.clicked.connect(self.bible_study_topics_clicked)
        self.pushButton_study_character.clicked.connect(self.bible_study_character_clicked)
        self.pushButton_bible_settings.clicked.connect(self.bible_settings_clicked)
        self.pushButton_bible_quit_app.clicked.connect(self.bible_quit_clicked)
        self.set_bible_books_actions()
        self.set_books_chapters_actions()

    # What happens when pushbutton menu is clicked
    def pushbutton_menu_clicked(self):
        if self.pushButton_menu.isChecked():
            self.leftScrollArea.hide()
        else:
            self.leftScrollArea.show()
        self.chaptersNumberFrame.hide()

    # What happens when hide-show-books button is clicked
    def hide_show_books_clicked(self):

        if self.hide_show_bible_books_pushbutton.isChecked():
            self.bibleBooksFrame.hide()
        else:
            self.bibleBooksFrame.show()
        self.chaptersNumberFrame.hide()

    # What happens when bible-content-tabWidget current widget is changed
    def bible_books_display_functionality(self):

        if self.bibleContentTabWidget.currentIndex() == 1:
            for x in deu_books_obj_names:
                self.bibleBooksFrame.findChild(QPushButton, x).setVisible(False)

        if self.bibleContentTabWidget.currentIndex() == 2:
            for x in deu_books_obj_names:
                self.bibleBooksFrame.findChild(QPushButton, x).setVisible(False)

        if self.bibleContentTabWidget.currentIndex() == 0:
            for x in deu_books_obj_names:
                self.bibleBooksFrame.findChild(QPushButton, x).setVisible(True)

        if self.bibleContentTabWidget.currentIndex() == 3:
            for x in deu_books_obj_names:
                self.bibleBooksFrame.findChild(QPushButton, x).setVisible(True)

    # What happens when bible-fun-facts button is clicked
    def bible_fun_facts_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    # What happens when bible-plan button is clicked
    def bible_study_plan_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    # What happens when bible-study-topics button is clicked
    def bible_study_topics_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

    # What happens when bible-study-character button is clicked
    def bible_study_character_clicked(self):
        self.stackedWidget.setCurrentIndex(4)

    # What happens when bible-settings button is clicked
    def bible_settings_clicked(self):
         self.stackedWidget.setCurrentIndex(5)

    # What happens when bible-quit button is clicked
    def bible_quit_clicked(self):
        self.close()

    # What happens when any of the bible-books buttons is clicked
    def set_bible_books_actions(self):
        for obj_name in books_obj_name:
            find_widget(self.bibleBooksFrame, QtWidgets.QPushButton, obj_name).clicked.connect(self.alter_number_of_chapters)

    # Alter the number of chapters, according to the number of chapters available to a book
    def alter_number_of_chapters(self):
        for obj_name in books_obj_name:
            the_widget = find_widget(self.bibleBooksFrame, QtWidgets.QPushButton, obj_name)
            if the_widget.isChecked():
                self.gn_book_label.setText(the_widget.text())
                self.amp_book_label.setText(the_widget.text())
                self.njb_book_label.setText(the_widget.text())
                self.kjv_book_label.setText(the_widget.text())
                for the_num in range(150):
                    if the_num < compile_chapter_numbers()[obj_name]:
                        find_widget(self.chaptersNumberInnerFrame, QtWidgets.QPushButton, f"chapter_{the_num + 1}").show()
                    else:
                        find_widget(self.chaptersNumberInnerFrame, QtWidgets.QPushButton, f"chapter_{the_num + 1}").hide()

    # What happens when any of books-chapters button is clicked
    def set_books_chapters_actions(self):
        for num in range(150):
            find_widget(self.chaptersNumberInnerFrame, QtWidgets.QPushButton, f"chapter_{num+1}").clicked.connect(self.alter_number_of_verses)

    @staticmethod
    # Alter the number of verses, according to the number of verses available to a chapter of a book
    def alter_number_of_verses():
        print("Is going to be altered")