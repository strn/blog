#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://strn.github.io'
DELETE_OUTPUT_DIRECTORY = False
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'
TAG_FEED_RSS = 'feeds/tags/%s.rss.xml'
PELICAN_COMMENT_SYSTEM_FEED = 'feeds/comment.%s.atom.xml'
RELATIVE_URLS = False

# Following items are often useful when publishing

