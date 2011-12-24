"""
Mac OS X app package maker script

FIRST OF ALL, READ THERE:

 * http://stackoverflow.com/questions/885906/enabling-jpeg-support-for-qimage-in-py2exe-compiled-python-scripts
 * http://www.thetoryparty.com/2009/08/27/pyqt-and-py2app-seriously-i-dont-know-what-to-do-with-you-when-youre-like-this/

Requirements:

    [altgraph](https://bitbucket.org/ronaldoussoren/altgraph/) is a fork of graphlib:
     a graph (network) package for constructing graphs, BFS and DFS traversals,
     topological sort, shortest paths, etc. with graphviz output.

    [macholib](https://bitbucket.org/ronaldoussoren/macholib/)
    is typically used as a dependency analysis tool,
    and also to rewrite dylib references in Mach-O headers to be @executable_path relative.

    [modulegraph](http://bitbucket.org/ronaldoussoren/modulegraph/)
    determines a dependency graph between Python modules primarily by bytecode analysis for import statements.

    [py2app](https://bitbucket.org/ronaldoussoren/py2app/) is a Python setuptools command which
    will allow you to make standalone Mac OS X application bundles and plugins from Python scripts.

NOTE: you **have to** install Python 2.7, PySide and qt4-mac by MacPorts,
		install py2app and its requirements by **manual**

Test environment:
    Mac OS X 10.6.8


TODO: strip dist/$APP_NAME.app/Contents/Frameworks

"""
import compileall
import os
from setuptools import setup
from setuptools import find_packages
import shutil
import sys


PWD = os.path.dirname(os.path.realpath(__file__))

APP_NAME = "foo"
APP_VERSION = "1.0"
APP_SCRIPT_NAME = '%s.py' % APP_NAME.lower()


def get_py2app_options():
    try:
        import PySide
        PyQt4 = None
    except ImportError:
        PySide = None
        try:
            import PyQt4
        except ImportError:
            exit(-1)

    python_qt = PySide or PyQt4

    #    import PyQt4
    #    python_qt = PyQt4


    qt_gui = "%s.QtGui" % python_qt.__name__
    qt_core = "%s.QtCore" % python_qt.__name__

    # specify third part python packages
    packages = ["lxml", "PIL"] + find_packages(exclude = ("demos", ))

    includes = ["sip", qt_gui, qt_core, "web", "BeautifulSoup"]
    excludes = ["bz2", "psycopg2", "xml", "Tkinter", "Tix", "turtle", "pydoc",
                "decimal", "pickletools", "mailbox", "optparse", "idlelib",
                "distutils", "Carbon", "unittest"]

    if PyQt4:
        pyqt_excludes = ["PyQt4.QtCLucene", "PyQt4.QtDeclarative", 'PyQt4.QtDesigner', "PyQt4.QtHelp",
                         "PyQt4.QtMultimedia", 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 'PyQt4.QtScript',
                         'PyQt4.QtSql', "PyQt4.QtSvg", 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.QtXmlPatterns',
                         "PyQt4.QtScriptTools"]
        excludes.extend(pyqt_excludes)
    else:
        pyside_excludes = ["PyQt4"]
        excludes.extend(pyside_excludes)

    frameworks = [
        "/opt/local/lib/libxml2.2.dylib",
    ]


    py2app_options = {
        "packages" : packages,
        "includes" : includes,
        "excludes" : excludes,
        "frameworks" : frameworks,
        }

    return py2app_options


plist = dict(
    CFBundleName = APP_NAME,
    CFBundleShortVersionString = APP_VERSION,
    CFBundleGetInfoString = ' '.join([APP_NAME, APP_VERSION]),
    CFBundleExecutable = APP_NAME,
    CFBundleIdentifier = 'org.shuge-lab.%s' % APP_NAME,
    )


data_files = [
    ("", ["/opt/local/lib/Resources/qt_menu.nib"]),
]

def _create_app():
    app_option = [
            {
            "script" : APP_SCRIPT_NAME,
            "plist" : plist,
            }
    ]

    setup(
        name = APP_NAME,
        version = APP_VERSION,
        description = "The Missing SMS client for Mac OS X",
        author = "Shuge Lee",
        author_email = "shuge.lee@gmail.com",
        platforms = ["Mac OS X"],
        license = "MIT License",
        url = "http://iblah.shuge-lab.org",

        scripts = [APP_SCRIPT_NAME],
        packages = find_packages(exclude = ("demos", )),

        app = app_option,
        options = {'py2app': get_py2app_options()},
        data_files = data_files,
        )


APP_RESOURCES_PATH = os.path.join(PWD, 'dist', '%s.app' % APP_NAME.lower(), 'Contents', 'Resources')


def delete_old_app():
    BUILD_PATH = os.path.join(PWD, "build")
    DIST_PATH = os.path.join(PWD, "dist")
    if os.path.exists(BUILD_PATH):
        shutil.rmtree(BUILD_PATH)
    if os.path.exists(DIST_PATH):
        shutil.rmtree(DIST_PATH)

def compile_py():
    compileall.compile_dir(PWD)

_QT_CONF_TPL = """
"""

def patch_qt_conf():
    dst = os.path.join(APP_RESOURCES_PATH, 'qt.conf')

    f = file(dst, "w")
    f.write(_QT_CONF_TPL)
    f.close()

def patch_qt_plugins():
    src = "/opt/local/share/qt4/plugins"

    contents_path = os.path.dirname(APP_RESOURCES_PATH)
    dst = os.path.join(contents_path, "PlugIns")

    shutil.copytree(src, dst)
    
def package_app_for_mac():
    delete_old_app()
    compile_py()
    _create_app()
    patch_qt_conf()
#    patch_qt_plugins()


def print_help():
    msg = "Usage: " + "\n"
    msg += "\t" + "python setup.py py2app build" + "\n"
    print msg

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print_help()

    elif args[0] == "py2app" and args[1] == "build":
        package_app_for_mac()

    else:
        print_help()