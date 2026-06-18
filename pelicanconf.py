#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime
NOW = datetime.now()

AUTHOR = 'Demo Author'
SITENAME = 'Notmyidea Vine'
SITESUBTITLE = 'A Pelican Theme Demo'
SITE_DESCRIPTION = 'Demo site for the notmyidea-vine Pelican theme'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

DATE_FORMATS = {
    'en': '%Y-%m-%d',
}

# Feed
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL structure
SLUGIFY_SOURCE = 'basename'
ARTICLE_URL = 'a/{slug}.html'
ARTICLE_SAVE_AS = 'a/{slug}.html'

YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'

# Navigation
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home', '/'),
    ('Feature', '/category/feature.html'),
    ('About', '/pages/about.html'),
    ('More', '/pages/more.html'),
)

# Pagination
DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATHS = ['plugins', 'themes/notmyidea-vine']
PLUGINS = ['i18n_subsites', 'template_filters', 'sitemap']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# i18n: single-language demo, no subsites
I18N_SUBSITES = {}

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {'articles': 0.5, 'indexes': 0.5, 'pages': 0.5},
    'changefreqs': {'articles': 'weekly', 'indexes': 'daily', 'pages': 'monthly'},
}

# Content paths
ARTICLE_PATHS = ['markdown']

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Theme
THEME = 'themes/notmyidea-vine'
CSS_FILE = 'main.css'

# Homepage
INDEX_TITLE = 'Notmyidea Vine'
INDEX_MESSAGE = 'A clean, modern Pelican theme. <a href="/pages/about.html">Learn more →</a>'

# Tags cloud
THEME_ENABLE_TAG_CLOUD = True

# About page avatar (optional)
# AUTHOR_AVATAR = 'https://example.com/avatar.jpg'

# About page: contact email (shown in a copy dialog; omit to hide the Contact button)
THEME_CONTACT_EMAIL = 'hello@example.com'

# More page sections (rendered below the auto-generated Categories block)
MORE_PAGE_SECTIONS = [
    {
        'title': 'Tags & Archives',
        'items': [
            {'name': 'Tags', 'url': '/tags.html', 'icon': 'tag'},
            {'name': 'Archives', 'url': '/archives.html', 'icon': 'archive'},
        ],
    },
    {
        'title': 'Pages',
        'items': [
            {'name': 'Friends', 'url': '/pages/friends.html', 'icon': 'users'},
            {'name': 'Site History', 'url': '/pages/website-history.html', 'icon': 'history'},
        ],
    },
]

# About page: "更多内容" link cards (omit to hide the section)
# Each entry needs: title (str), url (str), css_class (str, optional)
THEME_ABOUT_MORE_LINKS = [
    {'title': 'Friends', 'url': '/pages/friends.html', 'css_class': 'about-more-card--friends'},
    {'title': 'Site History', 'url': '/pages/website-history.html', 'css_class': 'about-more-card--history'},
    {'title': 'Copyright', 'url': '/pages/copyright.html', 'css_class': 'about-more-card--copyright'},
]

# Giscus comments (optional — fill in your own repo to enable)
# GISCUS_REPO = 'your-org/your-repo'
# GISCUS_REPO_ID = ''
# GISCUS_CATEGORY = 'Announcements'
# GISCUS_CATEGORY_ID = ''
# GISCUS_MAPPING = 'pathname'
# GISCUS_LANG = 'en'

# Footer
FOOTER_NOT_BY_AI = True

# Analytics (all disabled by default for demo)
ANALYTICS_GOOGLE_ENABLED = False
ANALYTICS_VERCOUNT_ENABLED = False
ANALYTICS_UMAMI_ENABLED = False
ANALYTICS_GOATCOUNTER_ENABLED = False

# Content settings
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Blog'
SUMMARY_MAX_LENGTH = 50

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False,
            'use_pygments': False,
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
