#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
use a ridiculous workaround way make image/jpeg works in .app

Test environment:
    Mac OS X 10.6.8

Reference:

 http://www.thetoryparty.com/2009/08/27/pyqt-and-py2app-seriously-i-dont-know-what-to-do-with-you-when-youre-like-this/

"""
import os
import sys

try:
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


from PIL import Image
import cStringIO

def jpg2png(path):
    img = Image.open(path)
    mem = cStringIO.StringIO()
    img.save(mem, format = "png")
    return mem


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        path = os.path.join(os.getenv("HOME"), "Desktop", "t.jpg")
        pix = QtGui.QPixmap()
        mem_file_obj = jpg2png(path)
        pix.loadFromData(mem_file_obj.getvalue())

        label = QtGui.QLabel(self)
        label.move(10, 10)
        label.setPixmap(pix)


    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
