#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
find item of QComboBox by typing keyword

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
        self.combo.move(20, 60)

        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.combo.currentIndexChanged.connect(self._combo_currentIndexChanged)

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
                fullname, icon_path, user_data = i[0], i[1], i[2]
                text = fullname
                self.combo.addItem(QtGui.QIcon(icon_path), text, user_data)
            else:
                self.combo.addItem(i)


    def _combo_currentIndexChanged(self, idx):
        activated_idx = idx

        if idx == -1:
            return
        
        item = self.items[idx]
        if not item:
            return
        
        text, icon_path, user_data = item[0], item[1], item[2]

        matched_idx = self.combo.findData(user_data)
        assert activated_idx == matched_idx

        print
        print "text:", text
        print "icon path:", icon_path
        print "user_data:", user_data


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())



