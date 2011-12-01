#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
layout in nest

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


class BeNestWidget(QtGui.QWidget):
    def __init__(self, container):
        super(BeNestWidget, self).__init__()

        container.addWidget(self)

        hbox = QtGui.QHBoxLayout(self)

        a_btn = QtGui.QPushButton("d", self)
        hbox.addWidget(a_btn)

        b_tn = QtGui.QPushButton("e", self)
        hbox.addWidget(b_tn)

        c_btn = QtGui.QPushButton("f", self)
        hbox.addWidget(c_btn)

        self.setLayout(hbox)


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        vbox = QtGui.QVBoxLayout(self)

        a_btn = QtGui.QPushButton("a", self)
        vbox.addWidget(a_btn)

        b_tn = QtGui.QPushButton("b", self)
        vbox.addWidget(b_tn)

        c_btn = QtGui.QPushButton("c", self)
        vbox.addWidget(c_btn)

        self.bn_widget = BeNestWidget(container = vbox)


        self.setLayout(vbox)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())