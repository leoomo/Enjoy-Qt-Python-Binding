#!/usr/bin/env python
"""
auto place secondary window next to primary window

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html
http://www.pyside.org/docs/pyside/PySide/QtCore/QRect.html
http://doc.qt.nokia.com/latest/qdesktopwidget.html
"""
import sys


try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class AnotherWindow(QtGui.QWidget):
    def __init__(self, primary_win):
        super(AnotherWindow, self).__init__()
        self.setWindowTitle('Another Window')

        w, h = 300, 400
        self.resize(w, h)

        self.primary_win = primary_win

    def smart_place(self):
        screen = QtGui.QApplication.desktop()

        primary_win_pos = 'right'
        if self.primary_win.x() < screen.width():
            left_screen = QtCore.QRect(0, 0, screen.width() / 2, screen.height())
            if left_screen.contains(self.primary_win.pos()) or left_screen.contains(self.primary_win.geometry().topRight()):
                primary_win_pos = 'left'

        y = (screen.height() - self.height() - 100) / 2
        if primary_win_pos == 'left':
            x = self.primary_win.x() + self.primary_win.width()
        else:
            x = self.primary_win.x() - self.width()

        self.move(x, y)

    def show(self):
        self.smart_place()
            
        super(AnotherWindow, self).show()


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.show_another_win_btn = QtGui.QPushButton("show", self)
        self.show_another_win_btn.clicked.connect(self._show_another_win_btn_cb)
        self.show_another_win_btn.move(10, 10)

        self.another_win = None

    def _show_another_win_btn_cb(self):
        if not self.another_win:
            self.another_win = AnotherWindow(primary_win = self)

        self.another_win.show()

    def show_and_raise(self):
        self.show()
        self.raise_()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())

