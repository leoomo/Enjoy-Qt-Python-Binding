#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
ComboBox with auto-complete and icon item

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QComboBox.html
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


        combo = QtGui.QComboBox(self)
        combo.move(20, 20)
        combo.activated.connect(self._cb_onActivated)
        combo.currentIndexChanged.connect(self._cb_currentIndexChanged)
        combo.highlighted.connect(self._cb_highlighted)

        items = ('', 'Lisp', 'C', 'Objective-C', 'Python', 'Java')
        combo.addItems(items)


        combo2 = QtGui.QComboBox(self)
        combo2.resize(200, 30)
#        combo2.setEditable(True)
        combo2.move(20, 60)
        self.connect(combo2, QtCore.SIGNAL('activated(int)'), self._cb_onActivated2)
        self.connect(combo2, QtCore.SIGNAL('currentIndexChanged(QString)'), self._cb_currentIndexChanged2)
        combo2.editTextChanged.connect(self._cb_editTextChanged2)

        items = (
            '',
            ('Lisp', 'lisp.png'),
            ('C', 'c.png'),
            ('Objective-C', 'objc.png'),
            ('Python', 'python.png'),
            ('Java', 'java.png'),
            )
        for i in items:
            if isinstance(i, tuple):
                text, icon_path = i[0], i[1]
                combo2.addItem(QtGui.QIcon(icon_path), text)
            else:
                combo2.addItem(i)

    def _cb_onActivated(self, a):
        print 'selected:', a

    def _cb_currentIndexChanged(self, a):
        print 'index:', a

    def _cb_highlighted(self, a):
        print 'highlighted:', a
        

    def _cb_onActivated2(self, a):
        print 'selected2:', a

    def _cb_currentIndexChanged2(self, a):
        print 'index2:', a

    def _cb_editTextChanged2(self, text):
        print "text:", text

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())



