#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
show Full width form punctuation

Test environment:
    Mac OS X 10.6.8

http://developer.qt.nokia.com/forums/viewthread/12102/        
"""
import sys


try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

from PyQt4 import QtCore
from PyQt4 import QtGui

start = u'\u3001'
end = u'\u301E'
buf = ""
for i in xrange(ord(start), ord(end)):
#    print hex(i), unichr(i)
    buf += unichr(i)



buf = (
    u'\u3001',
    u'\u3002',
    u'\u300a',    
    u'\u300b',
    u'\u300d',
    u'\u300e',
    u'\u300f')
buf = '\n'.join(buf)

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        te = QtGui.QTextEdit(self)
        te.move(10, 10)

        te.setText(buf)

#        font = QtGui.QFont("STHeiti", 24)
#        te.setFont(font)

    def show_and_raise(self):
        self.show()
        self.raise_()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
