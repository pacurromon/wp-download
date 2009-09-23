# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from distutils.core import setup
import os

setup(name='wp-download',
      version='0.1.1',
      description='Wikipedia database dump downloader',
      author='Wolodja Wentland',
      author_email='wentland@cl.uni-heidelberg.de',
      url='http://github.com/babilen/wp-download',
      license='GPLv3',
      scripts=['scripts/wp-download'],
      long_description = open('doc/description.rst').read(),
      data_files=[
          ('share/doc/wp-download/examples/', ['examples/wpdownloadrc.sample']),
          ('share/doc/wp-download/doc', ['doc/Makefile','doc/README']),
          ('share/doc/wp-download/doc/rst', ['doc/rst/index.rst',
                                             'doc/rst/conf.py']),
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Topic :: Database',
          'Topic :: Scientific/Engineering',
      ]
     )
