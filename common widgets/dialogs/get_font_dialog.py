#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Provides a dialog widget for selecting a font

Test environment:
    Mac OS X 10.6.8

http://www.pyside.org/docs/pyside/PySide/QtGui/QFont.html
"""
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


text = '''ABCDEFGHIJKLM
NOPQRSTUVWXYZ
abcdefghijklm
nopqrstuvwxyz
1234567890
'''

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        self.get_font_btn = QtGui.QPushButton('Specifying colors', self)
        x, y = 10, 10
        self.get_font_btn.move(x, y)
        self.get_font_btn.adjustSize()
        self.get_font_btn.clicked.connect(self._get_font_btn_cb)
        qsize = self.get_font_btn.frameSize()

        self.preview_text = QtGui.QLabel(text, self)
        x, y, w, h = 10, 10 + qsize.height() + 10, 280, 200
        self.preview_text.setGeometry(x, y, w, h)
        self.preview_text.setAlignment(QtCore.Qt.AlignHCenter)


        style = "QLabel { font-size: 28px }"
        self.preview_text.setStyleSheet(style)


        self.font_info_label = QtGui.QLabel(self)
        self.font_info_label.setGeometry(10, 350, 200, 20)

    def _get_font_btn_cb(self):
        qfont, ok = QtGui.QFontDialog.getFont()

        print qfont
        print qfont.family()
        print qfont.style()

        if ok:
            self.preview_text.setFont(qfont)
            
            self.font_info_label.setText(qfont.family())

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())