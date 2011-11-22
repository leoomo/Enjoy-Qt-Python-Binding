"""
Mac OS X app package maker script

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
"""
import os
from setuptools import setup, find_packages
import shutil
import sys
import glob


PWD = os.path.dirname(os.path.realpath(__file__))

APP_NAME = 'foo'
MAIN_APP_NAME = '%s.py' % APP_NAME
RES_PATH = os.path.join(PWD, 'dist', '%s.app' % APP_NAME, 'Contents', 'Resources')


data_files = [
        ("resources", glob.glob(os.path.join(PWD, "resources", "*.nib"))),
        #('/usr/share/applications',['foo.desktop']),
    ]

packages = find_packages()

plist = dict(
    CFBundleName = APP_NAME,
    CFBundleShortVersionString = '0.1',
    CFBundleGetInfoString = ' '.join([APP_NAME, '0.1']),
    CFBundleExecutable = APP_NAME,
    CFBundleIdentifier = 'org.shuge.fetion',
    # hide dock icon
#    LSUIElement = True,
)


def delete_old():
    BUILD_PATH = os.path.join(PWD, "build")
    DIST_PATH = os.path.join(PWD, "dist")
    if os.path.exists(BUILD_PATH):
         shutil.rmtree(BUILD_PATH)
    if os.path.exists(DIST_PATH):
        shutil.rmtree(DIST_PATH)

def create_app():
    apps = [
        {
            "script" : MAIN_APP_NAME,
            "plist" : plist,
        }
    ]

    OPTIONS = {'includes': ['PySide.QtGui']}

    setup(
        name = APP_NAME,
        version = '0.1',
        description = 'do nothing',
        author = 'anonymous',
        author_email = 'foo@example.com',
        platforms = ["Mac OSX"],
        license = "Shuge Property License",
        url = "http://bitbucket.org/shugelee/iblah/",
        scripts = [MAIN_APP_NAME],

        app = apps,
        options = {'py2app': OPTIONS},
        # setup_requires = ['py2app'],
#        data_files = data_files,
#        packages = packages,
    )

def qt_menu_patch():
    src = os.path.join(PWD, 'resources', 'qt_menu.nib')
    dst = os.path.join(RES_PATH, 'qt_menu.nib')
    if not os.path.exists(dst):
        shutil.copytree(src, dst)

_RUN_IN_TERM_PATCH = """import os
import sys

os.environ['RESOURCEPATH'] = os.path.dirname(os.path.realpath(__file__))

"""


def run_in_term_patch():
    BOOT_FILE_PATH = os.path.join(RES_PATH, "__boot__.py")
    with open(BOOT_FILE_PATH) as f:
        old = f.read()

    new = _RUN_IN_TERM_PATCH + old

    with open(BOOT_FILE_PATH, 'w') as f:
        f.write(new)

def data_files_patch():
    for item in data_files:
        if isinstance(item, tuple):
            folder_name = item[0]
        else:
            folder_name = item

        src = os.path.join(PWD, folder_name)
        dst = os.path.join(RES_PATH, folder_name)
        if not os.path.exists(dst):
            shutil.copytree(src, dst)

        
ACTION_CREATE = len(sys.argv) == 3 and sys.argv[-1] == "build"

if ACTION_CREATE:
    delete_old()
    create_app()
    qt_menu_patch()
    run_in_term_patch()
    data_files_patch()
else:
    create_app()
    print "Usage: python setup.py py2app build"