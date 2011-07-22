#!/usr/bin/env python

from distutils.code import setup

setup(name = "PyQtMud",
    version = "0.1",
    description = "A MUD client written for PyQt",
    author = "Jonathan Gardner",
    author_email = "jgardner@jonathangardner.net",
    url = "http://pyqtmud.jonathangardner.net/",
    packages = ["pyqtmud"],
    data_files = ['ui'],
    scripts = ['scripts/pyqtmud'],
)
