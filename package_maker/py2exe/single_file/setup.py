#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import glob
##
from distutils.core import setup
import py2exe
assert py2exe != None
##
osp=os.path

windows = [
    {
        "script": "btn.py",
        "icon_resources": [(1, "gui.ico")],
    }
]
options = {
    "py2exe": {
        "includes": ["PyQt4", "sip"],
        "dll_excludes": ["MSVCP90.dll"],
        "bundle_files" : 1,
        }
    }

setup(
    name = "foo",
    windows = windows,
    options = options,
    zipfile = None,
)