import sys
from PyQt4 import QtCore, QtGui

from ui.ui_chat import Ui_chatWindow


class ChatWindow(QtGui.QWidget, Ui_chatWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.chat_view = self.chatHistoryTextEdit


        self.convTab.clear()
        self.convTab.setDocumentMode(True)

        self.convTab.currentChanged.connect(self.current_tab_changed)
        self.convTab.tabBar().tabCloseRequested.connect(self.tab_close_requested)

    def add_tab(self, contact_uri):
        if self.isHidden():
            self.show()

        if contact_uri == '10000':
            label = "sys info"
        else:
            label = contact_uri

        chat_input = QtGui.QTextEdit()
        new_idx = self.convTab.addTab(chat_input, QtCore.QString(label))
        self.convTab.setCurrentIndex(new_idx)

        tabbar = self.convTab.tabBar()
        tabbar.setTabData(new_idx, contact_uri)
        #self.convTab.tabBar().setTabData(new_idx, contact_uri)
        #self.focus_on_current_chat_tab()
        self.convTab.setTabBar(tabbar)

        self.contactNameLabel.setText(label)

    def current_tab_changed(self, idx):
        print("current_tab_changed")
        print("current idx: %d" % idx)

        NO_TAB = -1
        if idx == NO_TAB:
            return

        tabbar = self.convTab.tabBar()

        display_name = tabbar.tabText(idx)
        self.contactNameLabel.setText(display_name)

        contact_uri = tabbar.tabData(idx)
        print "type:", contact_uri
        print "contact_uri:", contact_uri.toString()

    def tab_close_requested(self, idx):
        no_input = self.convTab.widget(idx).toPlainText()
        if not no_input:
            self.convTab.removeTab(idx)
        else:
            msg = "Pressing the ESC key will close this conversation. <br />" \
                    "Are you sure you want to continue ?"
            if popup_confirm(self, msg):
                self.convTab.removeTab(idx)

        if not self.convTab.count():
            self.hide()

    def _close_current_tab(self):
        self.convTab.removeTab(self.convTab.currentIndex())
        if not self.convTab.count():
            self.hide()

    def go_to_tab_by_uri(self, contact_uri):
        for idx in xrange(self.convTab.count()):
            tab_uri = str(self.convTab.tabBar().tabData(idx).toString())
            if tab_uri == contact_uri:
                print("go to existed chat tab")
                self.convTab.setCurrentIndex(idx)
                self.focus_on_current_chat_tab()
                return True
        return False


    def keyPressEvent(self, event):
        key = event.key()
        is_goto_prev_tab = (event.modifiers() == QtCore.Qt.ControlModifier) and (key == QtCore.Qt.Key_BracketLeft)
        is_goto_next_tab = (event.modifiers() == QtCore.Qt.ControlModifier) and (key == QtCore.Qt.Key_BracketRight)
        is_send_msg = key == QtCore.Qt.Key_Return
        is_close_tab = key == QtCore.Qt.Key_Escape
        is_switch_tab = (event.modifiers() == QtCore.Qt.ControlModifier) and (key >= QtCore.Qt.Key_1 and key <= QtCore.Qt.Key_9)
        CHAR_START_AT = 48

        if is_close_tab:
            if not self.convTab.count():
                self.hide()
                return

            no_input = self.convTab.currentWidget().toPlainText()
            if not no_input:
                self._close_current_tab()
            else:
                msg = "Pressing the ESC key will close this conversation. <br />" \
                        "Are you sure you want to continue ?"
                if popup_confirm(self, msg):
                    self._close_current_tab()

        elif is_send_msg:
            widget = self.convTab.currentWidget()
            if not widget:
                return
            msg = widget.toPlainText()
            if not msg:
                return
            widget.clear()
            print 'send'

        elif is_switch_tab:
            count = self.convTab.count()
            k = key.real - CHAR_START_AT
            if 1 > k and k > 9:
                return
            if k < count + 1:
                self.convTab.setCurrentIndex(k - 1)
        elif is_goto_prev_tab:
            count = self.convTab.count()
            cur_idx = self.convTab.currentIndex()

            if count == 1:
                return
            elif cur_idx == 0:
                self.convTab.setCurrentIndex(count - 1)
            else:
                self.convTab.setCurrentIndex(cur_idx - 1)
        elif is_goto_next_tab:
            count = self.convTab.count()
            cur_idx = self.convTab.currentIndex()

            if count == 1:
                return
            elif (count - 1) == cur_idx:
                self.convTab.setCurrentIndex(0)
            else:
                self.convTab.setCurrentIndex(cur_idx + 1)

class Main(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, parent = None)
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.chat_win = ChatWindow()

        self.chat_win.show()

        self.btn = QtGui.QPushButton(self)
        self.btn.clicked.connect(self.show_tab)

        self.add_btn = QtGui.QPushButton('add', self)
        self.add_btn.clicked.connect(self.add_tab)

        self.del_btn = QtGui.QPushButton('del', self)
        self.del_btn.clicked.connect(self.del_tab)

        qh = QtGui.QHBoxLayout()
        qh.addWidget(self.btn)
        qh.addWidget(self.add_btn)
        qh.addWidget(self.del_btn)

        self.setLayout(qh)

        self.show()

        self.c = 1

    def add_tab(self):

        self.chat_win.add_tab(str(self.c))

        self.c += 1
        
    def del_tab(self):
        pass

    def show_tab(self):
        self.chat_win.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    