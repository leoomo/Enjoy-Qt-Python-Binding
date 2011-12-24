#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
package .app with py2app demo

Test environment:
    Mac OS X 10.6.8
"""
import sys

try:
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui
#from PyQt4 import QtGui

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        path = "/Users/lee/Desktop/t.jpg"
        pix = QtGui.QPixmap(path)

        label = QtGui.QLabel(self)
        label.move(10, 10)
        label.setPixmap(pix)


    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
