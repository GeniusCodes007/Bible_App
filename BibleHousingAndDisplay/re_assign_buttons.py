import PySide6
from PySide6.QtWidgets import QMainWindow

from BibleHousingAndDisplay.ui_Bible_ui import Ui_MainWindow

from BibleRunFiles.bibleCompilation import wholeBibleBooks


def changeText(name: PySide6.QtWidgets.QPushButton, text: str):
    name.setText(text)
    name.setObjectName(text)

class ReAssignButtons(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.genesis = None
        self.exodus = None
        self.leviticus = None
        self.numbers = None
        self.deuteronomy = None
        self.joshua = None
        self.judges = None
        self.ruth = None
        self.sam_1 = None
        self.sam_2 = None
        self.kings_1 = None
        self.kings_2 = None
        self.chronicles_1 = None
        self.chronicles_2 = None
        self.ezra = None
        self.nehemiah = None
        self.esther = None
        self.job = None
        self.psalms = None
        self.proverbs = None
        self.ecclesiastes = None
        self.song_of_songs_solomon = None
        self.isaiah = None
        self.jeremiah = None
        self.lamentations = None
        self.ezekiel = None
        self.daniel = None
        self.hosea = None
        self.joel = None
        self.amos = None
        self.obadiah = None
        self.jonah = None
        self.micah = None
        self.nahum = None
        self.habakkuk = None
        self.zephaniah = None
        self.haggai = None
        self.zechariah = None
        self.malachi = None
        self.tobit = None
        self.judith = None
        self.esther_greek = None
        self.wisdom_of_solomon = None
        self.sirach = None
        self.baruch = None
        self.letter_of_jeremiah = None
        self.song_of_young_men = None
        self.susana = None
        self.bel_and_the_dragon = None
        self.maccabees_1 = None
        self.maccabees_2 = None
        self.matthew = None
        self.mark = None
        self.luke = None
        self.john = None
        self.acts = None
        self.romans = None
        self.corinth_1 = None
        self.corinth_2 = None
        self.galatians = None
        self.ephesians = None
        self.philippians = None
        self.colossians = None
        self.thessalonians_1 = None
        self.thessalonians_2 = None
        self.timothy_1 = None
        self.timothy_2 = None
        self.titus = None
        self.philemon = None
        self.hebrews = None
        self.james = None
        self.peter_1 = None
        self.peter_2 = None
        self.john_1 = None
        self.john_2 = None
        self.john_3 = None
        self.jude = None
        self.revelation = None
        self.setupUi(self)

        self.re_assign()

    def re_assign(self):
        self.genesis = self.pushButton
        changeText(self.genesis, wholeBibleBooks[0])

        self.exodus = self.pushButton_2
        changeText(self.exodus, wholeBibleBooks[1])

        self.leviticus = self.pushButton_3
        changeText(self.leviticus, wholeBibleBooks[2])

        self.numbers = self.pushButton_4
        changeText(self.numbers, wholeBibleBooks[3])

        self.deuteronomy = self.pushButton_5
        changeText(self.deuteronomy, wholeBibleBooks[4])

        self.joshua = self.pushButton_6
        changeText(self.joshua, wholeBibleBooks[5])

        self.judges = self.pushButton_7
        changeText(self.judges, wholeBibleBooks[6])

        self.ruth = self.pushButton_8
        changeText(self.ruth, wholeBibleBooks[7])

        self.sam_1 = self.pushButton_9
        changeText(self.sam_1, wholeBibleBooks[8])

        self.sam_2 = self.pushButton_10
        changeText(self.sam_2, wholeBibleBooks[9])

        self.kings_1 = self.pushButton_11
        changeText(self.kings_1, wholeBibleBooks[10])

        self.kings_2 = self.pushButton_12
        changeText(self.kings_2, wholeBibleBooks[11])

        self.chronicles_1 = self.pushButton_13
        changeText(self.chronicles_1, wholeBibleBooks[12])

        self.chronicles_2 = self.pushButton_14
        changeText(self.chronicles_2, wholeBibleBooks[13])

        self.ezra = self.pushButton_15
        changeText(self.ezra, wholeBibleBooks[14])

        self.nehemiah = self.pushButton_16
        changeText(self.nehemiah, wholeBibleBooks[15])

        self.esther = self.pushButton_17
        changeText(self.esther, wholeBibleBooks[16])

        self.job = self.pushButton_18
        changeText(self.job, wholeBibleBooks[17])

        self.psalms = self.pushButton_19
        changeText(self.psalms, wholeBibleBooks[18])

        self.proverbs = self.pushButton_20
        changeText(self.proverbs, wholeBibleBooks[19])

        self.ecclesiastes = self.pushButton_21
        changeText(self.ecclesiastes, wholeBibleBooks[20])

        self.song_of_songs_solomon = self.pushButton_22
        changeText(self.song_of_songs_solomon, wholeBibleBooks[21])

        self.isaiah = self.pushButton_23
        changeText(self.isaiah, wholeBibleBooks[22])

        self.jeremiah = self.pushButton_24
        changeText(self.jeremiah, wholeBibleBooks[23])

        self.lamentations = self.pushButton_25
        changeText(self.lamentations, wholeBibleBooks[24])

        self.ezekiel = self.pushButton_26
        changeText(self.ezekiel, wholeBibleBooks[25])

        self.daniel = self.pushButton_27
        changeText(self.daniel, wholeBibleBooks[26])

        self.hosea = self.pushButton_28
        changeText(self.hosea, wholeBibleBooks[27])

        self.joel = self.pushButton_29
        changeText(self.joel, wholeBibleBooks[28])

        self.amos = self.pushButton_30
        changeText(self.amos, wholeBibleBooks[29])

        self.obadiah = self.pushButton_31
        changeText(self.obadiah, wholeBibleBooks[30])

        self.jonah = self.pushButton_32
        changeText(self.jonah, wholeBibleBooks[31])

        self.micah = self.pushButton_33
        changeText(self.micah, wholeBibleBooks[32])

        self.nahum = self.pushButton_34
        changeText(self.nahum, wholeBibleBooks[33])

        self.habakkuk = self.pushButton_35
        changeText(self.habakkuk, wholeBibleBooks[34])

        self.zephaniah = self.pushButton_36
        changeText(self.zephaniah, wholeBibleBooks[35])

        self.haggai = self.pushButton_37
        changeText(self.haggai, wholeBibleBooks[36])

        self.zechariah = self.pushButton_38
        changeText(self.zechariah, wholeBibleBooks[37])

        self.malachi = self.pushButton_39
        changeText(self.malachi, wholeBibleBooks[38])

        self.tobit = self.pushButton_40
        changeText(self.tobit, wholeBibleBooks[39])

        self.judith = self.pushButton_41
        changeText(self.judith, wholeBibleBooks[40])

        self.esther_greek = self.pushButton_42
        changeText(self.esther_greek, wholeBibleBooks[41])

        self.wisdom_of_solomon = self.pushButton_43
        changeText(self.wisdom_of_solomon, wholeBibleBooks[42])

        self.sirach = self.pushButton_44
        changeText(self.sirach, wholeBibleBooks[43])

        self.baruch = self.pushButton_45
        changeText(self.baruch, wholeBibleBooks[44])

        self.letter_of_jeremiah = self.pushButton_46
        changeText(self.letter_of_jeremiah, wholeBibleBooks[45])

        self.song_of_young_men = self.pushButton_47
        changeText(self.song_of_young_men, wholeBibleBooks[46])

        self.susana = self.pushButton_48
        changeText(self.susana, wholeBibleBooks[47])

        self.bel_and_the_dragon = self.pushButton_49
        changeText(self.bel_and_the_dragon, wholeBibleBooks[48])

        self.maccabees_1 = self.pushButton_50
        changeText(self.maccabees_1, wholeBibleBooks[49])

        self.maccabees_2 = self.pushButton_51
        changeText(self.maccabees_2, wholeBibleBooks[50])

        self.matthew = self.pushButton_52
        changeText(self.matthew, wholeBibleBooks[51])

        self.mark = self.pushButton_53
        changeText(self.mark, wholeBibleBooks[52])

        self.luke = self.pushButton_54
        changeText(self.luke, wholeBibleBooks[53])

        self.john = self.pushButton_55
        changeText(self.john, wholeBibleBooks[54])

        self.acts = self.pushButton_56
        changeText(self.acts, wholeBibleBooks[55])

        self.romans = self.pushButton_57
        changeText(self.romans, wholeBibleBooks[56])

        self.corinth_1 = self.pushButton_58
        changeText(self.corinth_1, wholeBibleBooks[57])

        self.corinth_2 = self.pushButton_59
        changeText(self.corinth_2, wholeBibleBooks[58])

        self.galatians = self.pushButton_60
        changeText(self.galatians, wholeBibleBooks[59])

        self.ephesians = self.pushButton_61
        changeText(self.ephesians, wholeBibleBooks[60])

        self.philippians = self.pushButton_62
        changeText(self.philippians, wholeBibleBooks[61])

        self.colossians = self.pushButton_63
        changeText(self.colossians, wholeBibleBooks[62])

        self.thessalonians_1 = self.pushButton_64
        changeText(self.thessalonians_1, wholeBibleBooks[63])

        self.thessalonians_2 = self.pushButton_65
        changeText(self.thessalonians_2, wholeBibleBooks[64])

        self.timothy_1 = self.pushButton_66
        changeText(self.timothy_1, wholeBibleBooks[65])

        self.timothy_2 = self.pushButton_67
        changeText(self.timothy_2, wholeBibleBooks[66])

        self.titus = self.pushButton_68
        changeText(self.titus, wholeBibleBooks[67])

        self.philemon = self.pushButton_69
        changeText(self.philemon, wholeBibleBooks[68])

        self.hebrews = self.pushButton_70
        changeText(self.hebrews, wholeBibleBooks[69])

        self.james = self.pushButton_71
        changeText(self.james, wholeBibleBooks[70])

        self.peter_1 = self.pushButton_72
        changeText(self.peter_1, wholeBibleBooks[71])

        self.peter_2 = self.pushButton_73
        changeText(self.peter_2, wholeBibleBooks[72])

        self.john_1 = self.pushButton_74
        changeText(self.john_1, wholeBibleBooks[73])

        self.john_2 = self.pushButton_75
        changeText(self.john_2, wholeBibleBooks[74])

        self.john_3 = self.pushButton_76
        changeText(self.john_3, wholeBibleBooks[75])

        self.jude = self.pushButton_77
        changeText(self.jude, wholeBibleBooks[76])

        self.revelation = self.pushButton_78
        changeText(self.revelation, wholeBibleBooks[77])