from BibleHousingAndDisplay.books_buttons import BooksButtons
from PySide6.QtWidgets import QPushButton, QLabel

from BibleRunFiles.bibleCompilation import wholeBibleBooks


class ChapterButtons(BooksButtons):
    def __init__(self):
        super().__init__()

        for x in range(150):
            but = QPushButton(self.centralwidget)
            but.setObjectName(f"chap_but_{x + 1}")
            but.setText(f"Chapter {x + 1}")
            self.chaptersNumberGridLayout.addWidget(but, x, 0)
            if but.objectName() == f"chap_but_1":
                but.clicked.connect(self.s_1)
            elif but.objectName() == f"chap_but_2":
                but.clicked.connect(self.s_2)
            else:
                but.clicked.connect(self.s)


        for i in range(self.chaptersNumberGridLayout.count()):
            m = self.chaptersNumberGridLayout.findChild(QPushButton, f"chap_but_{i + 1}")
            #print(m)

    def s_1(self):
        print("but 1")
        text = self.findChild(QPushButton, "chap_but_2").text()
        print(text[len(text) - 1])

    def s_2(self):
        print("but 2")
        text = self.findChild(QPushButton, "chap_but_2").text()
        print(text[len(text) - 1])


        for x in range(50):
            lab = QLabel(self.gnScrollAreaContents)
            lab.setText(f"Verse {x + 1}")

            lab2 = QLabel(self.gnScrollAreaContents)
            lab2.setText(f"Chapter 2 vs. {x + 1}")

            self.gn_gridLayout.addWidget(lab, x, 0)
            #self.amp_gridLayout.addWidget(lab, x, 0)


            self.gn_gridLayout.addWidget(lab2, x, 1)
            #self.amp_gridLayout.addWidget(lab2, x, 1)

    def s(self):
        print("Pressed Here")