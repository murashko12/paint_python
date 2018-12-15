import sys
from PyQt5.QtWidgets import QApplication, QMainWindow




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint")
        self.setGeometry(0, 0, 1000, 800)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()