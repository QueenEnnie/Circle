import sys

from random import randint
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint_circle = False
        self.setWindowTitle("Circles")
        self.setMinimumSize(1000, 1000)
        self.button.clicked.connect(self.paint_circle)
        self.button.setFixedSize(300, 100)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        if self.do_paint_circle:
            self.draw_circle(painter)
        painter.end()

    def draw_circle(self, painter):
        radius = randint(10, 500)
        x_pos = randint(radius, 1000 - radius)
        y_pos = randint(radius, 1000 - radius)
        colour = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        painter.setBrush(colour)
        painter.drawEllipse(x_pos, y_pos, radius, radius)
        self.do_paint_circle = False

    def paint_circle(self):
        self.do_paint_circle = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
