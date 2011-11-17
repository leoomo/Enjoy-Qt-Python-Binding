#!/usr/bin/python
# -*- coding: utf-8 -*-

# calendar.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), 
            self.showDate)

        
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.label.move(130, 260)
        
        self.setWindowTitle('Calendar')  
        self.setGeometry(300, 300, 350, 300)
                
    def showDate(self):
      
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
