#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QComboBox

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QComboBox.html
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


        combo = QtGui.QComboBox(self)
        combo.move(20, 20)
        combo.activated.connect(self._cb_onActivated)
        combo.currentIndexChanged.connect(self._cb_currentIndexChanged)
        combo.highlighted.connect(self._cb_highlighted)

        items = ('', 'Lisp', 'C', 'Objective-C', 'Python', 'Java')
        combo.addItems(items)


    def _cb_onActivated(self, a):
        print 'selected:', a

    def _cb_currentIndexChanged(self, a):
        print 'index:', a

    def _cb_highlighted(self, a):
        print 'highlighted:', a

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())



