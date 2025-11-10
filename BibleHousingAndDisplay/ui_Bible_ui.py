# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bible_uiTMNiUu.ui'
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
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)
import my_bible_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 542)
        icon = QIcon()
        icon.addFile(u":/content_icons/bible_icon_2.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(78, 157, 78);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftScrollArea = QScrollArea(self.centralwidget)
        self.leftScrollArea.setObjectName(u"leftScrollArea")
        self.leftScrollArea.setMinimumSize(QSize(250, 502))
        self.leftScrollArea.setMaximumSize(QSize(229, 16777215))
        font = QFont()
        font.setBold(True)
        self.leftScrollArea.setFont(font)
        self.leftScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.leftScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.leftScrollArea.setWidgetResizable(True)
        self.leftScrollAreaContents = QWidget()
        self.leftScrollAreaContents.setObjectName(u"leftScrollAreaContents")
        self.leftScrollAreaContents.setGeometry(QRect(0, -1805, 238, 2313))
        self.verticalLayout_23 = QVBoxLayout(self.leftScrollAreaContents)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_content = QPushButton(self.leftScrollAreaContents)
        self.pushButton_content.setObjectName(u"pushButton_content")
        self.pushButton_content.setStyleSheet(u"background-color: rgb(121, 121, 90);")
        icon1 = QIcon()
        icon1.addFile(u":/content_icons/content_hidden.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/content_icons/content_shown.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_content.setIcon(icon1)
        self.pushButton_content.setIconSize(QSize(100, 25))
        self.pushButton_content.setCheckable(True)

        self.verticalLayout_23.addWidget(self.pushButton_content)

        self.bibleBooksFrame = QFrame(self.leftScrollAreaContents)
        self.bibleBooksFrame.setObjectName(u"bibleBooksFrame")
        self.bibleBooksFrame.setMinimumSize(QSize(220, 2100))
        self.bibleBooksFrame.setMaximumSize(QSize(211, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.bibleBooksFrame.setFont(font1)
        self.bibleBooksFrame.setStyleSheet(u"QPushButton{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}")
        self.bibleBooksFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.bibleBooksFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.bibleBooksFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.bibleBooksGridLayout = QGridLayout()
        self.bibleBooksGridLayout.setObjectName(u"bibleBooksGridLayout")
        self.pushButton_55 = QPushButton(self.bibleBooksFrame)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setMinimumSize(QSize(196, 22))
        font2 = QFont()
        font2.setFamilies([u"Segoe Print"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.pushButton_55.setFont(font2)
        self.pushButton_55.setCheckable(True)
        self.pushButton_55.setChecked(False)
        self.pushButton_55.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_55, 54, 0, 1, 1)

        self.pushButton_70 = QPushButton(self.bibleBooksFrame)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setMinimumSize(QSize(196, 22))
        self.pushButton_70.setFont(font2)
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.setChecked(False)
        self.pushButton_70.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_70, 69, 0, 1, 1)

        self.pushButton_26 = QPushButton(self.bibleBooksFrame)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(196, 22))
        self.pushButton_26.setFont(font2)
        self.pushButton_26.setCheckable(True)
        self.pushButton_26.setChecked(False)
        self.pushButton_26.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_26, 25, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.bibleBooksFrame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(196, 22))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_7, 6, 0, 1, 1)

        self.pushButton_61 = QPushButton(self.bibleBooksFrame)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setMinimumSize(QSize(196, 22))
        self.pushButton_61.setFont(font2)
        self.pushButton_61.setCheckable(True)
        self.pushButton_61.setChecked(False)
        self.pushButton_61.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_61, 60, 0, 1, 1)

        self.pushButton_32 = QPushButton(self.bibleBooksFrame)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(196, 22))
        self.pushButton_32.setFont(font2)
        self.pushButton_32.setCheckable(True)
        self.pushButton_32.setChecked(False)
        self.pushButton_32.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_32, 31, 0, 1, 1)

        self.pushButton_57 = QPushButton(self.bibleBooksFrame)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setMinimumSize(QSize(196, 22))
        self.pushButton_57.setFont(font2)
        self.pushButton_57.setCheckable(True)
        self.pushButton_57.setChecked(False)
        self.pushButton_57.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_57, 56, 0, 1, 1)

        self.pushButton_40 = QPushButton(self.bibleBooksFrame)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(196, 22))
        self.pushButton_40.setFont(font2)
        self.pushButton_40.setCheckable(True)
        self.pushButton_40.setChecked(False)
        self.pushButton_40.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_40, 39, 0, 1, 1)

        self.pushButton_72 = QPushButton(self.bibleBooksFrame)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setMinimumSize(QSize(196, 22))
        self.pushButton_72.setFont(font2)
        self.pushButton_72.setCheckable(True)
        self.pushButton_72.setChecked(False)
        self.pushButton_72.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_72, 71, 0, 1, 1)

        self.pushButton_20 = QPushButton(self.bibleBooksFrame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(196, 22))
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setChecked(False)
        self.pushButton_20.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_20, 19, 0, 1, 1)

        self.pushButton_50 = QPushButton(self.bibleBooksFrame)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(196, 22))
        self.pushButton_50.setFont(font2)
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setChecked(False)
        self.pushButton_50.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_50, 49, 0, 1, 1)

        self.pushButton_69 = QPushButton(self.bibleBooksFrame)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setMinimumSize(QSize(196, 22))
        self.pushButton_69.setFont(font2)
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.setChecked(False)
        self.pushButton_69.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_69, 68, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.bibleBooksFrame)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(196, 22))
        self.pushButton_28.setFont(font2)
        self.pushButton_28.setCheckable(True)
        self.pushButton_28.setChecked(False)
        self.pushButton_28.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_28, 27, 0, 1, 1)

        self.pushButton_58 = QPushButton(self.bibleBooksFrame)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setMinimumSize(QSize(196, 22))
        self.pushButton_58.setFont(font2)
        self.pushButton_58.setCheckable(True)
        self.pushButton_58.setChecked(False)
        self.pushButton_58.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_58, 57, 0, 1, 1)

        self.pushButton_37 = QPushButton(self.bibleBooksFrame)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(196, 22))
        self.pushButton_37.setFont(font2)
        self.pushButton_37.setCheckable(True)
        self.pushButton_37.setChecked(False)
        self.pushButton_37.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_37, 36, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.bibleBooksFrame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(196, 22))
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(False)
        self.pushButton_10.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_10, 9, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.bibleBooksFrame)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(196, 22))
        self.pushButton_27.setFont(font2)
        self.pushButton_27.setCheckable(True)
        self.pushButton_27.setChecked(False)
        self.pushButton_27.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_27, 26, 0, 1, 1)

        self.pushButton_75 = QPushButton(self.bibleBooksFrame)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setMinimumSize(QSize(196, 22))
        self.pushButton_75.setFont(font2)
        self.pushButton_75.setCheckable(True)
        self.pushButton_75.setChecked(False)
        self.pushButton_75.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_75, 74, 0, 1, 1)

        self.pushButton_48 = QPushButton(self.bibleBooksFrame)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(196, 22))
        self.pushButton_48.setFont(font2)
        self.pushButton_48.setCheckable(True)
        self.pushButton_48.setChecked(False)
        self.pushButton_48.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_48, 47, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.bibleBooksFrame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(196, 22))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_8, 7, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.bibleBooksFrame)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(196, 22))
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setChecked(False)
        self.pushButton_18.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_18, 17, 0, 1, 1)

        self.pushButton_66 = QPushButton(self.bibleBooksFrame)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setMinimumSize(QSize(196, 22))
        self.pushButton_66.setFont(font2)
        self.pushButton_66.setCheckable(True)
        self.pushButton_66.setChecked(False)
        self.pushButton_66.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_66, 65, 0, 1, 1)

        self.pushButton_35 = QPushButton(self.bibleBooksFrame)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(196, 22))
        self.pushButton_35.setFont(font2)
        self.pushButton_35.setCheckable(True)
        self.pushButton_35.setChecked(False)
        self.pushButton_35.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_35, 34, 0, 1, 1)

        self.pushButton = QPushButton(self.bibleBooksFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(196, 22))
        self.pushButton.setFont(font2)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.bibleBooksFrame)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(196, 22))
        self.pushButton_33.setFont(font2)
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setChecked(False)
        self.pushButton_33.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_33, 32, 0, 1, 1)

        self.pushButton_42 = QPushButton(self.bibleBooksFrame)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(196, 22))
        self.pushButton_42.setFont(font2)
        self.pushButton_42.setCheckable(True)
        self.pushButton_42.setChecked(False)
        self.pushButton_42.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_42, 41, 0, 1, 1)

        self.pushButton_52 = QPushButton(self.bibleBooksFrame)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMinimumSize(QSize(196, 22))
        self.pushButton_52.setFont(font2)
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.setChecked(False)
        self.pushButton_52.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_52, 51, 0, 1, 1)

        self.pushButton_43 = QPushButton(self.bibleBooksFrame)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMinimumSize(QSize(196, 22))
        self.pushButton_43.setFont(font2)
        self.pushButton_43.setCheckable(True)
        self.pushButton_43.setChecked(False)
        self.pushButton_43.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_43, 42, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.bibleBooksFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(196, 22))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)

        self.pushButton_41 = QPushButton(self.bibleBooksFrame)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(196, 22))
        self.pushButton_41.setFont(font2)
        self.pushButton_41.setCheckable(True)
        self.pushButton_41.setChecked(False)
        self.pushButton_41.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_41, 40, 0, 1, 1)

        self.pushButton_71 = QPushButton(self.bibleBooksFrame)
        self.pushButton_71.setObjectName(u"pushButton_71")
        self.pushButton_71.setMinimumSize(QSize(196, 22))
        self.pushButton_71.setFont(font2)
        self.pushButton_71.setCheckable(True)
        self.pushButton_71.setChecked(False)
        self.pushButton_71.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_71, 70, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.bibleBooksFrame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(196, 22))
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setChecked(False)
        self.pushButton_16.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_16, 15, 0, 1, 1)

        self.pushButton_24 = QPushButton(self.bibleBooksFrame)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(196, 22))
        self.pushButton_24.setFont(font2)
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setChecked(False)
        self.pushButton_24.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_24, 23, 0, 1, 1)

        self.pushButton_36 = QPushButton(self.bibleBooksFrame)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(196, 22))
        self.pushButton_36.setFont(font2)
        self.pushButton_36.setCheckable(True)
        self.pushButton_36.setChecked(False)
        self.pushButton_36.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_36, 35, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.bibleBooksFrame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(196, 22))
        self.pushButton_14.setFont(font2)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setChecked(False)
        self.pushButton_14.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_14, 13, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.bibleBooksFrame)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(196, 22))
        self.pushButton_25.setFont(font2)
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setChecked(False)
        self.pushButton_25.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_25, 24, 0, 1, 1)

        self.pushButton_73 = QPushButton(self.bibleBooksFrame)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setMinimumSize(QSize(196, 22))
        self.pushButton_73.setFont(font2)
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.setChecked(False)
        self.pushButton_73.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_73, 72, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.bibleBooksFrame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(196, 22))
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setChecked(False)
        self.pushButton_15.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_15, 14, 0, 1, 1)

        self.pushButton_77 = QPushButton(self.bibleBooksFrame)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setMinimumSize(QSize(196, 22))
        self.pushButton_77.setFont(font2)
        self.pushButton_77.setCheckable(True)
        self.pushButton_77.setChecked(False)
        self.pushButton_77.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_77, 76, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.bibleBooksFrame)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(196, 22))
        self.pushButton_19.setFont(font2)
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setChecked(False)
        self.pushButton_19.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_19, 18, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.bibleBooksFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(196, 22))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_53 = QPushButton(self.bibleBooksFrame)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(196, 22))
        self.pushButton_53.setFont(font2)
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setChecked(False)
        self.pushButton_53.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_53, 52, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.bibleBooksFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(196, 22))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_63 = QPushButton(self.bibleBooksFrame)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setMinimumSize(QSize(196, 22))
        self.pushButton_63.setFont(font2)
        self.pushButton_63.setCheckable(True)
        self.pushButton_63.setChecked(False)
        self.pushButton_63.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_63, 62, 0, 1, 1)

        self.pushButton_38 = QPushButton(self.bibleBooksFrame)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(196, 22))
        self.pushButton_38.setFont(font2)
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setChecked(False)
        self.pushButton_38.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_38, 37, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.bibleBooksFrame)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(196, 22))
        self.pushButton_30.setFont(font2)
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setChecked(False)
        self.pushButton_30.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_30, 29, 0, 1, 1)

        self.pushButton_64 = QPushButton(self.bibleBooksFrame)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setMinimumSize(QSize(196, 22))
        self.pushButton_64.setFont(font2)
        self.pushButton_64.setCheckable(True)
        self.pushButton_64.setChecked(False)
        self.pushButton_64.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_64, 63, 0, 1, 1)

        self.pushButton_74 = QPushButton(self.bibleBooksFrame)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setMinimumSize(QSize(196, 22))
        self.pushButton_74.setFont(font2)
        self.pushButton_74.setCheckable(True)
        self.pushButton_74.setChecked(False)
        self.pushButton_74.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_74, 73, 0, 1, 1)

        self.pushButton_62 = QPushButton(self.bibleBooksFrame)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMinimumSize(QSize(196, 22))
        self.pushButton_62.setFont(font2)
        self.pushButton_62.setCheckable(True)
        self.pushButton_62.setChecked(False)
        self.pushButton_62.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_62, 61, 0, 1, 1)

        self.pushButton_22 = QPushButton(self.bibleBooksFrame)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(196, 22))
        self.pushButton_22.setFont(font2)
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setChecked(False)
        self.pushButton_22.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_22, 21, 0, 1, 1)

        self.pushButton_31 = QPushButton(self.bibleBooksFrame)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(196, 22))
        self.pushButton_31.setFont(font2)
        self.pushButton_31.setCheckable(True)
        self.pushButton_31.setChecked(False)
        self.pushButton_31.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_31, 30, 0, 1, 1)

        self.pushButton_45 = QPushButton(self.bibleBooksFrame)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMinimumSize(QSize(196, 22))
        self.pushButton_45.setFont(font2)
        self.pushButton_45.setCheckable(True)
        self.pushButton_45.setChecked(False)
        self.pushButton_45.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_45, 44, 0, 1, 1)

        self.pushButton_49 = QPushButton(self.bibleBooksFrame)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(196, 22))
        self.pushButton_49.setFont(font2)
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.setChecked(False)
        self.pushButton_49.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_49, 48, 0, 1, 1)

        self.pushButton_51 = QPushButton(self.bibleBooksFrame)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMinimumSize(QSize(196, 22))
        self.pushButton_51.setFont(font2)
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.setChecked(False)
        self.pushButton_51.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_51, 50, 0, 1, 1)

        self.pushButton_76 = QPushButton(self.bibleBooksFrame)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setMinimumSize(QSize(196, 22))
        self.pushButton_76.setFont(font2)
        self.pushButton_76.setCheckable(True)
        self.pushButton_76.setChecked(False)
        self.pushButton_76.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_76, 75, 0, 1, 1)

        self.pushButton_59 = QPushButton(self.bibleBooksFrame)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setMinimumSize(QSize(196, 22))
        self.pushButton_59.setFont(font2)
        self.pushButton_59.setCheckable(True)
        self.pushButton_59.setChecked(False)
        self.pushButton_59.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_59, 58, 0, 1, 1)

        self.pushButton_68 = QPushButton(self.bibleBooksFrame)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMinimumSize(QSize(196, 22))
        self.pushButton_68.setFont(font2)
        self.pushButton_68.setCheckable(True)
        self.pushButton_68.setChecked(False)
        self.pushButton_68.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_68, 67, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.bibleBooksFrame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(196, 22))
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_13, 12, 0, 1, 1)

        self.pushButton_39 = QPushButton(self.bibleBooksFrame)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(196, 22))
        self.pushButton_39.setFont(font2)
        self.pushButton_39.setCheckable(True)
        self.pushButton_39.setChecked(False)
        self.pushButton_39.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_39, 38, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.bibleBooksFrame)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(196, 22))
        self.pushButton_21.setFont(font2)
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setChecked(False)
        self.pushButton_21.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_21, 20, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.bibleBooksFrame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(196, 22))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.bibleBooksFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(196, 22))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_44 = QPushButton(self.bibleBooksFrame)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(196, 22))
        self.pushButton_44.setFont(font2)
        self.pushButton_44.setCheckable(True)
        self.pushButton_44.setChecked(False)
        self.pushButton_44.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_44, 43, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.bibleBooksFrame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(196, 22))
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_9, 8, 0, 1, 1)

        self.pushButton_54 = QPushButton(self.bibleBooksFrame)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setMinimumSize(QSize(196, 22))
        self.pushButton_54.setFont(font2)
        self.pushButton_54.setCheckable(True)
        self.pushButton_54.setChecked(False)
        self.pushButton_54.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_54, 53, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.bibleBooksFrame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(196, 22))
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(False)
        self.pushButton_12.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_12, 11, 0, 1, 1)

        self.pushButton_34 = QPushButton(self.bibleBooksFrame)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(196, 22))
        self.pushButton_34.setFont(font2)
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setChecked(False)
        self.pushButton_34.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_34, 33, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.bibleBooksFrame)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(196, 22))
        self.pushButton_29.setFont(font2)
        self.pushButton_29.setCheckable(True)
        self.pushButton_29.setChecked(False)
        self.pushButton_29.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_29, 28, 0, 1, 1)

        self.pushButton_60 = QPushButton(self.bibleBooksFrame)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setMinimumSize(QSize(196, 22))
        self.pushButton_60.setFont(font2)
        self.pushButton_60.setCheckable(True)
        self.pushButton_60.setChecked(False)
        self.pushButton_60.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_60, 59, 0, 1, 1)

        self.pushButton_46 = QPushButton(self.bibleBooksFrame)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(196, 22))
        self.pushButton_46.setFont(font2)
        self.pushButton_46.setCheckable(True)
        self.pushButton_46.setChecked(False)
        self.pushButton_46.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_46, 45, 0, 1, 1)

        self.pushButton_65 = QPushButton(self.bibleBooksFrame)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setMinimumSize(QSize(196, 22))
        self.pushButton_65.setFont(font2)
        self.pushButton_65.setCheckable(True)
        self.pushButton_65.setChecked(False)
        self.pushButton_65.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_65, 64, 0, 1, 1)

        self.pushButton_56 = QPushButton(self.bibleBooksFrame)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMinimumSize(QSize(196, 22))
        self.pushButton_56.setFont(font2)
        self.pushButton_56.setCheckable(True)
        self.pushButton_56.setChecked(False)
        self.pushButton_56.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_56, 55, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.bibleBooksFrame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(196, 22))
        self.pushButton_11.setFont(font2)
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_11, 10, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.bibleBooksFrame)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(196, 22))
        self.pushButton_23.setFont(font2)
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setChecked(False)
        self.pushButton_23.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_23, 22, 0, 1, 1)

        self.pushButton_67 = QPushButton(self.bibleBooksFrame)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMinimumSize(QSize(196, 22))
        self.pushButton_67.setFont(font2)
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.setChecked(False)
        self.pushButton_67.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_67, 66, 0, 1, 1)

        self.pushButton_47 = QPushButton(self.bibleBooksFrame)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(196, 22))
        self.pushButton_47.setFont(font2)
        self.pushButton_47.setCheckable(True)
        self.pushButton_47.setChecked(False)
        self.pushButton_47.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_47, 46, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.bibleBooksFrame)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(196, 22))
        self.pushButton_17.setFont(font2)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setChecked(False)
        self.pushButton_17.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_17, 16, 0, 1, 1)

        self.pushButton_78 = QPushButton(self.bibleBooksFrame)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setMinimumSize(QSize(196, 22))
        self.pushButton_78.setFont(font2)
        self.pushButton_78.setCheckable(True)
        self.pushButton_78.setChecked(False)
        self.pushButton_78.setAutoExclusive(True)

        self.bibleBooksGridLayout.addWidget(self.pushButton_78, 77, 0, 1, 1)


        self.verticalLayout_21.addLayout(self.bibleBooksGridLayout)


        self.verticalLayout_23.addWidget(self.bibleBooksFrame)

        self.extras_Frame = QFrame(self.leftScrollAreaContents)
        self.extras_Frame.setObjectName(u"extras_Frame")
        self.extras_Frame.setMinimumSize(QSize(0, 150))
        self.extras_Frame.setStyleSheet(u"QPushButton{\n"
"	color: rgb(213, 213, 159);\n"
"border-radius: 10px;\n"
"	background-color: rgb(121, 121, 90);\n"
"border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(170, 170, 127);\n"
"selection-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"}")
        self.extras_Frame.setFrameShape(QFrame.Shape.WinPanel)
        self.extras_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.extras_Frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_fun_facts = QPushButton(self.extras_Frame)
        self.pushButton_fun_facts.setObjectName(u"pushButton_fun_facts")
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

        self.pushButton_quit_app = QPushButton(self.extras_Frame)
        self.pushButton_quit_app.setObjectName(u"pushButton_quit_app")

        self.verticalLayout_19.addWidget(self.pushButton_quit_app)


        self.verticalLayout_23.addWidget(self.extras_Frame)

        self.leftScrollArea.setWidget(self.leftScrollAreaContents)

        self.horizontalLayout.addWidget(self.leftScrollArea)

        self.chaptersNumberFrame = QFrame(self.centralwidget)
        self.chaptersNumberFrame.setObjectName(u"chaptersNumberFrame")
        self.chaptersNumberFrame.setMinimumSize(QSize(200, 524))
        self.chaptersNumberFrame.setMaximumSize(QSize(200, 524))
        self.chaptersNumberFrame.setFrameShape(QFrame.Shape.Panel)
        self.chaptersNumberFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.chaptersNumberFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.book_name_label = QLabel(self.chaptersNumberFrame)
        self.book_name_label.setObjectName(u"book_name_label")
        self.book_name_label.setMinimumSize(QSize(180, 16))
        self.book_name_label.setMaximumSize(QSize(180, 16))
        self.book_name_label.setFont(font1)
        self.book_name_label.setIndent(0)

        self.verticalLayout_3.addWidget(self.book_name_label)

        self.chapterNumberScrollArea = QScrollArea(self.chaptersNumberFrame)
        self.chapterNumberScrollArea.setObjectName(u"chapterNumberScrollArea")
        self.chapterNumberScrollArea.setFont(font1)
        self.chapterNumberScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.chapterNumberScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.chapterNumberScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 176, 478))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.chaptersNumberInnerFrame = QFrame(self.scrollAreaWidgetContents)
        self.chaptersNumberInnerFrame.setObjectName(u"chaptersNumberInnerFrame")
        self.chaptersNumberInnerFrame.setFont(font1)
        self.chaptersNumberInnerFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.chaptersNumberInnerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.chaptersNumberInnerFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.chaptersNumberGridLayout = QGridLayout()
        self.chaptersNumberGridLayout.setObjectName(u"chaptersNumberGridLayout")

        self.verticalLayout_5.addLayout(self.chaptersNumberGridLayout)


        self.verticalLayout_4.addWidget(self.chaptersNumberInnerFrame)

        self.chapterNumberScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.chapterNumberScrollArea)


        self.horizontalLayout.addWidget(self.chaptersNumberFrame)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(630, 524))
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
        self.frame_2 = QFrame(self.gn_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(627, 54))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gn_version_label = QLabel(self.frame_2)
        self.gn_version_label.setObjectName(u"gn_version_label")
        font4 = QFont()
        font4.setFamilies([u"Segoe Script"])
        font4.setPointSize(15)
        font4.setBold(True)
        self.gn_version_label.setFont(font4)

        self.horizontalLayout_11.addWidget(self.gn_version_label)

        self.gn_book_label = QLabel(self.frame_2)
        self.gn_book_label.setObjectName(u"gn_book_label")
        self.gn_book_label.setMaximumSize(QSize(16777215, 31))
        self.gn_book_label.setFont(font4)
        self.gn_book_label.setIndent(25)

        self.horizontalLayout_11.addWidget(self.gn_book_label)

        self.gn_chapter_label = QLabel(self.frame_2)
        self.gn_chapter_label.setObjectName(u"gn_chapter_label")
        self.gn_chapter_label.setMinimumSize(QSize(35, 30))
        self.gn_chapter_label.setMaximumSize(QSize(35, 30))
        self.gn_chapter_label.setFont(font1)
        self.gn_chapter_label.setIndent(0)

        self.horizontalLayout_11.addWidget(self.gn_chapter_label)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_9 = QFrame(self.gn_tab)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 41))
        self.frame_9.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gn_previous_pushButton = QPushButton(self.frame_9)
        self.gn_previous_pushButton.setObjectName(u"gn_previous_pushButton")
        self.gn_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.gn_previous_pushButton.setFont(font1)
        self.gn_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_2.addWidget(self.gn_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.gn_next_pushButton = QPushButton(self.frame_9)
        self.gn_next_pushButton.setObjectName(u"gn_next_pushButton")
        self.gn_next_pushButton.setMaximumSize(QSize(102, 24))
        self.gn_next_pushButton.setFont(font1)
        self.gn_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_2.addWidget(self.gn_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.gn_scrollArea = QScrollArea(self.gn_tab)
        self.gn_scrollArea.setObjectName(u"gn_scrollArea")
        self.gn_scrollArea.setMinimumSize(QSize(560, 450))
        self.gn_scrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.gn_scrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.gn_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 623, 446))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gn_gridLayout = QGridLayout()
        self.gn_gridLayout.setObjectName(u"gn_gridLayout")

        self.verticalLayout_8.addLayout(self.gn_gridLayout)

        self.gn_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_7.addWidget(self.gn_scrollArea)

        self.tabWidget.addTab(self.gn_tab, "")
        self.amp_tab = QWidget()
        self.amp_tab.setObjectName(u"amp_tab")
        self.verticalLayout_6 = QVBoxLayout(self.amp_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.amp_tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(627, 54))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.amp_version_label = QLabel(self.frame_3)
        self.amp_version_label.setObjectName(u"amp_version_label")
        self.amp_version_label.setFont(font4)

        self.horizontalLayout_10.addWidget(self.amp_version_label)

        self.amp_book_label = QLabel(self.frame_3)
        self.amp_book_label.setObjectName(u"amp_book_label")
        self.amp_book_label.setMaximumSize(QSize(16777215, 31))
        self.amp_book_label.setFont(font4)
        self.amp_book_label.setIndent(25)

        self.horizontalLayout_10.addWidget(self.amp_book_label)

        self.amp_chapter_label = QLabel(self.frame_3)
        self.amp_chapter_label.setObjectName(u"amp_chapter_label")
        self.amp_chapter_label.setMinimumSize(QSize(35, 30))
        self.amp_chapter_label.setMaximumSize(QSize(35, 30))
        self.amp_chapter_label.setFont(font1)

        self.horizontalLayout_10.addWidget(self.amp_chapter_label)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.amp_tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 41))
        self.frame_7.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.amp_previous_pushButton = QPushButton(self.frame_7)
        self.amp_previous_pushButton.setObjectName(u"amp_previous_pushButton")
        self.amp_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.amp_previous_pushButton.setFont(font1)
        self.amp_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_4.addWidget(self.amp_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.amp_next_pushButton = QPushButton(self.frame_7)
        self.amp_next_pushButton.setObjectName(u"amp_next_pushButton")
        self.amp_next_pushButton.setMaximumSize(QSize(102, 24))
        self.amp_next_pushButton.setFont(font1)
        self.amp_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_4.addWidget(self.amp_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.amp_outer_frame = QFrame(self.amp_tab)
        self.amp_outer_frame.setObjectName(u"amp_outer_frame")
        self.amp_outer_frame.setFrameShape(QFrame.Shape.WinPanel)
        self.amp_outer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.amp_outer_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.amp_ScrollArea = QScrollArea(self.amp_outer_frame)
        self.amp_ScrollArea.setObjectName(u"amp_ScrollArea")
        self.amp_ScrollArea.setMinimumSize(QSize(0, 0))
        self.amp_ScrollArea.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.amp_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.amp_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.amp_ScrollArea.setWidgetResizable(True)
        self.gnScrollAreaContents_2 = QWidget()
        self.gnScrollAreaContents_2.setObjectName(u"gnScrollAreaContents_2")
        self.gnScrollAreaContents_2.setGeometry(QRect(0, -45, 589, 388))
        self.verticalLayout_11 = QVBoxLayout(self.gnScrollAreaContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.amp_inner_frame = QFrame(self.gnScrollAreaContents_2)
        self.amp_inner_frame.setObjectName(u"amp_inner_frame")
        self.amp_inner_frame.setMinimumSize(QSize(490, 370))
        self.amp_inner_frame.setFrameShape(QFrame.Shape.WinPanel)
        self.amp_inner_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.amp_inner_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.amp_gridLayout = QGridLayout()
        self.amp_gridLayout.setObjectName(u"amp_gridLayout")

        self.horizontalLayout_5.addLayout(self.amp_gridLayout)


        self.verticalLayout_11.addWidget(self.amp_inner_frame)

        self.amp_ScrollArea.setWidget(self.gnScrollAreaContents_2)

        self.verticalLayout_14.addWidget(self.amp_ScrollArea)


        self.verticalLayout_6.addWidget(self.amp_outer_frame)

        self.tabWidget.addTab(self.amp_tab, "")
        self.kjv_tab = QWidget()
        self.kjv_tab.setObjectName(u"kjv_tab")
        self.verticalLayout_2 = QVBoxLayout(self.kjv_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.kjv_tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(627, 54))
        self.frame_4.setMaximumSize(QSize(16777215, 54))
        self.frame_4.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.kjv_version_label = QLabel(self.frame_4)
        self.kjv_version_label.setObjectName(u"kjv_version_label")
        self.kjv_version_label.setFont(font4)

        self.horizontalLayout_12.addWidget(self.kjv_version_label)

        self.kjv_book_label = QLabel(self.frame_4)
        self.kjv_book_label.setObjectName(u"kjv_book_label")
        self.kjv_book_label.setMaximumSize(QSize(16777215, 31))
        self.kjv_book_label.setFont(font4)
        self.kjv_book_label.setIndent(25)

        self.horizontalLayout_12.addWidget(self.kjv_book_label)

        self.kjv_chapter_label = QLabel(self.frame_4)
        self.kjv_chapter_label.setObjectName(u"kjv_chapter_label")
        self.kjv_chapter_label.setMinimumSize(QSize(35, 30))
        self.kjv_chapter_label.setMaximumSize(QSize(35, 30))
        self.kjv_chapter_label.setFont(font1)

        self.horizontalLayout_12.addWidget(self.kjv_chapter_label)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.kjv_tab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 41))
        self.frame_8.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.kjv_previous_pushButton = QPushButton(self.frame_8)
        self.kjv_previous_pushButton.setObjectName(u"kjv_previous_pushButton")
        self.kjv_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.kjv_previous_pushButton.setFont(font1)
        self.kjv_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_6.addWidget(self.kjv_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.kjv_next_pushButton = QPushButton(self.frame_8)
        self.kjv_next_pushButton.setObjectName(u"kjv_next_pushButton")
        self.kjv_next_pushButton.setMaximumSize(QSize(102, 24))
        self.kjv_next_pushButton.setFont(font1)
        self.kjv_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_6.addWidget(self.kjv_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.kjv_outer_frame = QFrame(self.kjv_tab)
        self.kjv_outer_frame.setObjectName(u"kjv_outer_frame")
        self.kjv_outer_frame.setFrameShape(QFrame.Shape.WinPanel)
        self.kjv_outer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.kjv_outer_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.kjv_ScrollArea = QScrollArea(self.kjv_outer_frame)
        self.kjv_ScrollArea.setObjectName(u"kjv_ScrollArea")
        self.kjv_ScrollArea.setMinimumSize(QSize(0, 0))
        self.kjv_ScrollArea.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.kjv_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.kjv_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.kjv_ScrollArea.setWidgetResizable(True)
        self.gnScrollAreaContents_3 = QWidget()
        self.gnScrollAreaContents_3.setObjectName(u"gnScrollAreaContents_3")
        self.gnScrollAreaContents_3.setGeometry(QRect(0, 0, 589, 388))
        self.verticalLayout_12 = QVBoxLayout(self.gnScrollAreaContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.kjv_inner_frame = QFrame(self.gnScrollAreaContents_3)
        self.kjv_inner_frame.setObjectName(u"kjv_inner_frame")
        self.kjv_inner_frame.setMinimumSize(QSize(490, 370))
        self.kjv_inner_frame.setFrameShape(QFrame.Shape.WinPanel)
        self.kjv_inner_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.kjv_inner_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.amp_gridLayout_3 = QGridLayout()
        self.amp_gridLayout_3.setObjectName(u"amp_gridLayout_3")

        self.horizontalLayout_7.addLayout(self.amp_gridLayout_3)


        self.verticalLayout_12.addWidget(self.kjv_inner_frame)

        self.kjv_ScrollArea.setWidget(self.gnScrollAreaContents_3)

        self.verticalLayout_17.addWidget(self.kjv_ScrollArea)


        self.verticalLayout_2.addWidget(self.kjv_outer_frame)

        self.tabWidget.addTab(self.kjv_tab, "")
        self.njb_tab = QWidget()
        self.njb_tab.setObjectName(u"njb_tab")
        self.verticalLayout = QVBoxLayout(self.njb_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.njb_tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(627, 54))
        self.frame_5.setMaximumSize(QSize(16777215, 54))
        self.frame_5.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.njb_version_label = QLabel(self.frame_5)
        self.njb_version_label.setObjectName(u"njb_version_label")
        self.njb_version_label.setFont(font4)

        self.horizontalLayout_13.addWidget(self.njb_version_label)

        self.njb_book_label = QLabel(self.frame_5)
        self.njb_book_label.setObjectName(u"njb_book_label")
        self.njb_book_label.setMaximumSize(QSize(16777215, 31))
        self.njb_book_label.setFont(font4)
        self.njb_book_label.setIndent(25)

        self.horizontalLayout_13.addWidget(self.njb_book_label)

        self.njb_chapter_label = QLabel(self.frame_5)
        self.njb_chapter_label.setObjectName(u"njb_chapter_label")
        self.njb_chapter_label.setMinimumSize(QSize(35, 30))
        self.njb_chapter_label.setMaximumSize(QSize(35, 30))
        self.njb_chapter_label.setFont(font1)

        self.horizontalLayout_13.addWidget(self.njb_chapter_label)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.njb_tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 41))
        self.frame_6.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.njb_previous_pushButton = QPushButton(self.frame_6)
        self.njb_previous_pushButton.setObjectName(u"njb_previous_pushButton")
        self.njb_previous_pushButton.setMaximumSize(QSize(103, 24))
        self.njb_previous_pushButton.setFont(font1)
        self.njb_previous_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_8.addWidget(self.njb_previous_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.njb_next_pushButton = QPushButton(self.frame_6)
        self.njb_next_pushButton.setObjectName(u"njb_next_pushButton")
        self.njb_next_pushButton.setMaximumSize(QSize(102, 24))
        self.njb_next_pushButton.setFont(font1)
        self.njb_next_pushButton.setStyleSheet(u"background-color: rgb(121, 121, 90);")

        self.horizontalLayout_8.addWidget(self.njb_next_pushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_6)

        self.njb_outer_frame = QFrame(self.njb_tab)
        self.njb_outer_frame.setObjectName(u"njb_outer_frame")
        self.njb_outer_frame.setFrameShape(QFrame.Shape.WinPanel)
        self.njb_outer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.njb_outer_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.njb_ScrollArea = QScrollArea(self.njb_outer_frame)
        self.njb_ScrollArea.setObjectName(u"njb_ScrollArea")
        self.njb_ScrollArea.setMinimumSize(QSize(0, 0))
        self.njb_ScrollArea.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.njb_ScrollArea.setFrameShape(QFrame.Shape.WinPanel)
        self.njb_ScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.njb_ScrollArea.setWidgetResizable(True)
        self.gnScrollAreaContents_4 = QWidget()
        self.gnScrollAreaContents_4.setObjectName(u"gnScrollAreaContents_4")
        self.gnScrollAreaContents_4.setGeometry(QRect(0, 0, 601, 343))
        self.horizontalLayout_3 = QHBoxLayout(self.gnScrollAreaContents_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.njb_gridLayout = QGridLayout()
        self.njb_gridLayout.setObjectName(u"njb_gridLayout")

        self.horizontalLayout_3.addLayout(self.njb_gridLayout)

        self.njb_ScrollArea.setWidget(self.gnScrollAreaContents_4)

        self.verticalLayout_18.addWidget(self.njb_ScrollArea)


        self.verticalLayout.addWidget(self.njb_outer_frame)

        self.tabWidget.addTab(self.njb_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bible", None))
        self.pushButton_content.setText("")
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_72.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_75.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_73.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_77.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_74.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_fun_facts.setText(QCoreApplication.translate("MainWindow", u"Bible Fun Facts", None))
        self.pushButton_bible_study.setText(QCoreApplication.translate("MainWindow", u"Bible Study Plan", None))
        self.pushButton_study_topic.setText(QCoreApplication.translate("MainWindow", u"Study Topics", None))
        self.pushButton_character.setText(QCoreApplication.translate("MainWindow", u"Study Character", None))
        self.pushButton_quit_app.setText(QCoreApplication.translate("MainWindow", u"Quit App", None))
        self.book_name_label.setText(QCoreApplication.translate("MainWindow", u"Book Name Label", None))
        self.gn_version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.gn_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.gn_chapter_label.setText(QCoreApplication.translate("MainWindow", u"Chapter Label", None))
        self.gn_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.gn_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gn_tab), QCoreApplication.translate("MainWindow", u"Good News ", None))
        self.amp_version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.amp_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.amp_chapter_label.setText(QCoreApplication.translate("MainWindow", u"Chapter Label", None))
        self.amp_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.amp_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.amp_tab), QCoreApplication.translate("MainWindow", u"Amplified", None))
        self.kjv_version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.kjv_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.kjv_chapter_label.setText(QCoreApplication.translate("MainWindow", u"Chapter Label", None))
        self.kjv_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.kjv_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.kjv_tab), QCoreApplication.translate("MainWindow", u"King James Version", None))
        self.njb_version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.njb_book_label.setText(QCoreApplication.translate("MainWindow", u"Book Label", None))
        self.njb_chapter_label.setText(QCoreApplication.translate("MainWindow", u"Chapter Label", None))
        self.njb_previous_pushButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.njb_next_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.njb_tab), QCoreApplication.translate("MainWindow", u"New Jerusalem Bible", None))
    # retranslateUi

