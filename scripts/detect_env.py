"""
Detect platform name and SIP/Python/PyQt/PySide version.

Test environment:

    Mac OS X 10.6.8
    Debian Linux Testing

References:
 - http://www.pyside.org/docs/pyside/pysideversion.html
"""
import platform
import sys
import time

try:
    import PySide
    from PySide import QtCore
except ImportError:
    from PyQt4 import QtCore
    PySide = None

try:
    import sip
except ImportError:
    sip = None

def get_platform():
    pl = None
    while not pl:
        try:
            pl = platform.system()
        except:
            # sometime system call failed on MacOS 10.6,
            # fix it in a quick and dirty way
            time.sleep(0.1)
            continue
    return pl

def get_python_version():
    return sys.version[:3]

print 'Platform:', get_platform()

print 'Python:', get_python_version()

if sip:
    print 'SIP:', sip.SIP_VERSION_STR

if not PySide:
    print "Qt:", QtCore.QT_VERSION_STR
    print 'PyQt:', QtCore.PYQT_VERSION_STR
else:
    print 'Qt:', QtCore.__version__
    print "PySide:", PySide.__version__




