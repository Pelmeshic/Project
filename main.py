from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream, Qt
from enum import Enum


APPLICATION = QApplication([])
WINDOW = QWidget()
WINDOW.show()



main_layout = QHBoxLayout()
WINDOW.setLayout(main_layout)



file = QFile("style.css")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
APPLICATION.setStyleSheet(stream.readAll())



class chang_color():
    clr = [100, 100, 100]
    widgets = []

    def __init__(self, main_l, index):
        self.index = index
        self.ver_layout = QVBoxLayout()
        main_l.addLayout(self.ver_layout)
        if index == 0:
            self.name_label = QLabel("R")
        elif index == 1:
            self.name_label = QLabel("G")
        elif index == 2:
            self.name_label = QLabel("B")
        self.val_edit = QTextEdit("64")
        self.rect_button = QPushButton()

        chang_color.widgets.append(self.rect_button)
        
        self.ver_layout.addWidget(self.name_label, alignment = Qt.AlignCenter)
        self.ver_layout.addWidget(self.rect_button, alignment = Qt.AlignCenter)
        self.ver_layout.addWidget(self.val_edit, alignment = Qt.AlignCenter)

        self.val_edit.textChanged.connect(self.text_changed)


    def get_style():
        return(
            "background-color: rgb(" 
            + str(chang_color.clr[0])
            + ","
            + str(chang_color.clr[1])
            + ","
            + str(chang_color.clr[2])
            + ");"
        )


    def set_style():
        style = chang_color.get_style()

        for widget in chang_color.widgets:
            widget.setStyleSheet(style)


    def text_changed(self):
        chang_color.clr[self.index] = int(self.val_edit.toPlainText())
        chang_color.set_style()

        
            

vidg_1 = chang_color(main_layout, 0)
vidg_2 = chang_color(main_layout, 1)
vidg_3 = chang_color(main_layout, 2)


APPLICATION.exec_()