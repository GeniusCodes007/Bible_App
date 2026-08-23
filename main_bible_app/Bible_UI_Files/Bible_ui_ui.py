# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bible_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Bible_MainWindow(object):
    def setupUi(self, Bible_MainWindow):
        if not Bible_MainWindow.objectName():
            Bible_MainWindow.setObjectName(u"Bible_MainWindow")
        Bible_MainWindow.resize(1149, 542)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        Bible_MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../bible_icons/bible_icon_5.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Bible_MainWindow.setWindowIcon(icon)
        Bible_MainWindow.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.centralwidget = QWidget(Bible_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_main_frame_verticalLayout = QVBoxLayout()
        self.left_main_frame_verticalLayout.setObjectName(u"left_main_frame_verticalLayout")
        self.pushButton_menu = QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setMinimumSize(QSize(45, 45))
        self.pushButton_menu.setMaximumSize(QSize(45, 45))
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_menu.setFont(font1)
        self.pushButton_menu.setStyleSheet(u"")
        self.pushButton_menu.setIconSize(QSize(35, 35))
        self.pushButton_menu.setCheckable(True)

        self.left_main_frame_verticalLayout.addWidget(self.pushButton_menu, 0, Qt.AlignmentFlag.AlignTop)

        self.leftScrollArea = QScrollArea(self.centralwidget)
        self.leftScrollArea.setObjectName(u"leftScrollArea")
        self.leftScrollArea.setMinimumSize(QSize(254, 450))
        self.leftScrollArea.setMaximumSize(QSize(229, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe Print"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.leftScrollArea.setFont(font2)
        self.leftScrollArea.setStyleSheet(u"")
        self.leftScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.leftScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.leftScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.leftScrollArea.setWidgetResizable(True)
        self.leftScrollAreaContents = QWidget()
        self.leftScrollAreaContents.setObjectName(u"leftScrollAreaContents")
        self.leftScrollAreaContents.setGeometry(QRect(0, 0, 238, 2513))
        self.verticalLayout_23 = QVBoxLayout(self.leftScrollAreaContents)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.hide_show_bible_books_pushbutton = QPushButton(self.leftScrollAreaContents)
        self.hide_show_bible_books_pushbutton.setObjectName(u"hide_show_bible_books_pushbutton")
        self.hide_show_bible_books_pushbutton.setMinimumSize(QSize(220, 33))
        self.hide_show_bible_books_pushbutton.setMaximumSize(QSize(220, 33))
        font3 = QFont()
        font3.setFamilies([u"Segoe Print"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.hide_show_bible_books_pushbutton.setFont(font3)
        self.hide_show_bible_books_pushbutton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"content_hidden.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u"content_shown.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.hide_show_bible_books_pushbutton.setIcon(icon1)
        self.hide_show_bible_books_pushbutton.setIconSize(QSize(100, 25))
        self.hide_show_bible_books_pushbutton.setCheckable(True)

        self.verticalLayout_23.addWidget(self.hide_show_bible_books_pushbutton)

        self.bibleBooksFrame = QFrame(self.leftScrollAreaContents)
        self.bibleBooksFrame.setObjectName(u"bibleBooksFrame")
        self.bibleBooksFrame.setMinimumSize(QSize(220, 2200))
        self.bibleBooksFrame.setMaximumSize(QSize(211, 16777215))
        self.bibleBooksFrame.setFont(font2)
        self.bibleBooksFrame.setStyleSheet(u"")
        self.bibleBooksFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.bibleBooksFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_21 = QVBoxLayout(self.bibleBooksFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.bibleBooksGridLayout = QGridLayout()
        self.bibleBooksGridLayout.setObjectName(u"bibleBooksGridLayout")
        self.esther = QPushButton(self.bibleBooksFrame)
        self.esther.setObjectName(u"esther")
        self.esther.setCheckable(True)
        self.esther.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.esther, 17, 0, 1, 1)

        self.hebrews = QPushButton(self.bibleBooksFrame)
        self.hebrews.setObjectName(u"hebrews")
        self.hebrews.setCheckable(True)
        self.hebrews.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.hebrews, 70, 0, 1, 1)

        self.romans = QPushButton(self.bibleBooksFrame)
        self.romans.setObjectName(u"romans")
        self.romans.setCheckable(True)
        self.romans.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.romans, 59, 0, 1, 1)

        self.chronicles_2 = QPushButton(self.bibleBooksFrame)
        self.chronicles_2.setObjectName(u"chronicles_2")
        self.chronicles_2.setCheckable(True)
        self.chronicles_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.chronicles_2, 14, 0, 1, 1)

        self.jonah = QPushButton(self.bibleBooksFrame)
        self.jonah.setObjectName(u"jonah")
        self.jonah.setCheckable(True)
        self.jonah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.jonah, 32, 0, 1, 1)

        self.song_of_the_three_young_men = QPushButton(self.bibleBooksFrame)
        self.song_of_the_three_young_men.setObjectName(u"song_of_the_three_young_men")
        self.song_of_the_three_young_men.setCheckable(True)
        self.song_of_the_three_young_men.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.song_of_the_three_young_men, 47, 0, 1, 1)

        self.timothy_2 = QPushButton(self.bibleBooksFrame)
        self.timothy_2.setObjectName(u"timothy_2")
        self.timothy_2.setCheckable(True)
        self.timothy_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.timothy_2, 67, 0, 1, 1)

        self.maccabees_2 = QPushButton(self.bibleBooksFrame)
        self.maccabees_2.setObjectName(u"maccabees_2")
        self.maccabees_2.setCheckable(True)
        self.maccabees_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.maccabees_2, 51, 0, 1, 1)

        self.john = QPushButton(self.bibleBooksFrame)
        self.john.setObjectName(u"john")
        self.john.setCheckable(True)
        self.john.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.john, 55, 0, 1, 1)

        self.joshua = QPushButton(self.bibleBooksFrame)
        self.joshua.setObjectName(u"joshua")
        self.joshua.setCheckable(True)
        self.joshua.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.joshua, 6, 0, 1, 1)

        self.joel = QPushButton(self.bibleBooksFrame)
        self.joel.setObjectName(u"joel")
        self.joel.setCheckable(True)
        self.joel.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.joel, 29, 0, 1, 1)

        self.galatians = QPushButton(self.bibleBooksFrame)
        self.galatians.setObjectName(u"galatians")
        self.galatians.setCheckable(True)
        self.galatians.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.galatians, 60, 0, 1, 1)

        self.judges = QPushButton(self.bibleBooksFrame)
        self.judges.setObjectName(u"judges")
        self.judges.setCheckable(True)
        self.judges.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.judges, 7, 0, 1, 1)

        self.revelation = QPushButton(self.bibleBooksFrame)
        self.revelation.setObjectName(u"revelation")
        self.revelation.setCheckable(True)
        self.revelation.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.revelation, 78, 0, 1, 1)

        self.thessalonians_2 = QPushButton(self.bibleBooksFrame)
        self.thessalonians_2.setObjectName(u"thessalonians_2")
        self.thessalonians_2.setCheckable(True)
        self.thessalonians_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.thessalonians_2, 65, 0, 1, 1)

        self.corinthians_1 = QPushButton(self.bibleBooksFrame)
        self.corinthians_1.setObjectName(u"corinthians_1")

        self.bibleBooksGridLayout.addWidget(self.corinthians_1, 57, 0, 1, 1)

        self.hosea = QPushButton(self.bibleBooksFrame)
        self.hosea.setObjectName(u"hosea")
        self.hosea.setCheckable(True)
        self.hosea.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.hosea, 28, 0, 1, 1)

        self.ephesians = QPushButton(self.bibleBooksFrame)
        self.ephesians.setObjectName(u"ephesians")
        self.ephesians.setCheckable(True)
        self.ephesians.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.ephesians, 61, 0, 1, 1)

        self.numbers = QPushButton(self.bibleBooksFrame)
        self.numbers.setObjectName(u"numbers")
        self.numbers.setCheckable(True)
        self.numbers.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.numbers, 4, 0, 1, 1)

        self.mark = QPushButton(self.bibleBooksFrame)
        self.mark.setObjectName(u"mark")
        self.mark.setCheckable(True)
        self.mark.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.mark, 53, 0, 1, 1)

        self.maccabees_1 = QPushButton(self.bibleBooksFrame)
        self.maccabees_1.setObjectName(u"maccabees_1")
        self.maccabees_1.setCheckable(True)
        self.maccabees_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.maccabees_1, 50, 0, 1, 1)

        self.judith = QPushButton(self.bibleBooksFrame)
        self.judith.setObjectName(u"judith")
        self.judith.setCheckable(True)
        self.judith.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.judith, 41, 0, 1, 1)

        self.micah = QPushButton(self.bibleBooksFrame)
        self.micah.setObjectName(u"micah")
        self.micah.setCheckable(True)
        self.micah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.micah, 33, 0, 1, 1)

        self.job = QPushButton(self.bibleBooksFrame)
        self.job.setObjectName(u"job")
        self.job.setCheckable(True)
        self.job.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.job, 18, 0, 1, 1)

        self.luke = QPushButton(self.bibleBooksFrame)
        self.luke.setObjectName(u"luke")
        self.luke.setCheckable(True)
        self.luke.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.luke, 54, 0, 1, 1)

        self.ezekiel = QPushButton(self.bibleBooksFrame)
        self.ezekiel.setObjectName(u"ezekiel")
        self.ezekiel.setCheckable(True)
        self.ezekiel.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.ezekiel, 26, 0, 1, 1)

        self.ruth = QPushButton(self.bibleBooksFrame)
        self.ruth.setObjectName(u"ruth")
        self.ruth.setCheckable(True)
        self.ruth.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.ruth, 8, 0, 1, 1)

        self.amos = QPushButton(self.bibleBooksFrame)
        self.amos.setObjectName(u"amos")
        self.amos.setCheckable(True)
        self.amos.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.amos, 30, 0, 1, 1)

        self.peter_2 = QPushButton(self.bibleBooksFrame)
        self.peter_2.setObjectName(u"peter_2")
        self.peter_2.setCheckable(True)
        self.peter_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.peter_2, 73, 0, 1, 1)

        self.sirach = QPushButton(self.bibleBooksFrame)
        self.sirach.setObjectName(u"sirach")
        self.sirach.setCheckable(True)
        self.sirach.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.sirach, 44, 0, 1, 1)

        self.kings_2 = QPushButton(self.bibleBooksFrame)
        self.kings_2.setObjectName(u"kings_2")
        self.kings_2.setCheckable(True)
        self.kings_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.kings_2, 12, 0, 1, 1)

        self.song_of_songs = QPushButton(self.bibleBooksFrame)
        self.song_of_songs.setObjectName(u"song_of_songs")
        self.song_of_songs.setCheckable(True)
        self.song_of_songs.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.song_of_songs, 22, 0, 1, 1)

        self.wisdom_of_solomon = QPushButton(self.bibleBooksFrame)
        self.wisdom_of_solomon.setObjectName(u"wisdom_of_solomon")
        self.wisdom_of_solomon.setCheckable(True)
        self.wisdom_of_solomon.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.wisdom_of_solomon, 43, 0, 1, 1)

        self.psalms = QPushButton(self.bibleBooksFrame)
        self.psalms.setObjectName(u"psalms")
        self.psalms.setCheckable(True)
        self.psalms.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.psalms, 19, 0, 1, 1)

        self.john_2 = QPushButton(self.bibleBooksFrame)
        self.john_2.setObjectName(u"john_2")
        self.john_2.setCheckable(True)
        self.john_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.john_2, 75, 0, 1, 1)

        self.jeremiah = QPushButton(self.bibleBooksFrame)
        self.jeremiah.setObjectName(u"jeremiah")
        self.jeremiah.setCheckable(True)
        self.jeremiah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.jeremiah, 24, 0, 1, 1)

        self.john_1 = QPushButton(self.bibleBooksFrame)
        self.john_1.setObjectName(u"john_1")
        self.john_1.setCheckable(True)
        self.john_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.john_1, 74, 0, 1, 1)

        self.timothy_1 = QPushButton(self.bibleBooksFrame)
        self.timothy_1.setObjectName(u"timothy_1")
        self.timothy_1.setCheckable(True)
        self.timothy_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.timothy_1, 66, 0, 1, 1)

        self.tobit = QPushButton(self.bibleBooksFrame)
        self.tobit.setObjectName(u"tobit")
        self.tobit.setCheckable(True)
        self.tobit.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.tobit, 40, 0, 1, 1)

        self.samuel_1 = QPushButton(self.bibleBooksFrame)
        self.samuel_1.setObjectName(u"samuel_1")
        self.samuel_1.setCheckable(True)
        self.samuel_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.samuel_1, 9, 0, 1, 1)

        self.nehemiah = QPushButton(self.bibleBooksFrame)
        self.nehemiah.setObjectName(u"nehemiah")
        self.nehemiah.setCheckable(True)
        self.nehemiah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.nehemiah, 16, 0, 1, 1)

        self.bel_and_the_dragon = QPushButton(self.bibleBooksFrame)
        self.bel_and_the_dragon.setObjectName(u"bel_and_the_dragon")
        self.bel_and_the_dragon.setCheckable(True)
        self.bel_and_the_dragon.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.bel_and_the_dragon, 49, 0, 1, 1)

        self.proverbs = QPushButton(self.bibleBooksFrame)
        self.proverbs.setObjectName(u"proverbs")
        self.proverbs.setCheckable(True)
        self.proverbs.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.proverbs, 20, 0, 1, 1)

        self.isaiah = QPushButton(self.bibleBooksFrame)
        self.isaiah.setObjectName(u"isaiah")
        self.isaiah.setCheckable(True)
        self.isaiah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.isaiah, 23, 0, 1, 1)

        self.acts = QPushButton(self.bibleBooksFrame)
        self.acts.setObjectName(u"acts")
        self.acts.setCheckable(True)
        self.acts.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.acts, 56, 0, 1, 1)

        self.genesis = QPushButton(self.bibleBooksFrame)
        self.genesis.setObjectName(u"genesis")
        self.genesis.setCheckable(True)
        self.genesis.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.genesis, 1, 0, 1, 1)

        self.colossians = QPushButton(self.bibleBooksFrame)
        self.colossians.setObjectName(u"colossians")
        self.colossians.setCheckable(True)
        self.colossians.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.colossians, 63, 0, 1, 1)

        self.daniel = QPushButton(self.bibleBooksFrame)
        self.daniel.setObjectName(u"daniel")
        self.daniel.setCheckable(True)
        self.daniel.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.daniel, 27, 0, 1, 1)

        self.leviticus = QPushButton(self.bibleBooksFrame)
        self.leviticus.setObjectName(u"leviticus")
        self.leviticus.setCheckable(True)
        self.leviticus.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.leviticus, 3, 0, 1, 1)

        self.ezra = QPushButton(self.bibleBooksFrame)
        self.ezra.setObjectName(u"ezra")
        self.ezra.setCheckable(True)
        self.ezra.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.ezra, 15, 0, 1, 1)

        self.esther_greek = QPushButton(self.bibleBooksFrame)
        self.esther_greek.setObjectName(u"esther_greek")
        self.esther_greek.setCheckable(True)
        self.esther_greek.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.esther_greek, 42, 0, 1, 1)

        self.philippians = QPushButton(self.bibleBooksFrame)
        self.philippians.setObjectName(u"philippians")
        self.philippians.setCheckable(True)
        self.philippians.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.philippians, 62, 0, 1, 1)

        self.haggai = QPushButton(self.bibleBooksFrame)
        self.haggai.setObjectName(u"haggai")
        self.haggai.setCheckable(True)
        self.haggai.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.haggai, 37, 0, 1, 1)

        self.john_3 = QPushButton(self.bibleBooksFrame)
        self.john_3.setObjectName(u"john_3")
        self.john_3.setCheckable(True)
        self.john_3.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.john_3, 76, 0, 1, 1)

        self.zechariah = QPushButton(self.bibleBooksFrame)
        self.zechariah.setObjectName(u"zechariah")
        self.zechariah.setCheckable(True)
        self.zechariah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.zechariah, 38, 0, 1, 1)

        self.philemon = QPushButton(self.bibleBooksFrame)
        self.philemon.setObjectName(u"philemon")
        self.philemon.setCheckable(True)
        self.philemon.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.philemon, 69, 0, 1, 1)

        self.jude = QPushButton(self.bibleBooksFrame)
        self.jude.setObjectName(u"jude")
        self.jude.setCheckable(True)
        self.jude.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.jude, 77, 0, 1, 1)

        self.exodus = QPushButton(self.bibleBooksFrame)
        self.exodus.setObjectName(u"exodus")
        self.exodus.setCheckable(True)
        self.exodus.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.exodus, 2, 0, 1, 1)

        self.thessalonians_1 = QPushButton(self.bibleBooksFrame)
        self.thessalonians_1.setObjectName(u"thessalonians_1")
        self.thessalonians_1.setCheckable(True)
        self.thessalonians_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.thessalonians_1, 64, 0, 1, 1)

        self.malachi = QPushButton(self.bibleBooksFrame)
        self.malachi.setObjectName(u"malachi")
        self.malachi.setCheckable(True)
        self.malachi.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.malachi, 39, 0, 1, 1)

        self.habakkuk = QPushButton(self.bibleBooksFrame)
        self.habakkuk.setObjectName(u"habakkuk")
        self.habakkuk.setCheckable(True)
        self.habakkuk.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.habakkuk, 35, 0, 1, 1)

        self.james = QPushButton(self.bibleBooksFrame)
        self.james.setObjectName(u"james")
        self.james.setCheckable(True)
        self.james.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.james, 71, 0, 1, 1)

        self.lamentations = QPushButton(self.bibleBooksFrame)
        self.lamentations.setObjectName(u"lamentations")
        self.lamentations.setCheckable(True)
        self.lamentations.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.lamentations, 25, 0, 1, 1)

        self.kings_1 = QPushButton(self.bibleBooksFrame)
        self.kings_1.setObjectName(u"kings_1")
        self.kings_1.setCheckable(True)
        self.kings_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.kings_1, 11, 0, 1, 1)

        self.samuel_2 = QPushButton(self.bibleBooksFrame)
        self.samuel_2.setObjectName(u"samuel_2")
        self.samuel_2.setCheckable(True)
        self.samuel_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.samuel_2, 10, 0, 1, 1)

        self.matthew = QPushButton(self.bibleBooksFrame)
        self.matthew.setObjectName(u"matthew")
        self.matthew.setCheckable(True)
        self.matthew.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.matthew, 52, 0, 1, 1)

        self.chronicles_1 = QPushButton(self.bibleBooksFrame)
        self.chronicles_1.setObjectName(u"chronicles_1")
        self.chronicles_1.setCheckable(True)
        self.chronicles_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.chronicles_1, 13, 0, 1, 1)

        self.zephaniah = QPushButton(self.bibleBooksFrame)
        self.zephaniah.setObjectName(u"zephaniah")
        self.zephaniah.setCheckable(True)
        self.zephaniah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.zephaniah, 36, 0, 1, 1)

        self.susana = QPushButton(self.bibleBooksFrame)
        self.susana.setObjectName(u"susana")
        self.susana.setCheckable(True)
        self.susana.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.susana, 48, 0, 1, 1)

        self.letter_of_jeremiah = QPushButton(self.bibleBooksFrame)
        self.letter_of_jeremiah.setObjectName(u"letter_of_jeremiah")
        self.letter_of_jeremiah.setCheckable(True)
        self.letter_of_jeremiah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.letter_of_jeremiah, 46, 0, 1, 1)

        self.obadiah = QPushButton(self.bibleBooksFrame)
        self.obadiah.setObjectName(u"obadiah")
        self.obadiah.setCheckable(True)
        self.obadiah.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.obadiah, 31, 0, 1, 1)

        self.peter_1 = QPushButton(self.bibleBooksFrame)
        self.peter_1.setObjectName(u"peter_1")
        self.peter_1.setCheckable(True)
        self.peter_1.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.peter_1, 72, 0, 1, 1)

        self.titus = QPushButton(self.bibleBooksFrame)
        self.titus.setObjectName(u"titus")
        self.titus.setCheckable(True)
        self.titus.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.titus, 68, 0, 1, 1)

        self.nahum = QPushButton(self.bibleBooksFrame)
        self.nahum.setObjectName(u"nahum")
        self.nahum.setCheckable(True)
        self.nahum.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.nahum, 34, 0, 1, 1)

        self.deuteronomy = QPushButton(self.bibleBooksFrame)
        self.deuteronomy.setObjectName(u"deuteronomy")
        self.deuteronomy.setCheckable(True)
        self.deuteronomy.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.deuteronomy, 5, 0, 1, 1)

        self.baruch = QPushButton(self.bibleBooksFrame)
        self.baruch.setObjectName(u"baruch")
        self.baruch.setCheckable(True)
        self.baruch.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.baruch, 45, 0, 1, 1)

        self.ecclesiastes = QPushButton(self.bibleBooksFrame)
        self.ecclesiastes.setObjectName(u"ecclesiastes")
        self.ecclesiastes.setCheckable(True)
        self.ecclesiastes.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.ecclesiastes, 21, 0, 1, 1)

        self.corinthians_2 = QPushButton(self.bibleBooksFrame)
        self.corinthians_2.setObjectName(u"corinthians_2")

        self.bibleBooksGridLayout.addWidget(self.corinthians_2, 58, 0, 1, 1)


        self.verticalLayout_21.addLayout(self.bibleBooksGridLayout)


        self.verticalLayout_23.addWidget(self.bibleBooksFrame)

        self.extras_Frame = QFrame(self.leftScrollAreaContents)
        self.extras_Frame.setObjectName(u"extras_Frame")
        self.extras_Frame.setMinimumSize(QSize(0, 250))
        self.extras_Frame.setStyleSheet(u"")
        self.extras_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.extras_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.extras_Frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_bible_fun_facts = QPushButton(self.extras_Frame)
        self.pushButton_bible_fun_facts.setObjectName(u"pushButton_bible_fun_facts")
        self.pushButton_bible_fun_facts.setFont(font2)
        self.pushButton_bible_fun_facts.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.pushButton_bible_fun_facts)

        self.pushButton_bible_study_plan = QPushButton(self.extras_Frame)
        self.pushButton_bible_study_plan.setObjectName(u"pushButton_bible_study_plan")
        self.pushButton_bible_study_plan.setFont(font2)
        self.pushButton_bible_study_plan.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.pushButton_bible_study_plan)

        self.pushButton_study_topic = QPushButton(self.extras_Frame)
        self.pushButton_study_topic.setObjectName(u"pushButton_study_topic")
        self.pushButton_study_topic.setFont(font2)
        self.pushButton_study_topic.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.pushButton_study_topic)

        self.pushButton_study_character = QPushButton(self.extras_Frame)
        self.pushButton_study_character.setObjectName(u"pushButton_study_character")

        self.verticalLayout_19.addWidget(self.pushButton_study_character)

        self.pushButton_bible_settings = QPushButton(self.extras_Frame)
        self.pushButton_bible_settings.setObjectName(u"pushButton_bible_settings")

        self.verticalLayout_19.addWidget(self.pushButton_bible_settings)

        self.pushButton_bible_quit_app = QPushButton(self.extras_Frame)
        self.pushButton_bible_quit_app.setObjectName(u"pushButton_bible_quit_app")

        self.verticalLayout_19.addWidget(self.pushButton_bible_quit_app)


        self.verticalLayout_23.addWidget(self.extras_Frame, 0, Qt.AlignmentFlag.AlignBottom)

        self.leftScrollArea.setWidget(self.leftScrollAreaContents)

        self.left_main_frame_verticalLayout.addWidget(self.leftScrollArea)


        self.horizontalLayout.addLayout(self.left_main_frame_verticalLayout)

        self.chaptersNumberFrame = QFrame(self.centralwidget)
        self.chaptersNumberFrame.setObjectName(u"chaptersNumberFrame")
        self.chaptersNumberFrame.setMinimumSize(QSize(0, 524))
        self.chaptersNumberFrame.setMaximumSize(QSize(200, 1000))
        self.chaptersNumberFrame.setStyleSheet(u"")
        self.chaptersNumberFrame.setFrameShape(QFrame.Shape.Panel)
        self.chaptersNumberFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.chaptersNumberFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.book_name_label = QLabel(self.chaptersNumberFrame)
        self.book_name_label.setObjectName(u"book_name_label")
        self.book_name_label.setMinimumSize(QSize(180, 16))
        self.book_name_label.setMaximumSize(QSize(180, 16))
        self.book_name_label.setFont(font2)
        self.book_name_label.setStyleSheet(u"")
        self.book_name_label.setIndent(0)

        self.verticalLayout_3.addWidget(self.book_name_label)

        self.chapterNumberScrollArea = QScrollArea(self.chaptersNumberFrame)
        self.chapterNumberScrollArea.setObjectName(u"chapterNumberScrollArea")
        self.chapterNumberScrollArea.setFont(font2)
        self.chapterNumberScrollArea.setStyleSheet(u"")
        self.chapterNumberScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.chapterNumberScrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.chapterNumberScrollArea.setWidgetResizable(True)
        self.chapters_scrollAreaWidgetContents = QWidget()
        self.chapters_scrollAreaWidgetContents.setObjectName(u"chapters_scrollAreaWidgetContents")
        self.chapters_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 180, 482))
        self.verticalLayout_4 = QVBoxLayout(self.chapters_scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.chaptersNumberInnerFrame = QFrame(self.chapters_scrollAreaWidgetContents)
        self.chaptersNumberInnerFrame.setObjectName(u"chaptersNumberInnerFrame")
        self.chaptersNumberInnerFrame.setFont(font2)
        self.chaptersNumberInnerFrame.setStyleSheet(u"")
        self.chaptersNumberInnerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.chaptersNumberInnerFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.chaptersNumberInnerFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.chaptersNumberGridLayout = QGridLayout()
        self.chaptersNumberGridLayout.setObjectName(u"chaptersNumberGridLayout")

        self.verticalLayout_5.addLayout(self.chaptersNumberGridLayout)


        self.verticalLayout_4.addWidget(self.chaptersNumberInnerFrame)

        self.chapterNumberScrollArea.setWidget(self.chapters_scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.chapterNumberScrollArea)


        self.horizontalLayout.addWidget(self.chaptersNumberFrame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(651, 524))
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.Shape.WinPanel)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.bible_content_display_page = QWidget()
        self.bible_content_display_page.setObjectName(u"bible_content_display_page")
        self.verticalLayout_9 = QVBoxLayout(self.bible_content_display_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.bibleContentTabWidget = QTabWidget(self.bible_content_display_page)
        self.bibleContentTabWidget.setObjectName(u"bibleContentTabWidget")
        self.bibleContentTabWidget.setMinimumSize(QSize(633, 524))
        self.bibleContentTabWidget.setFont(font2)
        self.bibleContentTabWidget.setStyleSheet(u"")
        self.bibleContentTabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.bibleContentTabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.gn_tab = QWidget()
        self.gn_tab.setObjectName(u"gn_tab")
        self.verticalLayout_7 = QVBoxLayout(self.gn_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Good_News_Upper_Frame = QFrame(self.gn_tab)
        self.Good_News_Upper_Frame.setObjectName(u"Good_News_Upper_Frame")
        self.Good_News_Upper_Frame.setMinimumSize(QSize(627, 54))
        self.Good_News_Upper_Frame.setMaximumSize(QSize(16777215, 100))
        self.Good_News_Upper_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.Good_News_Upper_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Good_News_Upper_Frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gn_version_label = QLabel(self.Good_News_Upper_Frame)
        self.gn_version_label.setObjectName(u"gn_version_label")
        self.gn_version_label.setFont(font2)

        self.horizontalLayout_5.addWidget(self.gn_version_label)

        self.gn_book_label = QLabel(self.Good_News_Upper_Frame)
        self.gn_book_label.setObjectName(u"gn_book_label")
        self.gn_book_label.setMinimumSize(QSize(266, 31))
        self.gn_book_label.setMaximumSize(QSize(16777215, 31))
        self.gn_book_label.setFont(font2)
        self.gn_book_label.setIndent(25)

        self.horizontalLayout_5.addWidget(self.gn_book_label)

        self.gn_chapter_label = QLabel(self.Good_News_Upper_Frame)
        self.gn_chapter_label.setObjectName(u"gn_chapter_label")
        self.gn_chapter_label.setMinimumSize(QSize(45, 30))
        self.gn_chapter_label.setMaximumSize(QSize(45, 30))
        self.gn_chapter_label.setFont(font2)
        self.gn_chapter_label.setFrameShape(QFrame.Shape.WinPanel)
        self.gn_chapter_label.setFrameShadow(QFrame.Shadow.Raised)
        self.gn_chapter_label.setIndent(0)

        self.horizontalLayout_5.addWidget(self.gn_chapter_label)


        self.verticalLayout_7.addWidget(self.Good_News_Upper_Frame)

        self.Good_News_Lower_Frame = QFrame(self.gn_tab)
        self.Good_News_Lower_Frame.setObjectName(u"Good_News_Lower_Frame")
        self.Good_News_Lower_Frame.setMaximumSize(QSize(16777215, 41))
        self.Good_News_Lower_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.Good_News_Lower_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Good_News_Lower_Frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gn_previous_pushButton = QPushButton(self.Good_News_Lower_Frame)
        self.gn_previous_pushButton.setObjectName(u"gn_previous_pushButton")
        self.gn_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.gn_previous_pushButton.setFont(font2)
        self.gn_previous_pushButton.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.gn_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.gn_next_pushButton = QPushButton(self.Good_News_Lower_Frame)
        self.gn_next_pushButton.setObjectName(u"gn_next_pushButton")
        self.gn_next_pushButton.setMaximumSize(QSize(102, 24))
        self.gn_next_pushButton.setFont(font2)
        self.gn_next_pushButton.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.gn_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.Good_News_Lower_Frame)

        self.gn_scrollArea = QScrollArea(self.gn_tab)
        self.gn_scrollArea.setObjectName(u"gn_scrollArea")
        self.gn_scrollArea.setMinimumSize(QSize(450, 450))
        self.gn_scrollArea.setStyleSheet(u"")
        self.gn_scrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.gn_scrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.gn_scrollArea.setWidgetResizable(True)
        self.gn_scrollAreaContents = QWidget()
        self.gn_scrollAreaContents.setObjectName(u"gn_scrollAreaContents")
        self.gn_scrollAreaContents.setGeometry(QRect(0, 0, 613, 446))
        self.verticalLayout_8 = QVBoxLayout(self.gn_scrollAreaContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gn_gridLayout = QGridLayout()
        self.gn_gridLayout.setObjectName(u"gn_gridLayout")

        self.verticalLayout_8.addLayout(self.gn_gridLayout)

        self.gn_scrollArea.setWidget(self.gn_scrollAreaContents)

        self.verticalLayout_7.addWidget(self.gn_scrollArea)

        self.bibleContentTabWidget.addTab(self.gn_tab, "")
        self.amp_tab = QWidget()
        self.amp_tab.setObjectName(u"amp_tab")
        self.verticalLayout_6 = QVBoxLayout(self.amp_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Amplified_Upper_Frame = QFrame(self.amp_tab)
        self.Amplified_Upper_Frame.setObjectName(u"Amplified_Upper_Frame")
        self.Amplified_Upper_Frame.setMinimumSize(QSize(627, 54))
        self.Amplified_Upper_Frame.setMaximumSize(QSize(16777215, 100))
        self.Amplified_Upper_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.Amplified_Upper_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Amplified_Upper_Frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.amp_version_label = QLabel(self.Amplified_Upper_Frame)
        self.amp_version_label.setObjectName(u"amp_version_label")
        self.amp_version_label.setFont(font2)

        self.horizontalLayout_10.addWidget(self.amp_version_label)

        self.amp_book_label = QLabel(self.Amplified_Upper_Frame)
        self.amp_book_label.setObjectName(u"amp_book_label")
        self.amp_book_label.setMaximumSize(QSize(16777215, 31))
        self.amp_book_label.setFont(font2)
        self.amp_book_label.setIndent(25)

        self.horizontalLayout_10.addWidget(self.amp_book_label)

        self.amp_chapter_label = QLabel(self.Amplified_Upper_Frame)
        self.amp_chapter_label.setObjectName(u"amp_chapter_label")
        self.amp_chapter_label.setMinimumSize(QSize(45, 30))
        self.amp_chapter_label.setMaximumSize(QSize(45, 30))
        self.amp_chapter_label.setFont(font2)
        self.amp_chapter_label.setFrameShape(QFrame.Shape.WinPanel)
        self.amp_chapter_label.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.amp_chapter_label)


        self.verticalLayout_6.addWidget(self.Amplified_Upper_Frame)

        self.Amplified_Lower_Frame = QFrame(self.amp_tab)
        self.Amplified_Lower_Frame.setObjectName(u"Amplified_Lower_Frame")
        self.Amplified_Lower_Frame.setMaximumSize(QSize(16777215, 41))
        self.Amplified_Lower_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.Amplified_Lower_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Amplified_Lower_Frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.amp_previous_pushButton = QPushButton(self.Amplified_Lower_Frame)
        self.amp_previous_pushButton.setObjectName(u"amp_previous_pushButton")
        self.amp_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.amp_previous_pushButton.setFont(font2)
        self.amp_previous_pushButton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.amp_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.amp_next_pushButton = QPushButton(self.Amplified_Lower_Frame)
        self.amp_next_pushButton.setObjectName(u"amp_next_pushButton")
        self.amp_next_pushButton.setMaximumSize(QSize(102, 24))
        self.amp_next_pushButton.setFont(font2)
        self.amp_next_pushButton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.amp_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.Amplified_Lower_Frame)

        self.amp_ScrollArea = QScrollArea(self.amp_tab)
        self.amp_ScrollArea.setObjectName(u"amp_ScrollArea")
        self.amp_ScrollArea.setMinimumSize(QSize(0, 0))
        self.amp_ScrollArea.setStyleSheet(u"")
        self.amp_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.amp_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.amp_ScrollArea.setWidgetResizable(True)
        self.amp_ScrollAreaContents = QWidget()
        self.amp_ScrollAreaContents.setObjectName(u"amp_ScrollAreaContents")
        self.amp_ScrollAreaContents.setGeometry(QRect(0, 0, 613, 360))
        self.verticalLayout_11 = QVBoxLayout(self.amp_ScrollAreaContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.amp_gridLayout = QGridLayout()
        self.amp_gridLayout.setObjectName(u"amp_gridLayout")

        self.verticalLayout_11.addLayout(self.amp_gridLayout)

        self.amp_ScrollArea.setWidget(self.amp_ScrollAreaContents)

        self.verticalLayout_6.addWidget(self.amp_ScrollArea)

        self.bibleContentTabWidget.addTab(self.amp_tab, "")
        self.kjv_tab = QWidget()
        self.kjv_tab.setObjectName(u"kjv_tab")
        self.verticalLayout_2 = QVBoxLayout(self.kjv_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.King_James_Upper_Frame = QFrame(self.kjv_tab)
        self.King_James_Upper_Frame.setObjectName(u"King_James_Upper_Frame")
        self.King_James_Upper_Frame.setMinimumSize(QSize(627, 54))
        self.King_James_Upper_Frame.setMaximumSize(QSize(16777215, 54))
        self.King_James_Upper_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.King_James_Upper_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.King_James_Upper_Frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.kjv_version_label = QLabel(self.King_James_Upper_Frame)
        self.kjv_version_label.setObjectName(u"kjv_version_label")
        self.kjv_version_label.setFont(font2)

        self.horizontalLayout_12.addWidget(self.kjv_version_label)

        self.kjv_book_label = QLabel(self.King_James_Upper_Frame)
        self.kjv_book_label.setObjectName(u"kjv_book_label")
        self.kjv_book_label.setMaximumSize(QSize(16777215, 31))
        self.kjv_book_label.setFont(font2)
        self.kjv_book_label.setIndent(25)

        self.horizontalLayout_12.addWidget(self.kjv_book_label)

        self.kjv_chapter_label = QLabel(self.King_James_Upper_Frame)
        self.kjv_chapter_label.setObjectName(u"kjv_chapter_label")
        self.kjv_chapter_label.setMinimumSize(QSize(45, 30))
        self.kjv_chapter_label.setMaximumSize(QSize(45, 30))
        self.kjv_chapter_label.setFont(font2)
        self.kjv_chapter_label.setFrameShape(QFrame.Shape.WinPanel)
        self.kjv_chapter_label.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.kjv_chapter_label)


        self.verticalLayout_2.addWidget(self.King_James_Upper_Frame)

        self.King_James_Lower_Frame = QFrame(self.kjv_tab)
        self.King_James_Lower_Frame.setObjectName(u"King_James_Lower_Frame")
        self.King_James_Lower_Frame.setMaximumSize(QSize(16777215, 41))
        self.King_James_Lower_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.King_James_Lower_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.King_James_Lower_Frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.kjv_previous_pushButton = QPushButton(self.King_James_Lower_Frame)
        self.kjv_previous_pushButton.setObjectName(u"kjv_previous_pushButton")
        self.kjv_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.kjv_previous_pushButton.setFont(font2)
        self.kjv_previous_pushButton.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.kjv_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.kjv_next_pushButton = QPushButton(self.King_James_Lower_Frame)
        self.kjv_next_pushButton.setObjectName(u"kjv_next_pushButton")
        self.kjv_next_pushButton.setMaximumSize(QSize(102, 24))
        self.kjv_next_pushButton.setFont(font2)
        self.kjv_next_pushButton.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.kjv_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.King_James_Lower_Frame)

        self.kjv_ScrollArea = QScrollArea(self.kjv_tab)
        self.kjv_ScrollArea.setObjectName(u"kjv_ScrollArea")
        self.kjv_ScrollArea.setMinimumSize(QSize(0, 0))
        self.kjv_ScrollArea.setStyleSheet(u"")
        self.kjv_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.kjv_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.kjv_ScrollArea.setWidgetResizable(True)
        self.kjv_ScrollAreaContents = QWidget()
        self.kjv_ScrollAreaContents.setObjectName(u"kjv_ScrollAreaContents")
        self.kjv_ScrollAreaContents.setGeometry(QRect(0, 0, 613, 360))
        self.verticalLayout_12 = QVBoxLayout(self.kjv_ScrollAreaContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.kjv_gridLayout = QGridLayout()
        self.kjv_gridLayout.setObjectName(u"kjv_gridLayout")

        self.verticalLayout_12.addLayout(self.kjv_gridLayout)

        self.kjv_ScrollArea.setWidget(self.kjv_ScrollAreaContents)

        self.verticalLayout_2.addWidget(self.kjv_ScrollArea)

        self.bibleContentTabWidget.addTab(self.kjv_tab, "")
        self.njb_tab = QWidget()
        self.njb_tab.setObjectName(u"njb_tab")
        self.verticalLayout = QVBoxLayout(self.njb_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.New_Jerusalem_Upper_Frame = QFrame(self.njb_tab)
        self.New_Jerusalem_Upper_Frame.setObjectName(u"New_Jerusalem_Upper_Frame")
        self.New_Jerusalem_Upper_Frame.setMinimumSize(QSize(627, 54))
        self.New_Jerusalem_Upper_Frame.setMaximumSize(QSize(16777215, 54))
        self.New_Jerusalem_Upper_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.New_Jerusalem_Upper_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.New_Jerusalem_Upper_Frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.njb_version_label = QLabel(self.New_Jerusalem_Upper_Frame)
        self.njb_version_label.setObjectName(u"njb_version_label")
        self.njb_version_label.setFont(font2)

        self.horizontalLayout_13.addWidget(self.njb_version_label)

        self.njb_book_label = QLabel(self.New_Jerusalem_Upper_Frame)
        self.njb_book_label.setObjectName(u"njb_book_label")
        self.njb_book_label.setMaximumSize(QSize(16777215, 31))
        self.njb_book_label.setFont(font2)
        self.njb_book_label.setIndent(25)

        self.horizontalLayout_13.addWidget(self.njb_book_label)

        self.njb_chapter_label = QLabel(self.New_Jerusalem_Upper_Frame)
        self.njb_chapter_label.setObjectName(u"njb_chapter_label")
        self.njb_chapter_label.setMinimumSize(QSize(45, 30))
        self.njb_chapter_label.setMaximumSize(QSize(45, 30))
        self.njb_chapter_label.setFont(font2)
        self.njb_chapter_label.setFrameShape(QFrame.Shape.WinPanel)
        self.njb_chapter_label.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.njb_chapter_label)


        self.verticalLayout.addWidget(self.New_Jerusalem_Upper_Frame)

        self.New_Jerusalem_Lower_Frame = QFrame(self.njb_tab)
        self.New_Jerusalem_Lower_Frame.setObjectName(u"New_Jerusalem_Lower_Frame")
        self.New_Jerusalem_Lower_Frame.setMaximumSize(QSize(16777215, 41))
        self.New_Jerusalem_Lower_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.New_Jerusalem_Lower_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.New_Jerusalem_Lower_Frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.njb_previous_pushButton = QPushButton(self.New_Jerusalem_Lower_Frame)
        self.njb_previous_pushButton.setObjectName(u"njb_previous_pushButton")
        self.njb_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.njb_previous_pushButton.setFont(font2)
        self.njb_previous_pushButton.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.njb_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.njb_next_pushButton = QPushButton(self.New_Jerusalem_Lower_Frame)
        self.njb_next_pushButton.setObjectName(u"njb_next_pushButton")
        self.njb_next_pushButton.setMaximumSize(QSize(102, 24))
        self.njb_next_pushButton.setFont(font2)
        self.njb_next_pushButton.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.njb_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.New_Jerusalem_Lower_Frame)

        self.njb_ScrollArea = QScrollArea(self.njb_tab)
        self.njb_ScrollArea.setObjectName(u"njb_ScrollArea")
        self.njb_ScrollArea.setMinimumSize(QSize(0, 0))
        self.njb_ScrollArea.setStyleSheet(u"")
        self.njb_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.njb_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.njb_ScrollArea.setWidgetResizable(True)
        self.njb_ScrollAreaContents = QWidget()
        self.njb_ScrollAreaContents.setObjectName(u"njb_ScrollAreaContents")
        self.njb_ScrollAreaContents.setGeometry(QRect(0, 0, 613, 360))
        self.horizontalLayout_3 = QHBoxLayout(self.njb_ScrollAreaContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.njb_gridLayout = QGridLayout()
        self.njb_gridLayout.setObjectName(u"njb_gridLayout")

        self.horizontalLayout_3.addLayout(self.njb_gridLayout)

        self.njb_ScrollArea.setWidget(self.njb_ScrollAreaContents)

        self.verticalLayout.addWidget(self.njb_ScrollArea)

        self.bibleContentTabWidget.addTab(self.njb_tab, "")

        self.verticalLayout_9.addWidget(self.bibleContentTabWidget)

        self.stackedWidget.addWidget(self.bible_content_display_page)
        self.bible_fun_facts_page = QWidget()
        self.bible_fun_facts_page.setObjectName(u"bible_fun_facts_page")
        self.verticalLayout_14 = QVBoxLayout(self.bible_fun_facts_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.fun_facts_frame = QFrame(self.bible_fun_facts_page)
        self.fun_facts_frame.setObjectName(u"fun_facts_frame")
        self.fun_facts_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.fun_facts_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.fun_facts_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Fun_Facts_Page_Title_Frame = QFrame(self.fun_facts_frame)
        self.Fun_Facts_Page_Title_Frame.setObjectName(u"Fun_Facts_Page_Title_Frame")
        self.Fun_Facts_Page_Title_Frame.setMinimumSize(QSize(0, 80))
        self.Fun_Facts_Page_Title_Frame.setMaximumSize(QSize(16777215, 80))
        self.Fun_Facts_Page_Title_Frame.setStyleSheet(u"")
        self.Fun_Facts_Page_Title_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fun_Facts_Page_Title_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Fun_Facts_Page_Title_Frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.fun_facts_page_title_label = QLabel(self.Fun_Facts_Page_Title_Frame)
        self.fun_facts_page_title_label.setObjectName(u"fun_facts_page_title_label")
        self.fun_facts_page_title_label.setMinimumSize(QSize(191, 50))
        self.fun_facts_page_title_label.setMaximumSize(QSize(16777215, 50))
        self.fun_facts_page_title_label.setFont(font2)
        self.fun_facts_page_title_label.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.fun_facts_page_title_label)

        self.fun_facts_page_intro_label = QLabel(self.Fun_Facts_Page_Title_Frame)
        self.fun_facts_page_intro_label.setObjectName(u"fun_facts_page_intro_label")
        self.fun_facts_page_intro_label.setMinimumSize(QSize(301, 50))
        self.fun_facts_page_intro_label.setMaximumSize(QSize(16777215, 50))
        self.fun_facts_page_intro_label.setFont(font2)

        self.horizontalLayout_7.addWidget(self.fun_facts_page_intro_label)


        self.verticalLayout_13.addWidget(self.Fun_Facts_Page_Title_Frame)

        self.fun_facts_scrollArea = QScrollArea(self.fun_facts_frame)
        self.fun_facts_scrollArea.setObjectName(u"fun_facts_scrollArea")
        self.fun_facts_scrollArea.setMinimumSize(QSize(625, 400))
        self.fun_facts_scrollArea.setWidgetResizable(True)
        self.fun_facts_scrollAreaWidgetContents = QWidget()
        self.fun_facts_scrollAreaWidgetContents.setObjectName(u"fun_facts_scrollAreaWidgetContents")
        self.fun_facts_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 623, 398))
        self.verticalLayout_15 = QVBoxLayout(self.fun_facts_scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.bible_fun_fact_gridLayout = QGridLayout()
        self.bible_fun_fact_gridLayout.setObjectName(u"bible_fun_fact_gridLayout")

        self.verticalLayout_15.addLayout(self.bible_fun_fact_gridLayout)

        self.fun_facts_scrollArea.setWidget(self.fun_facts_scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.fun_facts_scrollArea)


        self.verticalLayout_14.addWidget(self.fun_facts_frame)

        self.stackedWidget.addWidget(self.bible_fun_facts_page)
        self.bible_study_plan_page = QWidget()
        self.bible_study_plan_page.setObjectName(u"bible_study_plan_page")
        self.verticalLayout_25 = QVBoxLayout(self.bible_study_plan_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.bible_study_main_frame = QFrame(self.bible_study_plan_page)
        self.bible_study_main_frame.setObjectName(u"bible_study_main_frame")
        self.bible_study_main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bible_study_main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.bible_study_main_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.bible_study_plan_scrollArea = QScrollArea(self.bible_study_main_frame)
        self.bible_study_plan_scrollArea.setObjectName(u"bible_study_plan_scrollArea")
        self.bible_study_plan_scrollArea.setWidgetResizable(True)
        self.bible_study_plan_scrollAreaWidgetContents = QWidget()
        self.bible_study_plan_scrollAreaWidgetContents.setObjectName(u"bible_study_plan_scrollAreaWidgetContents")
        self.bible_study_plan_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 152, 452))
        self.verticalLayout_33 = QVBoxLayout(self.bible_study_plan_scrollAreaWidgetContents)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.bible_study_plan_intro_frame = QFrame(self.bible_study_plan_scrollAreaWidgetContents)
        self.bible_study_plan_intro_frame.setObjectName(u"bible_study_plan_intro_frame")
        self.bible_study_plan_intro_frame.setMinimumSize(QSize(0, 80))
        self.bible_study_plan_intro_frame.setMaximumSize(QSize(16777215, 80))
        self.bible_study_plan_intro_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bible_study_plan_intro_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.bible_study_plan_intro_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.study_plan_page_title_label = QLabel(self.bible_study_plan_intro_frame)
        self.study_plan_page_title_label.setObjectName(u"study_plan_page_title_label")
        self.study_plan_page_title_label.setFont(font2)

        self.horizontalLayout_15.addWidget(self.study_plan_page_title_label)


        self.verticalLayout_33.addWidget(self.bible_study_plan_intro_frame)

        self._365_days_plan_frame = QFrame(self.bible_study_plan_scrollAreaWidgetContents)
        self._365_days_plan_frame.setObjectName(u"_365_days_plan_frame")
        self._365_days_plan_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self._365_days_plan_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self._365_days_plan_frame)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self._365_days_plan_pushButton = QPushButton(self._365_days_plan_frame)
        self._365_days_plan_pushButton.setObjectName(u"_365_days_plan_pushButton")
        self._365_days_plan_pushButton.setFont(font2)

        self.verticalLayout_29.addWidget(self._365_days_plan_pushButton)

        self._365_days_tableWidget = QTableWidget(self._365_days_plan_frame)
        if (self._365_days_tableWidget.columnCount() < 7):
            self._365_days_tableWidget.setColumnCount(7)
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei"])
        font4.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self._365_days_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self._365_days_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self._365_days_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self._365_days_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self._365_days_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self._365_days_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(12)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self._365_days_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self._365_days_tableWidget.setObjectName(u"_365_days_tableWidget")

        self.verticalLayout_29.addWidget(self._365_days_tableWidget)


        self.verticalLayout_33.addWidget(self._365_days_plan_frame)

        self._180_days_frame = QFrame(self.bible_study_plan_scrollAreaWidgetContents)
        self._180_days_frame.setObjectName(u"_180_days_frame")
        self._180_days_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self._180_days_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self._180_days_frame)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self._180_days_plan_pushButton = QPushButton(self._180_days_frame)
        self._180_days_plan_pushButton.setObjectName(u"_180_days_plan_pushButton")
        self._180_days_plan_pushButton.setFont(font2)

        self.verticalLayout_31.addWidget(self._180_days_plan_pushButton)

        self._180_days_tableWidget = QTableWidget(self._180_days_frame)
        self._180_days_tableWidget.setObjectName(u"_180_days_tableWidget")

        self.verticalLayout_31.addWidget(self._180_days_tableWidget)


        self.verticalLayout_33.addWidget(self._180_days_frame)

        self._90_days_frame = QFrame(self.bible_study_plan_scrollAreaWidgetContents)
        self._90_days_frame.setObjectName(u"_90_days_frame")
        self._90_days_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self._90_days_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self._90_days_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self._90_days_plan_pushButton = QPushButton(self._90_days_frame)
        self._90_days_plan_pushButton.setObjectName(u"_90_days_plan_pushButton")
        self._90_days_plan_pushButton.setFont(font2)

        self.verticalLayout_32.addWidget(self._90_days_plan_pushButton)

        self._90_days_tableWidget = QTableWidget(self._90_days_frame)
        self._90_days_tableWidget.setObjectName(u"_90_days_tableWidget")

        self.verticalLayout_32.addWidget(self._90_days_tableWidget)


        self.verticalLayout_33.addWidget(self._90_days_frame)

        self.bible_study_plan_scrollArea.setWidget(self.bible_study_plan_scrollAreaWidgetContents)

        self.verticalLayout_30.addWidget(self.bible_study_plan_scrollArea)


        self.verticalLayout_25.addWidget(self.bible_study_main_frame)

        self.stackedWidget.addWidget(self.bible_study_plan_page)
        self.bible_study_topics_page = QWidget()
        self.bible_study_topics_page.setObjectName(u"bible_study_topics_page")
        self.verticalLayout_28 = QVBoxLayout(self.bible_study_topics_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.bible_study_topics_frame = QFrame(self.bible_study_topics_page)
        self.bible_study_topics_frame.setObjectName(u"bible_study_topics_frame")
        self.bible_study_topics_frame.setMinimumSize(QSize(0, 81))
        self.bible_study_topics_frame.setMaximumSize(QSize(16777215, 81))
        self.bible_study_topics_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bible_study_topics_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.bible_study_topics_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.bible_study_topics_label = QLabel(self.bible_study_topics_frame)
        self.bible_study_topics_label.setObjectName(u"bible_study_topics_label")
        self.bible_study_topics_label.setFont(font2)

        self.horizontalLayout_14.addWidget(self.bible_study_topics_label)


        self.verticalLayout_28.addWidget(self.bible_study_topics_frame)

        self.study_topics_content_frame = QFrame(self.bible_study_topics_page)
        self.study_topics_content_frame.setObjectName(u"study_topics_content_frame")
        self.study_topics_content_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.study_topics_content_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.study_topics_content_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.study_topics_scrollArea = QScrollArea(self.study_topics_content_frame)
        self.study_topics_scrollArea.setObjectName(u"study_topics_scrollArea")
        self.study_topics_scrollArea.setWidgetResizable(True)
        self.study_topics_scrollAreaWidgetContents = QWidget()
        self.study_topics_scrollAreaWidgetContents.setObjectName(u"study_topics_scrollAreaWidgetContents")
        self.study_topics_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 86, 40))
        self.verticalLayout_26 = QVBoxLayout(self.study_topics_scrollAreaWidgetContents)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.study_topics_content_edit_frame = QFrame(self.study_topics_scrollAreaWidgetContents)
        self.study_topics_content_edit_frame.setObjectName(u"study_topics_content_edit_frame")
        self.study_topics_content_edit_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.study_topics_content_edit_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.study_topics_content_edit_frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.study_topics_gridLayout = QGridLayout()
        self.study_topics_gridLayout.setObjectName(u"study_topics_gridLayout")

        self.verticalLayout_24.addLayout(self.study_topics_gridLayout)


        self.verticalLayout_26.addWidget(self.study_topics_content_edit_frame)

        self.study_topics_scrollArea.setWidget(self.study_topics_scrollAreaWidgetContents)

        self.verticalLayout_27.addWidget(self.study_topics_scrollArea)


        self.verticalLayout_28.addWidget(self.study_topics_content_frame)

        self.stackedWidget.addWidget(self.bible_study_topics_page)
        self.bible_study_character_page = QWidget()
        self.bible_study_character_page.setObjectName(u"bible_study_character_page")
        self.verticalLayout_16 = QVBoxLayout(self.bible_study_character_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.bible_study_character_scrollArea = QScrollArea(self.bible_study_character_page)
        self.bible_study_character_scrollArea.setObjectName(u"bible_study_character_scrollArea")
        self.bible_study_character_scrollArea.setWidgetResizable(True)
        self.bible_study_character_scrollAreaWidgetContents = QWidget()
        self.bible_study_character_scrollAreaWidgetContents.setObjectName(u"bible_study_character_scrollAreaWidgetContents")
        self.bible_study_character_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 596, 140))
        self.verticalLayout_17 = QVBoxLayout(self.bible_study_character_scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.study_character_frame = QFrame(self.bible_study_character_scrollAreaWidgetContents)
        self.study_character_frame.setObjectName(u"study_character_frame")
        self.study_character_frame.setMinimumSize(QSize(0, 60))
        self.study_character_frame.setMaximumSize(QSize(16777215, 60))
        self.study_character_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.study_character_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.study_character_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.study_character_title_label = QLabel(self.study_character_frame)
        self.study_character_title_label.setObjectName(u"study_character_title_label")
        self.study_character_title_label.setMinimumSize(QSize(261, 40))
        self.study_character_title_label.setMaximumSize(QSize(16777215, 40))
        self.study_character_title_label.setFont(font2)

        self.horizontalLayout_9.addWidget(self.study_character_title_label)

        self.study_character_intro_label = QLabel(self.study_character_frame)
        self.study_character_intro_label.setObjectName(u"study_character_intro_label")
        self.study_character_intro_label.setMinimumSize(QSize(291, 40))
        self.study_character_intro_label.setMaximumSize(QSize(16777215, 40))
        self.study_character_intro_label.setFont(font2)

        self.horizontalLayout_9.addWidget(self.study_character_intro_label)


        self.verticalLayout_17.addWidget(self.study_character_frame)

        self.study_characters_tableWidget = QTableWidget(self.bible_study_character_scrollAreaWidgetContents)
        self.study_characters_tableWidget.setObjectName(u"study_characters_tableWidget")

        self.verticalLayout_17.addWidget(self.study_characters_tableWidget)

        self.bible_study_character_scrollArea.setWidget(self.bible_study_character_scrollAreaWidgetContents)

        self.verticalLayout_16.addWidget(self.bible_study_character_scrollArea)

        self.stackedWidget.addWidget(self.bible_study_character_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_22 = QVBoxLayout(self.settings_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.setting_page_title_frame = QFrame(self.settings_page)
        self.setting_page_title_frame.setObjectName(u"setting_page_title_frame")
        self.setting_page_title_frame.setMinimumSize(QSize(641, 101))
        self.setting_page_title_frame.setMaximumSize(QSize(16777215, 101))
        self.setting_page_title_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.setting_page_title_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.setting_page_title_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.settings_page_label = QLabel(self.setting_page_title_frame)
        self.settings_page_label.setObjectName(u"settings_page_label")
        self.settings_page_label.setMinimumSize(QSize(621, 81))
        self.settings_page_label.setFont(font1)

        self.horizontalLayout_11.addWidget(self.settings_page_label)


        self.verticalLayout_22.addWidget(self.setting_page_title_frame)

        self.settings_content_frame = QFrame(self.settings_page)
        self.settings_content_frame.setObjectName(u"settings_content_frame")
        self.settings_content_frame.setMinimumSize(QSize(641, 395))
        self.settings_content_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settings_content_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.settings_content_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.settings_scrollArea = QScrollArea(self.settings_content_frame)
        self.settings_scrollArea.setObjectName(u"settings_scrollArea")
        self.settings_scrollArea.setMinimumSize(QSize(621, 375))
        self.settings_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 619, 373))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(619, 373))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.settinngs_edit_frame = QFrame(self.scrollAreaWidgetContents)
        self.settinngs_edit_frame.setObjectName(u"settinngs_edit_frame")
        self.settinngs_edit_frame.setMinimumSize(QSize(601, 355))
        self.settinngs_edit_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settinngs_edit_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.settinngs_edit_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.settings_gridLayout = QGridLayout()
        self.settings_gridLayout.setObjectName(u"settings_gridLayout")

        self.verticalLayout_10.addLayout(self.settings_gridLayout)


        self.verticalLayout_18.addWidget(self.settinngs_edit_frame)

        self.settings_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.settings_scrollArea)


        self.verticalLayout_22.addWidget(self.settings_content_frame)

        self.stackedWidget.addWidget(self.settings_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        Bible_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Bible_MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.bibleContentTabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Bible_MainWindow)
    # setupUi

    def retranslateUi(self, Bible_MainWindow):
        Bible_MainWindow.setWindowTitle(QCoreApplication.translate("Bible_MainWindow", u"Student of the Gospel Bible", None))
        self.pushButton_menu.setText("")
        self.hide_show_bible_books_pushbutton.setText("")
        self.esther.setText(QCoreApplication.translate("Bible_MainWindow", u"Esther", None))
        self.hebrews.setText(QCoreApplication.translate("Bible_MainWindow", u"Hebrews", None))
        self.romans.setText(QCoreApplication.translate("Bible_MainWindow", u"Romans", None))
        self.chronicles_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Chronicles", None))
        self.jonah.setText(QCoreApplication.translate("Bible_MainWindow", u"Jonah", None))
        self.song_of_the_three_young_men.setText(QCoreApplication.translate("Bible_MainWindow", u"Song of the Three Young Men", None))
        self.timothy_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Timothy", None))
        self.maccabees_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Maccabees", None))
        self.john.setText(QCoreApplication.translate("Bible_MainWindow", u"John", None))
        self.joshua.setText(QCoreApplication.translate("Bible_MainWindow", u"Joshua", None))
        self.joel.setText(QCoreApplication.translate("Bible_MainWindow", u"Joel", None))
        self.galatians.setText(QCoreApplication.translate("Bible_MainWindow", u"Galatians", None))
        self.judges.setText(QCoreApplication.translate("Bible_MainWindow", u"Judges", None))
        self.revelation.setText(QCoreApplication.translate("Bible_MainWindow", u"Revelation", None))
        self.thessalonians_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Thessalonians ", None))
        self.corinthians_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Corinthians", None))
        self.hosea.setText(QCoreApplication.translate("Bible_MainWindow", u"Hosea", None))
        self.ephesians.setText(QCoreApplication.translate("Bible_MainWindow", u"Ephesians", None))
        self.numbers.setText(QCoreApplication.translate("Bible_MainWindow", u"Numbers", None))
        self.mark.setText(QCoreApplication.translate("Bible_MainWindow", u"Mark", None))
        self.maccabees_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Maccabees", None))
        self.judith.setText(QCoreApplication.translate("Bible_MainWindow", u"Judith", None))
        self.micah.setText(QCoreApplication.translate("Bible_MainWindow", u"Micah", None))
        self.job.setText(QCoreApplication.translate("Bible_MainWindow", u"Job", None))
        self.luke.setText(QCoreApplication.translate("Bible_MainWindow", u"Luke", None))
        self.ezekiel.setText(QCoreApplication.translate("Bible_MainWindow", u"Ezekiel", None))
        self.ruth.setText(QCoreApplication.translate("Bible_MainWindow", u"Ruth", None))
        self.amos.setText(QCoreApplication.translate("Bible_MainWindow", u"Amos", None))
        self.peter_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Peter", None))
        self.sirach.setText(QCoreApplication.translate("Bible_MainWindow", u"Sirach", None))
        self.kings_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Kings", None))
        self.song_of_songs.setText(QCoreApplication.translate("Bible_MainWindow", u"Song of Songs", None))
        self.wisdom_of_solomon.setText(QCoreApplication.translate("Bible_MainWindow", u"Wisdom of Solomon", None))
        self.psalms.setText(QCoreApplication.translate("Bible_MainWindow", u"Psalms", None))
        self.john_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 John", None))
        self.jeremiah.setText(QCoreApplication.translate("Bible_MainWindow", u"Jeremiah", None))
        self.john_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 John", None))
        self.timothy_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Timothy", None))
        self.tobit.setText(QCoreApplication.translate("Bible_MainWindow", u"Tobit", None))
        self.samuel_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Samuel", None))
        self.nehemiah.setText(QCoreApplication.translate("Bible_MainWindow", u"Nehemiah", None))
        self.bel_and_the_dragon.setText(QCoreApplication.translate("Bible_MainWindow", u"Bel and the Dragon ", None))
        self.proverbs.setText(QCoreApplication.translate("Bible_MainWindow", u"Proverbs", None))
        self.isaiah.setText(QCoreApplication.translate("Bible_MainWindow", u"Isaiah", None))
        self.acts.setText(QCoreApplication.translate("Bible_MainWindow", u"Acts", None))
        self.genesis.setText(QCoreApplication.translate("Bible_MainWindow", u"Genesis", None))
        self.colossians.setText(QCoreApplication.translate("Bible_MainWindow", u"Colossians", None))
        self.daniel.setText(QCoreApplication.translate("Bible_MainWindow", u"Daniel", None))
        self.leviticus.setText(QCoreApplication.translate("Bible_MainWindow", u"Leviticus", None))
        self.ezra.setText(QCoreApplication.translate("Bible_MainWindow", u"Ezra", None))
        self.esther_greek.setText(QCoreApplication.translate("Bible_MainWindow", u"Esther (Greek)", None))
        self.philippians.setText(QCoreApplication.translate("Bible_MainWindow", u"Philippians", None))
        self.haggai.setText(QCoreApplication.translate("Bible_MainWindow", u"Haggai", None))
        self.john_3.setText(QCoreApplication.translate("Bible_MainWindow", u"3 John", None))
        self.zechariah.setText(QCoreApplication.translate("Bible_MainWindow", u"Zechariah", None))
        self.philemon.setText(QCoreApplication.translate("Bible_MainWindow", u"Philemon", None))
        self.jude.setText(QCoreApplication.translate("Bible_MainWindow", u"Jude", None))
        self.exodus.setText(QCoreApplication.translate("Bible_MainWindow", u"Exodus", None))
        self.thessalonians_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Thessalonians", None))
        self.malachi.setText(QCoreApplication.translate("Bible_MainWindow", u"Malachi", None))
        self.habakkuk.setText(QCoreApplication.translate("Bible_MainWindow", u"Habakkuk", None))
        self.james.setText(QCoreApplication.translate("Bible_MainWindow", u"James", None))
        self.lamentations.setText(QCoreApplication.translate("Bible_MainWindow", u"Lamentations", None))
        self.kings_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Kings", None))
        self.samuel_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Samuel", None))
        self.matthew.setText(QCoreApplication.translate("Bible_MainWindow", u"Matthew", None))
        self.chronicles_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Chronicles", None))
        self.zephaniah.setText(QCoreApplication.translate("Bible_MainWindow", u"Zephaniah", None))
        self.susana.setText(QCoreApplication.translate("Bible_MainWindow", u"Susana", None))
        self.letter_of_jeremiah.setText(QCoreApplication.translate("Bible_MainWindow", u"Letter of Jeremiah", None))
        self.obadiah.setText(QCoreApplication.translate("Bible_MainWindow", u"Obadiah", None))
        self.peter_1.setText(QCoreApplication.translate("Bible_MainWindow", u"1 Peter", None))
        self.titus.setText(QCoreApplication.translate("Bible_MainWindow", u"Titus", None))
        self.nahum.setText(QCoreApplication.translate("Bible_MainWindow", u"Nahum", None))
        self.deuteronomy.setText(QCoreApplication.translate("Bible_MainWindow", u"Deuteronomy", None))
        self.baruch.setText(QCoreApplication.translate("Bible_MainWindow", u"Baruch", None))
        self.ecclesiastes.setText(QCoreApplication.translate("Bible_MainWindow", u"Ecclesiastes", None))
        self.corinthians_2.setText(QCoreApplication.translate("Bible_MainWindow", u"2 Corinthians", None))
        self.pushButton_bible_fun_facts.setText(QCoreApplication.translate("Bible_MainWindow", u"Bible Fun Facts", None))
        self.pushButton_bible_study_plan.setText(QCoreApplication.translate("Bible_MainWindow", u"Bible Study Plan", None))
        self.pushButton_study_topic.setText(QCoreApplication.translate("Bible_MainWindow", u"Study Topics", None))
        self.pushButton_study_character.setText(QCoreApplication.translate("Bible_MainWindow", u"Study Character", None))
        self.pushButton_bible_settings.setText(QCoreApplication.translate("Bible_MainWindow", u"Settings", None))
        self.pushButton_bible_quit_app.setText(QCoreApplication.translate("Bible_MainWindow", u"Quit App", None))
        self.book_name_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Book Name Label", None))
        self.gn_version_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Good News", None))
        self.gn_book_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Book Label", None))
        self.gn_chapter_label.setText("")
        self.gn_previous_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Previous", None))
        self.gn_next_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Next", None))
        self.bibleContentTabWidget.setTabText(self.bibleContentTabWidget.indexOf(self.gn_tab), QCoreApplication.translate("Bible_MainWindow", u"Good News ", None))
        self.amp_version_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Amplified", None))
        self.amp_book_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Book Label", None))
        self.amp_chapter_label.setText("")
        self.amp_previous_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Previous", None))
        self.amp_next_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Next", None))
        self.bibleContentTabWidget.setTabText(self.bibleContentTabWidget.indexOf(self.amp_tab), QCoreApplication.translate("Bible_MainWindow", u"Amplified", None))
        self.kjv_version_label.setText(QCoreApplication.translate("Bible_MainWindow", u"King James", None))
        self.kjv_book_label.setText(QCoreApplication.translate("Bible_MainWindow", u"B Label", None))
        self.kjv_chapter_label.setText("")
        self.kjv_previous_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Previous", None))
        self.kjv_next_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Next", None))
        self.bibleContentTabWidget.setTabText(self.bibleContentTabWidget.indexOf(self.kjv_tab), QCoreApplication.translate("Bible_MainWindow", u"King James Version", None))
        self.njb_version_label.setText(QCoreApplication.translate("Bible_MainWindow", u"The New Jerusalem", None))
        self.njb_book_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Book Label", None))
        self.njb_chapter_label.setText("")
        self.njb_previous_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Previous", None))
        self.njb_next_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"Next", None))
        self.bibleContentTabWidget.setTabText(self.bibleContentTabWidget.indexOf(self.njb_tab), QCoreApplication.translate("Bible_MainWindow", u"New Jerusalem Bible", None))
        self.fun_facts_page_title_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Bible Fun Facts", None))
        self.fun_facts_page_intro_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Did You Know The Word of God is Fun ?", None))
        self.study_plan_page_title_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Bible Study Plan", None))
        self._365_days_plan_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"365 Days Plan", None))
        ___qtablewidgetitem = self._365_days_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Bible_MainWindow", u"Bible Study Day", None));
        ___qtablewidgetitem1 = self._365_days_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Bible_MainWindow", u"Book Chapters", None));
        ___qtablewidgetitem2 = self._365_days_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Bible_MainWindow", u"First Chapter", None));
        ___qtablewidgetitem3 = self._365_days_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Bible_MainWindow", u"Second Chapter", None));
        ___qtablewidgetitem4 = self._365_days_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Bible_MainWindow", u"Third Chapter", None));
        ___qtablewidgetitem5 = self._365_days_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Bible_MainWindow", u"Fourth Chapter", None));
        ___qtablewidgetitem6 = self._365_days_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Bible_MainWindow", u"Notes and Lessons", None));
        self._180_days_plan_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"180 Days Plan", None))
        self._90_days_plan_pushButton.setText(QCoreApplication.translate("Bible_MainWindow", u"90 Days Plan", None))
        self.bible_study_topics_label.setText(QCoreApplication.translate("Bible_MainWindow", u"What Topic Interests You Today ?", None))
        self.study_character_title_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Study Your Bible Models", None))
        self.study_character_intro_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Who Would Study Today?", None))
        self.settings_page_label.setText(QCoreApplication.translate("Bible_MainWindow", u"Settings Page", None))
    # retranslateUi

