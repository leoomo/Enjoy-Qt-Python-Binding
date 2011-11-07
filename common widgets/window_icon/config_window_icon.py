#!/usr/bin/env python
"""
Config application window icon

Test environment:
    Mac OS X 10.6.8
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class Foo(QtGui.QWidget):
    def __init__(self):
        super(Foo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        # NOTE: don't use following, it doesn't show icon in dock bar on Mac
#        icon = QtGui.QIcon("iphone-sms.png")
#        self.setWindowIcon(icon)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    icon = QtGui.QIcon("qt-logo.png")
    app.setWindowIcon(icon)

    foo = Foo()
    foo.show()

    sys.exit(app.exec_())
