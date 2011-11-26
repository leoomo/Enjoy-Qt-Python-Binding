#coding:utf-8
import sys
from PyQt4 import QtCore

SHUGE_DEFAULT_ENCODING = 'utf-8'

def to_unicode_obj(obj, is_filename = False):
    """ Convert string to unicode object.

    Arguments:
    - `is_filename`: set this True if `obj` is get from Microsoft Windows file
                  system, such as os.listdir. """

    if is_filename and sys.platform == "win32":
        file_sys_encoding = sys.getfilesystemencoding()
        return obj.decode(file_sys_encoding)

    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding = SHUGE_DEFAULT_ENCODING)
    return obj

txt = 'hello world'
print QtCore.QString(txt) == txt
print QtCore.QString(txt) == QtCore.QVariant(txt)
print QtCore.QVariant(txt) == txt
print QtCore.QVariant(txt).toString() == txt

txt = to_unicode_obj('hello world')
print QtCore.QString(txt) == txt
print QtCore.QString(txt) == QtCore.QVariant(txt)
print QtCore.QVariant(txt) == txt
print QtCore.QVariant(txt).toString() == txt

txt = '中文'
print QtCore.QString(txt) == txt
print QtCore.QString(txt) == QtCore.QVariant(txt)
print QtCore.QVariant(txt) == txt
print QtCore.QVariant(txt).toString() == txt

txt = to_unicode_obj('中文')
print QtCore.QString(txt) == txt
print QtCore.QString(txt) == QtCore.QVariant(txt)
print QtCore.QVariant(txt) == txt
print QtCore.QVariant(txt).toString() == txt

