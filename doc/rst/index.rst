***********
WP-Download
***********

Wikipedia database dumps are huge and downloading them for a lot of languages
and keeping them up to date is tedious work and I pity every system
administrator who does this on a regular basis. In the spirit of "Shut up! Or I
will replace you with a very small shell script" i have good news for everyone!

Just use wp-download ...

Usage
=====

You might want to figure out how you should use wp-download, which can be
achieved easily by asking it for help::

    $ wp-download --help
    Usage: wp-download [options] DIR

    Options:
      -h, --help            show this help message and exit
      -q, --quiet           do not generate output (only report errors)
      -v, --verbose         generate verbose output
      -c FILE, --config=FILE
                            load configuration from FILE [default:
                            /home/$USER/.wpdownloadrc]

      Logging:
        Specify log file handling.

        --log-file=FILE     write logs to FILE
        --log-file-level=LOG_FILE_LEVEL
                            set log level (DEBUG, INFO, WARNING, ERROR) [default:
                            INFO]

      Download:
        Change download behaviour

        --force             Force download of all files.
        --resume            Resume partial downloads.
        --timeout=TIMEOUT   Set timeout for download in seconds [default 30 s]
        --retries=RETRIES   Set number of download attempts [default 3]

The program is pretty easy to use. You create a directory where you want to
place newly downloaded dump files and configure the files and languages you
want to download within a configuration file. So let's configure wp-download::

    $ cp /usr/local/share/doc/wp-download/examples/wpdownloadrc.sample ~/.wpdownloadrc
    $ $EDITOR ~/.wpdownloadrc

Configuration
=============

You configure wp-download to your wishes by editing/creating a suitable
configuration file which you place at ``~/.wpdownloadrc`` or specify with the
``-c [FILE]`` option.

The configuration file has a couple of sections, but only ``[Files]`` and
``[Languages]`` are relevant. (for you!?) You might have guessed that you
configure files to download within ``[Files]`` and languages within
``[Languages]``.

If, for example, you want to download the ``redirect``, ``category`` and
``pages-article`` files for Swahili edit the sections like this::

    # wpdownloadrc.sample
    ...

    [Files]
    redirect = True
    category = True
    pages-articles = True
    all-other-files = False
    # or-commented = True
    ...
    [Languages]
    ...
    #sv = True
    sw = True
    #szl = True
    ...

Examples
========

To download all files simply call ``wp-download`` with the target directory::

    $ wp-download -v /path/to/wikipedia/dumps
    swwiki-20090821-redirect.sql.gz [***********] 100% Time: 00:00:00   1.42 M/s
    swwiki-20090821-category.sql.gz [***********] 100% Time: 00:00:00   2.23 M/s
    ...
    ...

The downloaded files will be placed in appropriate directories within
``/path/to/wikipedia/dumps``. The created directory structure looks like this::

    ../dumps/
        de/
            20090618/
            20090710/
            20090728/
            20090810/
        en/
            20090728/
            20090810/
        ...
        ...
        zh/
            20090728/
            20090810/

The downloader will download the most recent dumps for each language so that
it easy to always have the most recent dumps around by executing wp-download
multiple times.

Verbose Output
--------------

If you want more information about what is going on add the ``-v`` or
``--verbose`` option::

    $ wp-download -v /path/to/wikipedia/dumps
    Read configuration from: '/home/$USER/.wpdownloadrc'
    Set timeout to 30s
    Processing language: sw
    Creating directory: /path/to/wikipedia/dumps/sw/20090821
    Latest dump for (sw) is from Friday 21 August 2009
    swwiki-20090821-redirect.sql.gz [***********] 100% Time: 00:00:00   1.39 M/s
    swwiki-20090821-category.sql.gz [***********] 100% Time: 00:00:00   2.40 M/s
    ...
    ...

Resume downloads
----------------

As it might happen that an ongoing download is interrupted you can tell
wp-download to resume interrupted downloads by calling it with the
``--resume`` option::

    $ wp-download -v /path/to/wikipedia/dumps
    Read configuration from: '/home/$USER/.wpdownloadrc'
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

Exit Status
===========

To ease scripting and automatic monitoring of wp-download the following exit
status values are used:

=========== =========================================================
Exit status Meaning
=========== =========================================================
2           Wrong or missing argument
3           IO error
4           Error in template definition
5           Error in files definition
6           Language code error
7           Error parsing the configuration file
8           No such file or directory
=========== =========================================================

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

.. _Wikipedia: http://wikipedia.org
