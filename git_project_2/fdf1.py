import sys

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QColorDialog, QColorDialog, QApplication)


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

    def coise(s, e):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выберите форму",
            "ФОРМА",
            ("Рисование", "Прямая", "Прямоугольник", "Окружность", "Треугольник"),
            1,
            False)
        if okBtnPressed:
            '''if i == "":
                self.Ris() # рисование
            if i == "":
                self.Pr() # прямая'''
            if i == "Прямоугольник":
                self.Angl() # прямоуг
            '''if i == "":
                self.Cir() # кругообразное
            if i == "":
                self.Tri() # треуг'''
    def Angl():
        def mousePressEvent(self, event):
            s = False
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            if (event.button() == Qt.LeftButton) and s == False:
                x1 = event.x
                y1 = event.y
                s = True
            elif s == True:
                x2 = event.x
                y2 = event.y
            qp.drawRect(x1, y1, abs(x2 - x1), abs(y2 - y1))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())