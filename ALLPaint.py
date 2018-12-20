from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        '''stage = QGraphicsScene()
        brush = QBrush(Qt.red)
        pen = QPen(Qt.green)
        pen.setWidth(9)
        saw = QGraphicsView(stage, self)
        saw.setGeometry(0, 0, 1000, 800)

        krug = stage.addEllipse(1, 1, 400, 200, pen, brush)'''
        self.setWindowTitle("Paint")
        self.setGeometry(0, 0, 1000, 800)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.bg = Qt.white
        self.drawing = False
        self.brushSize = 1
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()                                   # написание основных кнопок миню
        fileMenu = mainMenu.addMenu("Файл")                         # кнопка файл (сохранение и удаление изображения)
        brushMenu = mainMenu.addMenu("Толщина линии")               # задаем толщину линии
        brushColor = mainMenu.addMenu("Цвет")                       # задаем цвет линии
        backgroundColor = mainMenu.addMenu("Цвет заднего фона")     # задаём цвет заднего фона
        geometryfigures = mainMenu.addMenu("Геометрические фигуры") # геометрические фигуры

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

        twentypxAction = QAction(QIcon("Project/paint_python/git_project_2/er20.png"), "20px для ластика", self) # толщина линии для ластика 1
        twentypxAction.setShortcut("Ctrl+1")
        brushMenu.addAction(twentypxAction)
        twentypxAction.triggered.connect(self.twentyPx)

        fourtypxAction = QAction(QIcon("Project/paint_python/git_project_2/er40.png"), "40px для ластика", self) # толщина линии для ластика 2
        fourtypxAction.setShortcut("Ctrl+2")
        brushMenu.addAction(fourtypxAction)
        fourtypxAction.triggered.connect(self.fourtyPx)

#-------------------------------------------------------------------------------------------------
        whiteAction = QAction(QIcon("Project/paint_python/git_project_2/white.png"), "Белый", self) # линия белого цвета
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.White_Color)

        blackAction = QAction(QIcon("Project/paint_python/git_project_2/black.png"), "Чёрный", self) # линия черного цвета
        blackAction.setShortcut("Ctrl+D")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.Black_Color)

        redAction = QAction(QIcon("Project/paint_python/git_project_2/red.png"), "Красный", self) # линия красного цвета
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.Red_Color)

        greenAction = QAction(QIcon("Project/paint_python/git_project_2/green.png"), "Зелёный", self) # линия зелёного цвета
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.Green_Color)

        yellowAction = QAction(QIcon("Project/paint_python/git_project_2/yellow.png"), "Желтый", self) # линия желтого цвета
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.Yellow_Color)

        blueAction = QAction(QIcon("Project/paint_python/git_project_2/blue.png"), "Синий", self) # линия синий цвета
        blueAction.setShortcut("Ctrl+B")
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.Blue_Color)

        eraseAction = QAction(QIcon("Project/paint_python/git_project_2/er40.png"), "Ластик", self) # ластик
        eraseAction.setShortcut("Ctrl+L")
        brushColor.addAction(eraseAction)
        eraseAction.triggered.connect(self.Erase_Color)

        ##################################################################
        '''
        eraser =
        '''
        ##################################################################
        back_ground_Color = QAction(QIcon("Project/paint_python/git_project_2/white.png"), "Белый", self) # цвет фона белый
        back_ground_Color.setShortcut("Ctrl+W")
        backgroundColor.addAction(back_ground_Color)
        back_ground_Color.triggered.connect(self.White_back_ground)

        back_ground_Color = QAction(QIcon("Project/paint_python/git_project_2/black.png"), "Чёрнай", self) # цвет фона чёрный
        back_ground_Color.setShortcut("Ctrl+B")
        backgroundColor.addAction(back_ground_Color)
        back_ground_Color.triggered.connect(self.Black_back_ground)

        back_ground_Color = QAction(QIcon("Project/paint_python/git_project_2/red.png"), "Красный", self) # цвет фона красный
        back_ground_Color.setShortcut("Ctrl+B")
        backgroundColor.addAction(back_ground_Color)
        back_ground_Color.triggered.connect(self.Red_back_ground)

        back_ground_Color = QAction(QIcon("Project/paint_python/git_project_2/green.png"), "Зеленый", self) # цвет фона зеленый
        back_ground_Color.setShortcut("Ctrl+G")
        backgroundColor.addAction(back_ground_Color)
        back_ground_Color.triggered.connect(self.Green_back_ground)

        back_ground_Color = QAction(QIcon("Project/paint_python/git_project_2/yellow.png"), "Жёлтый", self) # цвет фона жёлтый
        back_ground_Color.setShortcut("Ctrl+Y")
        backgroundColor.addAction(back_ground_Color)
        back_ground_Color.triggered.connect(self.Yellow_back_ground)

        back_ground_Color = QAction(QIcon("Project/paint_python/git_project_2/blue.png"), "Синий", self) # цвет фона синий
        back_ground_Color.setShortcut("Ctrl+B")
        backgroundColor.addAction(back_ground_Color)
        back_ground_Color.triggered.connect(self.Blue_back_ground)
#-------------------------------------------------------------------------------------------------

    def mousePressEvent(self, event):   # Задаём функции рисования для левой кнопки мыши
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
#-------------------------------------------------------------------------------------------------

    def saveFileDialog(self):                        # Функция сохранения изображения
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
        self.image.save(str(fileName), "PNG")
    def save(self):

        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        print(path)
        if path:
            self.image.save(path);
        else:
            self.image.save('noname.png')

        #----------------%
    def clear(self):                                            # Функция очистки
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

    def twentyPx(self):                                         # Толщина линии для ластика 1
        self.brushSize = 20

    def fourtyPx(self):                                         # Толщина линии для ластика 2
        self.brushSize = 40
#-------------------------------------------------------------------------------------------------

                                                    # Цвет линии

    def Black_Color(self):
        self.brushColor = Qt.black                 # Чёрная
        pen = QPen(Qt.black)
        brush = QBrush(Qt.black)

    def Erase_Color(self):
        self.brushColor = self.bg                 # Ластик

    def White_Color(self):
        self.brushColor = Qt.white                 # Белый
        pen = QPen(Qt.white)
        brush = QBrush(Qt.white)

    def Red_Color(self):
        self.brushColor = Qt.red                   # Красный
        pen = QPen(Qt.red)
        brush = QBrush(Qt.red)

    def Green_Color(self):
        self.brushColor = Qt.green                 # Зелёный
        pen = QPen(Qt.green)
        brush = QBrush(Qt.green)

    def Yellow_Color(self):
        self.brushColor = Qt.yellow                # Жёлтый
        pen = QPen(Qt.yellow)
        brush = QBrush(Qt.yellow)

    def Blue_Color(self):
        self.brushColor = Qt.blue                  # Синий
        pen = QPen(Qt.blue)
        brush = QBrush(Qt.blue)

#-------------------------------------------------------------------------------------------------

    def White_back_ground(self):            # Цвет заднего фона белый (стоит по умолчанию)
        self.image.fill(Qt.white)
        self.bg = Qt.white

    def Green_back_ground(self):            # Цвет заднего фона зелёный
        self.image.fill(Qt.green)
        self.bg = Qt.green

    def Black_back_ground(self):            # Цвет заднего фона чёрный
        self.image.fill(Qt.black)
        self.bg = Qt.black

    def Yellow_back_ground(self):           # Цвет заднего фона желтый
        self.image.fill(Qt.yellow)
        self.bg = Qt.yellow

    def Blue_back_ground(self):             # Цвет заднего фона синий
        self.image.fill(Qt.blue)
        self.bg = Qt.blue

    def Red_back_ground(self):              # Цвет заднего фона касный
        self.image.fill(Qt.red)
        self.bg = Qt.red

#-------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
