#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Provides a dialog widget for specifying colors

NOTE: it doesn't works on PySide.

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QColorDialog.html
"""
import sys

#try:
#    from PySide import QtCore
#    from PySide import QtGui
#except ImportError:
#    from PyQt4 import QtCore
#    from PyQt4 import QtGui

from PyQt4 import QtGui


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.get_color_btn = QtGui.QPushButton('Specifying colors', self)
        x, y = 10, 10
        self.get_color_btn.move(x, y)
        self.get_color_btn.adjustSize()
        self.get_color_btn.clicked.connect(self._get_color_btn_cb)
        qsize = self.get_color_btn.frameSize()


        self.preview_color = QtGui.QWidget(self)
        x, y, w, h = 10 + qsize.width() + 10, 10, 100, 100
        self.preview_color.setGeometry(x, y, w, h)

        color = QtGui.QColor(0, 0, 0)
        style = "QWidget { background-color: %s; }" % color.name()
        self.preview_color.setStyleSheet(style)

        
    def _get_color_btn_cb(self):
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            style = "QWidget { background-color: %s; }" % col.name()
            self.preview_color.setStyleSheet(style)


    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
