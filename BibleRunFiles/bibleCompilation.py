from typing import List

def no_chapters(book: str, chapters:int)-> List:
    _list = []
    for num_ in range(chapters):
        _list.append(f"{book} {num_ + 1}")
    return _list

print(no_chapters("Genesis", 31))


from BibleRunFiles.Bible_Books import *
from Bible_Content.TheNewJerusalemBible.BookOfGenesis import *

def sort_A_to_Z(what_to_sort: list[str]):
    sorted_ = []
    print(len(what_to_sort))
    while len(what_to_sort) > 0:
        mini = min(what_to_sort)
        print(mini)
        sorted_.append(mini)
        what_to_sort.remove(mini)
    print(len(sorted_))

def allBooks():
    for book in wholeBible:
        print(book)


new_jerusalem = {
    "Genesis": {"Chapter 1": genesis_1, "Chapter 2": genesis_2, "Chapter 3": genesis_3, "Chapter 4": genesis_4}
}

