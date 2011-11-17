#!/usr/bin/python
# -*- coding: utf-8 -*-

# slider.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), 
            self.changeValue)
        
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setWindowTitle('Slider')
        self.setGeometry(300, 300, 250, 150)
        
    
    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('../icons/mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap('../icons/min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap('../icons/med.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('../icons/max.png'))


if __name__ == '__main__':
  
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()