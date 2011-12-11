#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QToolButton demo

NOTE: you should set a icon for QToolButton

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qtoolbutton.html
"""
import sys
import qcommons

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

        qcommons.config_theme_path()

        tool_btn = QtGui.QToolButton(self)
        icon = QtGui.QIcon.fromTheme("edit-find")
        tool_btn.setIcon(icon)
        # the right size for tool button
        # "Choosing the Right Size and Format for Icons: Standard icon sizes for Windows Vista, Windows 7, Mac OS X, Linux GNOME and iPhone"
        # http://www.visualpharm.com/articles/icon_sizes.html
        tool_btn.setIconSize(32, 32)
        tool_btn.move(100, 100)
        tool_btn.clicked.connect(self._tool_btn_cb)

    def _tool_btn_cb(self):
        print 'clicked'

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())