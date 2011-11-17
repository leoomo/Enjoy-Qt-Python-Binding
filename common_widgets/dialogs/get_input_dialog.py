#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
get input dialog demo

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QInputDialog.html
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
        self.setGeometry(300, 300, 350, 80)

        self.button = QtGui.QPushButton('Popup', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button.move(20, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), 
            self._get_input)
        self.setFocus()
        
        self.label = QtGui.QLineEdit(self)
        self.label.move(130, 22)
            
    
    def _get_input(self):
        title, msg = 'Get Input Dialog', 'Enter your name:'
        text, resp = QtGui.QInputDialog.getText(self, title, msg)
        
        if resp:
            self.label.setText(web.utils.safeunicode(text))

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())