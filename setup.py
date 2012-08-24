#!/usr/bin/env python

from lintian import __appname__, __version__
from setuptools import setup

long_description = open('README.md').read()

setup(
    name=__appname__,
    version=__version__,
    packages=['lintian'],
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description='Do things with Lintian',
    license="GPL-2+",
    url="",
    platforms=['any']
)
