#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
clipboard demo

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qclipboard.html    
"""
import platform
import sys
import time

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


def get_platform_name():
    name = None
    while not name:
        try:
            return platform.system()
        except IOError:
            time.sleep(0.1)


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

#        if get_platform_name() == "Darwin":
#            self.setAttribute(QtCore.Qt.WA_MacBrushedMetal, True)


    def show_and_raise(self):
        self.show()
        self.raise_()

    def keyPressEvent(self, evt):
        key = evt.key()
        modifier = evt.modifiers()

        IS_PASTE = (modifier == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_V)
        if IS_PASTE:
            print 'is_paste'

            clipboard = QtGui.QApplication.clipboard()
            mime_data = clipboard.mimeData()

            print "urls:", [i.toLocalFile() for i in mime_data.urls()]
            print "text:", mime_data.text()
            print "html:", mime_data.html()            

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
