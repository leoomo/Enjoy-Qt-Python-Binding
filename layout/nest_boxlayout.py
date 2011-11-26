#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
nest box layout

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

class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        tool_hbox = QtGui.QHBoxLayout(self)
        tool_hbox.setContentsMargins(0, 0, 0, 0)
        tool_hbox.setSpacing(0)
#        vbox.addLayout(tool_hbox)


        send_files_btn = QtGui.QToolButton(self)
#        send_files_btn = QtGui.QPushButton(self)
        send_files_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        tool_hbox.addWidget(send_files_btn, 0, QtCore.Qt.AlignCenter)

        icon = QtGui.QIcon("send_files.png")
        send_files_a = QtGui.QAction(icon, "Send", self)
        send_files_a.setStatusTip("Send files")
        send_files_a.triggered.connect(self._send_files_cb)
        send_files_a.setShortcut('Ctrl+Shift+C')
        send_files_btn.setDefaultAction(send_files_a)


        voice_chat_btn = QtGui.QToolButton(self)
#        voice_chat_btn = QtGui.QPushButton(self)
        voice_chat_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        tool_hbox.addWidget(voice_chat_btn, 0, QtCore.Qt.AlignCenter)

        icon = QtGui.QIcon("mic.png")
        voice_chat_a = QtGui.QAction(icon, "Voice chat", self)
        voice_chat_a.setStatusTip("Voice chat")
        voice_chat_a.triggered.connect(self._voice_chat_cb)
        voice_chat_a.setShortcut('Ctrl+Shift+V')
        voice_chat_btn.setDefaultAction(voice_chat_a)


        video_chat_btn = QtGui.QToolButton(self)
#        video_chat_btn = QtGui.QPushButton(self)
        video_chat_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        tool_hbox.addWidget(video_chat_btn, 0, QtCore.Qt.AlignCenter)

        icon = QtGui.QIcon("camera.png")
        video_chat_a = QtGui.QAction(icon, "Voice chat", self)
        video_chat_a.setStatusTip("Voice chat")
        video_chat_a.triggered.connect(self._video_chat_cb)
        video_chat_a.setShortcut('Ctrl+Shift+B')
        video_chat_btn.setDefaultAction(video_chat_a)


        self.setLayout(tool_hbox)

    def _send_files_cb(self):
        print 'send files cb'

    def _voice_chat_cb(self):
        print 'voice chat cb'

    def _video_chat_cb(self):
        print 'video chat cb'

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())