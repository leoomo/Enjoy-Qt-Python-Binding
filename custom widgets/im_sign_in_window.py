#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
IM sign in window

Test environment:
    Mac OS X 10.6.8

https://bitbucket.org/shugelee/iblah/
"""
import sys
import webbrowser

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 600, 300
        self.setGeometry(x, y, w, h)


        account_label = QtGui.QLabel("Cellphone No./Fetion No./E-Mail:", self)
        x, y, w, h = 40, 40, 221, 30
        account_label.setGeometry(x, y, w, h)

        self.account_combox = QtGui.QComboBox(self)
        self.account_combox.setEditable(True)
        self.account_combox.setGeometry(70, 70, 200, 26)
        self.connect(self.account_combox, QtCore.SIGNAL('currentIndexChanged(QString)'),
                     self._account_combox_currentIndexChanged)


        sign_up_link = 'https://feixin.10086.cn/account/register'
        text = '<a href="%s">Sign Up</a>' % sign_up_link
        sign_up_label = QtGui.QLabel(text, self)
        sign_up_label.setGeometry(300, 70, 130, 30)
        sign_up_label.linkActivated.connect(self._show_sign_up_dlg)


        passwd_label = QtGui.QLabel("Password:", self)
        passwd_label.setGeometry(40, 110, 62, 30)

        self.passwd_lineedit = QtGui.QLineEdit(self)
        self.passwd_lineedit.setGeometry(70, 140, 200, 22)


        reset_passwd_link = 'http://my.feixin.10086.cn/password/find/'
        text = "<a href='%s'>Reset Password</a>" % reset_passwd_link
        reset_passwd_label = QtGui.QLabel(text, self)
        reset_passwd_label.setGeometry(300, 140, 130, 30)
        reset_passwd_label.linkActivated.connect(self._on_reset_passwd_label_clicked)
        reset_passwd_tips = 'CMCC user could send "p" to 12520 to reset password'
        reset_passwd_label.setToolTip(reset_passwd_tips)


        self.remember_me_checkbox = QtGui.QCheckBox("Remember me", self)
        self.remember_me_checkbox.setGeometry(40, 180, 140, 20)


        self.sign_in_btn = QtGui.QPushButton("Sign In", self)
        self.sign_in_btn.setGeometry(170, 210, 114, 32)


        report_bugs_link = '#'
        text = '<a href="%s">Report Bugs</a>' % report_bugs_link
        self.report_bugs_label = QtGui.QLabel(text, self)
        self.report_bugs_label.setGeometry(490, 210, 100, 30)
        self.report_bugs_label.linkActivated.connect(self.report_bugs_cb)

    def show_and_raise(self):
        self.show()
        self.raise_()

    def report_bugs_cb(self, link):
        webbrowser.open_new_tab(link)

    def _show_sign_up_dlg(self, link):
        webbrowser.open_new_tab(link)
    
    def _on_reset_passwd_label_clicked(self, link):
        webbrowser.open_new_tab(link)

    def _account_combox_currentIndexChanged(self, text):
        if not text:
            self.passwd_lineedit.setText("")
        else:
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()


    sys.exit(app.exec_())
