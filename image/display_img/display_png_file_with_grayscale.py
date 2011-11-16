#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
display png file with GrayScaled feature

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QPixmap.html
"""
import os
import sys

PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)


try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


def to_grayscaled(path):
    origin = QtGui.QPixmap(path)

    img = origin.toImage()
    for i in xrange(origin.width()):
        for j in xrange(origin.height()):
            col = img.pixel(i, j)
            gray = QtGui.qGray(col)
            img.setPixel(i, j, QtGui.qRgb(gray, gray, gray))

    dst = origin.fromImage(img)
    return dst


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

#        default_portrait_path = os.path.join(PWD, 'resources', 'default_avatar', 'online-50x50.png')
        default_portrait_path = os.path.join(PWD, 'online-50x50.png')
        self.label = QtGui.QLabel('online', self)
        pix = QtGui.QPixmap(default_portrait_path)
        self.label.setPixmap(pix)
        self.label.move(10, 10)

#        default_portrait_path = os.path.join(PWD, 'resources', 'default_avatar', 'online-50x50.png')
        default_portrait_path = os.path.join(PWD, 'offline-50x50.png')
        self.label = QtGui.QLabel('offline', self)
        pix = QtGui.QPixmap(default_portrait_path)
#        pix = to_grayscaled(default_portrait_path)
        self.label.setPixmap(pix)
        self.label.move(10, 70)


    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())