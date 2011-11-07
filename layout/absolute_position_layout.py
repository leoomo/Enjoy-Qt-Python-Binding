#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Absolute position layout demo

Test environment:
    Mac OS X 10.6.8
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 200, 100
        self.setGeometry(x, y, w, h)
        
        label1 = QtGui.QLabel('hello', self)
        label1.move(10, 10)

        label2 = QtGui.QLabel('world', self)
        label2.move(40, 40)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    app.exec_()

