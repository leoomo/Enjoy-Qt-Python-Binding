#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
QTextEdit demo

 - change text in MVC mode
 - custom CSS

Test environment:
    Mac OS X 10.6.8

http://doc.qt.nokia.com/latest/qtextedit.html
http://www.pyside.org/docs/pyside/PySide/QtGui/QTextEdit.html
"""
import os
import sys

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui



css = '''
div {
    line-height: 27px;
}
.nickname {
    color: #A52A2A;
    font-weight: bolder;
}
.ts {
    color: #7F7F7F;
}
'''

class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.qd = QtGui.QTextDocument()
        self.qd.setDefaultStyleSheet(css)

        self.qt = QtGui.QTextEdit(self)
        self.setCentralWidget(self.qt)
        self.qt.setDocument(self.qd)
        self.qt.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
#        self.qt.setReadOnly(True)
        self.log(msg = ' ')
        self.log(msg = 'hello\nworld')
        self.log(msg = 'hello\nworld')
        self.log(msg = u'中文输入\n法 KDE 桌面环境')
        self.log(msg = 'hello\nworld')
        self.log(msg = 'hello\nworld')
        self.log(msg = 'hello\nworld')
        self.log(msg = 'hello\nworld')

        self.top_btn = QtGui.QPushButton("top", self)
        self.top_btn.move(150, 280)
        self.top_btn.clicked.connect(self.goto_top_btn_clicked)

        self.buttom_btn = QtGui.QPushButton("bottom", self)
        self.buttom_btn.move(150, 300)
        self.buttom_btn.clicked.connect(self.goto_buttom_btn_clicked)
        
        #t = self.qt.toHtml()
        
        self.show()

    def goto_top_btn_clicked(self):
        scroll_bar = self.qt.verticalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.minimum())

    def goto_buttom_btn_clicked(self):
        scroll_bar = self.qt.verticalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.maximum())

    def log(self, nickname = 'foo', msg = None):
        t = QtCore.QTime()
        now_time = t.currentTime().toString()

        msg = msg.replace(os.linesep, '<br />')
        log = '''<div><span class="nickname">%s</span>&nbsp;&nbsp;<span class="ts">%s</span><p class="msg">%s</p></div>''' % \
            (nickname, now_time, msg)
        self.qt.append(log)

#        t = self.qd.toHtml()
#        with open('log.txt', 'w') as f:
#            f.write(t.toUtf8())

#        # buf = t
#        buf = QtCore.QString('<html><body>你好</body></html>'.decode('utf-8'))
#        self.qd.setHtml(buf)

#        t = self.qd.toHtml()
#        with open('log2.txt', 'w') as f:
#            f.write(t.toUtf8())

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())