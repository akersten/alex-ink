#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex Kersten'
SITENAME = 'alex ink'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['static']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('cute.works', 'http://cute.works/'),
         ('ece.rocks', 'http://ece.rocks/'),
         ('kersten.email', 'http://kersten.email/'),)
# Social widget
SOCIAL = (
          ('github', 'https://github.com/akersten'),
          ('@amkersten', 'https://twitter.com/amkersten'),
         )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
