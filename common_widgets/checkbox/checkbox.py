#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QCheckBox demo

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qcheckbox.html
http://doc.qt.nokia.com/latest/qabstractbutton.html
http://doc.qt.nokia.com/latest/qt.html#CheckState-enum
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

        self._checkbox = QtGui.QCheckBox("CheckBox", self)
        self._checkbox.move(10, 10)
        self._checkbox.stateChanged.connect(self._checkbox_cb)

    def _checkbox_cb(self, state):
        assert QtCore.Qt.Unchecked == 0
        assert QtCore.Qt.Checked == 2
        assert state in (QtCore.Qt.Checked, QtCore.Qt.Unchecked, QtCore.Qt.PartiallyChecked)
        
        print "state:", state


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())