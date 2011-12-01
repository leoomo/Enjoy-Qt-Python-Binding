#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
vertically layout demo

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

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        vbox = QtGui.QVBoxLayout(self)

        btn1 = QtGui.QPushButton('btn 1', self)
        vbox.addWidget(btn1)

        btn2 = QtGui.QPushButton('btn 2', self)
        vbox.addWidget(btn2)

        btn3 = QtGui.QPushButton('btn 3', self)
        vbox.addWidget(btn3)

        btn4 = QtGui.QPushButton('btn 4', self)
        vbox.addWidget(btn4)

        self.setLayout(vbox)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())