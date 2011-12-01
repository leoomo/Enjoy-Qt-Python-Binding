# Layout

http://doc.qt.nokia.com/latest/layout.html
http://doc.qt.nokia.com/latest/widgets-and-layouts.html

four types of layout

 - horizontally
 - vertically
 - in a grid layout
 - in a form layout


## Default layout

上下反转笛卡儿坐标系(Cartesian coordinate system)

使用绝对坐标布局时，c 是 b 的子 widget, b 是 a 的子 widget

    a -> b -> cd

c 在计算坐标时是以父 widget b 为参照。

例子：label, button 构建时候加上 parent 参数，它们会作为 parent 子 widget，呈现于 parent x = 0, y = 0 处。

    import sys, os
    try:
        from PySide import QtCore, QtGui
    except ImportError:
        from PyQt4 import QtCore, QtGui

    class Demo(QtGui.QWidget):
        def __init__(self):
            super(Demo, self).__init__()

            x, y, w, h = 500, 200, 300, 400
            self.setGeometry(x, y, w, h)

            self.label = QtGui.QLabel("foo", self)
            self.show()

    app = QtGui.QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())


## Widget size and position

disable resize

    self.setFixedSize(w, h)

references

 - http://www.velocityreviews.com/forums/t611856-re-pyqt-how-to-prevent-a-dialog-being-resized.html
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html#PySide.QtGui.PySide.QtGui.QWidget.setFixedSize
 - http://www.pyside.org/docs/pyside/PySide/QtGui/QWidget.html#size-hints-and-size-policies


## Qt doesn't supports nest layout

    QLayout: Attempting to add QLayout "" to ChatWin "", which already has a layout