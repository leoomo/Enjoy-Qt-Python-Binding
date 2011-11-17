#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
demo template

Test environment:
    Mac OS X 10.6.8
    
"""
import os
import sys

PWD = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(PWD)
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui


class DropArea(QtGui.QLabel):
    def __init__(self, parent):
        super(DropArea, self).__init__(parent)

        self.setMinimumSize(200, 200)
#        self.setFrameStyle(QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
#        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.clear()

    def dragEnterEvent(self, evt):

        self.setText("<drop content>")
        self.setBackgroundRole(QtGui.QPalette.Highlight)

        evt.acceptProposedAction()
#        self.emit changed(evt.mimeData())
        self.emit(QtCore.SIGNAL("changed(mime_data)"), evt.mimeData())

    def dragMoveEvent(self, evt):
        evt.acceptProposedAction()

    def dropEvent(self, evt):
        mime_data = evt.mimeData()

        if mime_data.hasImage():
            self.setPixmap(mime_data.imageData())
        elif mime_data.hasHtml():
            self.setText(mime_data.html())
            self.setTextFormat(QtCore.Qt.RichText)
        elif mime_data.hasText():
            self.setText(mime_data.text())
            self.setTextFormat(QtCore.Qt.PlainText)
        elif mime_data.hasUrls():
            urls = mime_data.urls()

            text = ""

            for url in urls:
                text += url + " "

            self.setText(text)

        else:
            self.setText("Cannot display data")

        self.setBackgroundRole(QtGui.QPalette.Dark)
        evt.acceptProposedAction()

    def dragLeaveEvent(self, evt):
        self.clear()
        evt.accept()

    def clear(self):
        self.setText("<drop content>")
        self.setBackgroundRole(QtGui.QPalette.Dark)
        self.emit(QtCore.SIGNAL("changed()"))


class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        buf = "This example accepts drags from other applications " + \
            "and displays the MIME types provided by the drag object."
        lab = QtGui.QLabel(buf, self)
        lab.setWordWrap(True)
        lab.adjustSize()

        dropArea = DropArea(self)
        self.connect(dropArea, QtCore.SIGNAL('changed(mime_data)'), self.updateFormatsTable)

        self.formatsTable = QtGui.QTableWidget(self)
        self.formatsTable.setColumnCount(2)
        self.formatsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        labels = ('Format', 'Content')
        self.formatsTable.setHorizontalHeaderLabels(labels)
        self.formatsTable.horizontalHeader().setStretchLastSection(True)
        
            
        clearButton = QtGui.QPushButton("Clear")
        quitButton = QtGui.QPushButton("Quit")
    
        buttonBox = QtGui.QDialogButtonBox()
        buttonBox.addButton(clearButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QtGui.QDialogButtonBox.RejectRole)

        quitButton.pressed.connect(self.close)
        self.connect(clearButton, QtCore.SIGNAL('pressed()'), dropArea, QtCore.SLOT('clear()'))

        mainLayout = QtGui.QVBoxLayout(self)
        mainLayout.addWidget(lab)
        mainLayout.addWidget(dropArea)
        mainLayout.addWidget(self.formatsTable)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
    
        self.setWindowTitle("Drop Site")
        self.setMinimumSize(350, 500)

    def updateFormatsTable(self, mime_data):
        self.formatsTable.setRowCount(0)

        if not mime_data:
            return

        for format in mime_data.formats():
            format_item = QtGui.QTableWidgetItem(format)
            format_item.setFlags(QtCore.Qt.ItemIsEnabled)
            format_item.setTextAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

            if format == 'text/plain':
                text = mime_data.text().simplified()
            elif format == 'text/html':
                text = mime_data.html().simplified()
            elif format == 'text/uri-list':
                text = ""
                for i in mime_data.urls():
                    text += ' ' + i
            else:
                text = 'binary data'

            row = self.formatsTable.rowCount()
            self.formatsTable.insertRow(row)
            self.formatsTable.setItem(row, 0, QtGui.QTableWidgetItem(format))
            self.formatsTable.setItem(row, 1, QtGui.QTableWidgetItem(text))

        self.formatsTable.resizeColumnsToContents(0)


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())