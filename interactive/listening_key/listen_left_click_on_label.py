#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import wraps
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


def left_click(func, parent):
    @wraps(func)
    def wrapper(evt):
        QtGui.QLabel.mousePressEvent(parent, evt)
        if evt.button() == QtCore.Qt.LeftButton:
            parent.emit(QtCore.SIGNAL('leftClicked()'))
        func(evt)
    return wrapper


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        pic_path = ""
        pix = QtGui.QPixmap(pic_path)

        label = QtGui.QLabel()
        label.move(10, 10)
        label.setPixmap(pix)
        label.mousePressEvent = left_click(label.mousePressEvent, label)

        self.connect(label, QtCore.SIGNAL('leftClicked()'), self.on_left_clicked)

    def show_and_raise(self):
        self.show()
        self.raise_()

    def on_left_clicked(self):
        print 'left clicked'


def main():
    app = QtGui.QApplication(sys.argv)
    demo = Demo()
    demo.show_and_raise()
    app.exec_()


if __name__ == '__main__':
    main()