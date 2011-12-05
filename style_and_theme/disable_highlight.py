#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
disable highlight focused widget

Test environment:
    Mac OS X 10.6.8

http://stackoverflow.com/questions/1987546/qt4-stylesheets-and-focus-rect
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


        # highlight
        tv = QtGui.QTreeView(self)
        tv.setGeometry(10, 10, 100, 100)


        # disable highlight
        tv2 = QtGui.QTreeView(self)
        tv2.setGeometry(10, 110, 100, 100)

        tv2.setFrameShape(QtGui.QFrame.NoFrame)
        tv2.setFrameShadow(QtGui.QFrame.Plain)
        tv2.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())