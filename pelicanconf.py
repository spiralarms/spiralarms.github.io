#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'voom4000'
SITENAME = u'voom & zoom'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Minsk'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('SICP Solutions', '/pages/sicp-solutions.html'),
)

# Social widget
SOCIAL = (('Weiqun Zhang', '#'),
          ('Other wannabe', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

################################

DISPLAY_PAGES_ON_MENU = False

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']

THEME='pelican-themes/bootstrap'
