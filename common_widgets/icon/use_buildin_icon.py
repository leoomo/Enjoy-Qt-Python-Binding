#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
using build-in/factory icon

Test environment:
    Mac OS X 10.6.8

Install Oxygen icon on Mac OS X via MacPorts:

    sudo port install oxygen-icons

http://doc.trolltech.com/latest/qicon.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QIcon.html
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


        QtGui.QIcon.setThemeName("Oxygen")
        custom_path = ['/opt/local/share/icons']
        QtGui.QIcon.setThemeSearchPaths(custom_path)

        print "themeName:", QtGui.QIcon.themeName()
        print "hasThemeIcon:", QtGui.QIcon.hasThemeIcon("edit-undo")


        icon = QtGui.QIcon.fromTheme("edit-undo", QtGui.QIcon(":/undo.png"))
        print "icon not found:", icon.isNull()

        lab = QtGui.QLabel('foo', self)
        pixmap = icon.pixmap(32, 32, QtGui.QIcon.Normal, QtGui.QIcon.On)
        lab.setPixmap(pixmap)
        lab.move(10, 10)


    def show_and_raise(self):
        self.show()
        self.raise_()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()


    sys.exit(app.exec_())