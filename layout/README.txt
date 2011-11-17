# Layout

http://doc.qt.nokia.com/latest/layout.html

## Default layout

label, button 构建时候加上 parent 参数，它们会作为 parent 子 widget，呈现于 parent x = 0, y = 0 处。 

    import sys, os
    from PySide import QtCore, QtGui

    class Demo(QtGui.QWidget):
        def __init__(self):
            super(Demo, self).__init__()

            x, y, w, h = 500, 200, 300, 400
            self.setGeometry(x, y, w, h)

            self.label = QtGui.QLabel("fooo", self)
            self.show()

    app = QtGui.QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())


## Coordinate system

上下反转笛卡儿坐标系(Cartesian coordinate system)

使用绝对坐标布局时，c 是 b 的子 widget, b 是 a 的子 widget

 a -> b -> c
 
c 在计算坐标时是以父 widget b 为参照。

## attribute Stretch

    btnLayout.addStretch()

    btnLayout.addWidget(okBtn)
    btnLayout.addWidget(cancelBtn)

button 使用 QHBoxLayout 布局，默认是水平放置的。
设置 Stretch 属性后，两个按钮会靠右放置，而且随着窗口大小的改变，也就是靠右边。
如果把 btnLayout.addStretch() 去掉，两个按钮的显示就变了，左右平局分布。'''


## Widget size and position

disable resize

    self.setFixedSize(w, h)

references

 - http://www.velocityreviews.com/forums/t611856-re-pyqt-how-to-prevent-a-dialog-being-resized.html
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html#PySide.QtGui.PySide.QtGui.QWidget.setFixedSize




auto resize widget by its content
size change notify

references

 - http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html#size-hints-and-size-policies


auto log its position

references
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html#PySide.QtGui.PySide.QtGui.QWidget.moveEvent


position

http://www.pyside.org/docs/pyside/PySide/QtCore/QRect.html#PySide.QtCore.QRect