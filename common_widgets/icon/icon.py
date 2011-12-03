#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
icon

Test environment:
    Mac OS X 10.6.8

http://doc.trolltech.com/latest/qicon.html
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

        icon = QtGui.QIcon("exit.png")
        lab = QtGui.QLabel('foo', self)
        pixmap = icon.pixmap(32, 32, QtGui.QIcon.Normal, QtGui.QIcon.On)
        lab.setPixmap(pixmap)
        x, y = 10, 10
        lab.move(x, y)

        print "icon:", icon.isNull()


        icon2 = QtGui.QIcon("exit.png")
        lab2 = QtGui.QLabel('foo', self)
        pixmap = icon2.pixmap(32, 32, QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        lab2.setPixmap(pixmap)
        x, y = 10, 110
        lab2.move(x, y)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()


    sys.exit(app.exec_())