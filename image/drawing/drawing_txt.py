#!/usr/bin/python
# -*- coding: utf-8 -*-

# drawtext.py

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Draw Text')

        self.text = u'中文天下'

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()


    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 20))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()