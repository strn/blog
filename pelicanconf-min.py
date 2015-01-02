#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General settings

AUTHOR = u'Пурамоца'
SITENAME = u'Мудровања'
SITESUBTITLE = 'Поднаслов сајта'
SITEURL = 'http://strn.github.io'
# Where is content stored
PATH = 'content'
TIMEZONE = 'Europe/Zurich'
LOCALE = 'sr_RS'
DEFAULT_LANG = 'sr'
DATE_FORMATS = {
	'sr' : '%d-%b-%Y',
	'en' : '%d/%b/%Y'
}
DEFAULT_CATEGORY = 'blog'
DEFAULT_DATE_FORMAT = ('%d %m %Y')
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
# static paths will be copied under the same name
STATIC_PATHS = [ "theme/images", "image" ]

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
CATEGORY_URL = 'category/{slug}.html'
RECENT_ARTICLE_COUNT = 7

# Archive options
YEAR_ARCHIVE_SAVE_AS = 'post/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'post/{date:%Y}/{date:%m}/index.html'

# Article options
ARTICLE_PATHS = [ 'sr/article' ]
ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Page options
PAGE_PATHS = [ 'sr/page' ]
PAGE_URL = 'page/{slug}.html'
PAGE_SAVE_AS = 'page/{slug}.html'
PAGE_LANG_URL = 'page/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'page/{slug}-{lang}.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Items appearing in main menu
MENUITEMS = (
	( 'Архива', '/archives.html' ),
	( 'Ознаке', '/tags.html' ),
	( 'О мени', '/page/about.html' ),
	( 'Контакт', '/en/место' )
)

# Specify only article that is being written
WRITE_SELECTED = []

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

# Pagination (articles per page)
DEFAULT_PAGINATION = 3

# Theme (copy-paste from appropriate .py file)
THEME = 'theme/pelican-octopress-theme'
FACEBOOK_LIKE = True
SEARCH_BOX = True
QR_CODE = False

# Where to create site
OUTPUT_PATH = 'output/'
# Whether to copy article sources
OUTPUT_SOURCES = False

# Plugins
PLUGIN_PATHS = [ '/opt/app/p/pelican-plugins' ]
PLUGINS      = [ 'asciidoc_reader', 'gravatar', 'extract_toc', 'tipue_search', 'i18n_subsites', ]

# Options for AsciiDoc plugin
ASCIIDOC_OPTIONS = []
ASCIIDOC_BACKEND = 'html5'

# Options for "sitemap" plugin

# Options for i18n_subsites plugin
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
	'en': {
		'AUTHOR' : 'Puramotza',
		'SITENAME': 'Wise Thoughts',
		'COMMENTS_INTRO' : 'Introduction to comments',
		'LICENSE' : 'Site licence',
		'SITE_DESCRIPTION' : 'Site description',
		'EMAIL_SUBSCRIPTION_LABEL' : 'Email subscription',
		'EMAIL_FIELD_PLACEHOLDER' : 'Your email address',
		'SUBSCRIBE_BUTTON_TITLE' : 'Subscribe',
		'MAILCHIMP_FORM_ACTION' : 'Mailchimp form',
		'THEME' : 'theme/pelican-octopress-theme',
		'SITESUBTITLE' : 'Site subtitle',
		'LOCALE' : 'en_US',
		'DEFAULT_LANG' : 'en',
		'ARTICLE_PATHS' : [ 'en/article' ],
		'PAGE_PATHS' : [ 'en/page' ],
		'OUTPUT_PATH' : 'output/en',
		'MENUITEMS' : (
			( 'Archive', '/en/archives.html' ),
			( 'Tags', '/en/tags.html' ),
			( 'About me', '/en/page/about.html' ),
			( 'Contact', '/en/place' )
		)
	},
}
