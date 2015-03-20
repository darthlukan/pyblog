# PyBlog:
Simple blogging platform for hosting your own blog on your server, without Wordpress or tools of that sort.
The configure.py will ask you what to call the blog, what the description, and set up and initial sample post.
You're free to edit the code, you can edit the theme, it's just one theme right now until I work on it a bit more.
If you want to edit the themes though, you have to know CSS and HTML, but if you want to add your own css, by my guest.
Just change the <div id=""> pyblog/html/body.html to your new CSS and add it to pyblog/html/head.html.
The client itself is written in Python, but it requires a webserver be installed that can do PHP. The best way I could get it to
do what I wanted was to add <?php include('/path/to/blog/dir/posts/post.html'); ?> in the index.php. So if you find a better way
to do this, then go ahead and change it.

Why I did this:
I did it because I was using a different platform that just, was kind of pissing me off. So I made my own. It was nearly impossible to theme anything, and changing any bit of the CSS kind of threw off anything. And WP is too heavy for me, and I like having my own blog on my own server without relying on other websites. Just have it be my own. So I made this, and I figured why not release it.
It's not done yet, but it will be soon.

TODO:
- Have user be able to change theme during configuration.
- Possibly add databases
- Add a comments
*Finished* Finish writing pyblog.py (not done as of this second 02/10/14 07:42)
*Finished* Test it out
*Finished* Release it
- Add multiple blog support
