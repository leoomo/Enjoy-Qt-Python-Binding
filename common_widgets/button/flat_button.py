#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
flat button

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qpushbutton.html#flat-prop
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

        self.btn = QtGui.QPushButton("Flat button", self)
        self.btn.setFlat(True)
        self.btn.clicked.connect(self._btn_cb)

    def _btn_cb(self):
        print "clicked"


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())