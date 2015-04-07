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
import logging
import getpass


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
        'user': getpass.getuser()
    },
    'windows': {
        'home': os.getenv('HOME'),
        'tmp': "{0}{1}{2}{1}".format(os.getenv('HOME'), os.pathsep, 'tmp'),
        'user': getpass.getuser()
    }
}

logging.basicConfig(filename="Errors.log", level=logging.ERROR)
logging.basicConfig(filename="Events.log", level=logging.INFO, filemode="w")

# Detect_Platform utilizes OS, Logging, and GetPass Modules to determine compatibility and define system variables

def detect_platform():
    system = platform.system().lower()
    base_config = None

    try:
        base_config = sysvars[system]
        base_config['system'] = system
        logging.info("Pyblog is running on %s" % (system))
    except KeyError, e:
        print "detect_platform caught: {0}".format(e.message)
        logging.error("Pyblog cannot run on %s" % (system))
    return base_config


def get_post_title():
    pass


def set_dir_structure(config):
    default_root = "{0}/public_html".format(config['home'])
    desired_root = raw_input(prompt='Full path where blog should be stored[default: {0}]: '.format(default_root))

    try:
        os.mkdir(desired_root)
        os.mkdir("{0}{1}templates".format(desired_root, os.pathsep))
        os.mkdir("{0}{1}js".format(desired_root, os.pathsep))
        os.mkdir("{0}{1}img".format(desired_root, os.pathsep))
        os.mkdir("{0}{1}styles".format(desired_root, os.pathsep))
        root = desired_root
    except (OSError, IOError, Exception), e:
        print "Caught: '{0}' while trying to set directory structure!".format(e.message)
        root = None

    return root


def populate_html():
    pass


def populate_php():
    pass


def save_files(htmlFile, phpFile):
    pass


def main():
    config = detect_platform()
    blog_dir = set_dir_structure(config)
    if blog_dir is not None:
        config['blogdir'] = blog_dir
    else:
        raise Exception('Unable to set blog directory root. Do you have permission to write to that directory?')
    pass

if __name__ == '__main__':
    main()
