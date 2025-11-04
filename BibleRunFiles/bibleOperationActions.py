from BibleRunFiles.bibleCompilation import *

class BibleOperationActions:

    @staticmethod
    def minVerse(*chapterContent):
        pass

    @staticmethod
    def maxVerse(*chapterContent):
        pass

    @staticmethod
    def getChapterByVersion( version: str, book: str,chapter:int ):
        try:
            if version in bibleVersions and book in wholeBibleBooks and chapter in wholeBibleContent[version][book]:
                response= wholeBibleContent[version][book][chapter]
                return response
            else:
                return None
        except KeyError:
            return None

    def getVerseByVersion(self, version: str, book: str, chapter: int, verse: int):
        try:
            if version in bibleVersions and book in wholeBibleBooks and chapter in wholeBibleContent[version][book]:
                response = self.getChapterByVersion(version, book, chapter)[verse]
                return response
            else:
                return None
        except KeyError:
            return None
