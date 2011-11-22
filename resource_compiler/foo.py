#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Qt resource system usage

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/resources.html
http://doc.qt.nokia.com/latest/rcc.html
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


import bar


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        pix = QtGui.QPixmap(":/resources/icons/camera.png")
        label = QtGui.QLabel(self)
        label.setPixmap(pix)
        label.move(10, 10)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())