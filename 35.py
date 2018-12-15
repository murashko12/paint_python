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
        whiteAction = QAction(QIcon("git_project_2/white.png"), "Белый", self) # линия белого цвета
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.White_Color)

        blackAction = QAction(QIcon("git_project_2/black.png"), "Чёрный", self) # линия черного цвета
        blackAction.setShortcut("Ctrl+D")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.Black_Color)

        redAction = QAction(QIcon("git_project_2/red.png"), "Красный", self) # линия красного цвета
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.Red_Color)

        greenAction = QAction(QIcon("git_project_2/green.png"), "Зелёный", self) # линия зелёного цвета
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.Green_Color)

        yellowAction = QAction(QIcon("git_project_2/yellow.png"), "Желтый", self) # линия желтого цвета
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.Yellow_Color)

        blueAction = QAction(QIcon("git_project_2/blue.png"), "Синий", self) # линия синий цвета
        blueAction.setShortcut("Ctrl+B")
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.Blue_Color)


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

                                                              # Цвет линии

    def Black_Color(self):
        self.brushColor = Qt.black                 # Чёрная

    def White_Color(self):
        self.brushColor = Qt.white                 # Белый

    def Red_Color(self):
        self.brushColor = Qt.red                   # Красный

    def Green_Color(self):
        self.brushColor = Qt.green                 # Зелёный

    def Yellow_Color(self):
        self.brushColor = Qt.yellow                # Жёлтый

    def Blue_Color(self):
        self.brushColor = Qt.blue                  # Синий





#-------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()