#!/usr/bin/env python
"""
custom application window icon

Test environment:
    Mac OS X 10.6.8
"""
import os
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


PWD = os.path.dirname(os.path.realpath(__file__))
icon_path = os.path.join(PWD, "qt-logo.png")


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        icon = QtGui.QIcon(icon_path)
        self.setWindowIcon(icon)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    icon = QtGui.QIcon(icon_path)
    app.setWindowIcon(icon)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
