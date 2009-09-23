# wp-download

It is a cumbersome task to administer local Wikipedia databases,
especially if you need access to multiple language versions of
Wikipedia.

With `wp-download` you can automatically download the newest
database dumps for all language edition you want:

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

## Installation

wp-download does *not* use setuptools but plain distutils, which gives you the
following installation options.

### setup.py

Using setup.py means that you will download the source distribution file and
run:

    $ tar xjf wp-download-0.1.tar.bz2
    # python setup.py install --prefix=/usr/local

which will install wp-download within `/usr/local`. You might have to include
`/usr/local/bin` in your `$PATH`.

    $ export PATH=/usr/local/bin:$PATH

To meet wp-downloads requirements you also have to install
[progressbar (=2.2)] [pbar] with an installation tool of your choice.

### pip

[pip] [] is an excellent tool for installing python software in a sane way. If
you already use it, or plan to do so you might be happy to hear that
wp-download provides a pip [requirements file] [pipreq] that can be used to
install wp-download and it's requirements.

You should *never* install software
into /usr which is used by the package management system of your distribution.

But fear not! [virtualenv] [] and [pip] [] make it easy to install software
like this into an completely isolated environment.

    # pip install -E wp-download -r requirements-0.1.1.txt

## Documentation

Documentation for wp-download can be found [here] [documentation]

[pbar]: http://pypi.python.org/pypi/progressbar/
[pip]: http://pip.openplans.org/
[virtualenv]: http://pypi.python.org/pypi/virtualenv
[pipreq]: /babilen/wp-download/tree/master/pip/requirements-0.1.1.txt
[documentation]: http://packages.python.org/wp-download/
