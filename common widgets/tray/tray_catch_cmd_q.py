"""
System tray icon and Prompt on PyQt/PySide application exit

NOTE: We do catch closeEvent cause by command-q on Mac,
    this feature bring a bug here, it could listen user clicks application icon/dock icon.

Test environment:
    Mac OS X 10.6.8

See also:
 - http://lists.trolltech.com/qt-interest/2007-06/msg00820.html
"""
import json
import os
import sys
import threading

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class PeriodicExecutorOnce(threading.Thread):
    def __init__(self, interval, func, *args, **kwargs):
        threading.Thread.__init__(self, name = "PeriodicExecutor")
        self._interval = interval
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._finished = threading.Event()

    def cancel(self):
        self._finished.set()

    def run(self):
        self._finished.wait(self._interval)
        self._func(*self._args, **self._kwargs)
        self._finished.set()


default_settings = {
    "confirm" : True,
    "x_action_is_quit" : 0,
}

default_settings_path = 'settings.json'


def save_settings(settings, path=default_settings_path):
    with open(path, 'w') as f:
        buf = json.dumps(settings)
        f.write(buf)

def load_settings(path=default_settings_path):
    if os.path.exists(path):
        with open(path) as f:
            c = f.read()
            settings = json.loads(c)
    else:
        global default_settings
        settings = default_settings

    return settings


def confirm_quit(main_win, close_evt=None):
    if main_win.settings["confirm"]:
        if main_win.settings['x_action_is_quit']:
            save_settings(main_win.settings)

            if close_evt:
                close_evt.accept()

            return True
        else:
            if close_evt:
                close_evt.ignore()

            main_win.hide()

            return False


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.settings = load_settings(default_settings_path)

        self._press_cmd_q = None
        self._last_key = None
        self._last_modifiers = None

        self._confirm_quit_t = None


    def _confirm_quit(self):
        if confirm_quit(self):
            save_settings(self.settings)

            QtCore.QCoreApplication.instance().quit()

    def keyReleaseEvent(self, evt):
        key = evt.key()

        if hasattr(QtCore.Qt.Key_Control, 'real'):
            # compitable with PyQt
            if key == QtCore.Qt.Key_Control.real:
                self._last_modifiers = QtCore.Qt.ControlModifier

            if key == QtCore.Qt.Key_Q.real:
                self._last_key = QtCore.Qt.Key_Q
        else:
            # compitable with PySide
            if key == QtCore.Qt.Key_Control:
                self._last_modifiers = QtCore.Qt.ControlModifier

            if key == QtCore.Qt.Key_Q:
                self._last_key = QtCore.Qt.Key_Q

        press_cmd_q = (self._last_modifiers == QtCore.Qt.ControlModifier) and (self._last_key == QtCore.Qt.Key_Q)

        if press_cmd_q:
            if confirm_quit(self, evt):
                QtCore.QCoreApplication.instance().quit()
                
            self._press_cmd_q = True
            self._last_key = None
            self._last_modifiers = None

            self._confirm_quit_t.cancel()

        super(Demo, self).keyReleaseEvent(evt)

    def event(self, evt):
        e_type = evt.type()

        if e_type == QtCore.QEvent.Close:
            self._confirm_quit_t = PeriodicExecutorOnce(0.1, self._confirm_quit)
            self._confirm_quit_t.start()

            evt.ignore()
            return False
        else:
            return super(Demo, self).event(evt)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    main = Demo()

    main.show()
    main.raise_()

    sys.exit(app.exec_())