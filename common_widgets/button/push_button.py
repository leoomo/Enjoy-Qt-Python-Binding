#!/usr/bin/env python
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class DemoBtn(QtGui.QWidget):
    def __init__(self):
        super(DemoBtn, self).__init__()
        
        x, y, w, h = 500, 200, 120, 50
        self.setGeometry(x, y, w, h)
        
        x, y, w, h = 10, 10, 96, 32
        btn = QtGui.QPushButton("Push button", self)
        btn.setGeometry(x, y, w, h)
        btn.clicked.connect(self._btn_cb)

    def _btn_cb(self):
        print "clicked"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    demo = DemoBtn()
    demo.show()
    sys.exit(app.exec_())
    