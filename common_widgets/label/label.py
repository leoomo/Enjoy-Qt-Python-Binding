#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Label

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QLabel.html
"""
import sys
import web

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

        # support basic rich text
        text1 = "Hello, <a href='http://www.pyside.org/'>PySide</a>"
        label1 = QtGui.QLabel(text1, self)
        x, y = 20, 20
        label1.move(x, y)
        label1.linkActivated.connect(self._label1_linkActivated)
        label1.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
    

        label2 = QtGui.QLabel(self)
        x, y = 20, 55
        label2.move(x, y)
        text2 = u'\u4e2d\u6587'
        label2.setText(text2)
        label2.setFrameStyle(QtGui.QFrame.Panel)

        print label1.text(), type(label1.text()), label1.text() == text1
        print label2.text(), type(label2.text()), label2.text() == web.safeunicode(text2)


    def show_and_raise(self):
        self.show()
        self.raise_()

    def _label1_linkActivated(self, link):
        print "you clicked the link:", link

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()


    sys.exit(app.exec_())

