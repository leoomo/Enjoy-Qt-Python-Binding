#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Custom QListView


This script demonstrates

 - DND item
 - sort item

Test environment:
    Mac OS X 10.6.8

Docs

 - http://doc.qt.nokia.com/latest/model-view-programming.html#using-drag-and-drop-with-item-views

 - Qt - QAbstractItemView, PySide - QListView
 - Qt - QAbstractItemModel, PySide - QAbstractItemModel


"""
import glob
import os
import sys

#try:
#    from PySide import QtCore
#    from PySide import QtGui
#except ImportError:
#    from PyQt4 import QtCore
#    from PyQt4 import QtGui

from PyQt4 import QtCore
from PyQt4 import QtGui


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, os_list):
        super(ListModel, self).__init__()
        self.os_list = os_list

    def rowCount(self, parent):
        return len(self.os_list)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        os_name, os_logo_path = self.os_list[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return os_name
        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(os_logo_path)

        return None

    def flags(self, idx):
        if idx.isValid():
            return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsDropEnabled |\
                   QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    # DND
    def supportedDropActions(self):
        return QtCore.Qt.MoveAction

    def mimeData(self, idxes):
        super(ListModel, self).mimeData(idxes)

        mime_data = QtCore.QMimeData()

        encoded_data = ""

        for idx in idxes:
            if idx.isValid():
                encoded_data += '\r\n' + self.data(idx, role = QtCore.Qt.DisplayRole)

        mime_data.setData('text/plain', encoded_data)

        return mime_data


class ListView(QtGui.QListView):
    def __init__(self, parent=None):
        super(ListView, self).__init__(parent)

        self.data_sources = create_data_source()
        list_model = ListModel(self.data_sources)
        self.setModel(list_model)

        # size
        self.setIconSize(QtCore.QSize(50, 50))
        self.setSpacing(5)
        self.setUniformItemSizes(True)

        # view
        self.setDropIndicatorShown(True)

        # interactive in DND mode
        self.setMovement(QtGui.QListView.Free)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, evt):
        if evt.mimeData().hasFormat('text/plain'):
            print self.childAt(evt.pos())
            
            if evt.source() == self:
                evt.setDropAction(QtCore.Qt.MoveAction)
                evt.accept()
            else:
                evt.acceptProposedAction()
        else:
            evt.ignore()

    dragMoveEvent = dragEnterEvent

    def dropEvent(self, evt):
        evt.accept()
        mime_data = evt.mimeData()

        print mime_data.data('text/plain')


def create_data_source():
    logos = glob.glob('*.png')
    return [(os.path.splitext(i)[0], i) for i in logos]


class ChatWin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ChatWin, self).__init__()
        self.demo = parent

        x, y, w, h = 200, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.setAcceptDrops(True)

    def show_and_raise(self):
        self.show()
        self.raise_()

    def dragEnterEvent(self, evt):
        evt.accept()
        if evt.mimeData().hasFormat('text/plain'):
            evt.accept()
        else:
            evt.ignore()

    def dropEvent(self, evt):
        evt.accept()
        mime_data = evt.mimeData()
        
        print mime_data.data('text/plain')

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.list_view = ListView(self)
        x, y, w, h = 5, 5, 290, 250
        self.list_view.setGeometry(x, y, w, h)

        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.move(5, 260)
        self.lineedit.textEdited.connect(self._lineedit_textEdited)


        self.chat_win = ChatWin(self)
        self.chat_win.show_and_raise()


    def _lineedit_textEdited(self, text):
        if not text:
            self.list_view.clearSelection()
        else:
            self.list_view.keyboardSearch(text)
            idx = self.list_view.currentIndex()

            if idx.isValid():
                if len(self.list_view.data_sources) - 1 >= idx.row():
                    self.list_view.data_sources.pop(idx.row())
                    self.list_view.update()

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())