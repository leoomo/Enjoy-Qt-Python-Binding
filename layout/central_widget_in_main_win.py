#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Central widget in main window

Test environment:
    Mac OS X 10.6.8


http://www.pyside.org/docs/pyside/PySide/QtGui/QMainWindow.html#qt-main-window-framework
http://doc.qt.nokia.com/latest/qmainwindow.html#qt-main-window-framework
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

    
class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        textEdit = QtGui.QTextEdit(self)
        self.setCentralWidget(textEdit)


    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())