#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QToolBar and QAction demo

Test environment:
    Mac OS X 10.6.8


http://doc.qt.nokia.com/latest/qaction.html
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


        exit_a = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exit_a.setShortcut('Ctrl+Q')
#        self.connect(exit_a, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        exit_a.triggered.connect(self.close)


        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_a)

        self._toolbar = toolbar

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())