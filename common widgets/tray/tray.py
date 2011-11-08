"""
System tray icon and Prompt on PyQt/PySide application exit

NOTE: We don't catch closeEvent cause by command-q on Mac.

Test environment:
    Mac OS X 10.6.8
"""
import json
import os
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


default_settings = {
    "confirm" : True,
    "x_action_is_quit" : False,
}

default_settings_path = 'settings.json'
logo_path = "qt-logo.png"


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


class CustomDlg(QtGui.QDialog):
    """
    Custom dialog template.

    You should override there method:
     - __init__
     - get_inputs
     - popup_and_get_inputs
    """
    def __init__(self, parent, settings):
        super(CustomDlg, self).__init__(parent)

        self.resize(400, 250)

        self._settings = settings
        self.setModal(True)

        # add custom sub-widgets here ...

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()
            return self._settings

    def get_inputs(self):
        # update self._settings from custom sub-widgets ...
        return self._settings

    @staticmethod
    def popup_and_get_inputs(parent, settings):
        dlg = CustomDlg(parent, settings)
        dlg.show()
        dlg.exec_()


class QuitConfirmDlg(CustomDlg):
    def __init__(self, parent, settings):
        super(QuitConfirmDlg, self).__init__(parent, settings)

        self.resize(400, 250)

        self.tips_label = QtGui.QLabel("When you click the close button should me:", self)
        self.tips_label.setGeometry(40, 40, 280, 15)

        self.minimize_rbtn = QtGui.QRadioButton("&Minimize to system tray", self)
        self.minimize_rbtn.setGeometry(70, 90, 180, 20)

        self.exit_rbtn = QtGui.QRadioButton("&Exit program", self)
        self.exit_rbtn.setGeometry(70, 120, 110, 20)

        self.no_confirm_cbox = QtGui.QCheckBox("&Don't ask me again", self)
        self.no_confirm_cbox.setGeometry(40, 180, 150, 20)

        self.minimize_rbtn.setChecked(not self._settings['x_action_is_quit'])
        self.exit_rbtn.setChecked(self._settings['x_action_is_quit'])
        self.no_confirm_cbox.setChecked(not self._settings['confirm'])

    def get_inputs(self):
        self._settings["x_action_is_quit"] = self.exit_rbtn.isChecked()
        self._settings["confirm"] = not self.no_confirm_cbox.isChecked()

        return self._settings

    @staticmethod
    def popup_and_get_inputs(parent, settings):
        dlg = QuitConfirmDlg(parent, settings)
        dlg.show()
        dlg.exec_()

        return dlg.get_inputs()


class Demo(QtGui.QMainWindow):
    def __init__(self, logo_icon):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.settings = load_settings(default_settings_path)

        self.sys_tray_icon = QtGui.QSystemTrayIcon(parent=self)
        self.sys_tray_icon.setIcon(logo_icon)
        self.sys_tray_icon.activated.connect(self.on_sys_tray_icon_clicked)
        self.sys_tray_icon.messageClicked.connect(self.on_sys_tray_icon_msg_clicked)
        self.sys_tray_icon.show()
        
#        self.sys_tray_icon_show_msg('title', 'msg')

    def show_and_raise(self):
        self.show()
        self.raise_()

    @staticmethod
    def confirm_quit(main_win, close_evt=None):
        if main_win.settings["confirm"]:
            QuitConfirmDlg.popup_and_get_inputs(main_win, main_win.settings)
            save_settings(main_win.settings)

        if main_win.settings['x_action_is_quit']:
            if close_evt:
                close_evt.accept()

            return True
        else:
            if close_evt:
                close_evt.ignore()

            main_win.hide()

            return False

    def closeEvent(self, evt):
        self.confirm_quit(self, evt)

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)
 
        if close_win_cmd_w or close_win_esc:
            self.close()

    def on_sys_tray_icon_clicked(self, activation_reason):
        assert activation_reason in (
            QtGui.QSystemTrayIcon.Trigger,
            QtGui.QSystemTrayIcon.DoubleClick,
            QtGui.QSystemTrayIcon.MiddleClick)

        self.show_and_raise()

    def on_sys_tray_icon_msg_clicked(self, *args, **kwargs):
        print 'msg clicked'

    def sys_tray_icon_show_msg(self, title, msg,
                               icon = QtGui.QSystemTrayIcon.MessageIcon(),
                               msecs = 10000):
        if self.sys_tray_icon.supportsMessages():
            self.sys_tray_icon.showMessage(title, msg, icon, msecs)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    logo_icon = QtGui.QIcon(logo_path)
    app.setWindowIcon(logo_icon)

    main = Demo(logo_icon=logo_icon)
    main.show_and_raise()
    
    sys.exit(app.exec_())