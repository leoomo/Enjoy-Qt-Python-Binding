#!/usr/bin/env python
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
    from PySide import QtWebKit
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui
    from PyQt4 import QtWebKit


class Foo(QtGui.QWidget):
    def __init__(self):
        super(Foo, self).__init__()

        x, y, w, h = 100, 100, 900, 600
        self.setGeometry(x, y, w, h)


        self.source = QtGui.QTextEdit(self)
        self.preview = QtWebKit.QWebView(self)

        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.source)
        self.splitter.addWidget(self.preview)

        self.hbox = QtGui.QHBoxLayout(self)
        self.hbox.addWidget(self.splitter)
        self.setLayout(self.hbox)

        
        self.font = QtGui.QFont("Monaco", 13)
        self.setFont(self.font)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    foo = Foo()
    foo.show()
    sys.exit(app.exec_())
