#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Box layout attribute addStretch demo

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


class Demo(QtGui.QDialog):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)
        
        okBtn = QtGui.QPushButton('ok')
        cancelBtn = QtGui.QPushButton('cancel') 

        btnLayout = QtGui.QHBoxLayout()

#        button 使用 QHBoxLayout 布局，默认是水平放置的。
#        设置 Stretch 属性后，两个按钮会靠右放置，而且随着窗口大小的改变，也是靠右边。
#        如果把 btnLayout.addStretch() 去掉，两个按钮的显示就变了，左右平局分布
        btnLayout.addStretch()

        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)
        
        layout = QtGui.QGridLayout()

#        layout.addLayout(btnLayout, int row, int column, int rowSpan, int columnSpan, alignment = 0)
        layout.addLayout(btnLayout, 2, 0, 1, 3)
        
        self.setLayout(layout)
        
    def show_and_raise(self):
        self.show()
        self.raise_()

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show()

    app.exec_()

