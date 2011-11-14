#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
move a button in DND II

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/dnd.html
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class DragWidget(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(DragWidget, self).__init__('DND me', parent)

    def mousePressEvent(self, evt):
        if not self.geometry().contains(evt.pos()):
            return

        if evt.button() == QtCore.Qt.MouseButton.LeftButton:
            mime_data = QtCore.QMimeData()
            mime_data.setText(self.text())

            drag = QtGui.QDrag(self)
            drag.setMimeData(mime_data)

#            drag.exec_() # show nothing while drag move
#            drag.exec_(QtCore.Qt.CopyAction) # show a `Plus/Copy icon' while drag move

            # These flags support drag it from PySide application internal to external.
            # for example, drag this into Finder on Mac OS X, it will auto creates a text file,
            # both file name and content are 'DND me'.
            drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction)


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.btn = DragWidget(self)
        self.btn.move(10, 10)

        self.setAcceptDrops(True)

    def show_and_raise(self):
        self.show()
        self.raise_()

    def dragEnterEvent(self, drag_enter_evt):
        mime_data = drag_enter_evt.mimeData()
        if mime_data.hasFormat('text/plain'):
            drag_enter_evt.acceptProposedAction()

    def dragMoveEvent(self, evt):
#        print 'dragMoveEvent', evt.pos()

        if self.btn.geometry().contains(evt.pos()):
            evt.ignore()

    def dropEvent(self, drop_evt):
        mime_data = drop_evt.mimeData()
        if not self.btn.geometry().contains(drop_evt.pos()) and \
            mime_data.hasFormat('text/plain'):

            print 'text:', mime_data.data('text/plain')

            drop_evt.accept()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())