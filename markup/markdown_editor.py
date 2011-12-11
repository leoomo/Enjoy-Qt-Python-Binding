#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
import web

try:
    from PySide import QtCore
    from PySide import QtGui
    from PySide import QtWebKit
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui
    from PyQt4 import QtWebKit


buf = '<msg id="2825" type="0" show-once="0"> <validity begin="2010-12-25 16:00:00.000" end="2015-10-26 15:59:59.000"/> <content type="text/plain">尊敬的用户，您的手机已停机，这将影响您使用飞信的部分功能。为了您的正常使用，请尽快充值。</content> <url style="auto:0;">http://space.fetion.com.cn/redirection/count/203</url> </msg>'

DEFAULT_STYLE = """
* {
font-family: Monaco;
font-size: 12px;
}
"""


class Foo(QtGui.QWidget):
    def __init__(self):
        super(Foo, self).__init__()

        x, y, w, h = 100, 100, 900, 600
        self.setGeometry(x, y, w, h)
        

        self.source = QtGui.QTextEdit(self)
#        self.preview = QtWebKit.QWebView(self)
        self.preview = QtGui.QTextEdit(self)
        self.preview.setReadOnly(True)
        self.preview.setFrameShape(QtGui.QFrame.NoFrame)

        qd = QtGui.QTextDocument()
        qd.setDefaultStyleSheet(DEFAULT_STYLE)

        self.preview.setDocument(qd)

        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.source)
        self.splitter.addWidget(self.preview)


#        widget = self.splitter.widget(0)
#        policy = widget.sizePolicy()
#        policy.setHorizontalStretch(1)
#        policy.setVerticalStretch(1)
#        widget.setSizePolicy(policy)

        self.hbox = QtGui.QHBoxLayout(self)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        self.hbox.addWidget(self.splitter)
        self.setLayout(self.hbox)

        
        self.font = QtGui.QFont("Monaco", 12)
        self.setFont(self.font)


        self.source.textChanged.connect(self.source_text_changed)
        
        self.source.setText(web.safeunicode(buf))

    def source_text_changed(self):
        buf = self.source.toPlainText()
#        import markdown
#        buf = markdown.markdown(buf)
        self.preview.setHtml(buf)
        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    foo = Foo()
    foo.show()
    sys.exit(app.exec_())
