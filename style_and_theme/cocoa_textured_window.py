#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Cocoa textured window

Test environment:
    Mac OS X 10.6.8

http://stackoverflow.com/questions/1413337/cocoa-textured-window-in-qt
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

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.setUnifiedTitleAndToolBarOnMac(True)
    demo.setAttribute(QtCore.Qt.WA_MacBrushedMetal, True)
    demo.show_and_raise()

    sys.exit(app.exec_())