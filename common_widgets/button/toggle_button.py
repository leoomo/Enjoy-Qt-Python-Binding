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

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.toggle_btn = QtGui.QPushButton("Toggle button", self)
        self.toggle_btn.setCheckable(True)
        self.toggle_btn.setChecked(True)
        self.toggle_btn.move(100, 100)
        self.toggle_btn.clicked.connect(self._toggle_btn_cb)

    def _toggle_btn_cb(self):
        print "is checked:", self.toggle_btn.isChecked()

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())