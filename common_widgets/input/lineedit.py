#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
demo template

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qlineedit.html
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.move(10, 10)

        # required >= Qt 4.7
        self.lineedit.setPlaceholderText("placeholder")


#        http://doc.qt.nokia.com/latest/qlineedit.html#inputMask-prop
#        mac_address_mask = "HH:HH:HH:HH:HH:HH;_"
#        self.lineedit.setInputMask(mac_address_mask)

        self.lineedit.cursorPositionChanged.connect(self._lineedit_cursorPositionChanged)
        self.lineedit.returnPressed.connect(self._lineedit_returnPressed)

        self.setFocus()

    def _lineedit_cursorPositionChanged(self, old, new):
        print old, new

    def _lineedit_returnPressed(self):
        print "text:", self.lineedit.text()

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())