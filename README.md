# PyBlog:

[![Join the chat at https://gitter.im/darthlukan/pyblog](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/darthlukan/pyblog?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

- Author: anak1n <anak1n@funtoo.org>
- Contributor: Brian Tomlinson <brian.tomlinson@linux.com>

> Pyblog is a simple blogging platform for hosting a blog on your own server without Wordpress or other related tools.
> It attempts to automate the initial setup of your blog by asking a few simple startup questions, such as the name
and basic description of your blog.  A generic first post will be created upon the ```configure``` script's completion.

> There is only one pre-configured theme, but the CSS can be configured to your individual taste.  Additional themes are planned
in future releases.

> The client itself is written in Python, but it requires a webserver be installed that can execute PHP. A way to get this
working is to add```<?php include('/path/to/blog/dir/posts/post.html'); ?>``` in the ```index.php``` file. 


## Why would you want to use this?

> Because WordPress is heavy as are a lot of tools for generating blogs for similar frameworks.  Also, it's fun to write
your own tools and share them.


## TODO:
- Selectable themes at blog generation
- More themes
- Possibly add databases
- Add a comments section
- Add multiple blog support
- Tests


# License

> GPLv3, See license file
