#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
layout in form

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

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        form = QtGui.QFormLayout(self)

        name_label = QtGui.QLabel("Name", self)
        name_lineedit = QtGui.QLineEdit(self)
        form.addRow(name_label, name_lineedit)

        age_label = QtGui.QLabel("Age", self)
        age_lineedit = QtGui.QLineEdit(self)
        form.addRow(age_label, age_lineedit)

        location_label = QtGui.QLabel("Location", self)
        location_lineedit = QtGui.QLineEdit(self)
        form.addRow(location_label, location_lineedit)


        self.setLayout(form)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())