from bible_books import wholeBible, pentecostalBible
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

g = dict(zip([1,2,3], ['a', 'b', 'c']))
#print(g)

wholeBibleContent = \
    {
        "New Jerusalem" : dict(),
        "Good News": '',
        "King James": '',
        "Amplified": ''
    }

new_jerusalem = {
    "Genesis": {"Chapter 1": genesis_1, "Chapter 2": genesis_2, "Chapter 3": genesis_3, "Chapter 4": genesis_4}
}
print(new_jerusalem["Genesis"]['Chapter 1'][14])

#print(wholeBibleContent['New Jerusalem'])