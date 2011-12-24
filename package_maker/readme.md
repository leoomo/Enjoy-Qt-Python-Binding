# Package Maker

 - [Aral Balkan · How to make standalone OS X application bundles from PyQt apps using py2app](http://aralbalkan.com/1675)
 - [Building Mac OS X applications with py2app](http://www.rkblog.rk.edu.pl/w/p/building-mac-os-x-applications-py2app/)
 - [Hatchet: hack frozen PySide apps down to size](http://www.rfk.id.au/blog/entry/hatchet-hack-frozen-pyside-apps/), Feb 2011
 - [How do I create a nice-looking DMG for Mac OS X using command-line tools?](http://stackoverflow.com/questions/96882/how-do-i-create-a-nice-looking-dmg-for-mac-os-x-using-command-line-tools/97025#97025)
 - [Problem using py2app with the lxml package](http://stackoverflow.com/questions/868510/problem-using-py2app-with-the-lxml-package)
 
TODO:

 - simple pyside
 - multiple packages/modules (third part/yours)
 - non-script resources, suck as icon, image, xml etc

## py2app bugs

    ./dist/your_app_name.app/Contents/MacOS/your_app_name


crash log

    Qt internal error: qt_menu.nib could not be loaded. The .nib file should be placed in QtGui.framework/Versions/Current/Resources/  or in the resources directory of your application bundle.
Abort trap

solution

    build package with [py2app_setup.py](https://gist.github.com/1378312)



crash log

    On Mac OS X, you might be loading two sets of Qt binaries into the same process. Check that all plugins are compiled against the right Qt binaries. Export DYLD_PRINT_LIBRARIES=1 and check that only one set of binaries are being loaded.
    Segmentation fault

solution

    sudo mv  /opt/local/lib/libQtGui.4.dylib ./



problem:

    loading two sets of Qt binaries

solution:

    create a empty qt.conf file

    http://www.thetoryparty.com/2009/08/27/pyqt-and-py2app-seriously-i-dont-know-what-to-do-with-you-when-youre-like-this/


problem:

    load and render image failed

solution:

    use PIL and convert image into png

    http://www.thetoryparty.com/2009/08/27/pyqt-and-py2app-seriously-i-dont-know-what-to-do-with-you-when-youre-like-this/


## py2exe bugs


### __file__ not defined

    NameError: global name '__file__' is not defined

 - http://www.py2exe.org/index.cgi/WhereAmI
 - http://stackoverflow.com/questions/595305/python-path-of-script
 - http://stackoverflow.com/questions/247770/retrieving-python-module-path

__file__ doesn't works in package build by py2exe.

solution:

    def we_are_frozen():
        """Returns whether we are frozen via py2exe.
        This will affect how we find out where we are located."""

        return hasattr(sys, "frozen")

    def module_path():
        """ This will get us the program's directory,
        even if we are frozen using py2exe"""

        if we_are_frozen():
            return os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))

        return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))

    #PWD = os.path.dirname(os.path.realpath(__file__))
    PWD = module_path()


### ImportError exception

    ImportError: No module named gzip
    ImportError: No module named dom

缺少什么模块，在 options -> py2exe -> includes 里添加什么模块。

    options = {
        "py2exe": {
            "includes": ["PyQt4", "sip", "gzip", "xml.dom.minidom"],


 - http://www.py2exe.org/index.cgi/Py2exeAndPyQt

