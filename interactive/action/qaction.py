#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QAction and QKeySequence demo

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


        del_contact = "Ctrl+Shift+d"
        key_seq = QtGui.QKeySequence(del_contact)

        act = QtGui.QAction(self)
        act.setShortcut(key_seq)
        
        self.addAction(act)
        act.triggered.connect(self._short_cut_cb)

    def _short_cut_cb(self):
        print "_short_cut_cb"

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())