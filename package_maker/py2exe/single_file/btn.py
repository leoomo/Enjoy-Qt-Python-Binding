#!/usr/bin/env python
#coding:utf-8
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Button(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)
        
        x, y, w, h = 190, 190, 96, 32
        login_btn = QtGui.QPushButton("Quit", self)
        login_btn.setGeometry(x, y, w, h)
        
        login_btn.clicked.connect(self.do_quit)

    def do_quit(self):
        QtGui.qApp.quit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    btn = Button()
    btn.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    