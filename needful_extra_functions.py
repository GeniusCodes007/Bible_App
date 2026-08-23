import PySide6 as py_sd6
from PySide6.QtGui import QFont

my_font = QFont()
my_font.setFamilies([u"Segoe Print"])
my_font.setPointSize(10)
my_font.setBold(True)

def find_widget(parent_widget: py_sd6.QtWidgets, child_widget_type: py_sd6.QtWidgets,widget_object_name: str):
    widget = parent_widget.findChild(child_widget_type, widget_object_name)
    return widget


old_test_books_obj_names = ["genesis","exodus","leviticus","numbers","deuteronomy","joshua","judges","ruth","samuel_1","samuel_2",
"kings_1","kings_2","chronicles_1","chronicles_2","ezra","nehemiah","esther","job","psalms",
"proverbs","ecclesiastes","song_of_songs","isaiah","jeremiah","lamentations","ezekiel","daniel",
"hosea","joel","amos","obadiah","jonah","micah","nahum","habakkuk","zephaniah","haggai","zechariah", "malachi",]

deu_books_obj_names = ["tobit", "judith", "esther_greek", "wisdom_of_solomon", "sirach", "baruch",
                          "letter_of_jeremiah", "song_of_the_three_young_men", "susana", "bel_and_the_dragon",
                          "maccabees_1", "maccabees_2"]

new_test_books_obj_names= ["matthew","mark","luke","john","acts","romans","corinthians_1","corinthians_2","galatians","ephesians","philippians",
"colossians","thessalonians_1","thessalonians_2","timothy_1","timothy_2","titus","philemon","hebrews","james",
"peter_1","peter_2","john_1","john_2","john_3","jude","revelation"]


books_obj_name = old_test_books_obj_names + deu_books_obj_names + new_test_books_obj_names

chapter_number = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4,
                  14, 16, 16, 19, 51, 6, 1, 1, 1, 1, 16, 15, 28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1,
                  1, 1, 22]





def compile_chapter_numbers():#gridlayout: QtWidgets.QGridLayout, grid_layout_parent_widget: QtWidgets.QWidget, widget_to_add: QtWidgets.QWidget):
    books_chapters_number:dict[str, int] = {}
    for num in range(len(books_obj_name)):
        new_dict:dict[str, int] = {books_obj_name[num]:chapter_number[num]}
        books_chapters_number.update(new_dict)
    return books_chapters_number
#print(compile_chapter_numbers())