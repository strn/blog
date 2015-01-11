#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General settings

AUTHOR = u'Пурамоца'
SITENAME = u'Мудровања'
SITESUBTITLE = 'Размишљања о којечему'
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
STATIC_PATHS = [
	'static'
]
EXTRA_PATH_METADATA = {
    'static/image/favicon.ico' : {'path': 'favicon.ico'}
}
TYPOGRIFY = True
# Markdown (MD) extensions
MD_EXTENSIONS = [ 'codehilite(css_class=highlight)', 'extra', 'headerid', 'admonition', 'smarty' ]
RECENT_ARTICLE_COUNT = 7
DELETE_OUTPUT_DIRECTORY = True
TAG_CLOUD_STEPS = 4	# Count of different font sizes in the tag cloud.
TAG_CLOUD_MAX_ITEMS = 17

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
FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'
TAG_FEED_RSS = 'feeds/tags/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Items appearing in main menu
MENUITEMS = (
	( 'Архива', '/archives.html' ),
	( 'Ознаке', '/tags.html' ),
	( 'О мени', '/page/about.html' ),
	( 'Контакт', '/page/contact.html' )
)

# Specify only article that is being written
WRITE_SELECTED = []

# Blogroll
LINKS = False

# Social widget
SOCIAL = ()

# Pagination (articles per page)
DEFAULT_PAGINATION = 3

THEME = 'theme/kernel-org-sr'

# Where to create site
OUTPUT_PATH = 'dev/'
# Whether to copy article sources
OUTPUT_SOURCES = False

# Plugins
PLUGIN_PATHS = [ '/opt/app/p/pelican-plugins' ]
PLUGINS      = [ 'asciidoc_reader', 'gravatar', 'tipue_search', 'i18n_subsites', 'neighbors', 'sitemap' ]

# Options for AsciiDoc plugin
ASCIIDOC_OPTIONS = [ "-a source-highlighter=pygments" ]
ASCIIDOC_BACKEND = 'html5'

# Options for i18n_subsites plugin
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
	'en': {
		'AUTHOR' : 'Puramotza',
		'SITENAME': 'Philosophizing',
		'LICENSE' : 'Site licence',
		'SITE_DESCRIPTION' : 'Site description',
		'EMAIL_SUBSCRIPTION_LABEL' : 'Email subscription',
		'EMAIL_FIELD_PLACEHOLDER' : 'Your email address',
		'SUBSCRIBE_BUTTON_TITLE' : 'Subscribe',
		'MAILCHIMP_FORM_ACTION' : 'Mailchimp form',
		'THEME' : 'theme/kernel-org-en',
		'SITESUBTITLE' : 'Intelectual juggling',
		'LOCALE' : 'en_US',
		'DEFAULT_LANG' : 'en',
		'ARTICLE_PATHS' : [ 'en/article' ],
		'PAGE_PATHS' : [ 'en/page' ],
		'OUTPUT_PATH' : 'dev/en',
		'ARTICLE_PATHS' : [ 'en/article' ],
		'MENUITEMS' : (
			( 'Archive', '/en/archives.html' ),
			( 'Tags', '/en/tags.html' ),
			( 'About me', '/en/page/about.html' ),
			( 'Contact', '/en/page/contact.html' )
		),
	},
}

SITEMAP = {
	'format': 'xml',
	'priorities': {
		'articles': 0.5,
		'indexes': 0.5,
		'pages': 0.5
	},
	'changefreqs': {
		'articles' : 'monthly',
		'indexes' : 'daily',
		'pages' : 'monthly'
	}
}

# Controlling icon size for RSS and ATOM
FEED_ICON_SIZE_TAG_CLOUD = 24
