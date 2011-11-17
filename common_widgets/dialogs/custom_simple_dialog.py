#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Custom simple dialog

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


default_settings = {
    "confirm" : True,
    "x_action_is_quit" : 0,
}


class QuitConfirmDlg(QtGui.QDialog):
    def __init__(self, parent, settings):
        super(QuitConfirmDlg, self).__init__(parent)

        self.resize(400, 250)

        self._settings = settings
        self.setModal(True)

        self.tips_label = QtGui.QLabel("When you click the close button should me:", self)
        self.tips_label.setGeometry(QtCore.QRect(40, 40, 280, 15))

        self.minimize_rbtn = QtGui.QRadioButton("Minimize to system tray", self)
        self.minimize_rbtn.setGeometry(QtCore.QRect(70, 90, 180, 20))

        self.exit_rbtn = QtGui.QRadioButton("Exit program", self)
        self.exit_rbtn.setGeometry(QtCore.QRect(70, 120, 110, 20))

        self.no_confirm_cbox = QtGui.QCheckBox("Don't ask me again", self)
        self.no_confirm_cbox.setGeometry(QtCore.QRect(40, 180, 150, 20))

        self.minimize_rbtn.setChecked(not self._settings['x_action_is_quit'])
        self.exit_rbtn.setChecked(self._settings['x_action_is_quit'])
        self.no_confirm_cbox.setChecked(not self._settings['confirm'])

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()
            return self._settings

    def get_inputs(self):
        self._settings["x_action_is_quit"] = self.exit_rbtn.isChecked()
        self._settings["confirm"] = not self.no_confirm_cbox.isChecked()

        return self._settings

    @staticmethod
    def popup_and_get_inputs(parent, settings):
        dlg = QuitConfirmDlg(parent, settings)
        dlg.show()

        result = dlg.exec_()
        assert result in (QtGui.QDialog.Accepted, QtGui.QDialog.Rejected)
#        if result == QtGui.QDialog.Accepted:
#            btn_val = True
#        else:
#            btn_val = False

        return dlg.get_inputs()


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.settings_btn = QtGui.QPushButton("Settings", self)
        self.settings_btn.clicked.connect(self._settings_btn_clicked)

    def _settings_btn_clicked(self):
        global default_settings
        settings = default_settings
        default_settings = QuitConfirmDlg.popup_and_get_inputs(self, settings)
        print "default_settings:", default_settings

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())
