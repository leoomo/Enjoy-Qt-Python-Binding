#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
custom QToolButton icon

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


        path = "mic-64x64.png"
        pix = QtGui.QPixmap(path)
        
        label = QtGui.QLabel(self)
        label.move(10, 10)
        label.setPixmap(pix)


        btn = QtGui.QToolButton(self)
        btn.move(10, 100)
        btn.setIconSize(QtCore.QSize(64, 64))

        # way A
#        btn.setIcon(pix)

        # way B
        icon = QtGui.QIcon(pix)
        act = QtGui.QAction(icon, "Send", self)
        btn.setDefaultAction(act)


        style = "QLabel, QToolButton { border : 1px solid red; }"
        self.setStyleSheet(style)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())