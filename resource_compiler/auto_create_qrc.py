#!/usr/bin/env python
"""
auto scan resources file and create Qt resource(qrc) file for PySide/PyQt project

Usage:
    python auto_create_qrc.py your_pictures_path > bar.qrc
    pyrcc4-2.7 -no-compress bar.qrc -o bar.py

Author: Shuge Lee <shuge.lee@gmail.com>
License: MIT License
"""
import os
import re
import sys
import web

PWD = os.path.dirname(os.path.realpath(__file__))


def tree(top = '.',
         filters = None,
         output_prefix = None,
         max_level = 4,
         followlinks = False,
         top_info = False,
         report = True):
    # The Element of filters should be a callable object or
    # is a byte array object of regular expression pattern.
    topdown = True
    total_directories = 0
    total_files = 0

    top_fullpath = os.path.realpath(top)
    top_par_fullpath_prefix = os.path.dirname(top_fullpath)

    if top_info:
        lines = top_fullpath
    else:
        lines = ""

    if filters is None:
        _default_filter = lambda x : not x.startswith(".")
        filters = [_default_filter]

    for root, dirs, files in os.walk(top = top_fullpath, topdown = topdown, followlinks = followlinks):
        assert root != dirs

        if max_level is not None:
            cur_dir = web.utils.strips(root, top_fullpath)
            path_levels = web.utils.strips(cur_dir, "/").count("/")
            if path_levels > max_level:
                continue

        total_directories += len(dirs)
        total_files += len(files)

        for filename in files:
            for _filter in filters:
                if callable(_filter):
                    if not _filter(filename):
                        total_files -= 1
                        continue
                elif not re.search(_filter, filename, re.UNICODE):
                    total_files -= 1
                    continue

                if output_prefix is None:
                    cur_file_fullpath = os.path.join(top_par_fullpath_prefix, root, filename)
                else:
                    buf = web.utils.strips(os.path.join(root, filename), top_fullpath)
                    if output_prefix != "''":
                        cur_file_fullpath = os.path.join(output_prefix, buf.strip('/'))
                    else:
                        cur_file_fullpath = buf

                lines = "%s%s%s" % (lines, os.linesep, cur_file_fullpath)

    lines = lines.lstrip(os.linesep)

    if report:
        report = "%d directories, %d files" % (total_directories, total_files)
        lines = "%s%s%s" % (lines, os.linesep * 2, report)

    return lines


QRC_TPL = """<!DOCTYPE RCC><RCC version="1.0">
<qresource>
%s
</qresource>
</RCC>"""


def scan_files(src_path = "."):
    filters = ['.(png|jpg|gif)$']
    output_prefix = './'
    report = False
    lines = tree(src_path, filters = filters, output_prefix = output_prefix, report = report)

    lines = lines.split('\n')
    if "" in lines:
        lines.remove("")

    return lines

def create_qrc_body(src_path):
    lines = scan_files(src_path)

    buf = ["<file>%s</file>" % i for i in lines]
    buf = "\n".join(buf)
    buf = QRC_TPL % buf

    return buf

def create_qrc(src_path, dst_file):
    buf = create_qrc_body(src_path)

    if dst_file:
        parent = os.path.dirname(dst_file)
        if not os.path.exists(parent):
            os.makedirs(parent)

        f = file(dst_file, "w")
        f.write(buf)
        f.close()
    else:
        sys.stdout.write(buf)

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        msg = "python auto_create_qrc.py <src_path> [dst_qrc_file]"
        sys.stdout.write('\n' + msg + '\n')
        sys.exit(-1)

    src_path = args[0]

    if len(args) > 1:
        dst_file = args[1]
    else:
        dst_file = None

    create_qrc(src_path, dst_file)
