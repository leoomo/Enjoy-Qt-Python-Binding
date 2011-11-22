#!/usr/bin/env python
"""
auto save window geometry

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qdesktopwidget.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html
"""
import json
import os
import sys
import web


try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


app_name = "foo"
#tmp_path = os.getenv("TMP") or "/tmp"
PWD = os.path.dirname(os.path.realpath(__file__))
tmp_path = PWD
app_data_path = os.path.join(tmp_path, app_name)


class AutoSaveGeo(QtGui.QWidget):
    def __init__(self, w = 300, h = 500, parent = None, user_data_path = None):
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

        buf = json.dumps(datas)
        web.utils.safewrite(config_path, buf)

    
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


class Demo(AutoSaveGeo):
    def __init__(self, parent = None, user_data_path = None):
        super(Demo, self).__init__(parent = parent, user_data_path = user_data_path)

    def show_and_raise(self):
        self.show()
        self.raise_()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo(user_data_path = app_data_path)
    demo.show_and_raise()

    sys.exit(app.exec_())

