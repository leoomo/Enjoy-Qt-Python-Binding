#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QToolBar and QAction demo

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QToolBar.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QAction.html
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

        self.exit = QtGui.QAction(QtGui.QIcon('../icons/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')

#        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.exit.triggered.connect(self.close)


        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())