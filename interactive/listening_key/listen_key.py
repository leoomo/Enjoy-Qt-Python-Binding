#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
listen key

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qwidget.html#events
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

    def show_and_raise(self):
        self.show()
        self.raise_()

    def keyPressEvent(self, evt):
        key = evt.key()
        modifier = evt.modifiers()
        DELETE_BUDDY = (modifier == QtCore.Qt.ControlModifier) and (key == QtCore.Qt.Key_Backspace)

        if DELETE_BUDDY:
            print 'pressed CMD - delete'

    def mouseDoubleClickEvent(self, evt):
        print "mouseDoubleClickEvent"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())