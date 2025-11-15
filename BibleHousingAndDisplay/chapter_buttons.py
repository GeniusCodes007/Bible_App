# Create and edit the buttons for displaying the content of the book toggled and chapter toggled
from books_content_organization import *
from PySide6.QtWidgets import QPushButton


class ChapterButtons(TheExtraButtons):
    font = QFont()
    font.setFamilies([u"Segoe UI"])
    font.setPointSize(10)
    font.setBold(True)
    def __init__(self):
        super().__init__()

    # Adding the maximum number of chapters in the bible, i.e., 150 chapters to the chaptersNumberGridLayout
        self.njb_verseContentLabel = None
        self.njb_verseLabel = None
        for x in range(150):
            but = QPushButton(self.centralwidget)
            but.setObjectName(f"chap_but_{x + 1}")
            but.setText(f"Chapter {x + 1}")
            self.chaptersNumberGridLayout.addWidget(but, x, 0)

    def addLabels(self):

        for x in range(len(Njb_Genesis.genesis_1)):
            self.njb_verseLabel = QLabel(self.njb_ScrollAreaContents)
            self.njb_verseLabel.setObjectName(f"v_{x + 1}")
            self.njb_verseLabel.setFont(self.font)
            self.njb_verseLabel.setMaximumSize(30, 30)
            self.njb_verseLabel.setMinimumSize(30, 30)
            self.njb_verseLabel.setFrameShape(QFrame().Shape.WinPanel)
            self.njb_verseLabel.setText(f"{x + 1}")
            self.njb_gridLayout.addWidget(self.njb_verseLabel, x, 0)

            self.njb_verseContentLabel = QLabel(self)
            self.njb_verseContentLabel.setFont(self.font)
            self.njb_verseContentLabel.setFrameShape(QFrame().Shape.WinPanel)
            self.njb_verseContentLabel.setFrameShadow(QFrame().Shadow.Raised)
            self.njb_verseContentLabel.setText(f"{Njb_Genesis.genesis_1[x+1]}")
            self.njb_gridLayout.addWidget(self.njb_verseContentLabel, x, 1)
            print(x)


    def display_function(self, num: int):
        var_ = self.findChild(QPushButton, f"chap_but_{num}")
        if var_.clicked:
            text = var_.text()[var_.text().index(" "):]
            self.gn_chapter_label.setText(text)
            self.amp_chapter_label.setText(text)
            self.kjv_chapter_label.setText(text)
            self.njb_chapter_label.setText(text)

        self.addLabels()
        #print(self.tabWidget.currentWidget())
        #print(self.tabWidget.currentIndex())



    def button_1(self): self.display_function(1)

    def button_2(self): self.display_function(2)

    def button_3(self): self.display_function(3)

    def button_4(self): self.display_function(4)

    def button_5(self): self.display_function(5)

    def button_6(self): self.display_function(6)

    def button_7(self): self.display_function(7)

    def button_8(self): self.display_function(8)

    def button_9(self): self.display_function(9)

    def button_10(self): self.display_function(10)

    def button_11(self): self.display_function(11)

    def button_12(self): self.display_function(12)

    def button_13(self): self.display_function(13)

    def button_14(self): self.display_function(14)

    def button_15(self): self.display_function(15)

    def button_16(self): self.display_function(16)

    def button_17(self): self.display_function(17)

    def button_18(self): self.display_function(18)

    def button_19(self): self.display_function(19)

    def button_20(self): self.display_function(20)

    def button_21(self): self.display_function(21)

    def button_22(self): self.display_function(22)

    def button_23(self): self.display_function(23)

    def button_24(self): self.display_function(24)

    def button_25(self): self.display_function(25)

    def button_26(self): self.display_function(26)

    def button_27(self): self.display_function(27)

    def button_28(self): self.display_function(28)

    def button_29(self): self.display_function(29)

    def button_30(self): self.display_function(30)

    def button_31(self): self.display_function(31)

    def button_32(self): self.display_function(32)

    def button_33(self): self.display_function(33)

    def button_34(self): self.display_function(34)

    def button_35(self): self.display_function(35)

    def button_36(self): self.display_function(36)

    def button_37(self): self.display_function(37)

    def button_38(self): self.display_function(38)

    def button_39(self): self.display_function(39)

    def button_40(self): self.display_function(40)

    def button_41(self): self.display_function(41)

    def button_42(self): self.display_function(42)

    def button_43(self): self.display_function(43)

    def button_44(self): self.display_function(44)

    def button_45(self): self.display_function(45)

    def button_46(self): self.display_function(46)

    def button_47(self): self.display_function(47)

    def button_48(self): self.display_function(48)

    def button_49(self): self.display_function(49)

    def button_50(self): self.display_function(50)

    def button_51(self): self.display_function(51)

    def button_52(self): self.display_function(52)

    def button_53(self): self.display_function(53)

    def button_54(self): self.display_function(54)

    def button_55(self): self.display_function(55)

    def button_56(self): self.display_function(56)

    def button_57(self): self.display_function(57)

    def button_58(self): self.display_function(58)

    def button_59(self): self.display_function(59)

    def button_60(self): self.display_function(60)

    def button_61(self): self.display_function(61)

    def button_62(self): self.display_function(62)

    def button_63(self): self.display_function(63)

    def button_64(self): self.display_function(64)

    def button_65(self): self.display_function(65)

    def button_66(self): self.display_function(66)

    def button_67(self): self.display_function(67)

    def button_68(self): self.display_function(68)

    def button_69(self): self.display_function(69)

    def button_70(self): self.display_function(70)

    def button_71(self): self.display_function(71)

    def button_72(self): self.display_function(72)

    def button_73(self): self.display_function(73)

    def button_74(self): self.display_function(74)

    def button_75(self): self.display_function(75)

    def button_76(self): self.display_function(76)

    def button_77(self): self.display_function(77)

    def button_78(self): self.display_function(78)

    def button_79(self): self.display_function(79)

    def button_80(self): self.display_function(80)

    def button_81(self): self.display_function(81)

    def button_82(self): self.display_function(82)

    def button_83(self): self.display_function(83)

    def button_84(self): self.display_function(84)

    def button_85(self): self.display_function(85)

    def button_86(self): self.display_function(86)

    def button_87(self): self.display_function(87)

    def button_88(self): self.display_function(88)

    def button_89(self): self.display_function(89)

    def button_90(self): self.display_function(90)

    def button_91(self): self.display_function(91)

    def button_92(self): self.display_function(92)

    def button_93(self): self.display_function(93)

    def button_94(self): self.display_function(94)

    def button_95(self): self.display_function(95)

    def button_96(self): self.display_function(96)

    def button_97(self): self.display_function(97)

    def button_98(self): self.display_function(98)

    def button_99(self): self.display_function(99)

    def button_100(self): self.display_function(100)

    def button_101(self): self.display_function(101)

    def button_102(self): self.display_function(102)

    def button_103(self): self.display_function(103)

    def button_104(self): self.display_function(104)

    def button_105(self): self.display_function(105)

    def button_106(self): self.display_function(106)

    def button_107(self): self.display_function(107)

    def button_108(self): self.display_function(108)

    def button_109(self): self.display_function(109)

    def button_110(self): self.display_function(110)

    def button_111(self): self.display_function(111)

    def button_112(self): self.display_function(112)

    def button_113(self): self.display_function(113)

    def button_114(self): self.display_function(114)

    def button_115(self): self.display_function(115)

    def button_116(self): self.display_function(116)

    def button_117(self): self.display_function(117)

    def button_118(self): self.display_function(118)

    def button_119(self): self.display_function(119)

    def button_120(self): self.display_function(120)

    def button_121(self): self.display_function(121)

    def button_122(self): self.display_function(122)

    def button_123(self): self.display_function(123)

    def button_124(self): self.display_function(124)

    def button_125(self): self.display_function(125)

    def button_126(self): self.display_function(126)

    def button_127(self): self.display_function(127)

    def button_128(self): self.display_function(128)

    def button_129(self): self.display_function(129)

    def button_130(self): self.display_function(130)

    def button_131(self): self.display_function(131)

    def button_132(self): self.display_function(132)

    def button_133(self): self.display_function(133)

    def button_134(self): self.display_function(134)

    def button_135(self): self.display_function(135)

    def button_136(self): self.display_function(136)

    def button_137(self): self.display_function(137)

    def button_138(self): self.display_function(138)

    def button_139(self): self.display_function(139)

    def button_140(self): self.display_function(140)

    def button_141(self): self.display_function(141)

    def button_142(self): self.display_function(142)

    def button_143(self): self.display_function(143)

    def button_144(self): self.display_function(144)

    def button_145(self): self.display_function(145)

    def button_146(self): self.display_function(146)

    def button_147(self): self.display_function(147)

    def button_148(self): self.display_function(148)

    def button_149(self): self.display_function(149)

    def button_150(self):  self.display_function(150)