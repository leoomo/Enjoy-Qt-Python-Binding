#!/usr/bin/env python
"""
enhance and wrap window for using convenience

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qdesktopwidget.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html
"""
import json
import os

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui

__all__ = [
    "auto_set_geometry",
    "AutoSaveGeo",
    "CustomDlg",
    "CustomWin",
    "CustomSheetWin",
    ]


class AutoSaveGeo(QtGui.QMainWindow):
    """ auto save (window) widget geometry before it destroy, and restore its geometry at next time. """
    def __init__(self, user_data_path, w = 300, h = 500, parent = None):
        super(AutoSaveGeo, self).__init__(parent)

        self.resize(w, h)

        self.user_data_path = user_data_path
        if self.user_data_path:
            self._load_win_geo()
    
    def closeEvent(self, evt):
        if hasattr(self, "user_data_path") and self.user_data_path:
            self._save_win_geo()

        return super(AutoSaveGeo, self).closeEvent(evt)

    def _save_win_geo(self):
        config_path = os.path.join(self.user_data_path, "win_geometry.json")

        if not os.path.exists(self.user_data_path):
            os.makedirs(self.user_data_path)

        if os.path.exists(config_path):
            f = file(config_path)
            buf = f.read()
            f.close()
        else:
            buf = None

        datas = None
        if buf:
            datas = json.loads(buf)

        if not datas:
            datas = {}

        win_geo_data = dict(
             x = self.x(),
             y = self.y(),
             w = self.width(),
             h = self.height())

        datas[self.__class__.__name__] = win_geo_data

        path = config_path
        content = json.dumps(datas)

        f = file(path, "w")
        f.write(content)
        f.close()
    
    def _load_win_geo(self):
        config_path = os.path.join(self.user_data_path, "win_geometry.json")

        if not os.path.exists(self.user_data_path):
            os.makedirs(self.user_data_path)

        desktop = QtGui.QApplication.desktop()
        x = desktop.width() / 2
        y = (desktop.height() - self.height()) / 2
        w = self.width()
        h = self.height()

        if os.path.exists(config_path):
            f = file(config_path)
            buf = f.read()
            f.close()
        else:
            buf = None

        datas = None
        if buf:
            datas = json.loads(buf)

        if datas:
            cls_name = self.__class__.__name__
            geo = datas.get(cls_name)

            if geo:
                x, y, w, h = geo['x'], geo['y'], geo['w'], geo['h']

        self.setGeometry(x, y, w, h)


class CustomDlg(QtGui.QDialog):
    """
    Custom dialog template.

    You should override there method:
     - __init__
     - get_inputs
     - popup_and_get_inputs
    """
    def __init__(self, parent, settings):
        """ You should override this method """
        super(CustomDlg, self).__init__(parent)

        self.resize(400, 250)

        self._settings = settings

        # add custom sub-widgets here ...

    def show_and_raise(self):
        self.show()
        self.raise_()

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()
            return self._settings

    def get_inputs(self):
        """ You should override this method
        update self._settings from custom sub-widgets ...
        """
        return self._settings

    @staticmethod
    def popup_and_get_inputs(parent, settings):
        """ You should override this method """
        dlg = CustomDlg(parent, settings)
        dlg.show()
        dlg.exec_()

        return dlg.get_inputs()


class CustomWin(QtGui.QWidget):
    """
    Custom window template.

    You should override there method:
     - __init__
     - get_inputs
     - popup_and_get_inputs
    """
    def __init__(self, parent, settings):
        """ You should override this method """
        super(CustomWin, self).__init__(parent)

        self.resize(400, 250)

        self._settings = settings

        # add custom sub-widgets here ...

    def show_and_raise(self):
        self.show()
        self.raise_()

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()
            return self._settings

    def get_inputs(self):
        """ You should override this method
        update self._settings from custom sub-widgets ...
        """
        return self._settings

    @staticmethod
    def popup_and_get_inputs(parent, settings):
        """ You should override this method """
        dlg = CustomWin(parent, settings)
        dlg.show()

        return dlg.get_inputs()


class CustomSheetWin(QtGui.QWidget):
    def __init__(self, parent = None):
        super(CustomSheetWin, self).__init__(parent)
        self.resize(400, 300)
        self.setWindowFlags(QtCore.Qt.Sheet)

    def closeEvent(self, evt):
        self.emit(QtCore.SIGNAL("sheet_window_close( QWidget * )"), self)
        return QtGui.QWidget.closeEvent(self, evt)

    def close_and_emit(self):
        self.emit(QtCore.SIGNAL("sheet_window_close_with_accept( QWidget * )"), self)
        self.close()

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()

        return super(CustomSheetWin, self).keyPressEvent(evt)


_auto_set_geometry_offset_is_zero_if_mare_then = 5
_auto_set_geometry_offset_last_x = 0
_auto_set_geometry_offset_step = 20

def _get_offset_for_auto_set_geometry():
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
    """ auto set the geometry of secondary window base on primary window geometry """
    desktop = QtGui.QApplication.desktop()

    px = primary.x()
    primary_in_left_screen = (desktop.width() / 2 - primary.width() / 2) >= px

    if primary_in_left_screen:
        secondary_x_start = px + primary.width() + (_auto_set_geometry_offset_step / 4)
    else:
        secondary_x_start = px - primary.width() - (_auto_set_geometry_offset_step / 4)

    secondary_y_start = (desktop.height() / 2) - (secondary.height() / 2) - _auto_set_geometry_offset_step

    offset_x, offset_y = _get_offset_for_auto_set_geometry()

    secondary.move(secondary_x_start + offset_x, secondary_y_start + offset_y)



def test_use_custom_dlg():
    class CustomDlgDemo(AutoSaveGeo):
        def __init__(self, parent = None, user_data_path = None):
            super(CustomDlgDemo, self).__init__(parent = parent, user_data_path = user_data_path)

            settings = {}
            new_settings = CustomDlg.popup_and_get_inputs(parent = self, settings = settings)
            print "new_settings:", new_settings

        def show_and_raise(self):
            self.show()
            self.raise_()

    app_name = "foo"
    #tmp_path = os.getenv("TMP") or "/tmp"
    PWD = os.path.dirname(os.path.realpath(__file__))
    tmp_path = PWD
    app_data_path = os.path.join(tmp_path, app_name)

    app = QtGui.QApplication(sys.argv)
    demo = CustomDlgDemo(user_data_path = app_data_path)
    demo.show_and_raise()
    sys.exit(app.exec_())


def test_use_auto_set_secondary_win_geometry():
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

    class AutoSetGeoDemo(QtGui.QWidget):
        def __init__(self):
            super(AutoSetGeoDemo, self).__init__()

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

    app = QtGui.QApplication(sys.argv)
    demo = AutoSetGeoDemo()
    demo.show_and_raise()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

#    test_use_custom_dlg()
    test_use_auto_set_secondary_win_geometry()