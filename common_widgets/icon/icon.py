#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
using build-in/factory icon

Test environment:
    Mac OS X 10.6.8

http://doc.trolltech.com/latest/qicon.html
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

        paths = list(QtGui.QIcon.themeSearchPaths())
#        custom_path = '/opt/local/share/qt4/demos/undo/icons'
        custom_path = '/opt/local/share/icons/oxygen/'
        paths.append(custom_path)
        QtGui.QIcon.setThemeSearchPaths(paths)
        
        print "theme search paths:"
        for i in QtGui.QIcon.themeSearchPaths():
            print i

        icon = QtGui.QIcon.fromTheme("file-exit", QtGui.QIcon(":/exit.png"))
        print icon.name(), icon.isNull()

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