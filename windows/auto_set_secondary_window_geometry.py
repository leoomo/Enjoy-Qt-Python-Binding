#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
auto set the geometry of secondary window base on primary window geometry 

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


_auto_set_geometry_offset_is_zero_if_mare_then = 5
_auto_set_geometry_offset_last_x = 0
_auto_set_geometry_offset_step = 10

def get_offset_for_auto_set_gemetry():
    global _auto_set_geometry_offset_is_zero_if_mare_then
    global _auto_set_geometry_offset_last_x
    global _auto_set_geometry_offset_step

    if _auto_set_geometry_offset_last_x > 0:
        th = _auto_set_geometry_offset_last_x / _auto_set_geometry_offset_step
        if th >= _auto_set_geometry_offset_is_zero_if_mare_then:
            _auto_set_geometry_offset_last_x = 0
        else:
            _auto_set_geometry_offset_last_x += _auto_set_geometry_offset_step
    else:
        _auto_set_geometry_offset_last_x += _auto_set_geometry_offset_step

    offset_x = offset_y = _auto_set_geometry_offset_last_x

    return offset_x, offset_y

def auto_set_geometry(primary, secondary):
    desktop = QtGui.QApplication.desktop()

    px = primary.x()
    primary_in_left_screen = desktop.width() / 2 + primary.width() / 2 >= px

    if primary_in_left_screen:
        secondary_x_start = px + primary.width() + 5
    else:
        secondary_x_start = px - primary.width() - 5
    secondary_y_start = (desktop.height() - secondary.height()) / 2

    offset_x, offset_y = get_offset_for_auto_set_gemetry()

    secondary.move(secondary_x_start + offset_x, secondary_y_start + offset_y)


class SecondaryWindow(QtGui.QWidget):
    def __init__(self, name = ""):
        super(SecondaryWindow, self).__init__()
        self.setWindowTitle('Window #%s' % name)

        self.resize(200, 200)

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()

            
class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        btn = QtGui.QPushButton("create", self)
        btn.clicked.connect(self._btn_cb)
        btn.move(20, 20)

        # following is optional
        self.win_list = []

    def _btn_cb(self):
        # following is optional
        win_name = str(len(self.win_list))

        secondary_win_obj = SecondaryWindow(name = win_name)
        auto_set_geometry(primary = self, secondary = secondary_win_obj)
        secondary_win_obj.show()

        # following is optional
        self.win_list.append(secondary_win_obj)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())