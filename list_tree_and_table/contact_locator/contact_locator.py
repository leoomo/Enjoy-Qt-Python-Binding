#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
contact list locator

Test environment:
    Mac OS X 10.6.8

"""
import re
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


datas_ = (
    ('C', 'c.png', 'c'),
    ('C#', 'csharp.png', 'csharp'),
    ('Lisp', 'lisp.png', 'lisp'),
    ('Objective-C', 'objc.png', 'objc'),
    ('Perl', 'perl.png', 'perl'),
    ('Ruby', 'ruby.png', 'ruby'),
    ('Python', 'python.png', 'py'),
    ('Java', 'java.png', 'java'),
    ('JavaScript', 'javascript.png', 'js')
)


class Magic:
    def __init__(self, fullname, icon_path, pid):
        self.fullname = fullname
        self.icon_path = icon_path
        self.pid = pid
    
    def __repr__(self):
        return "<Magic %s>" % self.fullname

    
class MagicBox(object):
    def __init__(self):
        self._magics = set()

        for i in datas_:
            fullname, logo_path, pid = i[0], i[1], i[2]
            magic = Magic(fullname, logo_path, pid)
            self._magics.add(magic)
            
        self._cache = list(self._magics)

    @property
    def magics_count(self):
        return len(self._magics)

    @property
    def all_magics(self):
        return self._magics
    
    @property
    def magics(self):
        return self._cache

    def filter_list_by_keyword(self, keyword):
        self._cache = [i
                      for i in self._magics
                          if i.fullname.find(keyword) != -1 or \
                             re.match(keyword, i.fullname, re.I)]


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, magic_box):
        super(ListModel, self).__init__()
        self.magic_box = magic_box

    def rowCount(self, parent):
        return len(self.magic_box.magics)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        magic = self.magic_box.magics[index.row()]
        fullname, icon_path, user_data = magic.fullname, magic.icon_path, magic.pid

        if role == QtCore.Qt.DisplayRole:
            return fullname

        elif role == QtCore.Qt.DecorationRole:
            return QtGui.QIcon(icon_path)

#        elif role == QtCore.Qt.BackgroundColorRole:
#            return QtGui.QBrush(QtGui.QColor("#d4d4d4"))

        return None


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.magic_box = MagicBox()

        
        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.resize(200, 30)
        self.lineedit.move(10, 10)

        self.lineedit.returnPressed.connect(self._lineedit_returnPressed)
        self.lineedit.textChanged.connect(self._lineedit_textChanged)

            
        self.list_view = QtGui.QListView(self)
        self.list_view.setGeometry(10, 50, 280, 300)
        
        self.list_model = ListModel(self.magic_box)
        self.list_view.setModel(self.list_model)

    def _lineedit_textChanged(self, text):
        print "text changed:", text

        self.magic_box.filter_list_by_keyword(text)
        self.list_view.update()

    def _lineedit_returnPressed(self):
        text = self.lineedit.text()

        print "return press:", text
        print "magics:", self.magic_box.magics


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())


