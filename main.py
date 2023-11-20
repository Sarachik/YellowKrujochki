import sys
import random as rr
import io
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        super().__init__()
        self.setMouseTracking(True)
        self.flag = False
        self.qp = QPainter()
        self.x = 0
        self.y = 0

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.figure = 1
        elif event.button() == Qt.RightButton:
            self.figure = 1
        self.drawf()

    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_rectangle(qp)
            # Завершаем рисование
            qp.end()

    def create_color(self):
        r = 255
        g = 255
        b = 0
        return r, g, b

    def draw_rectangle(self, qp):
        n = rr.randint(1, 400)
        if self.flag and self.figure == 2:
            x1 = self.x - (n // 2)
            y1 = self.y - (n // 2)
            x2 = self.x + (n // 2)
            y2 = self.y + (n // 2)
            color = self.create_color()
            print(color)
            qp.setBrush(QColor(*color))
            qp.drawRect(x1, y1, n, n)
        elif self.flag and self.figure == 1:
            x1 = self.x - (n // 2)
            y1 = self.y - (n // 2)
            color = self.create_color()
            qp.setBrush(QColor(*color))
            qp.drawEllipse(x1, y1, n, n)
        elif self.flag and self.figure == 3:
            x = self.x
            y = self.y
            coordinats = [QPoint(x, y - n), QPoint(int(x + (n ** 2 - (n // 2) ** 2) ** 0.5), y + n // 2),
                          QPoint(int(x - (n ** 2 - (n // 2) ** 2) ** 0.5), y + n // 2)]
            color = self.create_color()
            qp.setBrush(QColor(*color))
            qp.drawPolygon(coordinats)

    def drawf(self):
        self.flag = True
        self.update()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.figure = 1
            self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
