from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Paint")
        self.setGeometry(0, 0, 1000, 800)
        
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.bg = Qt.white
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        
        mainMenu = self.menuBar()                               # написание основных кнопок миню
        fileMenu = mainMenu.addMenu("Файл")                     # кнопка файл (сохранение и удаление изображения)
        brushMenu = mainMenu.addMenu("Толщина линии")           # задаем толщину линии
        brushColor = mainMenu.addMenu("Цвет")                   # задаем цвет линии
        backgroundColor = mainMenu.addMenu("Цвет заднего фона") # задаём цвет заднего фона




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
