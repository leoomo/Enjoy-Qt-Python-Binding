#!/usr/bin/env python
import sys
#try:
#    from PySide import QtGui, QtCore
#except ImportError:
#    from PyQt4 import QtGui, QtCore

from PyQt4 import QtGui, QtCore

FIRST_COLUMN = 0

class UserPresence:
    OFFLINE = 0
    ONLINE = 400

class Object:
    GROUP = 1
    USER = 2

class User():
    def __init__(self, uri, nickname, group = None):
        self._type = Object.USER
        self.uri = uri
        self.nickname = nickname
        self.group = group

    def get_type(self):
        return self._type

    def get_display_name(self):
        return self.nickname


class Group():
    def __init__(self, gid, gname, users = None):
        self._type = Object.GROUP
        self.gid = gid
        self.gname = gname
        self.user_list = []

        if users:
            for user in users:
                self.add_user(user)

    def add_user(self, user):
        if user not in self.user_list:
            self.user_list.append(user)

    def count(self):
        return len(self.user_list)

    def get_user_by_row(self, row):
        return self.user_list[row]

    def get_user_by_uri(self, uri):
        for user in self.user_list:
            if user.uri == uri:
                return user

    def get_display_name(self):
        return self.gname

    def get_type(self):
        return self._type


class GroupAgent:
    def __init__(self, groups = None):
        self.group_list = []

        if groups:
            for group in groups:
                self.add_group(group)

    def add_group(self, group):
        self.group_list.append(group)

    def count(self):
        return len(self.group_list)

    def get_group_by_row(self, row):
        return self.group_list[row]

    def index(self, group):
        return self.group_list.index(group)

    def get_user_by_uri(self, uri):
        for group in self.group_list:
            user = group.get_user_by_uri(uri)
            if user:
                return user


class Model(QtCore.QAbstractItemModel):
    COLUMN_COUNT = 1
    def __init__(self, group_agent):
        QtCore.QAbstractItemModel.__init__(self)
        self.group_agent = group_agent

    def columnCount(self, parent_idx):
        if not parent_idx.isValid():
            return self.COLUMN_COUNT

        parent_obj = parent_idx.internalPointer()
        return parent_obj.count()

    def rowCount(self, parent_idx):
        if not parent_idx.isValid():
            return self.group_agent.count()

        parent_obj = parent_idx.internalPointer()
        if parent_obj.get_type() == Object.GROUP:
            return parent_obj.count()

        return 0

    def index(self, row, column, parent_idx):
        assert column != None
        if not parent_idx.isValid():
            group = self.group_agent.get_group_by_row(row)
            return self.createIndex(row, column, group)

        parent_obj = parent_idx.internalPointer()
        if parent_obj.get_type() == Object.GROUP:
            item = parent_obj.get_user_by_row(row)
            return self.createIndex(row, column, item)

        return QtCore.QModelIndex()

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return QtCore.QVariant()

        obj = index.internalPointer()
        if role == QtCore.Qt.DisplayRole:
            if obj.get_type() in (Object.GROUP, Object.USER):
                return QtCore.QVariant(obj.get_display_name())

        elif role == QtCore.Qt.UserRole:
            obj_type = obj.get_type()
            if obj_type == Object.GROUP:
                return QtCore.QVariant(obj.gid)
            elif obj_type == Object.USER:
                return QtCore.QVariant(obj.uri)

        return QtCore.QVariant()

    def parent(self, child_index):
        if not child_index.isValid():
            return QtCore.QModelIndex()

        obj = child_index.internalPointer()
        if obj.get_type() == Object.USER:
            parent_obj = obj.group
            row = self.group_agent.index(parent_obj)
            return self.createIndex(row, FIRST_COLUMN, parent_obj)

        return QtCore.QModelIndex()

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

def create_group_agent():
    group_a = Group('10', 'Group A')
    for i in [('123', 'Mery'),
            ('132', 'Lily'),
            ('321', 'May')]:
        group_a.add_user(User(i[0], i[1], group_a))

    group_b = Group('20', 'Group B')
    user = User('213', 'Joe', group_b)
    group_b.add_user(user)

    ga = GroupAgent()
    ga.add_group(group_a)
    ga.add_group(group_b)
    return ga

class Demo(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        x, y, w, h = 300, 300, 300, 200
        self.setGeometry(x, y, w, h)

        self.tv = QtGui.QTreeView(self)

        self.ga = create_group_agent()
        model = Model(self.ga)

        self.tv.setHeaderHidden(True)
        self.tv.setModel(model)

        self.selection_model = self.tv.selectionModel()
        self.selection_model.currentRowChanged.connect(self.current_row_changed)

        user = self.ga.get_user_by_uri("123")
#        print user.__dict__
        user.nickname = "foo"

    def current_row_changed(self, current_idx, prev_idx):
        assert prev_idx != None
        item = current_idx.internalPointer()

        if item.get_type() != Object.USER:
            return

        print item.get_display_name()


if __name__ == "__main__":
    qa = QtGui.QApplication(sys.argv)

    app = Demo()
    app.show()
    qa.exec_()
