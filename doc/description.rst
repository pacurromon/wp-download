
wp-download
===========

It is a cumbersome task to administer local Wikipedia databases,
especially if you need access to multiple language versions of
Wikipedia.

With ``wp-download`` you can automatically download the newest
database dumps for all language edition you want::

    $ wp-download --resume -v /path/to/wikipedia/dumps
    Read configuration from: '/home/foobar/.wpdownloadrc'
    Set timeout to 30s
    Processing language: sw
    Creating directory: /path/to/wikipedia/dumps/sw/20090821
    Latest dump for (sw) is from Friday 21 August 2009
    Skip: swwiki-20090821-redirect.sql.gz
    Skip: swwiki-20090821-category.sql.gz
    Resume: swwiki-20090821-pages-articles.xml.bz2
    swwiki-20090821-pages-articles.xml.bz2 [****] 100% Time: 00:00:00   3.19 M/s
    ...
    ...

Installation
------------

This distribution does *not* use setuptools but plain distutils, so you will
have to install requirements by yourself or by using the pip requirements file
from the `homepage <http://github.com/babilen/wp-download>`_.

Requirements:

    * `progressbar <http://pypi.python.org/pypi/progressbar/2.2>`_

Documentation
-------------

Documentation can be found `here <http://packages.python.org/wp-download/>`_
