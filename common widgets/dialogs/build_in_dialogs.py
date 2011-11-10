#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Build-in dialogs demo

# NOTE: 'title' is invalid on Mac OS X 10.6.* .

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


def popup_confirm(parent, msg = None):
    title = "TIPS"
    reply = QtGui.QMessageBox.question(parent, title,
                 msg,
                 QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    if reply == QtGui.QMessageBox.Yes:
        return True
    else:
        return False

def popup_warning(parent, msg):
    title = "WARNING"
    QtGui.QMessageBox.warning(parent, title, msg, QtGui.QMessageBox.Close)

def popup_error(parent, msg):
    title = "ERROR"
    QtGui.QMessageBox.critical(parent, title, msg, QtGui.QMessageBox.Close)

def popup_about(parent, msg):
    title = "ABOUT"
    QtGui.QMessageBox.about(parent, title, msg)


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.show_and_raise()

        resp = popup_confirm(self, 'a')
        print 'resp:', resp

        popup_warning(self, 'warning message')

        popup_error(self, 'error message')

        popup_about(self, 'about message: <br />hello PyQt/PySide')

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()

    sys.exit(app.exec_())