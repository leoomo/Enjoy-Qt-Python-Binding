#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
ComboBox with auto-complete and custom icon style item

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

        
        self.combo = QtGui.QComboBox(self)
        self.combo.resize(200, 30)
#        self.combo.setEditable(True)
        self.combo.move(20, 60)

        self.combo.activated.connect(self._cb_onActivated)

        self.connect(self.combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self._cb_currentIndexChanged)
        self.combo.editTextChanged.connect(self._cb_editTextChanged)

        self.items = (
            '',
            ('Lisp', 'lisp.png', 'llll'),
            ('C', 'c.png', 'cccc'),
            ('Objective-C', 'objc.png', 'oooo'),
            ('Python', 'python.png', 'pppp'),
            ('Java', 'java.png', 'jjjj'),
            )
        for i in self.items:
            if isinstance(i, tuple):
                text, icon_path, user_data = i[0], i[1], i[2]
                self.combo.addItem(QtGui.QIcon(icon_path), text, user_data)
            else:
                self.combo.addItem(i)

    def _cb_onActivated(self, idx):
        print 'selected2:', idx

        item = self.items[idx]
        text, icon_path, user_data = item[0], item[1], item[2]

        print "matched idx:", self.combo.findData(user_data)

    def _cb_currentIndexChanged(self, a):
        print 'index2:', a

    def _cb_editTextChanged(self, text):
        print "text:", text

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())



