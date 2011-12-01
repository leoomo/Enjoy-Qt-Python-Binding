import os
import sys

try:
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui


def get_best_qfont():
    IS_GNOME = os.getenv("GDMSESSION") and os.getenv("GDMSESSION") == "gnome"

    font = None

    if sys.platform == "linux2" and IS_GNOME:
        font = QtGui.QFont("WenQuanYi Zen Hei", 12) # 'DejaVu Sans'
    return font

def auto_set_qfont(widget, font=None):
    qfont = font or get_best_qfont()
    if qfont:
        widget.setFont(qfont)


class Main(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, parent = None)
        
        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)
        
        self.label = QtGui.QLabel('hello world', self)
        qf = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        self.label.setFont(qf)
        self.label.move(10, 10)
        
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    