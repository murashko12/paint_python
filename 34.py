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
        self.brushSize = 1
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()                               # написание основных кнопок миню
        fileMenu = mainMenu.addMenu("Файл")                     # кнопка файл (сохранение и удаление изображения)
        brushMenu = mainMenu.addMenu("Толщина линии")           # задаем толщину линии
        brushColor = mainMenu.addMenu("Цвет")                   # задаем цвет линии
        backgroundColor = mainMenu.addMenu("Цвет заднего фона") # задаём цвет заднего фона

        save_Action = QAction("Сохранить", self)   # сохранение изображения
        save_Action.setShortcut("Ctrl+S")
        fileMenu.addAction(save_Action)
        save_Action.triggered.connect(self.save)

        clear_Action = QAction("Очистить", self) # удаление изображения
        clear_Action.setShortcut("Ctrl+C")
        fileMenu.addAction(clear_Action)
        clear_Action.triggered.connect(self.clear)

#-------------------------------------------------------------------------------------------------
        onepxAction = QAction("1px", self) # толщина линии в 1 пикселя
        onepxAction.setShortcut("Ctrl+O")
        brushMenu.addAction(onepxAction)
        onepxAction.triggered.connect(self.onePx)

        threepxAction = QAction("3px", self) # толщина линии в 3 пикселя
        threepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction("5px", self) # толщина линии в 5 пиксей
        fivepxAction.setShortcut("Ctrl+F")
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction("7px", self) # толщина линии в 7 пиксей
        sevenpxAction.setShortcut("Ctrl+C")
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction("9px", self) # толщина линии в 9 пиксей
        ninepxAction.setShortcut("Ctrl+N")
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)


#-------------------------------------------------------------------------------------------------

    def save(self):                                            # Функционал для кнопки сохранения
        save_file = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if save_file == "":
            return
        self.image.save(save_file)
        #----------------%
    def clear(self):                                           # Функция очистки
        self.image.fill(self.bg)
        self.update()
        #----------------%
    def onePx(self):                                           # Толщина линии 1 px
        self.brushSize = 1

    def threePx(self):                                         # Толщина линии 3 px
        self.brushSize = 3

    def fivePx(self):                                          # Толщина линии 5 px
        self.brushSize = 5

    def sevenPx(self):                                         # Толщина линии 7 px
        self.brushSize = 7

    def ninePx(self):                                         # Толщина линии 9 px
        self.brushSize = 9




#-------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()