#!/usr/bin/env python2

#    PyBlog: Simple managed self-hosted blog.
#    Copyright (C) 2014 anakin | anak1n@funtoo.org
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import time
import commands
import subprocess

from time import sleep

# TODO: Offload all of this to the pyblog file or other libs as needed.
# color = {
#     'Blue': '\033[94m',
#     'Green': '\033[92m',
#     'Yellow': '\033[93m',
#     'Bold': '\033[1m',
#     'End': '\033[0m'
# }
#
#
# def detect_user():
#     if os.geteuid() == 0:
#         print "%s You are root continuing! %s" % (color['Bold'], color['End'])
#         return True
#     print "%s %s PyBlog configuration needs to be run as root! Sorry! %s" % (color['Bold'], color['Yellow'], color['End'])
#     return False
#
#
# def define_blog():
#     blogdir = raw_input("%s What is the main directory of your blog? ex: [/var/www/myblog] %s" % (color['Bold'], color['End']))
#     blogtitle = raw_input("%s What is the title of your blog? ex: My Cool Blog %s " % (color['Bold'], color['End']))
#     return blogdir, blogtitle
#
#
# def detect_webserver():
#     webserver = None
#     servers = {
#         'apache': commands.getoutput('which apache2'),
#         'nginx': commands.getoutput('which nginx'),
#         'lighthttpd': commands.getoutput('which lighttpd')
#     }
#     print "%sThis program relies on a webserver such as Apache, Nginx, or Lighttpd.%s" % (color['Bold'], color['End'])
#
#     for server, val in servers.items():
#         if "which: no" not in val:
#             print "%s%s found, continuing" % (color['Bold'], server)
#             webserver = server
#             break
#         else:
#             print "No webserver found, please install either Apache2, Nginx, or Lighttpd to continue %s" % color['End']
#             continue
#
#     return webserver


def main():
    print "%s Welcome to the PyBlog configuration!" % color['Bold']
    print "%s Use this to configure your new blog! %s" % (color['Bold'], color['End'])

    run = True
    while run:
        webserver = detect_webserver()
        if not detect_user():
            break
        elif webserver is None:
            break
        else:
            blogdir, blogtitle = define_blog()
            print "User: root, webserver: %s, blogdir: %s, blogtitle: %s" % (webserver, blogdir, blogtitle)
            # Exit the loop, we don't have enough logic to keep going.
            run = False


if __name__ == '__main__':
    main()


