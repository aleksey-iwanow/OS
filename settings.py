import platform, socket, re, uuid, json, psutil, logging
import os
from PyQt5.QtWidgets import QGraphicsColorizeEffect
import subprocess as sp
import psutil
import GPUtil
import sys
from datetime import datetime
import subprocess
from os import listdir, path, getcwd
from PIL import Image
from PyQt5 import uic, QtGui  # Импортируем uic
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QSize, QTimer, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor, QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QListWidgetItem, QWidget, QFileDialog, \
    QGraphicsOpacityEffect, QLabel, QTextEdit, QLineEdit, QPushButton, QFrame
import ctypes
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


commands = {
    'cd': ['cd',
           'Переходит по указанной директории'],
    'systeminfo': ['systeminfo',
                   'Системная информация'],
    'clear': ['clear',
              'Очищает консоль'],
    'help': ['help',
             'Выводит все команды'],
    'ls': ['ls',
           'Выводит все файлы и папки в текущей директории'],
    'nano': ['nano',
             'текстовый редактор'],
    'ls.dirs': ['ls.dirs',
                'Выводит только папки в текущей директории'],
    'ls.files': ['ls.files',
                 'Выводит только файлы в текущей директории'],
    'system': ['system',
               'Выполняет системную команду'],
}
#rgb(83,184,35)
style_but = '''
        QPushButton{background-color: rgb(0,0,0,0)}
        QPushButton:hover{border: none; color: rgb(0,0,0); background-color: rgb(83,184,35);}
        '''
style_but2 = '''
        QPushButton{background-color: rgb(0,0,0,0)}
        QPushButton:hover{border: none; color: rgb(0,0,0); background-color: rgb(83,184,35);}
        '''

errorFormat = '<font style="color:red">{}</font>'
warningFormat = '<font color="orange">{}</font>'
validFormat = '<font color="green">{}</font>'
darkgreenFormat = '<font color="#80CF0C";">{}</font>'
whiteFormat = '<font style="color:#A1A1A1">{}</font>'
titleFormat = '<font style="color:#010101; background-color: #1F4D3C">{}</font>'


def get_system_info():
    try:
        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

Left, Right = 1, 2
Top, Bottom = 4, 8
TopLeft = Top|Left
TopRight = Top|Right
BottomRight = Bottom|Right
BottomLeft = Bottom|Left


class App:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()


class ResizableLabel(QLabel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizeMargin = 4
        self.app = app
        # note that the Left, Top, Right, Bottom constants cannot be used as class
        # attributes if you want to use list comprehension for better performance,
        # and that's due to the variable scope behavior on Python 3
        self.sections = [x | y for x in (Left, Right) for y in (Top, Bottom)]
        self.cursors = {
            Left: Qt.SizeHorCursor,
            Top | Left: Qt.SizeFDiagCursor,
            Top: Qt.SizeVerCursor,
            Top | Right: Qt.SizeBDiagCursor,
            Right: Qt.SizeHorCursor,
            Bottom | Right: Qt.SizeFDiagCursor,
            Bottom: Qt.SizeVerCursor,
            Bottom | Left: Qt.SizeBDiagCursor,
        }
        self.startPos = self.section = None
        self.rects = {section:QRect() for section in self.sections}
        # mandatory for cursor updates
        self.setMouseTracking(True)

        # just for demonstration purposes
        background = QtGui.QPixmap(3, 3)
        background.fill(Qt.transparent)
        qp = QtGui.QPainter(background)
        pen = QtGui.QPen(Qt.darkGray, .5)
        qp.setPen(pen)
        qp.drawLine(0, 2, 2, 0)
        qp.end()
        self.background = QtGui.QBrush(background)

    def updateCursor(self, pos):
        for section, rect in self.rects.items():
            if pos in rect:
                self.setCursor(self.cursors[section])
                self.section = section
                return section
        self.unsetCursor()

    def adjustSize(self):
        del self._sizeHint
        super().adjustSize()

    def minimumSizeHint(self):
        try:
            return self._sizeHint
        except:
            return super().minimumSizeHint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.updateCursor(event.pos()):
                self.startPos = event.pos()
                return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            delta = event.pos() - self.startPos
            is_right = False

            if self.section & Left:
                is_right = True
            elif not self.section & (Left|Right):
                delta.setX(0)

            if self.section & Top:
                is_right = True

            elif not self.section & (Top|Bottom):
                delta.setY(0)
            newSize = QSize(self.width() + delta.x(), self.height() + delta.y())
            if not is_right:
                self.resize(newSize)
                self.app.WIDTH, self.app.HEIGHT = newSize.width() - 8, newSize.height() - 43
            else:
                pass
            self.startPos = event.pos()
        elif not event.buttons():
            self.updateCursor(event.pos())
        super().mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.updateCursor(event.pos())
        self.startPos = self.section = None
        self.setMinimumSize(0, 0)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        outRect = self.rect()
        inRect = self.rect().adjusted(self.resizeMargin, self.resizeMargin, -self.resizeMargin, -self.resizeMargin)
        self.rects[Left] = QRect(outRect.left(), inRect.top(), self.resizeMargin, inRect.height())
        self.rects[TopLeft] = QRect(outRect.topLeft(), inRect.topLeft())
        self.rects[Top] = QRect(inRect.left(), outRect.top(), inRect.width(), self.resizeMargin)
        self.rects[TopRight] = QRect(inRect.right(), outRect.top(), self.resizeMargin, self.resizeMargin)
        self.rects[Right] = QRect(inRect.right(), self.resizeMargin, self.resizeMargin, inRect.height())
        self.rects[BottomRight] = QRect(inRect.bottomRight(), outRect.bottomRight())
        self.rects[Bottom] = QRect(inRect.left(), inRect.bottom(), inRect.width(), self.resizeMargin)
        self.rects[BottomLeft] = QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized()

    # ---- optional, mostly for demonstration purposes ----

    def enterEvent(self, event):
        self.update()

    def leaveEvent(self, event):
        self.update()


class ClickedLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()


class AppWidget:
    def start(self, ex, child, W=900, H=700):
        self.W = W
        self.H = H
        self.WIDTH = self.W - 4
        self.HEIGHT = self.H - 39
        self.X = 200
        self.Y = 200
        self.on_click = False
        self.delta_pos = None

        self.child = child
        self.ex = ex
        self.app = ResizableLabel(self, self.ex)

        self.app.show()
        self.app.setMinimumSize(400, 250)
        self.app.resize(self.W + 4, self.H + 4)
        self.app.move(self.X - 2, self.Y - 2)
        self.app.setObjectName("app")
        self.app.setStyleSheet("""
    QLabel#app {
        background-color: rgb(0,0,0);
        
        border: 4px solid rgb(83,184,35);
        outline: 5px solid darkblue;
        color: #fff;
    }
    QWidget{color: rgb(83,184,35);font-size: 30px;font-family: 'CatV 6x12 9'}
""")

        self.title = ClickedLabel(self.app)
        self.title.clicked.connect(self.click_title)
        self.title.show()
        self.title.setText(self.child.TITLE)
        self.title.resize(self.W, 35)
        self.title.move(0, 0)
        self.title.setStyleSheet('background-color: rgb(83,184,35); color: rgb(0,0,0)')

        self.window = QLabel(self.app)
        self.window.show()
        self.window.resize(self.W, self.H - 35)
        self.window.move(0, 35)
        self.window.setStyleSheet('background-color: rgb(0,0,0,0);')

        self.button_close = QPushButton(self.title)
        self.button_close.setStyleSheet('''QPushButton
{   
    border: none;
	background-color: rgb(83,184,35);
}

QPushButton:hover
{
    border: none;
	background-color: red;
}''')
        self.button_close.show()
        self.button_close.resize(40, 35)
        self.button_close.setIconSize(QSize(35, 30))
        self.button_close.setIcon(self.ex.icon_close)
        self.button_close.move(self.W - 40, 0)
        self.button_close.clicked.connect(lambda: self.close_())

    def resizeAppEvent(self):
        self.title.resize(self.app.width()-4, self.title.height())
        self.button_close.move(self.app.width() - 44, 0)
        self.window.resize(self.app.width() - 4, self.app.height() - 39)
        self.child.resizeEvent()

    def close_(self):
        self.ex.apps.remove(self.child)
        self.app.hide()

    def click_title(self):
        self.on_click = False
        self.title.setStyleSheet('background-color: rgb(83,184,35); color: rgb(0,0,0)')

    def move(self, x, y):
        if not self.delta_pos:
            self.delta_pos = [x - self.app.x(), y - self.app.y()]

        if self.on_click:
            y_pos = y - self.delta_pos[1]
            self.app.move(x - self.delta_pos[0], (self.ex.HEIGHT_T if y_pos < self.ex.HEIGHT_T else y_pos))

    def down(self):
        self.on_click = True
        self.delta_pos = None
        self.app.setParent(self.ex)
        self.app.show()
        self.title.setStyleSheet('background-color: rgb(113,184,135); color: rgb(0,0,0)')




