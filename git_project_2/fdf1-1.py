import sys

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QColorDialog, QInputDialog, QApplication)
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

k = {'00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,
     '00': 0,


a = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Растровый графический редактор')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Цвет")
        self.button_1.clicked.connect(self.run)

        self.button_2 = QPushButton(self)
        self.button_2.move(100, 40)
        self.button_2.setText("Форма")
        self.button_2.clicked.connect(self.coise)

        self.show()

    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_1.setStyleSheet(
                "background-color: {}".format(color.name()))
            print(color.name())

    def coise(self):
        global a
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выберите форму",
            "ФОРМА",
            ("Прямоугольник", "Окружность", "Треугольник", "Прямая"),
            0,
            False
        )
        if okBtnPressed:
            '''if i == "":
                self.Ris() # рисование
            if i == "":
                self.Pr() # прямая'''
            if i == "Прямоугольник":
                a = 1 # прямоуг

            '''if i == "":
                self.Cir() # кругообразное
            if i == "":
                self.Tri() # треуг'''
    def mousePressEvent(self, event):
        s = False
        global x1
        global x2
        global y1
        global y2
        while (event.button() == Qt.LeftButton):
            if (event.button() == Qt.LeftButton) and s == False:
                x1 = event.x
                y1 = event.y
                s = True
            elif s == True:
                x2 = event.x
                y2 = event.y
    def convert(self, a):
        for i in range(0, len(a) - 1, 2):
            a[i:i + 2]

    def paintEvent(self, event):
        global x1
        global x2
        global y1
        global y2
        qp = QPainter()
        qp.begin(self)
        if a == 1:
            qp.drawRect(x1, y1, abs(x2 - x1), abs(y2 - y1))
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
