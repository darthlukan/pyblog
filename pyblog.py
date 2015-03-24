#!/usr/bin/env python
# PyBlog: Simple managed self-hosted blog.
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
import platform


# Perform the following via functions
# 1. Title of post
# 2. directory structure
# 3. populate name.html and name.php with dir and title (name)
# 4. Write files to dir

# Dir structure == /var/www/myblog (myblog == title)/posts/name.html || name.php
# Dir structure Windows == C:\Users\<user>\Public\myblog\posts\name.html || name.php

sysvars = {
    'linux': {
        'home': os.getenv('HOME'),
        'tmp': "{0}/tmp".format(os.getenv('HOME')),
        'user': os.getlogin()
    },
    'windows': {
        'home': os.getenv('HOME'),
        'tmp': "{0}{1}{2}{1}".format(os.getenv('HOME'), os.pathsep, 'tmp'),
        'user': os.getlogin()
    }
}


def detect_platform():
    system = platform.system().lower()
    base_config = None

    try:
        base_config = sysvars[system]
        base_config['system'] = system
    except KeyError, e:
        print "detect_platform caught: {0}".format(e.message)
    return base_config


def get_post_title():
    pass


def set_dir_structure():
    pass


def populate_html():
    pass


def populate_php():
    pass


def save_files(htmlFile, phpFile):
    pass
