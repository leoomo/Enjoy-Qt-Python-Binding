#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QPixmap alphaChannel

Test environment:
    Mac OS X 10.6.8


Install Oxygen icon on Mac OS X via MacPorts:

    sudo port install oxygen-icons


http://doc.qt.nokia.com/latest/qpixmap.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QPixmap.html#PySide.QtGui.PySide.QtGui.QPixmap.alphaChannel
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


        if sys.platform == "darwin":
            QtGui.QIcon.setThemeName("Oxygen")
            QtGui.QIcon.setThemeSearchPaths(["/opt/local/share/icons"])

        icon = QtGui.QIcon.fromTheme("user-online")
#        icon = QtGui.QIcon("online.png")
        
        pix = icon.pixmap(100, 100)
        new_pix = pix.alphaChannel()

        label = QtGui.QLabel(self)
        label.move(10, 10)
        label.setPixmap(pix)

        label2 = QtGui.QLabel(self)
        label2.move(10, 110)
        label2.setPixmap(new_pix)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())