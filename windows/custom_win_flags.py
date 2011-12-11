#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
demo template

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


class SheetWin(QtGui.QWidget):
    def __init__(self, parent = None):
        super(SheetWin, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.Sheet)


        btn = QtGui.QPushButton("close", self)
        btn.move(10, 10)
        btn.clicked.connect(self.close)
        

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        btn = QtGui.QPushButton("btn", self)
        btn.clicked.connect(self.btn_cb)

    def btn_cb(self):
        sw_obj = SheetWin(self)
        sw_obj.show()

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())