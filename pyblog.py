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
import sys
import time


class color:
    Green = '\033[92m'
    Bold = '\033[1m'
    End = '\033[0m'


time = time.strftime("%d.%m.%Y - %H:%M")

# TODO: This try block is way too big!
try:
    print(color.Bold + 'Welcome!')
    print('Use this to add contents to your blog!' + color.End)
    print('The default editor is ' + color.Green + 'nano')
    title = raw_input(color.Bold + 'What is the title of this post? ' + color.End)
    editor = raw_input(color.Bold + 'What is your main editor? [vi/emacs/nano]: ' + color.End)
    if ' ' in title:
        newtitle = "-".join(title.split())
        os.system(
            'touch ' + blogdir + '/posts/' + newtitle + '.html && touch ' + blogdir + '/perm/' + newtitle + '.php')
        # TODO: Why do we care about editors?
        if editor == 'vi':
            author = raw_input(color.Bold + 'Who is the author of this post? ' + color.End)
            os.system('vi ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Updating index.php')
            htmltitle = newtitle.replace('-', ' ')
            os.system(
                'echo \'<h2 class="title">' + htmltitle + '</h2>\' >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('echo "<h3 class=\'date\'>' + time + '</h3>" >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('cat ' + blogdir + '/posts/tmp.html >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system(
                'echo \'<div id="author">Posted by: ' + author + '</div> | <a href=\"' + blogurl + '/perm/' + newtitle + '.php\" title="Permalink">\' >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system(
                'sed -i "2i <?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" ' + blogdir + '/index.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/head.html\'); include(\'' + blogdir + '/html/body.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system('echo "<title>' + htmltitle + '</title>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo \'<small><center><a href="' + blogurl + '" title="Back to blog">Back to blog</a></center></small>\' >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/footer.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system('rm ' + blogdir + '/posts/tmp.html')
            print(
            color.Bold + 'Complete! You can view your post at ' + blogurl + '/perm/' + newtitle + '.php' + color.End)
        elif editor == 'emacs':
            author = raw_input(color.Bold + 'Who is the author of this post? ' + color.End)
            os.system('emacs ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Updating index.php')
            htmltitle = newtitle.replace('-', ' ')
            os.system('echo \'<h2 class="title">' + newtitle + '</h2>\' >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('echo "<h3 class=\'date\'>' + time + '</h3>" >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('cat ' + blogdir + '/posts/tmp.html >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system(
                'echo \'<div id="author">Posted by: ' + author + '</div> | <a href=\"' + blogurl + '/perm/' + newtitle + '.php\" title="Permalink">Permalink</a></div>\' >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system(
                'sed -i "2i <?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" ' + blogdir + '/index.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/head.html\'); include(\'' + blogdir + '/html/body.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system('echo "<title>' + htmltitle + '</title>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo \'<small><center><a href="' + blogurl + '" title="Back to blog">Back to blog</a></center></small>\' >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/footer.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            print(
            color.Bold + 'Complete! You can view your post at ' + blogurl + '/perm/' + newtitle + '.php' + color.End)
        else:
            author = raw_input(color.Bold + 'Who is the author of this post? ' + color.End)
            os.system('nano ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Updating index.php')
            htmltitle = newtitle.replace('-', ' ')
            os.system(
                'echo \'<h2 class="title">' + htmltitle + '</h2>\' >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('echo "<h3 class=\'date\'>' + time + '</h3>" >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('cat ' + blogdir + '/posts/tmp.html >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system(
                'echo \'<div id="author">Posted by: ' + author + ' | <a href=\"' + blogurl + '/perm/' + newtitle + '.php\" title="Permalink">Permalink</a></div>\' >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system(
                'sed -i "2i <?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" ' + blogdir + '/index.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/head.html\'); include(\'' + blogdir + '/html/body.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system('echo "<title>' + htmltitle + '</title>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo \'<small><center><a href="' + blogurl + '" title="Back to blog">Back to blog</a></center></small>\' >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/footer.html\'); ?>" >> ' + blogdir + '/perm/' + newtitle + '.php')
            os.system('rm ' + blogdir + '/posts/tmp.html')
            print(
            color.Bold + 'Complete! You can view your post at ' + blogurl + '/perm/' + newtitle + '.php' + color.End)
    else:
        os.system('touch ' + blogdir + title + '.html && touch ' + blogdir + '/perm/' + title + '.php')
        if editor == 'vi':
            author = raw_input(color.Bold + 'Who is the author of this post? ' + color.End)
            os.system('vi ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Updating index.php')
            os.system('echo \'<h2 class="title">' + title + '</h2>\' >> ' + blogdir + '/posts/' + title + '.html')
            os.system('echo "<h3 class=\'date\'>' + time + '</h3>" >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('cat ' + blogdir + '/posts/tmp.html >> ' + blogdir + '/posts/' + title + '.html')
            os.system(
                'echo \'<div id="author">Posted by: ' + author + '</div> | <a href=\"' + blogurl + '/perm/' + title + '.php\" title="Permalink">Permalink</a></div>\' >> ' + blogdir + '/posts/' + title + '.html')
            os.system(
                'sed -i "2i <?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" ' + blogdir + '/index.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/head.html\'); include(\'' + blogdir + '/html/body.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system('echo "<title>' + title + '</title>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/posts/' + title + '.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo \'<small><center><a href="' + blogurl + '" title="Back to blog">Back to blog</a></center></small>\' >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/footer.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system('rm ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Complete! You can view your post at ' + blogurl + '/perm/' + title + '.php' + color.End)
        elif editory == 'emacs':
            author = raw_input(color.Bold + 'Who is the author of this post? ' + color.End)
            os.system('emacs ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Updating index.php')
            os.system('echo \'<h2 class="title">' + title + '</h2>\' >> ' + blogdir + '/posts/' + title + '.html')
            os.system('echo "<h3 class=\'date\'>' + time + '</h3>" >> ' + blogdir + '/posts/' + newtitle + '.html')
            os.system('cat ' + blogdir + '/posts/tmp.html >> ' + blogdir + '/posts/' + title + '.html')
            os.system(
                'echo \'<div id="author">Posted by: ' + author + '</div> | <a href=\"' + blogurl + '/perm/' + title + '.php\" title="Permalink">Permalink</a></div>\' >> ' + blogdir + '/posts/' + title + '.html')
            os.system(
                'sed -i "2i <?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" ' + blogdir + '/index.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/head.html\'); include(\'' + blogdir + '/html/body.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system('echo "<title>' + title + '</title>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/posts/' + title + '.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo \'<small><center><a href="' + blogurl + '" title="Back to blog">Back to blog</a></center></small>\' >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/footer.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system('rm ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Complete! You can view your post at ' + blogurl + '/perm/' + title + '.php' + color.End)
        else:
            author = raw_input(color.Bold + 'Who is the author of this post? ' + color.End)
            os.system('nano ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Updating index.php')
            os.system('echo \'<h2 class="title">' + title + '</h2>\' >> ' + blogdir + '/posts/' + title + '.html')
            os.system('echo "<h3 class=\'date\'>' + time + '</h3>" >> ' + blogdir + '/posts/' + newtitle)
            os.system('cat ' + blogdir + '/posts/tmp.html >> ' + blogdir + '/posts/' + title + '.html')
            os.system(
                'echo \'<div id="author">Posted by: ' + author + '</div> | <a href=\"' + blogurl + '/perm/' + title + '.php\" title="Permalink">Permalink</a></div>\' >> ' + blogdir + '/posts/' + title + '.html')
            os.system(
                'sed -i "2i <?php include(\'' + blogdir + '/posts/' + newtitle + '.html\'); ?>" ' + blogdir + '/index.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/head.html\'); include(\'' + blogdir + '/html/body.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system('echo "<title>' + title + '</title>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/posts/' + title + '.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo \'<small><center><a href="' + blogurl + '" title="Back to blog">Back to blog</a></center></small>\' >> ' + blogdir + '/perm/' + title + '.php')
            os.system(
                'echo "<?php include(\'' + blogdir + '/html/footer.html\'); ?>" >> ' + blogdir + '/perm/' + title + '.php')
            os.system('rm ' + blogdir + '/posts/tmp.html')
            print(color.Bold + 'Complete! You can view your post at ' + blogurl + '/perm/' + title + '.php' + color.End)
# TODO: We should catch meaningful exceptions, what about "OSError"?
except KeyboardInterrupt:
    print(' ')
    sys.exit(0)

