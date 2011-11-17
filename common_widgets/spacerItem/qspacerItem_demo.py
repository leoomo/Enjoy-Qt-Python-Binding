#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QSpacerItem demo

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


class Demo(QtGui.QDialog):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)
        
        okBtn = QtGui.QPushButton('ok')
        cancelBtn = QtGui.QPushButton('cancel') 

        btnLayout = QtGui.QHBoxLayout()

        btnLayout.addWidget(okBtn)

        btnLayout.addSpacerItem(QtGui.QSpacerItem(50, 50))

        btnLayout.addWidget(cancelBtn)
        
        layout = QtGui.QGridLayout()

#        layout.addLayout(btnLayout, int row, int column, int rowSpan, int columnSpan, alignment = 0)
        layout.addLayout(btnLayout, 2, 0, 1, 3)
        
        self.setLayout(layout)
        
    def show_and_raise(self):
        self.show()
        self.raise_()

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show()

    app.exec_()

