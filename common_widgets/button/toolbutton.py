#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QToolButton demo

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qtoolbutton.html
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

        tool_btn = QtGui.QToolButton(self)
#        tool_btn.setIcon()
        tool_btn.move(100, 100)
        tool_btn.clicked.connect(self._tool_btn_cb)

    def _tool_btn_cb(self):
        print 'clicked'

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())