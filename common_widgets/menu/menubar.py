#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
menubar demo

NOTE: it doesn't works on Mac OS X

Test environment:
    Mac OS X 10.6.8

see also: toolbar.py
"""
import sys

#try:
#    from PySide import QtCore
#    from PySide import QtGui
#except ImportError:
#    from PyQt4 import QtCore
#    from PyQt4 import QtGui

from PyQt4 import QtCore
from PyQt4 import QtGui


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        exit_a = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exit_a.setShortcut('Ctrl+S')
        exit_a.setStatusTip('Exit application')
#        self.connect(exit_a, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        exit_a.triggered.connect(self.close)


        menubar = QtGui.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 731, 29))
        self.setMenuBar(menubar)


        file_menu = QtGui.QMenu(menubar)
        exit_menu = file_menu.addMenu('&Exit')
        exit_menu.addAction(exit_a)


        qt_mac_set_dock_menu


        say_a = QtGui.QAction('Say', self)
        say_a.triggered.connect(self.say)


        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_a)
        
        toolbar = self.addToolBar('Say')
        toolbar.addAction(say_a)

        

        sbar = QtGui.QStatusBar(self)
        self.setStatusBar(sbar)


    def say(self):
        print 'say'

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())