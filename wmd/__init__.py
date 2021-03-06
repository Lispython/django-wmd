#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
wmd
~~~~~~~~~

Collection of utilities and extensions for jinja2.

:copyright: (c) 2013 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/django-wmd
"""

__all__ = 'get_version',
__author__ = "Alexandr Lispython (alex@obout.ru)"
__license__ = "BSD, see LICENSE for more details"
__build__ = 0x000001
__maintainer__ = "Alexandr Lispython"

try:
    __version__ = __import__('pkg_resources') \
        .get_distribution('wmd').version
except Exception, e:
    __version__ = 'unknown'

if __version__ == 'unknown':
    __version_info__ = (0, 0, 0)
else:
    __version_info__ = __version__.split('.')


def get_version():
    return __version__

