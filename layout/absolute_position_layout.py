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

        x, y, w, h = 500, 200, 300, 100
        self.setGeometry(x, y, w, h)


        label1 = QtGui.QLabel('hello', self)
        x, y = 10, 10
        label1.move(x, y)
        label1.resize(200, 30)


        text = str(label1.frameSize())
        label1.setText(text)

        # PySide.QtCore.QSize(200, 30) --> x, y
        print 'label1:', text


        label2 = QtGui.QLabel('world', self)
        x, y = 20, 40
        label2.move(x, y)
        label2.resize(300, 30)

        text = str(label2.geometry())
        label2.setText(text)

        # PySide.QtCore.QRect(20, 40, 300, 30) --> x, y, w, h
        print 'label2:', text


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    app.exec_()

