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
# Where to create site
OUTPUT_PATH = 'prod/'
DELETE_OUTPUT_DIRECTORY = False
# Disqus plugin
DISQUS_SITENAME = 'mudrovanya-sr'
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'
TAG_FEED_RSS = 'feeds/tags/%s.rss.xml'
PELICAN_COMMENT_SYSTEM_FEED = 'feeds/comment.%s.atom.xml'
RELATIVE_URLS = False

I18N_SUBSITES = {
	'en': {
		'AUTHOR' : 'Puramotza',
		'SITENAME': 'Philosophizing',
		'SITE_DESCRIPTION' : 'Site description',
		'EMAIL_SUBSCRIPTION_LABEL' : 'Email subscription',
		'EMAIL_FIELD_PLACEHOLDER' : 'Your email address',
		'SUBSCRIBE_BUTTON_TITLE' : 'Subscribe',
		'MAILCHIMP_FORM_ACTION' : 'Mailchimp form',
		'THEME' : 'theme/kernel-org-en',
		'SITESUBTITLE' : 'Random thoughts of everything',
		'LOCALE' : 'en_US',
		'DEFAULT_LANG' : 'en',
		'ARTICLE_PATHS' : [ 'en/article' ],
		'PAGE_PATHS' : [ 'en/page' ],
		'OUTPUT_PATH' : 'prod/en',
		'MENUITEMS' : (
			( 'Archive', '/en/archives.html' ),
			( 'Tags', '/en/tags.html' ),
			( 'About me', '/en/page/about.html' ),
			( 'Contact', '/en/page/contact.html' )
		),
		'DISQUS_SITENAME' : 'mudrovanja',
	},
}

# Following items are often useful when publishing

