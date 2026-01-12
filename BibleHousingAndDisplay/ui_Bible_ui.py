# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bible_uiDZTbId.ui'
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
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)
import my_Bible_Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1149, 542)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/appIcons/bible_icon_5.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(78, 157, 78);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_menu = QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setMinimumSize(QSize(40, 40))
        self.pushButton_menu.setMaximumSize(QSize(40, 40))
        self.pushButton_menu.setStyleSheet(u"QPushButton{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/buttonIcons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/buttonIcons/menu2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_menu.setIcon(icon1)
        self.pushButton_menu.setIconSize(QSize(35, 35))
        self.pushButton_menu.setCheckable(True)

        self.verticalLayout_10.addWidget(self.pushButton_menu, 0, Qt.AlignmentFlag.AlignTop)

        self.leftScrollArea = QScrollArea(self.centralwidget)
        self.leftScrollArea.setObjectName(u"leftScrollArea")
        self.leftScrollArea.setMinimumSize(QSize(254, 450))
        self.leftScrollArea.setMaximumSize(QSize(229, 16777215))
        font1 = QFont()
        font1.setBold(True)
        self.leftScrollArea.setFont(font1)
        self.leftScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.leftScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.leftScrollArea.setWidgetResizable(True)
        self.leftScrollAreaContents = QWidget()
        self.leftScrollAreaContents.setObjectName(u"leftScrollAreaContents")
        self.leftScrollAreaContents.setGeometry(QRect(0, -2041, 238, 2513))
        self.verticalLayout_23 = QVBoxLayout(self.leftScrollAreaContents)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_content = QPushButton(self.leftScrollAreaContents)
        self.pushButton_content.setObjectName(u"pushButton_content")
        self.pushButton_content.setMinimumSize(QSize(220, 33))
        self.pushButton_content.setMaximumSize(QSize(220, 33))
        self.pushButton_content.setStyleSheet(u"background-color: rgb(121, 121, 90);")
        icon2 = QIcon()
        icon2.addFile(u":/buttonIcons/content_hidden2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/buttonIcons/content_shown2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_content.setIcon(icon2)
        self.pushButton_content.setIconSize(QSize(100, 25))
        self.pushButton_content.setCheckable(True)

        self.verticalLayout_23.addWidget(self.pushButton_content)

        self.bibleBooksFrame = QFrame(self.leftScrollAreaContents)
        self.bibleBooksFrame.setObjectName(u"bibleBooksFrame")
        self.bibleBooksFrame.setMinimumSize(QSize(220, 2200))
        self.bibleBooksFrame.setMaximumSize(QSize(211, 16777215))
        self.bibleBooksFrame.setFont(font)
        self.bibleBooksFrame.setStyleSheet(u"QPushButton{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}")
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
        self.extras_Frame.setStyleSheet(u"QPushButton{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}")
        self.extras_Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.extras_Frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.extras_Frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_fun_facts = QPushButton(self.extras_Frame)
        self.pushButton_fun_facts.setObjectName(u"pushButton_fun_facts")
        font2 = QFont()
        font2.setFamilies([u"Segoe Print"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton_fun_facts.setFont(font2)
        self.pushButton_fun_facts.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.verticalLayout_19.addWidget(self.pushButton_fun_facts)

        self.pushButton_bible_study = QPushButton(self.extras_Frame)
        self.pushButton_bible_study.setObjectName(u"pushButton_bible_study")
        self.pushButton_bible_study.setFont(font2)
        self.pushButton_bible_study.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.verticalLayout_19.addWidget(self.pushButton_bible_study)

        self.pushButton_study_topic = QPushButton(self.extras_Frame)
        self.pushButton_study_topic.setObjectName(u"pushButton_study_topic")
        self.pushButton_study_topic.setFont(font2)
        self.pushButton_study_topic.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.verticalLayout_19.addWidget(self.pushButton_study_topic)

        self.pushButton_character = QPushButton(self.extras_Frame)
        self.pushButton_character.setObjectName(u"pushButton_character")

        self.verticalLayout_19.addWidget(self.pushButton_character)

        self.pushButton_settings = QPushButton(self.extras_Frame)
        self.pushButton_settings.setObjectName(u"pushButton_settings")

        self.verticalLayout_19.addWidget(self.pushButton_settings)

        self.pushButton_quit_app = QPushButton(self.extras_Frame)
        self.pushButton_quit_app.setObjectName(u"pushButton_quit_app")

        self.verticalLayout_19.addWidget(self.pushButton_quit_app)


        self.verticalLayout_23.addWidget(self.extras_Frame, 0, Qt.AlignmentFlag.AlignBottom)

        self.leftScrollArea.setWidget(self.leftScrollAreaContents)

        self.verticalLayout_10.addWidget(self.leftScrollArea)


        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.chaptersNumberFrame = QFrame(self.centralwidget)
        self.chaptersNumberFrame.setObjectName(u"chaptersNumberFrame")
        self.chaptersNumberFrame.setMinimumSize(QSize(0, 524))
        self.chaptersNumberFrame.setMaximumSize(QSize(200, 1000))
        self.chaptersNumberFrame.setFrameShape(QFrame.Shape.Panel)
        self.chaptersNumberFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.chaptersNumberFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.book_name_label = QLabel(self.chaptersNumberFrame)
        self.book_name_label.setObjectName(u"book_name_label")
        self.book_name_label.setMinimumSize(QSize(180, 16))
        self.book_name_label.setMaximumSize(QSize(180, 16))
        self.book_name_label.setFont(font2)
        self.book_name_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}")
        self.book_name_label.setIndent(0)

        self.verticalLayout_3.addWidget(self.book_name_label)

        self.chapterNumberScrollArea = QScrollArea(self.chaptersNumberFrame)
        self.chapterNumberScrollArea.setObjectName(u"chapterNumberScrollArea")
        self.chapterNumberScrollArea.setFont(font)
        self.chapterNumberScrollArea.setStyleSheet(u"QPushButton{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}\n"
"QLabel{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}")
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
        self.chaptersNumberInnerFrame.setFont(font)
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
        self.bible_content_display_page = QWidget()
        self.bible_content_display_page.setObjectName(u"bible_content_display_page")
        self.verticalLayout_9 = QVBoxLayout(self.bible_content_display_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.bible_content_display_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(633, 524))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        self.tabWidget.setFont(font3)
        self.tabWidget.setStyleSheet(u"background-color: rgb(0, 148, 0);")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
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
        font4 = QFont()
        font4.setFamilies([u"Segoe Script"])
        font4.setPointSize(15)
        font4.setBold(True)
        self.gn_version_label.setFont(font4)

        self.horizontalLayout_5.addWidget(self.gn_version_label)

        self.gn_book_label = QLabel(self.Good_News_Upper_Frame)
        self.gn_book_label.setObjectName(u"gn_book_label")
        self.gn_book_label.setMinimumSize(QSize(266, 31))
        self.gn_book_label.setMaximumSize(QSize(16777215, 31))
        self.gn_book_label.setFont(font4)
        self.gn_book_label.setIndent(25)

        self.horizontalLayout_5.addWidget(self.gn_book_label)

        self.gn_chapter_label = QLabel(self.Good_News_Upper_Frame)
        self.gn_chapter_label.setObjectName(u"gn_chapter_label")
        self.gn_chapter_label.setMinimumSize(QSize(45, 30))
        self.gn_chapter_label.setMaximumSize(QSize(45, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe Script"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.gn_chapter_label.setFont(font5)
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
        self.gn_previous_pushButton.setFont(font)
        self.gn_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_2.addWidget(self.gn_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.gn_next_pushButton = QPushButton(self.Good_News_Lower_Frame)
        self.gn_next_pushButton.setObjectName(u"gn_next_pushButton")
        self.gn_next_pushButton.setMaximumSize(QSize(102, 24))
        self.gn_next_pushButton.setFont(font)
        self.gn_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_2.addWidget(self.gn_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.Good_News_Lower_Frame)

        self.gn_scrollArea = QScrollArea(self.gn_tab)
        self.gn_scrollArea.setObjectName(u"gn_scrollArea")
        self.gn_scrollArea.setMinimumSize(QSize(450, 450))
        self.gn_scrollArea.setStyleSheet(u"")
        self.gn_scrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.gn_scrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.gn_scrollArea.setWidgetResizable(True)
        self.gn_scrollAreaWidgetContents = QWidget()
        self.gn_scrollAreaWidgetContents.setObjectName(u"gn_scrollAreaWidgetContents")
        self.gn_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 617, 446))
        self.verticalLayout_8 = QVBoxLayout(self.gn_scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gn_gridLayout = QGridLayout()
        self.gn_gridLayout.setObjectName(u"gn_gridLayout")

        self.verticalLayout_8.addLayout(self.gn_gridLayout)

        self.gn_scrollArea.setWidget(self.gn_scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.gn_scrollArea)

        self.tabWidget.addTab(self.gn_tab, "")
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
        self.amp_version_label.setFont(font4)

        self.horizontalLayout_10.addWidget(self.amp_version_label)

        self.amp_book_label = QLabel(self.Amplified_Upper_Frame)
        self.amp_book_label.setObjectName(u"amp_book_label")
        self.amp_book_label.setMaximumSize(QSize(16777215, 31))
        self.amp_book_label.setFont(font4)
        self.amp_book_label.setIndent(25)

        self.horizontalLayout_10.addWidget(self.amp_book_label)

        self.amp_chapter_label = QLabel(self.Amplified_Upper_Frame)
        self.amp_chapter_label.setObjectName(u"amp_chapter_label")
        self.amp_chapter_label.setMinimumSize(QSize(45, 30))
        self.amp_chapter_label.setMaximumSize(QSize(45, 30))
        self.amp_chapter_label.setFont(font5)
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
        self.amp_previous_pushButton.setFont(font)
        self.amp_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_4.addWidget(self.amp_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.amp_next_pushButton = QPushButton(self.Amplified_Lower_Frame)
        self.amp_next_pushButton.setObjectName(u"amp_next_pushButton")
        self.amp_next_pushButton.setMaximumSize(QSize(102, 24))
        self.amp_next_pushButton.setFont(font)
        self.amp_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_4.addWidget(self.amp_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.Amplified_Lower_Frame)

        self.amp_ScrollArea = QScrollArea(self.amp_tab)
        self.amp_ScrollArea.setObjectName(u"amp_ScrollArea")
        self.amp_ScrollArea.setMinimumSize(QSize(0, 0))
        self.amp_ScrollArea.setStyleSheet(u"background-color: rgb(0, 148, 0);")
        self.amp_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.amp_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.amp_ScrollArea.setWidgetResizable(True)
        self.amp_ScrollAreaContents = QWidget()
        self.amp_ScrollAreaContents.setObjectName(u"amp_ScrollAreaContents")
        self.amp_ScrollAreaContents.setGeometry(QRect(0, 0, 617, 365))
        self.verticalLayout_11 = QVBoxLayout(self.amp_ScrollAreaContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.amp_gridLayout = QGridLayout()
        self.amp_gridLayout.setObjectName(u"amp_gridLayout")

        self.verticalLayout_11.addLayout(self.amp_gridLayout)

        self.amp_ScrollArea.setWidget(self.amp_ScrollAreaContents)

        self.verticalLayout_6.addWidget(self.amp_ScrollArea)

        self.tabWidget.addTab(self.amp_tab, "")
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
        self.kjv_version_label.setFont(font4)

        self.horizontalLayout_12.addWidget(self.kjv_version_label)

        self.kjv_book_label = QLabel(self.King_James_Upper_Frame)
        self.kjv_book_label.setObjectName(u"kjv_book_label")
        self.kjv_book_label.setMaximumSize(QSize(16777215, 31))
        self.kjv_book_label.setFont(font4)
        self.kjv_book_label.setIndent(25)

        self.horizontalLayout_12.addWidget(self.kjv_book_label)

        self.kjv_chapter_label = QLabel(self.King_James_Upper_Frame)
        self.kjv_chapter_label.setObjectName(u"kjv_chapter_label")
        self.kjv_chapter_label.setMinimumSize(QSize(45, 30))
        self.kjv_chapter_label.setMaximumSize(QSize(45, 30))
        self.kjv_chapter_label.setFont(font5)
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
        self.kjv_previous_pushButton.setFont(font)
        self.kjv_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_6.addWidget(self.kjv_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.kjv_next_pushButton = QPushButton(self.King_James_Lower_Frame)
        self.kjv_next_pushButton.setObjectName(u"kjv_next_pushButton")
        self.kjv_next_pushButton.setMaximumSize(QSize(102, 24))
        self.kjv_next_pushButton.setFont(font)
        self.kjv_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_6.addWidget(self.kjv_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.King_James_Lower_Frame)

        self.kjv_ScrollArea = QScrollArea(self.kjv_tab)
        self.kjv_ScrollArea.setObjectName(u"kjv_ScrollArea")
        self.kjv_ScrollArea.setMinimumSize(QSize(0, 0))
        self.kjv_ScrollArea.setStyleSheet(u"background-color: rgb(0, 148, 0);")
        self.kjv_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.kjv_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.kjv_ScrollArea.setWidgetResizable(True)
        self.kjv_ScrollAreaContents = QWidget()
        self.kjv_ScrollAreaContents.setObjectName(u"kjv_ScrollAreaContents")
        self.kjv_ScrollAreaContents.setGeometry(QRect(0, 0, 617, 365))
        self.verticalLayout_12 = QVBoxLayout(self.kjv_ScrollAreaContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.kjv_gridLayout = QGridLayout()
        self.kjv_gridLayout.setObjectName(u"kjv_gridLayout")

        self.verticalLayout_12.addLayout(self.kjv_gridLayout)

        self.kjv_ScrollArea.setWidget(self.kjv_ScrollAreaContents)

        self.verticalLayout_2.addWidget(self.kjv_ScrollArea)

        self.tabWidget.addTab(self.kjv_tab, "")
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
        self.njb_version_label.setFont(font4)

        self.horizontalLayout_13.addWidget(self.njb_version_label)

        self.njb_book_label = QLabel(self.New_Jerusalem_Upper_Frame)
        self.njb_book_label.setObjectName(u"njb_book_label")
        self.njb_book_label.setMaximumSize(QSize(16777215, 31))
        self.njb_book_label.setFont(font4)
        self.njb_book_label.setIndent(25)

        self.horizontalLayout_13.addWidget(self.njb_book_label)

        self.njb_chapter_label = QLabel(self.New_Jerusalem_Upper_Frame)
        self.njb_chapter_label.setObjectName(u"njb_chapter_label")
        self.njb_chapter_label.setMinimumSize(QSize(45, 30))
        self.njb_chapter_label.setMaximumSize(QSize(45, 30))
        self.njb_chapter_label.setFont(font5)
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
        self.njb_previous_pushButton.setFont(font)
        self.njb_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_8.addWidget(self.njb_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.njb_next_pushButton = QPushButton(self.New_Jerusalem_Lower_Frame)
        self.njb_next_pushButton.setObjectName(u"njb_next_pushButton")
        self.njb_next_pushButton.setMaximumSize(QSize(102, 24))
        self.njb_next_pushButton.setFont(font)
        self.njb_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_8.addWidget(self.njb_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.New_Jerusalem_Lower_Frame)

        self.njb_ScrollArea = QScrollArea(self.njb_tab)
        self.njb_ScrollArea.setObjectName(u"njb_ScrollArea")
        self.njb_ScrollArea.setMinimumSize(QSize(0, 0))
        self.njb_ScrollArea.setStyleSheet(u"background-color: rgb(0, 148, 0);")
        self.njb_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.njb_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.njb_ScrollArea.setWidgetResizable(True)
        self.njb_ScrollAreaContents = QWidget()
        self.njb_ScrollAreaContents.setObjectName(u"njb_ScrollAreaContents")
        self.njb_ScrollAreaContents.setGeometry(QRect(0, 0, 617, 365))
        self.horizontalLayout_3 = QHBoxLayout(self.njb_ScrollAreaContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.njb_gridLayout = QGridLayout()
        self.njb_gridLayout.setObjectName(u"njb_gridLayout")

        self.horizontalLayout_3.addLayout(self.njb_gridLayout)

        self.njb_ScrollArea.setWidget(self.njb_ScrollAreaContents)

        self.verticalLayout.addWidget(self.njb_ScrollArea)

        self.tabWidget.addTab(self.njb_tab, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.bible_content_display_page)
        self.bible_fun_facts_page = QWidget()
        self.bible_fun_facts_page.setObjectName(u"bible_fun_facts_page")
        self.verticalLayout_13 = QVBoxLayout(self.bible_fun_facts_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea = QScrollArea(self.bible_fun_facts_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 643, 504))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Page_Title_Frame = QFrame(self.scrollAreaWidgetContents_2)
        self.Page_Title_Frame.setObjectName(u"Page_Title_Frame")
        self.Page_Title_Frame.setMinimumSize(QSize(0, 80))
        self.Page_Title_Frame.setMaximumSize(QSize(16777215, 80))
        self.Page_Title_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Page_Title_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Page_Title_Frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.page_title = QLabel(self.Page_Title_Frame)
        self.page_title.setObjectName(u"page_title")
        self.page_title.setMinimumSize(QSize(191, 50))
        self.page_title.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamilies([u"Segoe Script"])
        font6.setPointSize(11)
        font6.setBold(True)
        self.page_title.setFont(font6)

        self.horizontalLayout_7.addWidget(self.page_title)

        self.page_intro = QLabel(self.Page_Title_Frame)
        self.page_intro.setObjectName(u"page_intro")
        self.page_intro.setMinimumSize(QSize(301, 50))
        self.page_intro.setMaximumSize(QSize(16777215, 50))
        self.page_intro.setFont(font6)

        self.horizontalLayout_7.addWidget(self.page_intro)


        self.verticalLayout_15.addWidget(self.Page_Title_Frame)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_10 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_10)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_18)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_11)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_15)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_14.addWidget(self.frame_13)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_13.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.bible_fun_facts_page)
        self.bible_study_plan_page = QWidget()
        self.bible_study_plan_page.setObjectName(u"bible_study_plan_page")
        self.verticalLayout_26 = QVBoxLayout(self.bible_study_plan_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_5 = QLabel(self.bible_study_plan_page)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_26.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.bible_study_plan_page)
        self.bible_study_topics_page = QWidget()
        self.bible_study_topics_page.setObjectName(u"bible_study_topics_page")
        self.verticalLayout_24 = QVBoxLayout(self.bible_study_topics_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame = QFrame(self.bible_study_topics_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_25.addWidget(self.label)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_25.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_25.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_25.addWidget(self.pushButton_3)


        self.verticalLayout_24.addWidget(self.frame)

        self.stackedWidget.addWidget(self.bible_study_topics_page)
        self.bible_study_character_page = QWidget()
        self.bible_study_character_page.setObjectName(u"bible_study_character_page")
        self.verticalLayout_16 = QVBoxLayout(self.bible_study_character_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.scrollArea_2 = QScrollArea(self.bible_study_character_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 596, 450))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_19 = QFrame(self.scrollAreaWidgetContents)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 60))
        self.frame_19.setMaximumSize(QSize(16777215, 60))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.frame_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(261, 40))
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setFont(font6)

        self.horizontalLayout_9.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_19)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(291, 40))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setFont(font6)

        self.horizontalLayout_9.addWidget(self.label_4)


        self.verticalLayout_20.addWidget(self.frame_19)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_79 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setMinimumSize(QSize(280, 40))
        self.pushButton_79.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_79)

        self.pushButton_82 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setMinimumSize(QSize(280, 40))
        self.pushButton_82.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_82)

        self.pushButton_86 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_86.setObjectName(u"pushButton_86")
        self.pushButton_86.setMinimumSize(QSize(280, 40))
        self.pushButton_86.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_86)

        self.pushButton_84 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_84.setObjectName(u"pushButton_84")
        self.pushButton_84.setMinimumSize(QSize(280, 40))
        self.pushButton_84.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_84)

        self.pushButton_85 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_85.setObjectName(u"pushButton_85")
        self.pushButton_85.setMinimumSize(QSize(280, 40))
        self.pushButton_85.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_85)

        self.pushButton_83 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_83.setObjectName(u"pushButton_83")
        self.pushButton_83.setMinimumSize(QSize(280, 40))
        self.pushButton_83.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_83)

        self.pushButton_81 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_81.setObjectName(u"pushButton_81")
        self.pushButton_81.setMinimumSize(QSize(280, 40))
        self.pushButton_81.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_81)

        self.pushButton_80 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_80.setObjectName(u"pushButton_80")
        self.pushButton_80.setMinimumSize(QSize(280, 40))
        self.pushButton_80.setMaximumSize(QSize(280, 40))

        self.verticalLayout_17.addWidget(self.pushButton_80)


        self.horizontalLayout_11.addLayout(self.verticalLayout_17)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.horizontalLayout_11.addWidget(self.widget)


        self.verticalLayout_20.addLayout(self.horizontalLayout_11)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_16.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.bible_study_character_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_22 = QVBoxLayout(self.settings_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_2 = QLabel(self.settings_page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_22.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.settings_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Student of the Gospel Bible", None))
        self.pushButton_menu.setText("")
        self.pushButton_content.setText("")
        self.esther.setText(QCoreApplication.translate("MainWindow", u"Esther", None))
        self.hebrews.setText(QCoreApplication.translate("MainWindow", u"Hebrews", None))
        self.romans.setText(QCoreApplication.translate("MainWindow", u"Romans", None))
        self.chronicles_2.setText(QCoreApplication.translate("MainWindow", u"2 Chronicles", None))
        self.jonah.setText(QCoreApplication.translate("MainWindow", u"Jonah", None))
        self.song_of_the_three_young_men.setText(QCoreApplication.translate("MainWindow", u"Song of the Three Young Men", None))
        self.timothy_2.setText(QCoreApplication.translate("MainWindow", u"2 Timothy", None))
        self.maccabees_2.setText(QCoreApplication.translate("MainWindow", u"2 Maccabees", None))
        self.john.setText(QCoreApplication.translate("MainWindow", u"John", None))
        self.joshua.setText(QCoreApplication.translate("MainWindow", u"Joshua", None))
        self.joel.setText(QCoreApplication.translate("MainWindow", u"Joel", None))
        self.galatians.setText(QCoreApplication.translate("MainWindow", u"Galatians", None))
        self.judges.setText(QCoreApplication.translate("MainWindow", u"Judges", None))
        self.revelation.setText(QCoreApplication.translate("MainWindow", u"Revelation", None))
        self.thessalonians_2.setText(QCoreApplication.translate("MainWindow", u"2 Thessalonians ", None))
        self.corinthians_1.setText(QCoreApplication.translate("MainWindow", u"1 Corinthians", None))
        self.hosea.setText(QCoreApplication.translate("MainWindow", u"Hosea", None))
        self.ephesians.setText(QCoreApplication.translate("MainWindow", u"Ephesians", None))
        self.numbers.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.mark.setText(QCoreApplication.translate("MainWindow", u"Mark", None))
        self.maccabees_1.setText(QCoreApplication.translate("MainWindow", u"1 Maccabees", None))
        self.judith.setText(QCoreApplication.translate("MainWindow", u"Judith", None))
        self.micah.setText(QCoreApplication.translate("MainWindow", u"Micah", None))
        self.job.setText(QCoreApplication.translate("MainWindow", u"Job", None))
        self.luke.setText(QCoreApplication.translate("MainWindow", u"Luke", None))
        self.ezekiel.setText(QCoreApplication.translate("MainWindow", u"Ezekiel", None))
        self.ruth.setText(QCoreApplication.translate("MainWindow", u"Ruth", None))
        self.amos.setText(QCoreApplication.translate("MainWindow", u"Amos", None))
        self.peter_2.setText(QCoreApplication.translate("MainWindow", u"2 Peter", None))
        self.sirach.setText(QCoreApplication.translate("MainWindow", u"Sirach", None))
        self.kings_2.setText(QCoreApplication.translate("MainWindow", u"2 Kings", None))
        self.song_of_songs.setText(QCoreApplication.translate("MainWindow", u"Song of Songs", None))
        self.wisdom_of_solomon.setText(QCoreApplication.translate("MainWindow", u"Wisdom of Solomon", None))
        self.psalms.setText(QCoreApplication.translate("MainWindow", u"Psalms", None))
        self.john_2.setText(QCoreApplication.translate("MainWindow", u"2 John", None))
        self.jeremiah.setText(QCoreApplication.translate("MainWindow", u"Jeremiah", None))
        self.john_1.setText(QCoreApplication.translate("MainWindow", u"1 John", None))
        self.timothy_1.setText(QCoreApplication.translate("MainWindow", u"1 Timothy", None))
        self.tobit.setText(QCoreApplication.translate("MainWindow", u"Tobit", None))
        self.samuel_1.setText(QCoreApplication.translate("MainWindow", u"1 Samuel", None))
        self.nehemiah.setText(QCoreApplication.translate("MainWindow", u"Nehemiah", None))
        self.bel_and_the_dragon.setText(QCoreApplication.translate("MainWindow", u"Bel and the Dragon ", None))
        self.proverbs.setText(QCoreApplication.translate("MainWindow", u"Proverbs", None))
        self.isaiah.setText(QCoreApplication.translate("MainWindow", u"Isaiah", None))
        self.acts.setText(QCoreApplication.translate("MainWindow", u"Acts", None))
        self.genesis.setText(QCoreApplication.translate("MainWindow", u"Genesis", None))
        self.colossians.setText(QCoreApplication.translate("MainWindow", u"Colossians", None))
        self.daniel.setText(QCoreApplication.translate("MainWindow", u"Daniel", None))
        self.leviticus.setText(QCoreApplication.translate("MainWindow", u"Leviticus", None))
        self.ezra.setText(QCoreApplication.translate("MainWindow", u"Ezra", None))
        self.esther_greek.setText(QCoreApplication.translate("MainWindow", u"Esther (Greek)", None))
        self.philippians.setText(QCoreApplication.translate("MainWindow", u"Philippians", None))
        self.haggai.setText(QCoreApplication.translate("MainWindow", u"Haggai", None))
        self.john_3.setText(QCoreApplication.translate("MainWindow", u"3 John", None))
        self.zechariah.setText(QCoreApplication.translate("MainWindow", u"Zechariah", None))
        self.philemon.setText(QCoreApplication.translate("MainWindow", u"Philemon", None))
        self.jude.setText(QCoreApplication.translate("MainWindow", u"Jude", None))
        self.exodus.setText(QCoreApplication.translate("MainWindow", u"Exodus", None))
        self.thessalonians_1.setText(QCoreApplication.translate("MainWindow", u"1 Thessalonians", None))
        self.malachi.setText(QCoreApplication.translate("MainWindow", u"Malachi", None))
        self.habakkuk.setText(QCoreApplication.translate("MainWindow", u"Habakkuk", None))
        self.james.setText(QCoreApplication.translate("MainWindow", u"James", None))
        self.lamentations.setText(QCoreApplication.translate("MainWindow", u"Lamentations", None))
        self.kings_1.setText(QCoreApplication.translate("MainWindow", u"1 Kings", None))
        self.samuel_2.setText(QCoreApplication.translate("MainWindow", u"2 Samuel", None))
        self.matthew.setText(QCoreApplication.translate("MainWindow", u"Matthew", None))
        self.chronicles_1.setText(QCoreApplication.translate("MainWindow", u"1 Chronicles", None))
        self.zephaniah.setText(QCoreApplication.translate("MainWindow", u"Zephaniah", None))
        self.susana.setText(QCoreApplication.translate("MainWindow", u"Susana", None))
        self.letter_of_jeremiah.setText(QCoreApplication.translate("MainWindow", u"Letter of Jeremiah", None))
        self.obadiah.setText(QCoreApplication.translate("MainWindow", u"Obadiah", None))
        self.peter_1.setText(QCoreApplication.translate("MainWindow", u"1 Peter", None))
        self.titus.setText(QCoreApplication.translate("MainWindow", u"Titus", None))
        self.nahum.setText(QCoreApplication.translate("MainWindow", u"Nahum", None))
        self.deuteronomy.setText(QCoreApplication.translate("MainWindow", u"Deuteronomy", None))
        self.baruch.setText(QCoreApplication.translate("MainWindow", u"Baruch", None))
        self.ecclesiastes.setText(QCoreApplication.translate("MainWindow", u"Ecclesiastes", None))
        self.corinthians_2.setText(QCoreApplication.translate("MainWindow", u"2 Corinthians", None))
        self.pushButton_fun_facts.setText(QCoreApplication.translate("MainWindow", u"Bible Fun Facts", None))
        self.pushButton_bible_study.setText(QCoreApplication.translate("MainWindow", u"Bible Study Plan", None))
        self.pushButton_study_topic.setText(QCoreApplication.translate("MainWindow", u"Study Topics", None))
        self.pushButton_character.setText(QCoreApplication.translate("MainWindow", u"Study Character", None))
        self.pushButton_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_quit_app.setText(QCoreApplication.translate("MainWindow", u"Quit App", None))
        self.book_name_label.setText(QCoreApplication.translate("MainWindow", u"Book Name Label", None))
        self.gn_version_label.setText(QCoreApplication.translate("MainWindow", u"Good News", None))
        self.gn_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.gn_chapter_label.setText("")
        self.gn_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.gn_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gn_tab), QCoreApplication.translate("MainWindow", u"Good News ", None))
        self.amp_version_label.setText(QCoreApplication.translate("MainWindow", u"Amplified", None))
        self.amp_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.amp_chapter_label.setText("")
        self.amp_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.amp_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.amp_tab), QCoreApplication.translate("MainWindow", u"Amplified", None))
        self.kjv_version_label.setText(QCoreApplication.translate("MainWindow", u"King James", None))
        self.kjv_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.kjv_chapter_label.setText("")
        self.kjv_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.kjv_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kjv_tab), QCoreApplication.translate("MainWindow", u"King James Version", None))
        self.njb_version_label.setText(QCoreApplication.translate("MainWindow", u"The New Jerusalem", None))
        self.njb_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.njb_chapter_label.setText("")
        self.njb_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.njb_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.njb_tab), QCoreApplication.translate("MainWindow", u"New Jerusalem Bible", None))
        self.page_title.setText(QCoreApplication.translate("MainWindow", u"Bible Fun Facts", None))
        self.page_intro.setText(QCoreApplication.translate("MainWindow", u"Did You Know The Word of God is Fun ?", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bible Study Plan", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Finish The Blble In :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"A Year Plan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Six Months Plan", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Three Months Plan", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Study Your Bible Models", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Who Would Study Today?", None))
        self.pushButton_79.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_82.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_86.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_84.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_85.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_83.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_81.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_80.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
    # retranslateUi

