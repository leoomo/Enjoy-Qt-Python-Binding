import sys, os
from PyQt4 import QtCore, QtGui

class Main(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, parent = None)
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)
        
        self.label = QtGui.QLabel('hello world', self)
        qf = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        self.label.setFont(qf)
        self.label.move(10, 10)
        
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    