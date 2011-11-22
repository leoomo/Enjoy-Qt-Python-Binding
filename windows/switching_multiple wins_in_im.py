#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
switching multiple windows in instant message application
"""
import sys

#from PySide import QtCore
from PySide import QtGui


class ContactListWidow(QtGui.QWidget):
    def __init__(self, sign_in_win):
        super(ContactListWidow, self).__init__()
        self.setWindowTitle('ContactListWidow')

        x, y, w, h = 200, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.sign_in_win = sign_in_win

        self.switch_btn = QtGui.QPushButton('switch', self)
        self.switch_btn.clicked.connect(self._switch_btn_cb)
        self.switch_btn.move(10, 10)

    def _switch_btn_cb(self):
        self.close()
        self.sign_in_win.show()

    def show_and_raise(self):
        self.show()
        self.raise_()


class SignInWin(QtGui.QMainWindow):
    def __init__(self):
        super(SignInWin, self).__init__()
        self.setWindowTitle('SignInWin')

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.switch_btn = QtGui.QPushButton('switch', self)
        self.switch_btn.clicked.connect(self._switch_btn_cb)
        self.switch_btn.move(10, 10)

        self.cat_list_win = None

    def _switch_btn_cb(self):
        self.close()

        if not self.cat_list_win:
            self.cat_list_win = ContactListWidow(self)

        self.cat_list_win.show_and_raise()

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = SignInWin()
    demo.show_and_raise()

    sys.exit(app.exec_())

