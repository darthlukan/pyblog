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

import os, sys, subprocess, time, commands
from time import sleep

class color:
    Blue = '\033[94m'
    Yellow = '\033[93m'
    Bold = '\033[1m'
    End = '\033[0m'

apache = commands.getoutput('which apache2')
nginx = commands.getoutput('which nginx')
lighttpd = commands.getoutput('which lighttpd')
try:
    print(color.Bold + 'Welcome to PyBlog configuration!')
    print('Use this to configure your new blog!')
    sleep(1)
    if os.geteuid() != 0:
        print(color.Bold + 'PyBlog configuration needs to be run as root! Sorry!' + color.End)
        sys.exit()
    else:
        print(color.Bold + 'You are root continuing!' + color.End)
    print(color.Bold + 'This program relies on a webserver such as Apache, Nginx, or Lighttpd.' + color.End)
    print color.Bold + "searching... \\",
    syms = ['\\', '|', '/', '-']
    bs = '\b'
    for _ in range(5):
	for sym in syms:
	    sys.stdout.write("\b%s" % sym)
	    sys.stdout.flush()
	    sleep(.5)
    print(' ')
    if nginx != 'which: no nginx in (/sbin:/bin:/usr/sbin:/usr/bin)':
	print(color.Bold + 'Nginx found, continuing!')
    elif apache != 'which: no apache2 in (/sbin:/bin:/usr/sbin:/usr/bin)':
	print('Apache2 found, continuing!')
    elif lighttpd != 'which: no lighttpd in (/sbin:/bin:/usr/sbin:/usr/bin)':
	print('Lighttpd found, continuing!')
    else:
	print('No webserver found, please install either Apache2, Nginx, or Lighttpd to continue' + color.End)
    sleep(1)
    blogdir = raw_input(color.Bold + 'What directory do you want the blog to be installed into? ' + color.Blue + '[Use absolute path i.e.: /var/wwww/myblog/]: ' + color.End)
    os.system('sed -i "8i blogdir = \'' + blogdir + '\'" pyblog.py')
    print(color.Bold + color.Yellow + 'Installing blog into ' + blogdir + color.End)
    os.system('install -d ' + blogdir + '/html')
    os.system('cp html/* ' + blogdir + '/html/')
    blogtitle = raw_input(color.Bold + 'What would you like your blog to be called? ' + color.End)  
    blogdesc = raw_input(color.Bold + 'Enter a short description of your blog: ' + color.End)
    blogurl = raw_input(color.Bold + 'What is the URL of your blog? ' + color.End)
    os.system('sed -i \'9i blogurl = "%s"\' pyblog.py' % blogurl)
    os.system('touch ' + blogdir + '/index.php')
    os.system('cp -r css/ ' + blogdir)
    os.system('install -d ' + blogdir + '/posts')
    os.system('install -d ' + blogdir + '/imgs')
    os.system('install -d ' + blogdir + '/perm')
    os.system('cp samplepost.html ' + blogdir + '/posts/samplepost.html')
    os.system('cp pyblog.py /usr/bin/pyblog && chmod +x /usr/bin/pyblog')
    os.chdir(blogdir)
    os.system('sed -i \'4i <title>' + blogtitle + '</title>\' html/head.html')
    os.system('sed -i \'4i <a href=\"' + blogurl + '\"><center>' + blogtitle + '</center></a>\' html/body.html')
    os.system('sed -i \'7i ' + blogdesc + '\' html/body.html')
    os.system('echo "<?php include(\'html/head.html\'); include(\'html/body.html\'); ?>" >> ' + blogdir + '/index.php')
    os.system('echo "<?php include(\'posts/samplepost.html\'); ?>" >> ' + blogdir + '/index.php')
    os.system('echo "<?php include(\'' + blogdir + '/html/footer.html\') ?>" >> ' + blogdir + '/index.php')
    print(color.Bold + 'Completed! PyBlog is installed to /usr/bin/pyblog. To add a new post just run ' + color.Blue + 'pyblog ' + color.End + color.Bold + 'from your terminal. During the configure process it will automatically put everything in the directory you specified for your blog. You can run it from anywhere! Enjoy!' + color.End)
except KeyboardInterrupt:
    print(' ')
    sys.exit(0)

