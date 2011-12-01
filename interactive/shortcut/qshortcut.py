#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
shortcut

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

        btn = QtGui.QToolButton(self)
        btn.setGeometry(10, 10, 100, 100)
        btn.clicked.connect(self._act_cb)

        del_contact = "Ctrl+Shift+h"
        key_seq = QtGui.QKeySequence(del_contact)
        btn.setShortcut(key_seq)

    def _act_cb(self):
        print "_act_cb"

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())