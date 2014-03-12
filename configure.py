#!/usr/bin/env python

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

import subprocess
import sys
import time
import commands
import os

from time import sleep

class color:
    Blue = '\033[94m'
    Yellow = '\033[93m'
    Bold = '\033[1m'
    End = '\033[0m'

def user():
    if os.geteuid() != 0:
        print(color.Bold + color.Yellow + 'PyBlog configuration needs to be run as root! Sorry!' + color.End)
        sys.exit()
    else:
        print(color.Bold + 'You are root continuing!' + color.End)

def blog():
    blogdir = raw_input(color.Bold + 'What is the main directory of your blog? ex: [/var/www/myblog] ' + color.End)
    blogtitle = raw_input(color.Bold + 'What is the title of your blog? ex: My Cool Blog' + color.End)

def webserver():
    apache = commands.getoutput('which apache2')
    nginx = commands.getoutput('which nginx')
    lighttpd = commands.getoutput('which lighttpd')
    print(color.Bold + 'This program relies on a webserver such as Apache, Nginx, or Lighttpd.' + color.End)
    if nginx != 'which: no nginx in (/sbin:/bin:/usr/sbin:/usr/bin)':
        print(color.Bold + 'Nginx found, continuing!')
    elif apache != 'which: no apache2 in (/sbin:/bin:/usr/sbin:/usr/bin)':
        print('Apache2 found, continuing!')
    elif lighttpd != 'which: no lighttpd in (/sbin:/bin:/usr/sbin:/usr/bin)':
        print('Lighttpd found, continuing!')
    else:
        print('No webserver found, please install either Apache2, Nginx, or Lighttpd to continue' + color.End)

print(color.Bold + 'Welcome to the PyBlog configuration!')
print(color.Bold + 'Use this to configure your new blog!' + color.End)


