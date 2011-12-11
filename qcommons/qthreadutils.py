import time

try:
    from PySide import QtCore
except ImportError:
    from PyQt4 import QtCore

__all__ = ['kill_qthread', 'QT', 'QTKiller']


def kill_qthread(t):
    if not t:
        return

    t.terminate()
#    t.wait()


class QT(QtCore.QThread):
    def __init__(self, func, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._return = None

    def run(self):
        self._return = self._func(*self._args, **self._kwargs)
        self.emit(QtCore.SIGNAL('thread_finished()'))

    def get_return(self):
        return self._return


class QTKiller(QtCore.QThread):
    def __init__(self, target_t, timeout = 10):
        QtCore.QThread.__init__(self)
        self._target_t = target_t
        self._timeout = timeout

    def run(self):
        i = 0
        while i < self._timeout:
            time.sleep(1)
            self.emit(QtCore.SIGNAL('thread_running()'))
            i += 1
        self.emit(QtCore.SIGNAL('kill_qthread()'))
        while not self._target_t.isFinished():
            time.sleep(0.1)