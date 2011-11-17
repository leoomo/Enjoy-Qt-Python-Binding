#!/usr/bin/python

# menubar.py 

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('menubar')

        exit = QtGui.QAction(QtGui.QIcon('../icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+S')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))


        menubar = QMenuBar(self)
        self.setMenuBar(menubar)
        menubar.setGeometry(QRect(0, 0, 731, 29))

        menu_file = QMenu(menubar)
        file = menubar.addMenu('&File')
        file.addAction(exit)

        action_say = QAction(self)
        action_say.triggered.connect(self.say)

        sbar = QStatusBar()
        self.setStatusBar(sbar)

        self.show()

    def say(self):
        print 'say'

app = QtGui.QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec_())