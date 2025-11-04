

from Bible_Content.KingJamesVersion.BookOfJude import *


traditionalBibleVersions:list[str]= ["The New Jerusalem", "Good News"]

modernBibleVersions:list[str]= ["King James"]

bibleVersions = traditionalBibleVersions + modernBibleVersions

oldTestament = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel",
                "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther","Job",
                "Psalms", "Proverbs", "Ecclesiastes", "Song of Songs", "Isaiah", "Jeremiah", "Lamentations",
                "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
                "Zephaniah", "Haggai", "Zechariah", "Malachi",]

deuterocanonicalTestament = ["Tobit", "Judith", "Esther(Greek)", "Wisdom of Solomon", "Sirach", "Baruch", "Letter of Jeremiah",
                             "Song of the Three Young Men", "Susana", "Bel and the Dragon", "1 Maccabees", "2 Maccabees"]

newTestament = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians",
                "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
                "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation" ]

wholeBibleBooks = oldTestament + deuterocanonicalTestament + newTestament
pentecostalBible = oldTestament + newTestament

wholeBibleContent = \
    {
        "The New Jerusalem" : {},
        "Good News": {},
        "King James": {"Jude": {1: chapter_1}},
        "Amplified": {}
    }


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
    for book in wholeBibleBooks:
        print(book)

#sort_A_to_Z(wholeBibleBooks)
#allBooks()

