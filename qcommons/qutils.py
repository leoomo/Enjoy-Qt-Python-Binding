"""
add custom theme name and search path for fix icon file not found on Mac OS X

Install Oxygen icon on Mac OS X via MacPorts:

    sudo port install oxygen-icons

"""
import sys

try:
    from PySide import QtGui
    from PySide import QtCore
except ImportError:
    from PyQt4 import QtGui
    from PyQt4 import QtCore


__all__ = [
    "config_theme_path",
    "icon2pix",
]


def config_theme_path():
    if sys.platform != "darwin":
        return

    theme_name = str(QtGui.QIcon.themeName())

    if theme_name != "Oxygen":
        QtGui.QIcon.setThemeName("Oxygen")


    search_paths = list(QtGui.QIcon.themeSearchPaths())

    custom_path = "/opt/local/share/icons"
    if custom_path not in search_paths:
        search_paths.append(custom_path)

    QtGui.QIcon.setThemeSearchPaths(search_paths)


def icon2pix(icon, size = QtCore.QSize(30, 30), grayscaled = True):
    if grayscaled:
        return icon.pixmap(size, mode = QtGui.QIcon.Disabled)
    else:
        return icon.pixmap(size)
